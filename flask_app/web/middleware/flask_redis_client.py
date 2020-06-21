import redis


def get_redis_client():
    return redis.Redis(host = '172.28.1.4', port = 6379, password = 'SeCrEtPaSsWoRd', decode_responses = True)
