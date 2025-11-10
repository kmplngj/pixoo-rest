"""Send endpoints - sending text and images to the Pixoo display."""

from fastapi import APIRouter, Depends, HTTPException
from pixoo import Pixoo

from pixoo_rest.models.requests import SendTextRequest, SuccessResponse

router = APIRouter(prefix="/send", tags=["send"])


# This will be injected by the app
_pixoo_instance: Pixoo | None = None


def set_pixoo_instance(pixoo_instance: Pixoo):
    """Set the global Pixoo instance."""
    global _pixoo_instance
    _pixoo_instance = pixoo_instance


def get_pixoo() -> Pixoo:
    """Dependency to get the Pixoo instance."""
    if _pixoo_instance is None:
        raise HTTPException(status_code=503, detail="Pixoo device not initialized")
    return _pixoo_instance


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
