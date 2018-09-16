from Network import BasicTCPSocket as MySocket
import time
from decimal import Decimal as Decimal


class MiscTools:
    # socket = BasicTCPSocket();
    # HOST, PORT = "192.168.1.21", 1109
    HOST = "192.168.1.20"
    HOSTPORT = 1109

    @staticmethod
    def singleMessage(host, port, msg):
        TWOPLACES = Decimal(10) ** -3
        start = time.time()
        sock = MySocket.BasicTCPSocket()
        sock.connect(host, port)
        sock.sendMessage(msg)
        sock.disconnect()
        end = time.time()
        print("Time to send singleMessage: ",
              Decimal((end - start) * 1000).quantize(TWOPLACES),
              " ms")

    @staticmethod
    def listenOnPort(port):
        TWOPLACES = Decimal(10) ** -3
        start = time.time()
        sock = MySocket.BasicTCPSocket()
        sock.bind(port)
        sock.listen()
        sock.disconnect()
        end = time.time()
        print("Time to send singleMessage: ",
              Decimal((end - start) * 1000).quantize(TWOPLACES),
              " ms")


if __name__ == "__main__":
    # MiscTools.singleMessage("192.168.1.21", 1109, "Test James")
MiscTools.listenOnPort(1109)
