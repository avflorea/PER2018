import socket

PORT = 8091
IP = "212.128.255.131"
MAX_OPEN_REQUESTS = 5
SERVICE_PRICE_EUROS = 20
# RMB is the China currency: Renminbi is the currency, Yuan is the unit
SERVICE_PRICE_RM = SERVICE_PRICE_EUROS/0.13
SERVICE_PRICE_DOLLARS = SERVICE_PRICE_EUROS * 1.22


def process_client(clientsocket):
    print(clientsocket)
    send_message = "Hola desde el servidor: %i€ needed\n" % SERVICE_PRICE_EUROS
    # utf8 supports all lanaguages chars
    send_message += "你好从服务器：需要: %i¥ 需要\n" % SERVICE_PRICE_RM
    send_message += "Hello from the server: %i$ needed\n" % SERVICE_PRICE_DOLLARS
    # Serializing the data to be transmitted
    send_bytes = str.encode(send_message)
    # We must write bytes, not a string
    clientsocket.send(send_bytes)
    clientsocket.close()


# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
