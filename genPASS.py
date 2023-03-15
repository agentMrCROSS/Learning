# Программа для генерации сложного пароля
import random , time
print("*" * 8 , "Генератор сложного пароля" , "*" * 8)
print("Введи y - да , n - завершить программу")
rand_num = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}[]/<>/?1234567890abcdefghijklmnopqrstuvwxyz"
while True:
    q = input("Сгенерировать? ")
    if q == "y":
        password = ""
        for x in range(16):
            password += random.choice(rand_num)
        print(password) 
    else:
        print("*" * 8 , "Программа завершена" ,"*" * 8)
        time.sleep(1)
        break

