"""USE PROTOCOL UDP"""
#  Сторона сервера(Наша сторона, подставить свой IP и PORT компьютера)
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 8888))
result = s.recv(1024)
print('Message:', result.decode('utf-8'))
s.close()
