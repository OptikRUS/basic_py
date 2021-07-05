# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt

with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    requests_list = []
    for line in f:
        remote_addr = line[:line.find(' ')]
        request_type = line[line.find('"') + 1:line.find('"') + 4]
        requested_resource = line[line.find('/d'):line.find('HTTP') - 1]
        tuple_requests = (remote_addr, request_type, requested_resource)
        requests_list.append(tuple_requests)
print(requests_list, len(requests_list))