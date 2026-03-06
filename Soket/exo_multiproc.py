import socket # Модуль дял работы с сетевыми соединениями
import multiprocessing # Модуль для многопроцессной обработки клиентов

# Определяем IP-адрес и порт сервера
HOST = '127.0.0.1' # Сервер будет работать на локальном ПК (localhost)
PORT = 12345 # Порт, на котором сервер будет прослушивать входящие соединения

# Создаем серверный сокет (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к указанному IP-адресу и порту
server_socket.bind((HOST, PORT))

# Переводим сервер в режим прослушивания входящих соединений
server_socket.listen()

print(f'Сервер запущен на {HOST}:{PORT}... ') # Выводим информацию о запуске сервера

def handle_client(client_socket, client_address):
    """
    Функция обработки подключения клиента.
    Выполняется в отдельном процессе для каждого нового клиента. 
    """
    print(f'Подключение от {client_address}') # Выводим информацию о новом подключение

    while True:
        data= client_socket.recv(1024) # Получаем данные от клиента (не более 1024 байт)
        if not data: # Если данные отсутствуют (клиент отключился), выходим из цикла
            break
        client_socket.sendall(data) # Отправляем полученные данные обратно клиентку (эхо-ответ)
    
    client_socket.close() # Закрываем соединение с клиентом
    print(f'Клиент {client_address} отключился') # Выводим сообщение об отключение клиента

# Основной цикл сервера: ждет подключения клиентов и создает новый процесс для каждого из них
while True:
    client_socket, client_address = server_socket.accept() # Принимаем новое соединение
    process = multiprocessing.Process(target=handle_client, args=(client_socket, client_address)) # Создаем новый процесс для клиента 
    process.start() # Запускаем процесс


