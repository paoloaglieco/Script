import socket
import threading

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(20)
        sock.connect((ip, port))
        print(f"[+] Port {port} is open")
        sock.close()
    except Exception as e:
        pass

def main():
    ip = "10.10.206.119"
    ports = range(1, 65536) 

    threads = []

    for port in ports:
        thread = threading.Thread(target=scan_port, args=(ip, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
