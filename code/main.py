import socketserver
import datetime
import os

now = datetime.datetime.now().time().replace(microsecond = 0)
print("[" + str(now) + "] Server is Starting！")

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        now = datetime.datetime.now().time().replace(microsecond=0)
        print("[" + str(now) + "]Discover connections, from: " + str(self.client_address[0]))
        command = bytes()

        while True:
            next_char = self.request.recv(1)
            if next_char in [b"", b"\r", b"\n"]:
                break
            else:
                command += next_char

        try:
            now = datetime.datetime.now().time().replace(microsecond=0)
            print("[" + str(now) + "]utf-8 decoding: Command: " + command.decode("utf-8"))
            if command.decode("utf-8") == "/exit":
                now = datetime.datetime.now().time().replace(microsecond=0)
                print("[" + str(now) + "]Server down.")
                os._exit(0)

        except UnicodeDecodeError:
            now = datetime.datetime.now().time().replace(microsecond=0)
            print("[" + str(now) + "]gbk decoding: Command: " + command.decode("gbk"))
            if command.decode("gbk") == "/exit":
                now = datetime.datetime.now().time().replace(microsecond=0)
                print("[" + str(now) + "]Server down.")
                os._exit(0)

        print("-------------------------------")

if __name__ == "__main__":
    HOST, PORT = "localhost", 20121
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    now = datetime.datetime.now().time().replace(microsecond=0)
    print("[" + str(now) + "] Server start.")
    print("-------------------------------")
    server.serve_forever()
