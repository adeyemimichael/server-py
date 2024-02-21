import socket

PORT = 8080
BUFFER_SIZE = 1024

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address
sock.bind(('0.0.0.0', PORT))

print("UDP server is running...")

# Receive data from client
while True:
    try:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        print(f"Received from {addr[0]}:{addr[1]}: {data.decode()}")

        # Send a response (optional)
        # sock.sendto(b"Hello from server!", addr)
    except BlockingIOError:
        pass

# Close the socket
sock.close()
