import tkinter as tk
import socket
from Project_Canvas_Screen import CanvasScreen

def main():
    HOST_IP = '192.168.1.24'
    DST_PORT = 1729
    my_socket = socket.socket()

    try:
        my_socket.connect((HOST_IP, DST_PORT))
    except socket.error as exc:
        print("no server is waiting....")
        exit()

    client_canvas_obj = CanvasScreen()
    client_canvas_obj.run_canvas()

    # my_socket.close()

    if __name__ == "__main__":
        main()