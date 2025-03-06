from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "postgresql+asyncpg://user:qwerty321@localhost:5435/practice"
    db_echo: bool = True


settings = Settings()
