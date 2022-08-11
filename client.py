from socket import *
import json

def main():
    serverName = "127.0.0.1"
    serverPort = 47123
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    print(f"Connected to: {serverName} on port: {serverPort}\n\nEnter message to send...")
    client_message = {
        "principal":1800,
        "rate_of_interest":0.03,
        "number":12,
        "time":30}
    client_message = json.dumps(client_message)
    clientSocket.send(client_message.encode())
    server_message = clientSocket.recv(1024).decode()
    server_message = json.loads(server_message)
    print(f"Final calculation: {server_message['end_calculation']}. Err: {server_message['error']}")

if __name__ == "__main__":
    main()
