#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 8080
#define BUFFER_SIZE 1024

int main() {
    int sockfd;
    char buffer[BUFFER_SIZE];
    struct sockaddr_in servaddr, cliaddr;
    socklen_t addrlen = sizeof(cliaddr);

    // Create socket
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Set up server address structure
    bzero(&servaddr, sizeof(servaddr));
    servaddr.sin_family = AF_INET;
    servaddr.sin_addr.s_addr = INADDR_ANY;
    servaddr.sin_port = htons(PORT);

    // Bind the socket to the address
    if (bind(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) < 0) {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }

    printf("UDP server is running...\n");

    // Receive data from client
    while (1) {
        ssize_t recv_len;
        if ((recv_len = recvfrom(sockfd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&cliaddr, &addrlen)) == -1) {
            perror("recvfrom failed");
            exit(EXIT_FAILURE);
        }
        buffer[recv_len] = '\0'; // Null-terminate the received data

        // Print received data and client address
        printf("Received from %s:%d: %s\n", inet_ntoa(cliaddr.sin_addr), ntohs(cliaddr.sin_port), buffer);

        // Send a response (optional)
        // sendto(sockfd, "Hello from server!", strlen("Hello from server!"), 0, (struct sockaddr *)&cliaddr, addrlen);
    }

    // Close the socket (won't be reached in an infinite loop)
    close(sockfd);

    return 0;
}
