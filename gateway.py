from blinker import signal

class Callback:

    @classmethod
    def on_server_connected(cls, sender):
        pass

class ConnectionPool:
    def __init__(self) -> None:
        pass 

    def add(conenction_obj, type_):
        ready = signal(f'{type_}_connected')
        ready.connect(Callback.on_server_connected)

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
