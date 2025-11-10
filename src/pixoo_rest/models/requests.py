"""Pydantic models for API requests and responses."""

from pydantic import BaseModel, Field


# Common models
class RGBColor(BaseModel):
    """RGB color representation."""

    r: int = Field(..., ge=0, le=255, description="Red component (0-255)")
    g: int = Field(..., ge=0, le=255, description="Green component (0-255)")
    b: int = Field(..., ge=0, le=255, description="Blue component (0-255)")


class Position(BaseModel):
    """2D position coordinates."""

    x: int = Field(..., description="X coordinate")
    y: int = Field(..., description="Y coordinate")


# Draw endpoints
class DrawPixelRequest(BaseModel):
    """Request model for drawing a pixel."""

    x: int = Field(..., description="X coordinate")
    y: int = Field(..., description="Y coordinate")
    r: int = Field(..., ge=0, le=255, description="Red component")
    g: int = Field(..., ge=0, le=255, description="Green component")
    b: int = Field(..., ge=0, le=255, description="Blue component")
    push_immediately: bool = Field(default=True, description="Push changes immediately")


class DrawCharacterRequest(BaseModel):
    """Request model for drawing a character."""

    character: str = Field(..., max_length=1, description="Character to draw")
    x: int = Field(..., description="X coordinate")
    y: int = Field(..., description="Y coordinate")
    r: int = Field(..., ge=0, le=255, description="Red component")
    g: int = Field(..., ge=0, le=255, description="Green component")
    b: int = Field(..., ge=0, le=255, description="Blue component")
    push_immediately: bool = Field(default=True, description="Push changes immediately")


class DrawLineRequest(BaseModel):
    """Request model for drawing a line."""

    x1: int = Field(..., description="Start X coordinate")
    y1: int = Field(..., description="Start Y coordinate")
    x2: int = Field(..., description="End X coordinate")
    y2: int = Field(..., description="End Y coordinate")
    r: int = Field(..., ge=0, le=255, description="Red component")
    g: int = Field(..., ge=0, le=255, description="Green component")
    b: int = Field(..., ge=0, le=255, description="Blue component")
    push_immediately: bool = Field(default=True, description="Push changes immediately")


class DrawRectangleRequest(BaseModel):
    """Request model for drawing a rectangle."""

    x1: int = Field(..., description="Top-left X coordinate")
    y1: int = Field(..., description="Top-left Y coordinate")
    x2: int = Field(..., description="Bottom-right X coordinate")
    y2: int = Field(..., description="Bottom-right Y coordinate")
    r: int = Field(..., ge=0, le=255, description="Red component")
    g: int = Field(..., ge=0, le=255, description="Green component")
    b: int = Field(..., ge=0, le=255, description="Blue component")
    push_immediately: bool = Field(default=True, description="Push changes immediately")


class DrawFillRequest(BaseModel):
    """Request model for filling the screen."""

    r: int = Field(..., ge=0, le=255, description="Red component")
    g: int = Field(..., ge=0, le=255, description="Green component")
    b: int = Field(..., ge=0, le=255, description="Blue component")
    push_immediately: bool = Field(default=True, description="Push changes immediately")


class DrawTextRequest(BaseModel):
    """Request model for drawing text."""

    text: str = Field(..., description="Text to draw")
    x: int = Field(..., description="X coordinate")
    y: int = Field(..., description="Y coordinate")
    r: int = Field(..., ge=0, le=255, description="Red component")
    g: int = Field(..., ge=0, le=255, description="Green component")
    b: int = Field(..., ge=0, le=255, description="Blue component")
    font: int = Field(default=2, description="Font ID")
    push_immediately: bool = Field(default=True, description="Push changes immediately")


# Send endpoints
class SendTextRequest(BaseModel):
    """Request model for sending scrolling text."""

    text: str = Field(..., description="Text to display")
    x: int = Field(default=0, description="X coordinate")
    y: int = Field(default=0, description="Y coordinate")
    r: int = Field(..., ge=0, le=255, description="Red component")
    g: int = Field(..., ge=0, le=255, description="Green component")
    b: int = Field(..., ge=0, le=255, description="Blue component")
    identifier: int = Field(default=1, description="Text identifier")
    font: int = Field(default=2, description="Font ID")
    text_width: int = Field(default=64, description="Text width")
    scroll_speed: int = Field(default=100, ge=0, description="Scroll speed (0=no scroll)")
    scroll_direction: int = Field(default=0, description="Scroll direction")


class SendImageUrlRequest(BaseModel):
    """Request model for sending an image from URL."""

    url: str = Field(..., description="URL of the image to display")
    ssl_verify: bool = Field(default=True, description="Verify SSL certificates")
    skip_first_frame: bool = Field(default=False, description="Skip first frame of GIF")


