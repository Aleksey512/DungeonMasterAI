from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = Field("sqlite+aiosqlite:///database.db", alias="DATABASE_URL")
    rabbitmq_url: str = Field("", alias="RABBITMQ_URL")
    redis_url: str = Field("", alias="REDIS_URL")

    taskiq_result_ex_time: int = Field(
        60 * 60 * 24, alias="TASKIQ_RESULT_EX_TIME"
    )  # 24 hours
    env: str = Field("local", alias="ENVIRONMENT")

    model_config = SettingsConfigDict(secrets_dir="/run/secrets")


settings = Settings()  # type: ignore
