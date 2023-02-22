import os
import socket

class BlockingServerBase:
    def __init__(self, timeout:int=1024, buffer:int=1024):
        self.__socket = None
        self.__timeout = timeout
        self.__buffer = buffer
        self.close()

    def __del__(self):
        self.close()

    def close(self) -> None:
        try:
            self.__socket.shutdown(socket.SHUT_RDWR)
            self.__socket.close()
        except:
            pass

    def accept(self, address, family:int, typ:int, proto:int) -> None:
        while True:
            self.__socket = socket.socket(family, typ, proto)#socketオブジェクトを生成
            self.__socket.settimeout(self.__timeout)
            self.__socket.bind(address)#adress:("localhost",8080)
            self.__socket.listen(1)#同時接続数
            print("Server started :", address)
            conn, _ = self.__socket.accept()#connは接続を通じてデータの送受信を行うための新しいソケットオブジェクト,_は無視

            while True:
                try:
                    #ここにプログラムを記述############################################################################
                    message_recv = conn.recv(self.__buffer).decode('utf-8')#recvの返り値はbytes オブジェクト
                    message_resp = self.respond(message_recv)
                    conn.send(message_resp.encode('utf-8'))
                    #################################################################################################
                except ConnectionResetError:
                    break
                except BrokenPipeError:
                    break
                except ConnectionAbortedError: 
                    break
            self.close()

    def respond(self, message:str) -> str:  #プロトタイプ宣言みたいなものかな？下で定義してる。
        return ""
    
class InetServer(BlockingServerBase):
    def __init__(self, host:str="localhost", port:int=8080) -> None:
        self.server=(host,port)
        super().__init__()
        self.accept(self.server, socket.AF_INET, socket.SOCK_STREAM, 0)

    def respond(self, message:str) -> str:  #この関数の返り値はどこでも使ってない。
        print("received -> ", message)
        return "Server accepted !!"

if __name__=="__main__":
    InetServer()