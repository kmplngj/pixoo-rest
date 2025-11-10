"""Send endpoints - sending text and images to the Pixoo display."""

from fastapi import APIRouter, HTTPException

from pixoo_rest.models.requests import SendTextRequest, SendImageUrlRequest, SuccessResponse

router = APIRouter(prefix="/send", tags=["send"])


# This will be injected by the app
pixoo = None


def set_pixoo_instance(pixoo_instance):
    """Set the global Pixoo instance."""
    global pixoo
    pixoo = pixoo_instance


@router.post("/text", response_model=SuccessResponse)
async def send_text(request: SendTextRequest):
    """Send scrolling text to the Pixoo display."""
    if pixoo is None:
        raise HTTPException(status_code=503, detail="Pixoo device not initialized")

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
        raise HTTPException(status_code=500, detail=f"Failed to send text: {str(e)}")
