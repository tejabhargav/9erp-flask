import os
import json
from dotenv import load_dotenv

class Config(object):
    """
    Common configurations
    
    Attrubutes:
        DEBUG: Enable/disable debug mode
        TESTING: Enable/disable testing mode
        MONGO_URI: MongoDB URI

    """

    basedir = os.path.abspath(os.path.dirname(__file__))

    load_dotenv(os.path.join(basedir, '../env', '.env'))
    MONGO_URI = os.environ.get('MONGO_URI')
    BASE_DOMAIN = os.environ.get('BASE_DOMAIN')