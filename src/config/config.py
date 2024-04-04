from environs import Env


env = Env()
env.read_env()

BOT_TOKEN: str = env.str("BOT_TOKEN")

ENV: str = env.str("ENV")

if ENV == "local":
	MEDIA_PATH: str = env.str("MEDIA_LOCAL")
else:
	MEDIA_PATH: str = env.str("MEDIA_PROD")

PG_HOST: str = env.str("POSTGRES_HOST")
PG_USER: str = env.str("POSTGRES_USER")
PG_PASSWORD: str = env.str("POSTGRES_PASSWORD")
PG_DATABASE: str = env.str("POSTGRES_DB")

USE_CACHE: bool = env.bool("USE_CACHE")

if USE_CACHE:
	REDIS_PORT: int = env.int("REDIS_PORT")
	REDIS_HOST: str = env.str("REDIS_HOST")
	REDIS_USER: str = env.str("REDIS_USER")
	REDIS_PASSWORD: str = env.str("REDIS_PASSWORD")


