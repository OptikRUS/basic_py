import os
import json

for root, dirs, files in os.walk('some_data'):
    size = [file.split('.')[-1] for file in files]
    size_100000 = [file.split('.')[-1] for file in files if os.stat(os.path.join(root, file)).st_size > 10000]
    size_10000 = [file.split('.')[-1] for file in files if 1000 < os.stat(os.path.join(root, file)).st_size < 10000]
    size_1000 = [file.split('.')[-1] for file in files if 100 < os.stat(os.path.join(root, file)).st_size < 1000]
    size_100 = [file.split('.')[-1] for file in files if os.stat(os.path.join(root, file)).st_size < 100]

res = {'Всего: ': (len(size), list(set(size))),
       100000: (len(size_100000), list(set(size_100000))),
       10000: (len(size_10000), list(set(size_10000))),
       1000: (len(size_1000), list(set(size_1000))),
       100: (len(size_100), list(set(size_100)))}

with open('some_data_summary.json', 'w') as f:
    json.dump(res, f, ensure_ascii=False)