import os 
import logging
from typing import List, Type

# You need to replace the next values with the appropriate values for your configuration
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    CONFIG_NAME = "base"
    USE_MOCK_EQUIVALENCY = False
    DEBUG = False
    PORT = os.getenv("APP_PORT") if os.getenv("APP_PORT") else 8000
    HOST = os.getenv("APP_HOST") if os.getenv("APP_HOST") else "0.0.0.0"


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True 



EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}


logging.basicConfig(
    # level=CONSTANTS.get("LOG_LEVEL"),
    format="%(asctime)s %(levelname)s: %(message)s " "[from %(message)s:%("
           "lineno)d]",
    datefmt="%Y%m%d-%H:%M%p",
)
logger = logging.getLogger('server')


