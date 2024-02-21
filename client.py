import socket
import ipywidgets as widgets

PORT = 8080
MAXLINE = 1024

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Filling server information
servaddr = ('127.0.0.1', PORT)  # Assuming the server is running locally

# Define text input widget
text_input = widgets.Text(placeholder="Enter message to send to server")
display(text_input)

def send_message(sender):
    message = text_input.value.encode()
    sock.sendto(message, servaddr)
    print("Message sent to server.")

# Define event handler for text input
text_input.on_submit(send_message)

# Receive message from server
while True:
    data, _ = sock.recvfrom(MAXLINE)
    print("Server:", data.decode())

# Close the socket (this won't be reached in an infinite loop)
sock.close()
