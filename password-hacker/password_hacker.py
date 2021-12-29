import socket
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("hostname")
parser.add_argument("port")
parser.add_argument("message")

args = parser.parse_args()
hostname = args.hostname
port = int(args.port)
message = args.message

with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)

    data = message.encode()

    client_socket.send(data)

    response = client_socket.recv(1024)

    response = response.decode()
    print(response)
