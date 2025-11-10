"""Download endpoints for the Pixoo REST API."""

import httpx
from fastapi import APIRouter, Depends, HTTPException
from pixoo import Pixoo

from pixoo_rest.dependencies import get_pixoo
from pixoo_rest.models.requests import DownloadTextRequest

router = APIRouter(prefix="/download", tags=["download"])


@router.post("/text")
async def download_text(
    request: DownloadTextRequest,
    pixoo: Pixoo = Depends(get_pixoo)
) -> dict:
    """Display text that updates from a URL.
    
    The URL should return plain text content that will be displayed
    and automatically updated at the specified interval.
    
    Args:
        request: Text download configuration
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"http://{pixoo.ip_address}/post",
                json={
                    "Command": "Draw/SendHttpItemList",
                    "ItemList": [
                        {
                            "type": 23,
                            "TextId": request.id,
                            "TextString": request.url,
                            "x": request.x,
                            "y": request.y,
                            "dir": request.scroll_direction,
                            "font": 4,
                            "TextWidth": request.text_width,
                            "Textheight": request.text_height,
                            "speed": request.scroll_speed,
                            "update_time": request.update_interval,
                            "align": request.horizontal_alignment,
                            "color": f"#{request.r:02x}{request.g:02x}{request.b:02x}"
                        }
                    ]
                }
            )
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to configure text download: {str(e)}"
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to send text download command: {str(e)}"
        ) from e
