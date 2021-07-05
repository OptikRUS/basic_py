# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания

with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    remote_addr_list = []
    for line in f:
        remote_addr = line[:line.find(' ')]
        remote_addr_list.append(remote_addr)

print(max(set(remote_addr_list), key=remote_addr_list.count))