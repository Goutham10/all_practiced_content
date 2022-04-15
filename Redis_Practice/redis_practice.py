import redis

class Database:
    """In database class"""
    @classmethod
    def initialise(cls):
        connection_config = {
            'host' : 'localhost',
            'port' : 6379,
            # 'password' : 'Goutham@1005',
            'decode_responses' : 'True'
        }
        redis_conn = redis.ConnectionPool(max_connections=10, **connection_config)
        # print(redis_conn.get_connection)
        
        r = redis.Redis(connection_pool=redis_conn)

        r.set('xyz', "jahfjksahskjsadjk")
        # print(r.keys())

        # print(r.get('xyz'))

        #sets Datatype

        r.sadd('pythonlist', "matplotlib", "pyplot", "graph", "test")
        r.sadd('pythonlist_1', "random", "flask", "django", "pyplot")
        # print(r.sinter( 'pythonlist', 'pythonlist_1'))
        # print(r.sunion('pythonlist', 'pythonlist_1'))
        print(r.sdiff('pythonlist', 'pythonlist_1'))
        #many more methods are there. try them

        #hashes

        r.hset('hero', 'name','prabhas')
        r.hset('hero', 'name', 'AA')

        # print(r.hgetall('hero'))


        #pipeline 
        pipeline = r.pipeline(transaction= True)
        pipeline.sadd('mylist', 'firstelement')
        pipeline.sadd('mylist', 'secondelement')
        pipeline.sadd('mylist', 'thirdelement')
        pipeline.sadd('mylist', 'fourthelement')
        pipeline.sadd('mylist', 'fivelement')
        # print(pipeline.smembers('mylist'))
        # print(pipeline.execute())


        with r.pipeline() as mypipe:
            print(mypipe.smembers('mylist'))
            print(mypipe.execute())
    
data = Database()
data.initialise()