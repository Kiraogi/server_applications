import socket # Модуль для работы с сетевыми соединениями
import threading # Модуль для многопоточного выполнения

# Определяем IP-адрес и порт сервера
HOST = '127.0.0.1' # Сервер будет работать только на локальном ПК (localhost)
PORT = 12345 # Порт, на котором сервер будет принимать подключение

# создание серверных сокет (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к указанному IP-адресу и порту
server_socket.bind((HOST, PORT))

# Переводим сервер в режим прослушивания входящих соединений 
server_socket.listen()

print(f'Сервер запущен на {HOST}:{PORT}...') # Выводим информацию о запуске сервера

def handle_client(client_socket, client_address):
    """
    Функция обработки подключения клиента.
    Запускается в отдельном потоке для каждого нового клиента. 
    """
    print(f'Подключение от {client_address}') # Выводим информацию о новом подключение
    while True:
        data = client_socket.recv(1024) # Получаем данные от клиента (но не более 1024 байт)
        if not data: # Если данные отсутствуют (клиент отключается), выходим из цикла
            break
        client_socket.sendall(data) # Отправить полученные данные обратно клиенту (эхо-ответом)
    
    client_socket.close() # Закрываем соединение с клиентом
    print(f'Клиент{client_address} отключился') # Выводим сообщение об отключение клиента

# Основной цикл сервера: ждет подключения клиентов и создает новый поток для каждого из них
while True:
    client_socket, client_address = server_socket.accept() # Принимаем новое соединение
    thread = threading.Thread(target=handle_client, args=(client_socket, client_address)) # Создаем поток для клиента
    thread.start() # Запуск потока 

