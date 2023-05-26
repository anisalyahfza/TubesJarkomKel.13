#Prepare a sever socket
from socket import *


#Fill in start
serverSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 80
serverSocket.bind(("localhost", serverPort))
serverSocket.listen(1)
#Fill in end
while True:

    #Establish the connection

    print ("Siap Untuk Dipakai...")

    connectionSocket, addr = serverSocket.accept()

    #Fill in end

    try:

        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open (filename [1:])
        outputdata = f.read()
        #Send one HTTP header line into socket
        header = "HTTP/1.1 200 OK\nContent-Type:text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        #Send the content of the requested file to the client
        for i in range (0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            
        connectionSocket.send("\r\n".encode())
        connectionSocket.close() 
    except IOError:
        
        #send response message forfile not found
        #FILL in start
       
        error = 'HTTP/1.1 404 Not Found\r\nContent-Type:text/html\r\n\r\n'
        connectionSocket.send(error.encode())
        connectionSocket.send()
        
        #Fill in end

        #Close client socket

        #Fill in start
        connectionSocket.close()
        #Fill in end

serverSocket.close()

sys.exit() #Terminate the program after sending the corresponding data