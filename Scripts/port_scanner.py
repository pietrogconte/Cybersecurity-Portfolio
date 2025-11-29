#!/usr/bin/env python3
"""
Port Scanner Simples
Autor: Pietro Giacomin Conte
Data: 2025
Descrição: Scanner de portas básico usando socket
"""

import socket
import sys
from datetime import datetime

def scan_port(target, port):
    """
    Tenta conectar a uma porta específica do alvo.
    Retorna True se a porta estiver aberta, False caso contrário.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except socket.error:
        return False

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 port_scanner.py <IP_ALVO>")
        sys.exit(1)
    
    target = sys.argv[1]
    
    print("-" * 50)
    print(f"Escaneando alvo: {target}")
    print(f"Início: {datetime.now()}")
    print("-" * 50)
    
    # Portas mais comuns
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389, 8080, 8443]
    
    open_ports = []
    
    for port in common_ports:
        if scan_port(target, port):
            print(f"[+] Porta {port} está ABERTA")
            open_ports.append(port)
        else:
            print(f"[-] Porta {port} está fechada")
    
    print("-" * 50)
    print(f"Scan completo: {datetime.now()}")
    print(f"Total de portas abertas: {len(open_ports)}")
    print("-" * 50)

if __name__ == "__main__":
    main()
