from sanic import Blueprint
from sanic.response import json

from app.cache import CacheHandler

cms_router = Blueprint('cms', url_prefix='/',)

@cms_router.route('/', methods=['GET'])
async def home(request):
    cache_handler = CacheHandler(request)
    counter_name = 'hits'
    
    await cache_handler.incr(counter_name)
    visitor_count = await cache_handler.get(counter_name)

    return json({
        'hello': 'world',
        'visitor_count': visitor_count,
    })