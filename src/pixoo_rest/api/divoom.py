"""Divoom API passthrough endpoints for the Pixoo REST API."""

import httpx
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/divoom", tags=["divoom"])

DIVOOM_API_URL = "https://app.divoom-gz.com"


class GetDialListRequest(BaseModel):
    """Request model for getting dial list."""

    dial_type: str = Field(default="Game", description="Type of dial (e.g., 'Game', 'Clock')")
    page_number: int = Field(default=1, ge=1, description="Page number")


@router.post("/device/lan")
async def get_lan_devices() -> dict:
    """Get Divoom devices on the local network.
    
    Returns information about Divoom devices available on the same LAN.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{DIVOOM_API_URL}/Device/ReturnSameLANDevice"
            )
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to query Divoom API: {str(e)}"
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get LAN devices: {str(e)}"
        ) from e


@router.post("/channel/dial/types")
async def get_dial_types() -> dict:
    """Get available dial types from Divoom.
    
    Returns the list of available clock/dial types.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{DIVOOM_API_URL}/Channel/GetDialType"
            )
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to query Divoom API: {str(e)}"
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get dial types: {str(e)}"
        ) from e


@router.post("/channel/dial/list")
async def get_dial_list(request: GetDialListRequest) -> dict:
    """Get list of available dials/clocks from Divoom.
    
    Returns a paginated list of available clock faces for the specified type.
    
    Args:
        request: Dial list request with type and page number
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{DIVOOM_API_URL}/Channel/GetDialList",
                json={
                    "DialType": request.dial_type,
                    "Page": request.page_number
                }
            )
            return response.json()
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to query Divoom API: {str(e)}"
        ) from e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to get dial list: {str(e)}"
        ) from e
