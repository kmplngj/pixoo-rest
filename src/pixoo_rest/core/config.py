"""Application configuration using Pydantic Settings."""

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Pixoo Device Settings
    pixoo_host: str = Field(default="Pixoo64", description="Pixoo device hostname or IP address")
    pixoo_screen_size: int = Field(default=64, description="Pixoo screen size (16, 32, or 64)")
    pixoo_debug: bool = Field(default=False, description="Enable Pixoo debug mode")
    pixoo_test_connection_retries: int = Field(
        default=2147483647,  # sys.maxsize equivalent
        description="Number of connection retries before failing",
    )

    # REST API Settings
    pixoo_rest_debug: bool = Field(default=False, description="Enable REST API debug mode")
    pixoo_rest_host: str = Field(default="127.0.0.1", description="REST API host address")
    pixoo_rest_port: int = Field(default=5000, description="REST API port")


# Global settings instance
settings = Settings()
