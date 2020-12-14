import tkinter as tk
import socket
from Project_Canvas_Screen import CanvasScreen

def main():
    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", 1729))
    server_socket.listen(1)

    (client_socket, client_address) = server_socket.accept()

    server_canvas_obj = CanvasScreen()
    server_canvas_obj.run_canvas()

    # client_socket.close()
    # server_socket.close()


if __name__ == "__main__":
    main()