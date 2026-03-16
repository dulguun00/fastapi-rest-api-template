from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = Field(default="sqlite:///./app.db", alias="DATABASE_URL")
    jwt_secret_key: str = Field(default="change-this-secret", alias="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(
        default=60, alias="ACCESS_TOKEN_EXPIRE_MINUTES"
    )

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
