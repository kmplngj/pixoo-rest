"""Drawing endpoints for the Pixoo REST API."""

from fastapi import APIRouter, Depends, HTTPException
from pixoo import Pixoo

from pixoo_rest.dependencies import get_pixoo
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


@router.post("/pixel", response_model=SuccessResponse)
async def draw_pixel(request: DrawPixelRequest, pixoo: Pixoo = Depends(get_pixoo)):
    """Draw a single pixel at the specified coordinates with the given color."""
    try:
        pixoo.draw_pixel_at_location_rgb(request.x, request.y, request.r, request.g, request.b)

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to draw pixel: {str(e)}") from e


@router.post("/character", response_model=SuccessResponse)
async def draw_character(request: DrawCharacterRequest, pixoo: Pixoo = Depends(get_pixoo)):
    """Draw a character at the specified coordinates with the given color."""
    try:
        pixoo.draw_character_at_location_rgb(
            request.character, request.x, request.y, request.r, request.g, request.b
        )

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to draw character: {str(e)}") from e


@router.post("/line", response_model=SuccessResponse)
async def draw_line(request: DrawLineRequest, pixoo: Pixoo = Depends(get_pixoo)):
    """Draw a line from (x1, y1) to (x2, y2) with the given color."""
    try:
        pixoo.draw_line_from_start_to_stop_rgb(
            request.x1, request.y1, request.x2, request.y2, request.r, request.g, request.b
        )

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to draw line: {str(e)}") from e


@router.post("/rectangle", response_model=SuccessResponse)
async def draw_rectangle(request: DrawRectangleRequest, pixoo: Pixoo = Depends(get_pixoo)):
    """Draw a rectangle from (x1, y1) to (x2, y2) with the given color."""
    try:
        pixoo.draw_rectangle_from_top_left_to_bottom_right_rgb(
            request.x1, request.y1, request.x2, request.y2, request.r, request.g, request.b
        )

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to draw rectangle: {str(e)}") from e


@router.post("/fill", response_model=SuccessResponse)
async def draw_fill(request: DrawFillRequest, pixoo: Pixoo = Depends(get_pixoo)):
    """Fill the entire screen with the given color."""
    try:
        pixoo.fill_rgb(request.r, request.g, request.b)

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fill screen: {str(e)}") from e


@router.post("/text", response_model=SuccessResponse)
async def draw_text(request: DrawTextRequest, pixoo: Pixoo = Depends(get_pixoo)):
    """Draw text at the specified coordinates with the given color."""
    try:
        # Note: pixoo library's draw_text_at_location_rgb doesn't support font parameter
        pixoo.draw_text_at_location_rgb(
            request.text, request.x, request.y, request.r, request.g, request.b
        )

        if request.push_immediately:
            pixoo.push()

        return SuccessResponse()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to draw text: {str(e)}") from e
