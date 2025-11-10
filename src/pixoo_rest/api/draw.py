"""Draw endpoints - drawing primitives on the Pixoo display."""

from fastapi import APIRouter, HTTPException

from pixoo_rest.models.requests import (
    DrawCharacterRequest,
    DrawFillRequest,
    DrawLineRequest,
    DrawPixelRequest,
    DrawRectangleRequest,
    DrawTextRequest,
    SuccessResponse,
)

router = APIRouter(prefix="/draw", tags=["draw"])


# This will be injected by the app
pixoo = None


def set_pixoo_instance(pixoo_instance):
    """Set the global Pixoo instance."""
    global pixoo
    pixoo = pixoo_instance


@router.post("/pixel", response_model=SuccessResponse)
async def draw_pixel(request: DrawPixelRequest):
    """Draw a single pixel at the specified coordinates with the given color."""
    if pixoo is None:
        raise HTTPException(status_code=503, detail="Pixoo device not initialized")

    try:
        pixoo.draw_pixel_at_location_rgb(request.x, request.y, request.r, request.g, request.b)

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to draw pixel: {str(e)}")


@router.post("/character", response_model=SuccessResponse)
async def draw_character(request: DrawCharacterRequest):
    """Draw a character at the specified coordinates with the given color."""
    if pixoo is None:
        raise HTTPException(status_code=503, detail="Pixoo device not initialized")

    try:
        pixoo.draw_character_at_location_rgb(
            request.character, request.x, request.y, request.r, request.g, request.b
        )

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to draw character: {str(e)}")


@router.post("/line", response_model=SuccessResponse)
async def draw_line(request: DrawLineRequest):
    """Draw a line from (x1, y1) to (x2, y2) with the given color."""
    if pixoo is None:
        raise HTTPException(status_code=503, detail="Pixoo device not initialized")

    try:
        pixoo.draw_line_from_start_to_stop_rgb(
            request.x1, request.y1, request.x2, request.y2, request.r, request.g, request.b
        )

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to draw line: {str(e)}")


@router.post("/rectangle", response_model=SuccessResponse)
async def draw_rectangle(request: DrawRectangleRequest):
    """Draw a rectangle from (x1, y1) to (x2, y2) with the given color."""
    if pixoo is None:
        raise HTTPException(status_code=503, detail="Pixoo device not initialized")

    try:
        pixoo.draw_rectangle_from_top_left_to_bottom_right_rgb(
            request.x1, request.y1, request.x2, request.y2, request.r, request.g, request.b
        )

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to draw rectangle: {str(e)}")


@router.post("/fill", response_model=SuccessResponse)
async def draw_fill(request: DrawFillRequest):
    """Fill the entire screen with the given color."""
    if pixoo is None:
        raise HTTPException(status_code=503, detail="Pixoo device not initialized")

    try:
        pixoo.fill_rgb(request.r, request.g, request.b)

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fill screen: {str(e)}")


@router.post("/text", response_model=SuccessResponse)
async def draw_text(request: DrawTextRequest):
    """Draw text at the specified coordinates with the given color."""
    if pixoo is None:
        raise HTTPException(status_code=503, detail="Pixoo device not initialized")

    try:
        # Note: pixoo library's draw_text_at_location_rgb doesn't support font parameter
        pixoo.draw_text_at_location_rgb(
            request.text, request.x, request.y, request.r, request.g, request.b
        )

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to draw text: {str(e)}")
