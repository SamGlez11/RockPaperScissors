import socket
import pickle

class NetworkHost:
    """Network class for the host player (running on same machine as server)"""
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"  # Connect to local server
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(1024).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(1024))
        except socket.error as e:
            print(e)

class NetworkRemote:
    """Network class for remote players (connecting from different computers)"""
    def __init__(self, host_ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = host_ip  # Connect to host's IP
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(1024).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(1024))
        except socket.error as e:
            print(e)

# Default Network class (for backward compatibility)
class Network(NetworkHost):
    pass
