# Arquivo: port_scan.py
# Funçao: Scannear portas
# Autor: Joni
# Data: 16/06

import argparse
import socket
import threading
import pyfiglet
import time


def port_scan(tgt_host, tgt_ports):
    ascii_banner = pyfiglet.figlet_format("port scanner")
    print(
        f'{ascii_banner}\n[+] Joni escaneador de portas\n[+] Alvo: {tgt_host}\n[+] Portas: {tgt_ports}')
    time.sleep(2)
    try:
        tgt_ip = socket.gethostbyname(tgt_host)
    except socket.herror:
        print(f'[-] Não decifrei {tgt_host}: É desconhecido')
        return
    try:
        tgt_name = socket.gethostbyaddr(tgt_ip)
        print(f'\n[+] Resultados do pente fino feito em: {tgt_name[0]}')
        time.sleep(2)
    except socket.herror:
        print(f'\n[+] Resultados do: {tgt_ip}')

    socket.setdefaulttimeout(1)

    for ports in tgt_ports:
        t = threading.Thread(target=conn_scan, args=(tgt_host,int(ports)))
        t.start()


def conn_scan(tgt_host, tgt_ports):
    screen_lock = threading.Semaphore()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn_sckt:
        try:
            conn_sckt.connect((tgt_host, tgt_ports))
            conn_sckt.send(b'aaa\r\n')
            results = conn_sckt.recv(100).decode('utf-8')
            screen_lock.acquire()
            print(f'[+] {tgt_ports}/tcp open')
            print(f'[>] Resultados\n{results}\n[-]')
            time.sleep(1)
        except OSError:
            screen_lock.acquire()
            print(f'[-] {tgt_ports}/tcp closed')
            time.sleep(1)
        finally:
            screen_lock.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage='port_scan.py TARGET_HOST -p TARGET_PORTS'
        '\nexample: python3 port_scan.py scanme.nmap.org -p 21,80'
    )
    parser.add_argument('tgt_host', type=str,
                        metavar='TARGET_HOST', help='[?] host alvo')
    parser.add_argument('-p', required=True, metavar='TARGET_PORTS',
                        help='[?] porta[s] separadas por virgulas')

    args = parser.parse_args()

    args.tgt_ports = str(args.p).split(',')
    port_scan(args.tgt_host, args.tgt_ports)
