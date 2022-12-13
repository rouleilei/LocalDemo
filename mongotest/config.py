import motor.motor_asyncio
import typing

CONNECTORS = {
    'MONGODB': motor.motor_asyncio.AsyncIOMotorClient,
}
ENABLED_DATABASES = (
    'MONGODB',
)
_MONGODB_HOST = 'mongodb://localhost:27017'

POOLS = {db: None for db in ENABLED_DATABASES}


class Config(object):
    # mongodb config
    MONGODB_document_class = dict
    MONGODB_tz_aware = False
    MONGODB_connect = True
    MONGODB_maxPoolSize = 2 << 5
    MONGODB_minPoolSize = 2 << 0
    MONGODB_maxIdleTimeMS = None
    MONGODB_socketTimeoutMS = None
    MONGODB_connectTimeoutMS = 20 * 1000

    # MONGODB_retryWrites = False

    @classmethod
    def get_config_by_prefix(cls, prefix: str) -> typing.Mapping:
        if not prefix.isupper():
            prefix = prefix.upper()
        config = {}
        for key in dir(cls):
            if key.startswith(prefix):
                k = '_'.join(key.split('_')[1:])
                config[k] = getattr(cls, key)
        return config


class DevelopConfig(Config):
    # mongodb overwrites
    COLLECTION = 'python_db'
    MONGO_DB = 'user'
    MONGODB_host = _MONGODB_HOST
    MONGODB_maxPoolSize = 2 << 3
    MONGODB_minPoolSize = 2 << 0


Conf = DevelopConfig()
