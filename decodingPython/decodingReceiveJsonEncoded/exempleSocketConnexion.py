from pwn import *
import json
import codecs

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)




received = json_recv()
print(received)
print("Received type: ")
print(received["type"])
print("Received encoded value: ")
print(received["encoded"])


to_send = {
    "decoded": "changeme ,"
}

print(to_send)
json_send(to_send)

#json_recv()
