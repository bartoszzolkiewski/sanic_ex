class CacheHandler(object):
    def __init__(self, request):
        self._connector = request.app.redis

    async def incr(self, variable_name):
        with await self._connector as r:
            await r.incr(variable_name)

    async def get(self, variable_name):
        with await self._connector as r:
            return await r.get(variable_name)