import socketserver


class MyServerRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print("from conn:", self.request)


class MySocketServer(object):

    def __init__(self, server_address):
        self.socket = socketserver.ThreadingTCPServer(server_address, MyServerRequestHandler)

    def run(self):
        self.socket.serve_forever()
