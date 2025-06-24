import redis

r = redis.Redis(host='localhost', port=80, decode_responses=True)
print(r.smembers("user:0:genres"))