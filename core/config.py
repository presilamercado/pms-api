from starlette.config import Config

config = Config(".env")
VERSION: str = config("VERSION")
PROJECT_NAME: str = config("PROJECT_NAME")
SQLALCHAMY_DATABASE_URL: str = config("SQLALCHAMY_DATABASE_URL")