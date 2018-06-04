import redis

class RedisPool:
	pool = None
	def getConnect():
		if(RedisPool.pool == None):
			RedisPool.pool = redis.ConnectionPool(host='47.95.235.55',password='Admin888',port=6379)
		return redis.Redis(connection_pool=RedisPool.pool)