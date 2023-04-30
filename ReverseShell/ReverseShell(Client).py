"""USE PROTOCOL UDP"""

#  Сторона клиента(сторона компьютера на котором будет этот файл. Подставить IP и PORT машины,вместо предложенного!)
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'<Your message>', ('127.0.0.1', 8888))  # Вместо Your message подставить свое сообщение
