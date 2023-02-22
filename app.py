from init_server import InetServer, set_AF_INET , set_SOCK_STREAM

#ここがアプリケーション部分#######

def main(message,window,event,values):#この関数はデータを受信したときにそれを引数:messageに保持して動く
    window['-DATA-'].update(message)
    print(message)


################################

class create_server(InetServer):
    def __init__(self):
        super().__init__()
        
    def app(self,message,window,event,values):
        main(message,window,event,values)   
    
server = create_server()
server.accept(("localhost",8080), set_AF_INET, set_SOCK_STREAM, 0)