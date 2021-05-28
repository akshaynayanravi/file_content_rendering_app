from pathlib import Path
from environs import Env

env = Env()
env.read_env()

# Paths
BASE_DIR: Path = env.path("BASE_DIR")

# Flask
FLASK_HOST: str = env.str("FLASK_HOST", "127.0.0.1")
FLASK_PORT: int = env.int("FLASK_PORT", 5000)
FLASK_DEBUG: bool = env.bool("DEBUG", True)