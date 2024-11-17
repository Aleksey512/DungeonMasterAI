from gateway.settings.const import FIVE_MINUTES, TEN_DAYS
from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    # Application
    debug: bool = Field(False, alias="DEBUG")
    secret_key: str = Field("", alias="SECRET_KEY")
    algorithm: str = Field("HS256", alias="ALGRORITHM")
    access_token_expire_seconds: int = Field(
        FIVE_MINUTES, alias="ACCESS_TOKEN_EXPIRY_SECONDS"
    )
    refresh_token_expire_seconds: int = Field(
        TEN_DAYS, alias="REFRESH_TOKEN_EXPIRY_SECONDS"
    )
