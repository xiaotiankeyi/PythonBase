from redis import Redis
from redis import StrictRedis


# conn = Redis(host='192.168.0.121', port=6380, db=0)
conn = Redis(host='192.168.0.121', port=6379, db=0, decode_responses=True)

print(conn)
print(conn.keys())
# print(conn.get('k3'))
# conn.set('name','tom')

if __name__ == "__main__":
    pass