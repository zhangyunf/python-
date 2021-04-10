from pymongo import MongoClient

class Client(MongoClient):

    def __init__(self,
            host=None,
            port=None,
            document_class=dict,
            tz_aware=None,
            connect=None,
            type_registry=None,
            **kwargs):
        super(Client, self).__init__(host=host, port=port, document_class=document_class, tz_aware=tz_aware, connect=connect, type_registry=type_registry, **kwargs)



    def insert(self):
        pass

    def get(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

if __name__ == '__main__':
    clinet = MongoClient.__init__()