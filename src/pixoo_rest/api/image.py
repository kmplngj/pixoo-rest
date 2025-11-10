"""Image and GIF handling endpoints for the Pixoo REST API."""

import base64
from io import BytesIO

import httpx
from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from PIL import Image
from pixoo import Pixoo

from pixoo_rest.dependencies import get_pixoo
from pixoo_rest.models.requests import (
    DownloadGifRequest,
    DownloadImageRequest,
    SuccessResponse,
)

router = APIRouter(tags=["image"])


async def _send_gif_to_device(
    pixoo: Pixoo,
    gif: Image.Image,
    speed: int,
    skip_first_frame: bool,
    client: httpx.AsyncClient
) -> None:
    """Send a GIF to the Pixoo device.
    
    Args:
        pixoo: Pixoo device instance
        gif: PIL Image object (GIF)
        speed: Animation speed
        skip_first_frame: Whether to skip the first frame
        client: httpx AsyncClient to reuse for requests
    """
    if not gif.is_animated:
        # Not animated, just draw as static image
        pixoo.draw_image(gif)
        pixoo.push()
        return

    # Reset GIF state
    await client.post(
        f"http://{pixoo.ip_address}/post",
        json={"Command": "Draw/ResetHttpGifId"}
    )

    # Extract frames
    gif_frames = []
    start_frame = 1 if skip_first_frame else 0
    
    for i in range(start_frame, min(gif.n_frames, 59 + start_frame)):
        gif.seek(i)
        
        # Resize if needed
        if gif.size not in ((16, 16), (32, 32), (64, 64)):
            frame = gif.resize((pixoo.size, pixoo.size)).convert("RGB")
        else:
            frame = gif.convert("RGB")
        
        gif_frames.append(frame)

    # Send each frame
    for offset, frame in enumerate(gif_frames):
        await client.post(
            f"http://{pixoo.ip_address}/post",
            json={
                "Command": "Draw/SendHttpGif",
                "PicID": 1,
                "PicNum": len(gif_frames),
                "PicOffset": offset,
                "PicWidth": frame.width,
                "PicSpeed": speed,
                "PicData": base64.b64encode(frame.tobytes()).decode("utf-8")
            }
        )


@router.post("/image")
async def upload_image(
    image: UploadFile = File(None),
    image_url: str = Form(None),
    speed: int = Form(100),
    skip_first_frame: bool = Form(False),
    pixoo: Pixoo = Depends(get_pixoo)
) -> SuccessResponse:
    """Upload an image or provide URL to display.
    
    Supports both static images and animated GIFs.
    Provide either 'image' file or 'image_url' parameter.
    
    Args:
        image: Image file upload
        image_url: URL of image to download
        speed: Animation speed for GIFs (default: 100)
        skip_first_frame: Skip first frame of GIF (default: False)
    """
    try:
        # Use a shared HTTP client for all requests in this endpoint
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            # Check if image file was uploaded
            if image:
                content = await image.read()
                img = Image.open(BytesIO(content))
            # Check if URL was provided
            elif image_url and image_url.startswith('http'):
                response = await client.get(image_url)
                response.raise_for_status()
                img = Image.open(BytesIO(response.content))
            else:
                raise HTTPException(
                    status_code=400,
                    detail="Must provide either 'image' file or 'image_url' parameter"
                )

            # Handle GIF or static image
            if img.format == 'GIF':
                await _send_gif_to_device(pixoo, img, speed, skip_first_frame, client)
            else:
                pixoo.draw_image(img)
                pixoo.push()

        return SuccessResponse()
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to download image: {str(e)}"
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process image: {str(e)}"
        ) from e


@router.post("/sendGif")
async def upload_gif(
    gif: UploadFile = File(...),
    speed: int = Form(100),
    skip_first_frame: bool = Form(False),
    pixoo: Pixoo = Depends(get_pixoo)
) -> SuccessResponse:
    """Upload and display a GIF.
    
    Args:
        gif: GIF file to upload
        speed: Animation speed (default: 100)
        skip_first_frame: Skip first frame (default: False)
    """
    try:
        content = await gif.read()
        img = Image.open(BytesIO(content))
        
        # Use HTTP client for sending GIF frames
        async with httpx.AsyncClient(timeout=30.0) as client:
            await _send_gif_to_device(pixoo, img, speed, skip_first_frame, client)
        
        return SuccessResponse()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process GIF: {str(e)}"
        ) from e


@router.post("/download/gif")
async def download_gif(
    request: DownloadGifRequest,
    pixoo: Pixoo = Depends(get_pixoo)
) -> SuccessResponse:
    """Download and display a GIF from URL.
    
    Args:
        request: GIF download request with URL and options
    """
    try:
        async with httpx.AsyncClient(
            timeout=request.timeout,
            verify=request.ssl_verify,
            follow_redirects=True
        ) as client:
            response = await client.get(request.url)
            response.raise_for_status()
            
            img = Image.open(BytesIO(response.content))
            await _send_gif_to_device(pixoo, img, request.speed, request.skip_first_frame, client)
        
        return SuccessResponse()
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to download GIF: {str(e)}"
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process GIF: {str(e)}"
        ) from e


@router.post("/download/image")
async def download_image(
    request: DownloadImageRequest,
    pixoo: Pixoo = Depends(get_pixoo)
) -> SuccessResponse:
    """Download and display an image from URL.
    
    Args:
        request: Image download request with URL and position
    """
    try:
        async with httpx.AsyncClient(
            timeout=request.timeout,
            verify=request.ssl_verify,
            follow_redirects=True
        ) as client:
            response = await client.get(request.url)
            response.raise_for_status()
            
            img = Image.open(BytesIO(response.content))
            pixoo.draw_image_at_location(img, request.x, request.y)
            
            if request.push_immediately:
                pixoo.push()
        
        return SuccessResponse()
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to download image: {str(e)}"
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process image: {str(e)}"
        ) from e
