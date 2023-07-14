import socket


def main():
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    server_socket.listen()
    conn, add = server_socket.accept()  # wait for client
    with server_socket:
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.send(b"+PONG\r\n")




if __name__ == "__main__":
    main()
