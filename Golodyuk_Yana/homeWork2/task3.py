# Программа считывает с клавиатуры число  𝑛 , и рисует звездочный квадрат размера  𝑛∗𝑛 
# Пример:
# Ввод
# 3
# Вывод

def func():
    n = int(input())
    for _ in range(n):
        print("*" * n)
    
if __name__ == "__main__":
    func()
    