import socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('<HOST>', <PORT>)) # <HOST> - ваш IP машины, <PORT> - ваш порт машины -> int
    while True:
        data = s.recv(4096)
        if not data:
            continue
        st = data.decode('ascii')
        #  Здесь идет алгоритм обработки задачи, результаты работы которого должны оказаться в переменной result
        s.send(str(result)+'\n'.encode('utf-8')) # result создасться,когда сработает алгоритм
finally:
    s.close()
