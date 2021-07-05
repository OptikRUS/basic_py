#Написать регулярное выражение для парсинга файла логов web-сервера nginx_logs.txt для получения информации вида:
# (<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>)

import re

with open('nginx_logs.txt', 'r', encoding="utf-8") as f:
    text = f.read()

pattern_remote_addr = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b\s'
remote_addr = re.findall(pattern_remote_addr, text, flags=re.ASCII)

pattern_request_datetime = r'\b(\d{2}\/\w{3}\/\d{4}\:\d{2}\:\d{2}\:\d{2}\ \+\d{4})\b'
request_datetime = re.findall(pattern_request_datetime, text, flags=re.ASCII)

pattern_request_type = r'\"(\w+)\b\s\/'
request_type = re.findall(pattern_request_type, text, flags=re.ASCII)

pattern_requested_resource = r'\"\w+\b\s(\/\w+\/\w+)\s\w+\/\d\.\d\"'
requested_resource = re.findall(pattern_requested_resource, text, flags=re.ASCII)

pattern_response_code = r'\"\w+\b\s\/\w+\/\w+\s\w+\/\d\.\d\"\s\b(\d+)\b\s'
response_code = re.findall(pattern_response_code, text, flags=re.ASCII)

pattern_response_size = r'\"\w+\b\s\/\w+\/\w+\s\w+\/\d\.\d\"\s\b\d+\b\s(\d+)\b\s\"'
response_size = re.findall(pattern_response_size, text, flags=re.ASCII)

print(*zip(remote_addr, request_datetime, request_type, requested_resource, response_code, response_size))