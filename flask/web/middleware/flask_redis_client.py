import redis


def get_redis_client():
    return redis.Redis(host='redis.flaskapp.local', port=6379, password='SeCrEtPaSsWoRd', decode_responses=True)
