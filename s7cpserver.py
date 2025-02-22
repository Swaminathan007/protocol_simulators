import socket

def start_server(host, port):
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the port
    server_address = (host, port)
    print(f"Starting up on {server_address[0]} port {server_address[1]}")
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print("Waiting for a connection...")
        connection, client_address = sock.accept()
        try:
            print(f"Connection from {client_address}")

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(1024)
                if data:
                    # Here you would typically decode the S7comm-Plus packet, but for now, we'll just print it as hex
                    print(f"Received data: {data.hex()}")
                    # Optionally, send back some acknowledgment or response if required by the protocol
                    # connection.sendall(data)
                else:
                    # No more data from the client, close this connection
                    print("No data from client, closing connection")
                    break
        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    HOST = '0.0.0.0'  # Listen on all interfaces
    PORT = 102  # Example port, adjust according to where S7comm-Plus typically communicates
    start_server(HOST, PORT)