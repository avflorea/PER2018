import socket

PORT = 8090
IP = '212.128.255.131'
MAX_OPEN_REQUESTS = 2

# Numero de conexiones establecidas, para llevar la cuenta
# en la pantalla
n = 0

# Crear un socket para recibir peticiones
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Obtener el nombre del servidor, del sistema
# hostname = socket.gethostname()

try:
    # Asociar el socket a este servidor y el puerto elegido
    serversocket.bind((IP, PORT))

    # Configurar el socket: modo servidor
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:

        # Esperar conexiones
        print()
        print("Esperando Conexiones en {} {}".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Se ha recibido una conexión de un cliente
        # Incrementar el numero de conexiones y mostrar informacion
        # sobre la conexion recibida
        n += 1
        print("Conexion {}".format(n))
        print(clientsocket)
        print("Conexion desde: {}".format(address))

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
