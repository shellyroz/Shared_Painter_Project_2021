import socket
import threading
from Project_Screens_trial import SampleApp
from Project_Canvas_Screen import CanvasScreen
import pickle

class Server(object):

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.count = 0

    def start(self):
        try:
           print('server starts up on ip %s port %s' % (self.ip, self.port))
           # Create a TCP/IP socket
           sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           sock.bind((self.ip, self.port))
           sock.listen(3)

           while True:
                print('waiting for a new client')
                # block
                clientSocket, client_address = sock.accept()

                # print('new client entered')
                i = 1
                print('client number ' + str(i) + ' entered')
                i = i + 1

                # send receive example
                clientSocket.sendall('Hello this is server'.encode())
                msg = clientSocket.recv(1024)
                print('received message: %s' % msg.decode())
                self.count += 1
                print(self.count)
                # implement here your main logic
                self.handleClient(clientSocket, self.count)
        except socket.error as e:
            print(e)

    def handleClient(self, clientSock, current):
        print("hello")
        client_handler = threading.Thread(target=self.handle_client_connection, args=(clientSock, current,))
        # without comma you'd get a... TypeError: handle_client_connection() argument after * must be a sequence, not _socketobject
        client_handler.start()

    def handle_client_connection(self, client_socket, current):
        # request = client_socket.recv(1024).decode()
        # if request == "PAINT":
        #     client_socket.sendall("OK".encode())
        #     # server_canvas = CanvasScreen()
        #     # server_canvas.design_canvas_screen()
        #     while True:
        #         if client_socket.recv(1024).decode() == "re":
        #             color_pos = pickle.loads(client_socket.recv(16384))
        #             print(color_pos)
        server_canvas = CanvasScreen()
        server_canvas.design_canvas_screen()
        server_canvas.run_canvas_for_server()
        while True:
            if client_socket.recv(1024).decode() == "re":
                color_pos = pickle.loads(client_socket.recv(16384))
                print(color_pos)
                for tup in color_pos:
                    server_canvas.color_pixel_for_server(server_canvas.photo, tup[1], tup[0])
                    server_canvas.root.mainloop()





        client_socket.close()



if __name__ == '__main__':
   ip = '0.0.0.0'
   port = 1730
   s = Server(ip, port)
   # s.start()
   server_thread = threading.Thread(target=s.start)
   server_thread.start()
   # login = tk.Button(root, text="PARTICIPENTS", command=server_thread.start, font=('Eras Bold ITC', 16),
   #                   fg="midnight blue")
   # login.place(x=60, y=50)
