"""Send endpoints for the Pixoo REST API."""

from fastapi import APIRouter, Depends, HTTPException
from pixoo import Pixoo

from pixoo_rest.dependencies import get_pixoo
from pixoo_rest.models.requests import SendTextRequest, SuccessResponse

router = APIRouter(prefix="/send", tags=["send"])


@router.post("/text", response_model=SuccessResponse)
async def send_text(request: SendTextRequest, pixoo: Pixoo = Depends(get_pixoo)):
    """Send scrolling text to the Pixoo display."""
    try:
        pixoo.send_text(
            request.text,
            (request.x, request.y),
            (request.r, request.g, request.b),
            request.identifier,
            request.font,
            request.text_width,
            request.scroll_speed,
            request.scroll_direction,
        )

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send text: {str(e)}") from e
