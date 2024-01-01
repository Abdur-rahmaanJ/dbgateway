from blinker import signal

class Callback:

    

    @classmethod
    def general(cls, type_):
        return cls.methods[type_]

    @classmethod
    def on_server_connected(cls, sender):
        pass

    @classmethod
    def methods(cls):
        return {
        'on_server_connected': cls.on_server_connected
    }

class ConnectionPool:
    def __init__(self) -> None:
        pass 

    def add(conenction_obj, type_):
        ready = signal(f'{type_}_connected')
        ready.connect(Callback.methods['on_server_connected'])

    def remove(connection_obj):
        pass 


class DatabaseGateway:
    def __init__(self) -> None:
        self.pools = {
            'servers': ConnectionPool(),
            'clients': ConnectionPool()
        }

    def pass_to_server(self, connection_obj):
        pass 


    def run_server(self):
        pass 

    def load_plugins(self):
        pass 