# Download endpoints
class DownloadGifRequest(BaseModel):
    """Request model for downloading and displaying a GIF."""

    url: str = Field(..., description="URL of the GIF to download")
    speed: int = Field(default=100, ge=1, description="Animation speed")
    skip_first_frame: bool = Field(default=False, description="Skip first frame")
    timeout: int = Field(default=30, ge=1, description="Download timeout in seconds")
    ssl_verify: bool = Field(default=True, description="Verify SSL certificates")


class DownloadImageRequest(BaseModel):
    """Request model for downloading and displaying an image."""

    url: str = Field(..., description="URL of the image to download")
    x: int = Field(default=0, description="X coordinate")
    y: int = Field(default=0, description="Y coordinate")
    timeout: int = Field(default=30, ge=1, description="Download timeout in seconds")
    ssl_verify: bool = Field(default=True, description="Verify SSL certificates")
    push_immediately: bool = Field(default=True, description="Push changes immediately")


class DownloadTextRequest(BaseModel):
    """Request model for text that updates from URL."""

    url: str = Field(..., description="URL that returns text content")
    id: int = Field(default=1, description="Text identifier")
    x: int = Field(default=0, description="X coordinate")
    y: int = Field(default=0, description="Y coordinate")
    r: int = Field(..., ge=0, le=255, description="Red component")
    g: int = Field(..., ge=0, le=255, description="Green component")
    b: int = Field(..., ge=0, le=255, description="Blue component")
    scroll_direction: int = Field(default=0, description="Scroll direction")
    scroll_speed: int = Field(default=100, description="Scroll speed")
    text_width: int = Field(default=64, description="Text width")
    text_height: int = Field(default=64, description="Text height")
    update_interval: int = Field(default=60, description="Update interval in seconds")
    horizontal_alignment: int = Field(default=1, description="Horizontal alignment (1=left, 2=center, 3=right)")


# Image/GIF upload endpoints
class SendGifRequest(BaseModel):
    """Request model for sending a GIF."""

    speed: int = Field(default=100, ge=1, description="Animation speed")
    skip_first_frame: bool = Field(default=False, description="Skip first frame")


# Set endpoints
class SetBrightnessRequest(BaseModel):
    """Request model for setting brightness."""

    brightness: int = Field(..., ge=0, le=100, description="Brightness level (0-100)")


class SetScreenRequest(BaseModel):
    """Request model for setting screen on/off."""

    screen: bool = Field(..., description="Screen state (true=on, false=off)")


# Response models
class SuccessResponse(BaseModel):
    """Standard success response."""

    status: str = Field(default="success", description="Operation status")
    message: str = Field(default="OK", description="Response message")


class ErrorResponse(BaseModel):
    """Standard error response."""

    status: str = Field(default="error", description="Operation status")
    message: str = Field(..., description="Error message")
    detail: str | None = Field(None, description="Detailed error information")


class HealthCheckResponse(BaseModel):
    """Health check endpoint response."""

    status: str = Field(..., description="Health status (healthy/unhealthy)")
    pixoo_host: str = Field(..., description="Configured Pixoo device hostname/IP")


class RootResponse(BaseModel):
    """Root endpoint response with API information."""

    name: str = Field(..., description="API name")
    version: str = Field(..., description="API version")
    description: str = Field(..., description="API description")
    docs: str = Field(..., description="OpenAPI documentation URL (Swagger UI)")
    redoc: str = Field(..., description="OpenAPI documentation URL (ReDoc)")
    openapi: str = Field(..., description="OpenAPI JSON schema URL")


# Divoom API response models
class DivoomApiResponse(BaseModel):
    """Base model for Divoom API responses.
    
    Note: Divoom API responses are dynamic and may contain additional fields.
    This model accepts extra fields to handle the flexible API structure.
    """

    model_config = {"extra": "allow"}

    error_code: int = Field(..., alias="error_code", description="Divoom API error code (0 = success)")


class DivoomLanDevicesResponse(DivoomApiResponse):
    """Response from Divoom LAN device discovery endpoint."""

    device_list: list[dict] = Field(
        default_factory=list,
        alias="DeviceList",
        description="List of discovered Divoom devices on LAN"
    )


class DivoomDialTypesResponse(DivoomApiResponse):
    """Response from Divoom dial types endpoint."""

    dial_type_list: list[dict] = Field(
        default_factory=list,
        alias="DialTypeList",
        description="List of available dial/clock types"
    )


class DivoomDialListResponse(DivoomApiResponse):
    """Response from Divoom dial list endpoint."""

    dial_list: list[dict] = Field(
        default_factory=list,
        alias="DialList",
        description="List of available dials/clocks for the specified type"
    )
    total_num: int = Field(default=0, alias="TotalNum", description="Total number of available dials")
