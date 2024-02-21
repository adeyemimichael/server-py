#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#define PORT 8080
#define MAXLINE 1024

int main() {
    int sockfd;
    char buffer[MAXLINE];
    struct sockaddr_in servaddr;

    // Create socket file descriptor
    if ((sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    memset(&servaddr, 0, sizeof(servaddr));

    // Filling server information
    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);
    servaddr.sin_addr.s_addr = INADDR_ANY;

    // Prompt user to enter a message to send to the server
    printf("Enter message to send to server : ");
    fgets(buffer, sizeof(buffer), stdin);

    // Send message to server
    sendto(sockfd, (const char *)buffer, strlen(buffer),
        0, (const struct sockaddr *)&servaddr,
        sizeof(servaddr));
    printf("Message sent to server.\n");

    // Receive message from server
    int n = recvfrom(sockfd, (char *)buffer, MAXLINE,
                     0, (struct sockaddr *)&servaddr,
                     &(socklen_t){sizeof(servaddr)});
    buffer[n] = '\0';
    printf("Server: %s\n", buffer);

    // Close the socket
    close(sockfd);

    return 0;
}
