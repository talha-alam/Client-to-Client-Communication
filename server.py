import socket
import threading

# Choose a port that is free
# An IPv4 address is obtained for the server.   
PORT=5000
SERVER=socket.gethostbyname(socket.gethostname())
ADDRESS= (SERVER, PORT)
# the format in which encoding and decoding will occur
FORMAT="utf-8"

# Lists that will contain all the clients connected to 
# the server and their names.
clients=[]
names=[]

# Create a new socket for the server and
# bind the address of the server to the socket 
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDRESS)

# method to start the connection
def startChat():
	print("server is working on "+SERVER)
	# listening for connections 
	server.listen()
	while True:
		# accept connections
		# returns a new connection to the client and 
		# the address bound to it 
		conn, addr= server.accept()
		conn.send("NAME".encode(FORMAT))
		# 1024 represents the max amount of data that can be received (bytes)
		name=conn.recv(1024).decode(FORMAT)
		names.append(name)
		clients.append(conn)
		print(f"Name is :{name}")
		broadcastMessage(f"{name} has joined the chat!".encode(FORMAT))
		conn.send('Connection successful!'.encode(FORMAT))
		# Start the handling thread
		thread=threading.Thread(target=handle, args=(conn, addr))
		thread.start()
		# no. of clients connected to the server
		print(f"active connections {threading.activeCount()-1}")

# method to handle the incoming messages 
def handle(conn, addr):
	print(f"new connection {addr}")
	connected=True
	while  connected:
		message=conn.recv(1024)
		broadcastMessage(message)
	conn.close()

# method for broadcasting messages to the clients
def broadcastMessage(message):
    for client in clients:
        client.send(message)

# call the method to begin the communication
startChat()