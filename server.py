from sanic import Sanic
from sanic_redis import SanicRedis
from aoiklivereload import LiveReloader

from common.config import MODULES
from importlib import import_module


if __name__ == "__main__":
    reloader = LiveReloader()
    reloader.start_watcher_thread()
    
    app = Sanic(__name__)
    app.config.update({
        'REDIS': {
            'address': ('redis', 6379),
        }
    })
    redis = SanicRedis()
    redis.init_app(app)
    for module_name in MODULES:
        module = import_module(module_name)
        print("Initializing route %s" % module.blueprint)
        app.blueprint(module.blueprint)

    app.run(host="0.0.0.0", port=5000)