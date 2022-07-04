#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include<pthread.h>

int clnt_cnt = -1;
pthread_mutex_t  mutex = PTHREAD_MUTEX_INITIALIZER;
int clnt_socks[3];
void error_handling(char *message);

void* service_application(void *clnt_sock) {
	
	pthread_mutex_lock(&mutex);
	clnt_socks[++clnt_cnt] = clnt_sock;
	pthread_mutex_unlock(&mutex);

	char result;
	int bytes_read = 0;
	char nresult[1];
	int input;
	
	bytes_read = read(clnt_sock, input, sizeof(input));
	result = bytes_read;
	if(bytes_read >=0 || bytes_read<10)
	{
		result = 'A';
	}
	else
	{
		result = 'B';
	}
	nresult[0] = result;
	write(clnt_sock, nresult, sizeof(nresult));
	close(clnt_sock);
	pthread_exit(NULL);
}

#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<arpa/inet.h>
#include<sys/socket.h>

#define BUF_SIZE 1024
void error_handling(char *message);

int main(int argc, char *argv[]) {
	pthread_t thread[3];
	int sockfd, newsockfd;
	char recvBuf[BUF_SIZE];
	int str_len, i;

	struct sockaddr_in serv_adr, clnt_adr;
	socklen_t clnt_adr_sz;

	if (argc != 2) {
		printf("Usage: %s <port>\n", argv[0]);
		exit(1);
	}

	sockfd = socket(PF_INET, SOCK_STREAM, 0);
	if (sockfd == -1)
		error_handling("socket() error");

	memset(&serv_adr, 0, sizeof(serv_adr));
	serv_adr.sin_family = AF_INET;
	serv_adr.sin_addr.s_addr = htonl(INADDR_ANY);
	serv_adr.sin_port = htons(atoi(argv[1]));

	if (bind(sockfd, (struct sockaddr*)&serv_adr, sizeof(serv_adr)) == -1)
		error_handling("bind() error");

	if (listen(sockfd, 5) == -1)
		error_handling("listen() error");

	for (int i = 0; i < 4; i++) {
		clnt_adr_sz = sizeof(clnt_adr);
		newsockfd = accept(sockfd, (struct sockaddr*)&clnt_adr, &clnt_adr_sz);

		pthread_create(&thread[i], NULL, service_application, newsockfd);
		pthread_detach(thread[i]);
	}

	close(sockfd);
	return 0;
}

void error_handling(char *message) {
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(1);
}
