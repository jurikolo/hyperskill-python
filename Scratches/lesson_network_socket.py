import socket

# OLD WAY OF WORKING WITH SOCKETS
# creating the socket
client_socket = socket.socket()
hostname = '127.0.0.1'
port = 9090
address = (hostname, port)

# connecting to the server
client_socket.connect(address)

data = 'Wake up, Neo'
# converting to bytes
data = data.encode()

# sending through socket
client_socket.send(data)

# receiving the response
response = client_socket.recv(1024)

# decoding from bytes to string
response = response.decode()
print(response)

client_socket.close()

# THE NEW WAY
# working with a socket as a context manager
with socket.socket() as client_socket:
    hostname = '127.0.0.1'
    port = 9090
    address = (hostname, port)

    client_socket.connect(address)

    data = 'Wake up, Neo'
    data = data.encode()

    client_socket.send(data)

    response = client_socket.recv(1024)

    response = response.decode()
    print(response)