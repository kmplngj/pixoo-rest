"""Settings endpoints for the Pixoo REST API."""

from fastapi import APIRouter, Depends, HTTPException
from pixoo import Channel, Pixoo

from pixoo_rest.dependencies import get_pixoo
from pixoo_rest.models.requests import SuccessResponse

router = APIRouter(prefix="/set", tags=["settings"])


@router.put("/brightness/{percentage}")
async def set_brightness(
    percentage: int,
    pixoo: Pixoo = Depends(get_pixoo)
) -> SuccessResponse:
    """Set the screen brightness.
    
    Args:
        percentage: Brightness level (0-100)
    """
    try:
        pixoo.set_brightness(percentage)
        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to set brightness: {str(e)}") from e


@router.put("/channel/{number}")
async def set_channel(
    number: int,
    pixoo: Pixoo = Depends(get_pixoo)
) -> SuccessResponse:
    """Set the channel.
    
    Args:
        number: Channel number
    """
    try:
        pixoo.set_channel(Channel(number))
        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to set channel: {str(e)}") from e


@router.put("/face/{number}")
async def set_face(
    number: int,
    pixoo: Pixoo = Depends(get_pixoo)
) -> SuccessResponse:
    """Set the face/clock display.
    
    Args:
        number: Face number
    """
    try:
        pixoo.set_face(number)
        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to set face: {str(e)}") from e


@router.put("/visualizer/{number}")
async def set_visualizer(
    number: int,
    pixoo: Pixoo = Depends(get_pixoo)
) -> SuccessResponse:
    """Set the visualizer mode.
    
    Args:
        number: Visualizer number
    """
    try:
        pixoo.set_visualizer(number)
        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to set visualizer: {str(e)}") from e


@router.put("/clock/{number}")
async def set_clock(
    number: int,
    pixoo: Pixoo = Depends(get_pixoo)
) -> SuccessResponse:
    """Set the clock display.
    
    Args:
        number: Clock number
    """
    try:
        pixoo.set_clock(number)
        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to set clock: {str(e)}") from e


@router.put("/screen/{on_off}")
async def set_screen(
    on_off: bool,
    pixoo: Pixoo = Depends(get_pixoo)
) -> SuccessResponse:
    """Turn the screen on or off.
    
    Args:
        on_off: True to turn on, False to turn off
    """
    try:
        pixoo.set_screen(on_off)
        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to set screen: {str(e)}") from e
