import socket
import threading


PORT=5000
SERVER="http://4fd149bd6cca.ngrok.io/"
ADDRESS= (SERVER, PORT)
FORMAT="utf-8"

name=input("ENTER YOUR NAME: ")

# Create a new client socket and connect to the server
client= socket.socket()
client.connect(ADDRESS)

def receive():
	while True:
		try:
			message = client.recv(1024).decode(FORMAT)
			if message == 'NAME':
				# server asks for the name
				client.send(name.encode(FORMAT))
			else:
			    print(message)
		except:
		    print("An error occured!")
		    # close the connection if an error has occured
		    client.close()
		    break 		

# method to send messages
def sendMessage():
	while True:
		message = (f"{name}: {input('')}")
		client.send(message.encode(FORMAT))

# method to receive messages

# threads for receiving and sending
rcv = threading.Thread(target=receive)
rcv.start()

snd= threading.Thread(target=sendMessage)
snd.start()