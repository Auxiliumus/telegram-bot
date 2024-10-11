from app.app_config import (
    AppConfig,
    TelegramConfig,
    PostgresConfig,
    RedisConfig,
    MinioConfig,
)


def create_app_config() -> AppConfig:
    return AppConfig(
        telegram=TelegramConfig(),
        postgres=PostgresConfig(),
        redis=RedisConfig(),
        minio=MinioConfig(),
    )
