# !/usr/bin/env python
# _*_coding:utf-8_*_

from MyServers.MySocketServer.socketserver_main import MySocketServer


def run_socket_server():
    server_address = ("127.0.0.1", 7788)
    myServer = MySocketServer(server_address)
    myServer.run()


if __name__ == '__main__':
    run_socket_server()

