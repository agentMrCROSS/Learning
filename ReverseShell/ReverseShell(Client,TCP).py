"""USE PROTOCOL TCP"""
#  Сторона клиента(сторона компьютера на котором будет этот файл. Подставить IP и PORT машины,вместо предложенного!)
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 8888))
s.send(b'<Your message>')  # Вместо Your message подставить свое сообщение
s.close()
