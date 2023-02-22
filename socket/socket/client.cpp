#include <stdio.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdio.h>

/* Ws2_32.lib1�������N���ɒǉ�����R�����g */
#pragma comment(lib, "Ws2_32.lib")

int main(int argc, char* argv[]) {
    /* IP �A�h���X�A�|�[�g�ԍ��A�\�P�b�g */
    char destination[80] = "127.0.0.1";
    unsigned short port = 8080;
    int dstSocket;

    /* sockaddr_in �\���� */
    struct sockaddr_in dstAddr;
    /* �e��p�����[�^ */
    int status;
    int numsnt;
    /*const char* send_data = "this is test";*/
    const char* send_data = argv[1];

    /************************************************************/

    /* Windows �Ǝ��̐ݒ� */
    WSADATA data;
    WSAStartup(MAKEWORD(2, 0), &data);

    /* �����A�h���X�̓��� */
    /* �ʐM���鑊����n�[�h�R�[�f�B���O�������߃R�����g�A�E�g */
    /*printf("Connect to ? : (name or IP address) ");
    scanf("%s", destination);*/

    /* sockaddr_in �\���̂̃Z�b�g */
    memset(&dstAddr, 0, sizeof(dstAddr));
    dstAddr.sin_port = htons(port);
    dstAddr.sin_family = AF_INET;
    dstAddr.sin_addr.s_addr = inet_addr(destination);

    /* �\�P�b�g���� */
    dstSocket = socket(AF_INET, SOCK_STREAM, 0);

    /* �ڑ� */
    connect(dstSocket, (struct sockaddr*)&dstAddr, sizeof(dstAddr));

    /* �p�P�b�g���o */
    send(dstSocket, send_data, strlen(send_data) + 1, 0);

    /* Windows �Ǝ��̐ݒ� */
    closesocket(dstSocket);
    WSACleanup();
}
