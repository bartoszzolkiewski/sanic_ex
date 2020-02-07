from sanic import Sanic
from sanic_redis import SanicRedis
import sys
from aoiklivereload import LiveReloader

from app.config import MODULES, APP_CONFIG
from importlib import import_module


app = Sanic(__name__)

if __name__ == "__main__":
    app.config.update({
        'REDIS': {
            'address': ('redis', 6379),
        }
    })
    redis = SanicRedis()
    redis.init_app(app)

    for module_name in MODULES:
        module = import_module(module_name)
        print("Initializing route for module: %s" % module.__name__)
        app.blueprint(module.blueprint)

    app.run(**APP_CONFIG)