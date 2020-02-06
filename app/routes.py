from sanic import Blueprint
from sanic.response import json

from common.cache import CacheHandler

app_router = Blueprint('app', url_prefix='/',)

@app_router.route('/home', methods=['GET'])
async def home(request):
    cache_handler = CacheHandler(request)
    counter_name = 'hits'
    
    await cache_handler.incr(counter_name)
    visitor_count = await cache_handler.get(counter_name)

    return json({
        'hello': 'world',
        'visitor_count': visitor_count,
    })