import socket
import threading

tables = {}

def create_table(tables, tablename):
    tables[tablename] = {}
    
def parse_sql(string):
    words = string.split()
    if words[0] == 'create':
        if words[1] == 'table':
             create_table(tables, words[2])
    
connection_pool = {
}



def handle_client(client_socket, addr):
    ip = addr[0]
    port = addr[1]
    try:
        while True:
            # receive and print client messages
            request = client_socket.recv(1024).decode("utf-8")
            parse_sql(request)
            if request.lower() == "close":
                client_socket.send("closed".encode("utf-8"))
                break
            print(f"Received: {request}")
            # convert and send accept response to the client
            response = "accepted"
            client_socket.send(response.encode("utf-8"))
    except Exception as e:
        print(f"Error when hanlding client: {e}")
    finally:
        client_socket.close()
        del connection_pool[f'{ip}:{port}']
        print(f"Connection to client ({ip}:{port}) closed")


def run_server():
    server_ip = "127.0.0.1"  # server hostname or IP address
    port = 8000  # server port number
    # create a socket object
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # bind the socket to the host and port
        server.bind((server_ip, port))
        # listen for incoming connections
        server.listen()
        print(f"Listening on {server_ip}:{port}")

        while True:
            # accept a client connection
            client_socket, addr = server.accept()
            client_ip = addr[0]
            client_port = addr[1]
            connection_pool[f'{client_ip}:{client_port}'] = {}
            print(f"Accepted connection from {client_ip}:{client_port}")
            # start a new thread to handle the client
            thread = threading.Thread(target=handle_client, args=(client_socket, addr,))
            thread.start()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.close()

if __name__ == '__main__':
    run_server()
