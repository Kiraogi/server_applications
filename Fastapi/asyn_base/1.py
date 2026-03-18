import time

def fetch_data():
    print("Запрос данных...")
    time.sleep(3)  # Имитация долгого запроса
    print("Данные получены!")

print("Начало работы")
fetch_data()
print("Программа завершена")
