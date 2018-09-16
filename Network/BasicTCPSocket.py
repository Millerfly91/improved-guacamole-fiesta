import socket
import sys
import time


class BasicTCPSocket:
    HOST, PORT = "", 9999
    sock = ""

    def __init__(self):
        self.HOST, self.PORT = "192.168.1.21", 1109
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.HOST, self.PORT = host, port
        print("Attempting to connect to {}:{}".format(self.HOST, self.PORT))
        self.sock.connect((self.HOST, self.PORT))

    def bind(self, port):
        self.HOST, self.PORT = "192.168.1.20", port
        print("Attempting to bind to {}:{}".format(self.HOST, self.PORT))
        self.sock.bind((self.HOST, self.PORT))

    def disconnect(self):
        self.sock.close()

    def sendMessage(self, message):
        self.sock.sendall(bytes(message + "\n", "utf-8"))
        received = str(self.sock.recv(1024), "utf-8")
        print("Sent:     {}".format(message))
        print("Received: {}".format(received))

    def listen(self):
        self.sock.listen(1)
        print("Listening on port []".format(self.PORT))
        while True:
            print(sys.stderr, 'waiting for a connection')
            connection, client_address = self.sock.accept()
            try:
                print(sys.stderr, 'client connected:', client_address)
                while True:
                    data = connection.recv(16)
                    print(sys.stderr, 'received ', data)
                    if data:
                        connection.sendall(data)
                    else:
                        break
            finally:
                connection.close()


if __name__ == "__main__":
    testsock = BasicTCPSocket()
    testip = "192.168.1.20"
    testsock.setAddress(testip, 1109)
    heard = testsock.listen()
    print(" I heard : {} from {}".format(heard, testip))
    # testsock.setAddress("192.168.1.21", 1109)
    # testsock.sendMessage("pen islandS")
    # testsock.sendMessage("Test 2")
    # testsock.sendMessage("TEST 3 TEST 2 TEST # TEST 3 TEST 3 TEST 3 TEST3")
