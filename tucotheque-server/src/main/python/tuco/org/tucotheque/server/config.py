import os

from pyhocon import ConfigFactory

TUCOTHEQUE_CONFIG = os.getenv("TUCOTHEQUE_CONFIG", None)

# Config
config = ConfigFactory.parse_file(
            os.path.join(TUCOTHEQUE_CONFIG))

def get(key, default=None):
    return config.get(key, default)