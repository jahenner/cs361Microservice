#!/usr/bin/env python3

from socket import *
from datetime import datetime
import json

def compound_interest(data: dict) -> dict:
    needed_params = ["principal", "rate_of_interest", "number", "time"]
    result = {'end_calculation': -1, 'error': {'ok': True, 'msg':"OK"}}
    for param in needed_params:
        if param not in data:
            result['error']['ok'] = False
            result['error']['msg'] = f"Missing {param} or misspelled"
            print(result)
            return result
    
    compounded_return = data['principal'] * ((1 + (data['rate_of_interest'] / data['number'])) ** (data['number'] * data['time']))
    result['end_calculation'] = round(compounded_return, 2)
    
    with open('logs.txt', 'a') as log:
        log.write(f"{datetime.now().isoformat(timespec='minutes')}\nPrincipal: {data['principal']}, Rate: {data['rate_of_interest']}, Compounded per year: {data['number']}, Time: {data['time']}, Final Answer: {result['end_calculation']}\n\n")
    return result

def main():
    serverName = '127.0.0.1'
    serverPort = 47123
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # bind the socket to the server environment
    serverSocket.bind((serverName, serverPort))

    # listen set to only allow 1 connection at a time
    serverSocket.listen(1)
    print(f'Server listening on: localhost port: {serverPort}')
    
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(f"Connected by: {addr}\nWaiting on a message...")
        client_message = connectionSocket.recv(1024).decode()
        client_message = json.loads(client_message)
        print(f"Received message from client: {client_message}")
        server_message = json.dumps(compound_interest(client_message))
        connectionSocket.send(server_message.encode())

if __name__ == "__main__":
    main()
