import socket
import time

ip = '216.107.139.152'
port = 1337

def get_flag(ip, port):
    flag = ''
    
    for i in range(104):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            initial_prompt = s.recv(1024).decode()
            s.sendall(f'{i}\n'.encode())
            time.sleep(0.1)
            data = s.recv(1024).decode()
            
            if "Character at index" in data:
                char = data.split()[-1].strip()
                flag += char
                print(f'Flag: {flag}')
            else:
                print(f'Unexpected data: {data}')
                
        print(f'Flag: {flag}')

get_flag(ip, port)