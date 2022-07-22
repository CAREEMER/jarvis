from pydantic import BaseSettings


class Config(BaseSettings):
    BOT_TOKEN: str

    class Config:
        env_file = 'local.env'
        env_file_encoding = 'utf-8'


app_config = Config()
