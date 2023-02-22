#include <stdio.h>
#include <winsock2.h>
#include <ws2tcpip.h>
#include <stdio.h>

/* Ws2_32.lib1をリンク時に追加するコメント */
#pragma comment(lib, "Ws2_32.lib")

int main(int argc, char* argv[]) {
    /* IP アドレス、ポート番号、ソケット */
    char destination[80] = "127.0.0.1";
    unsigned short port = 8080;
    int dstSocket;

    /* sockaddr_in 構造体 */
    struct sockaddr_in dstAddr;
    /* 各種パラメータ */
    int status;
    int numsnt;
    /*const char* send_data = "this is test";*/
    const char* send_data = argv[1];

    /************************************************************/

    /* Windows 独自の設定 */
    WSADATA data;
    WSAStartup(MAKEWORD(2, 0), &data);

    /* 相手先アドレスの入力 */
    /* 通信する相手をハードコーディングしたためコメントアウト */
    /*printf("Connect to ? : (name or IP address) ");
    scanf("%s", destination);*/

    /* sockaddr_in 構造体のセット */
    memset(&dstAddr, 0, sizeof(dstAddr));
    dstAddr.sin_port = htons(port);
    dstAddr.sin_family = AF_INET;
    dstAddr.sin_addr.s_addr = inet_addr(destination);

    /* ソケット生成 */
    dstSocket = socket(AF_INET, SOCK_STREAM, 0);

    /* 接続 */
    connect(dstSocket, (struct sockaddr*)&dstAddr, sizeof(dstAddr));

    /* パケット送出 */
    send(dstSocket, send_data, strlen(send_data) + 1, 0);

    /* Windows 独自の設定 */
    closesocket(dstSocket);
    WSACleanup();
}
