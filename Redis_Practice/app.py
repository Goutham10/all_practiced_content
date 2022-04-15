from typing import Mapping
import redis
import json

redis_host = 'localhost'
redis_port = 6379

def redis_string():
    try:
        r = redis.Redis(  host=redis_host, 
                                port=redis_port,
                                password='Goutham@1005',
                                decode_responses=True)
        # r.hset(name="user", key=12, value= 45, mapping=Mapping["key","goutham"] | None)
        # hash_var = r.hget("user")
        # print(hash_var)
        r.set("message","Hello redis")
        msg = r.get("message")
        username = r.get('name')
        print(username)
        print(msg)

        r.set('testing',json.dumps({
                                    "name": "goutham",
                                    "age" : 25,
                                    "company" : "scriptbees",
                                    "role" : "python developer",
                                    }))
        temp = r.get('testing')
        print(temp)
        # print(temp['name'])        
    except:
        print("something went wrong")
    
if __name__ == "__main__":
    redis_string()