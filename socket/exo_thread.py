import socket  # Модуль для работы с сетевыми соединениями
import threading  # Модуль для многопоточного выполнения

# Определяем IP-адрес и порт сервера
HOST = "127.0.0.1"  # Сервер будет работать только на локальном компьютере (localhost)
PORT = 12345  # Порт, на котором сервер будет принимать подключения

# Создаём серверный сокет (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к указанному IP-адресу и порту
server_socket.bind((HOST, PORT))

# Переводим сервер в режим прослушивания входящих соединений
server_socket.listen()

print(f"Сервер запущен на {HOST}:{PORT}...")  # Выводим информацию о запуске сервера


def handle_client(client_socket, client_address):
    """
    Функция обработки подключения клиента.
    Запускается в отдельном потоке для каждого нового клиента.
    """
    print(f"Подключение от {client_address}")  # Выводим информацию о новом подключении

    while True:
        data = client_socket.recv(1024)  # Получаем данные от клиента (не более 1024 байт)
        if not data:  # Если данные отсутствуют (клиент отключился), выходим из цикла
            break
        client_socket.sendall(data)  # Отправляем полученные данные обратно клиенту (эхо-ответ)

    client_socket.close()  # Закрываем соединение с клиентом
    print(f"Клиент {client_address} отключился")  # Выводим сообщение об отключении клиента


# Основной цикл сервера: ждёт подключения клиентов и создаёт новый поток для каждого из них
while True:
    client_socket, client_address = server_socket.accept()  # Принимаем новое соединение
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address))  # Создаём поток для клиента
    thread.start()  # Запускаем поток
