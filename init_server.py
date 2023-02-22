import socket
import GUI

set_AF_INET = socket.AF_INET
set_SOCK_STREAM = socket.SOCK_STREAM



class BlockingServerBase:
    def __init__(self, timeout:int=1024, buffer:int=1024):
        self.__socket = None
        self.__timeout = timeout
        self.__buffer = buffer

    def __del__(self):
        self.close()

    def close(self) -> None:
        try:
            self.__socket.shutdown(socket.SHUT_RDWR)
            self.__socket.close()
        except:
            pass
        
    def app(self):
        return ""

    def accept(self, address, family:int, typ:int, proto:int) -> None:
        window = GUI.init_window()
        while True:             
            event, values = window.read(timeout = 0) #timeoutを0にすることで無理やりguiの入力をスキップしてデータ受信に制御を移している。入力を利用したい場合問題が発生する。
            self.__socket = socket.socket(family, typ, proto)#socketオブジェクトを生成
            self.__socket.settimeout(self.__timeout)
            self.__socket.bind(address)#adress:("localhost",8080)
            self.__socket.listen(1)#同時接続数
            conn, _ = self.__socket.accept()#connは接続を通じてデータの送受信を行うための新しいソケットオブジェクト,_は無視
            while True:
                try:
                    message_recv = conn.recv(self.__buffer).decode('utf-8')#recvの返り値はbytes オブジェクト
                    self.app(message_recv,window,event,values)#アプリケーションに受け取った値を渡す
                    break
                except ConnectionResetError:
                    break
                except BrokenPipeError:
                    break
                except ConnectionAbortedError: 
                    break
            self.close()
            
            """ try: #socketのtimeoutを使って制御をguiに戻すことを考えたが、結局根本的な問題解決ではないのでコメントアウト
                conn, _ = self.__socket.accept()#connは接続を通じてデータの送受信を行うための新しいソケットオブジェクト,_は無視
                while True:
                    try:
                        message_recv = conn.recv(self.__buffer).decode('utf-8')#recvの返り値はbytes オブジェクト
                        self.app(message_recv,window,event,values)#アプリケーションに受け取った値を渡す
                        break
                    except ConnectionResetError:
                        break
                    except BrokenPipeError:
                        break
                    except ConnectionAbortedError: 
                        break
                self.close()
            except TimeoutError:
                self.close() """

        

    
class InetServer(BlockingServerBase):
    def __init__(self, host:str="localhost", port:int=8080) -> None:
        self.server=(host,port)
        super().__init__()


    