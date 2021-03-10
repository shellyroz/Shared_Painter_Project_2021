from Project_Client_Canvas_Trial import Client


def main():
    ip = '192.168.1.35'
    # ip = '172.19.225.89'
    port = 1730
    c = Client(ip, port)
    c.start()

if __name__ == '__main__':
    main()