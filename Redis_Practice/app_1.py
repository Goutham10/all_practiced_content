# import random
# import redis
# import json

# r = redis.Redis(db=0)
# # print(r)

# random.seed(444)
# hats = {f"hat:{random.getrandbits(32)}": i for i in (
#     {
#         "color": "black",
#         "price": 49.99,
#         "style": "fitted",
#         "quantity": 1000,
#         "npurchased": 0,
#     },
#     {
#         "color": "maroon",
#         "price": 59.99,
#         "style": "hipster",
#         "quantity": 500,
#         "npurchased": 0,
#     },
#     {
#         "color": "green",
#         "price": 99.99,
#         "style": "baseball",
#         "quantity": 200,
#         "npurchased": 0,
#     })
# }

# # print(hats)

# # with r.pipeline() as pipe:
# #     for h_id, hat in hats.items():
# #         pipe.hset(h_id, hat)
# #     pipe.execute()

# r.bgsave()


# r.set("test1" ,json.dumps(hats))
# json.loads(r.get('test1'))


# # for key in sorted(r.keys('test1')):
# # print(r.get('test1'))


# for i in sorted(r.keys('test1')):
#     print(i)



import redis
from redis.commands.json.path import Path

client = redis.Redis(host='localhost', port=6379, db=0)

jane = {
     'name': "Jane", 
     'Age': 33, 
     'Location': "Chawton"
   }

client.json().set('person:1', Path.root_path(), jane)

result = client.json().get('person:1')
print(result)