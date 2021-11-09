from starlette.config import Config
config = Config(".env_example")
POSTGRES_USER = config("POSTGRES_USER", cast=str, default='postgres')
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", default='postgres')
POSTGRES_SERVER = config("POSTGRES_SERVER", cast=str, default="localhost")
POSTGRES_PORT = config("POSTGRES_PORT", cast=str, default="5432")
POSTGRES_DB = config("POSTGRES_DB", cast=str, default="statistic")
EXTERNAL_API = config("EXTERNAL_API", cast=str, default="statistic")
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
