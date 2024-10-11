from app.app_config import (AppConfig, MinioConfig, PostgresConfig,
                            RedisConfig, TelegramConfig)


def create_app_config() -> AppConfig:
    return AppConfig(
        telegram=TelegramConfig(),
        postgres=PostgresConfig(),
        redis=RedisConfig(),
        minio=MinioConfig(),
    )
