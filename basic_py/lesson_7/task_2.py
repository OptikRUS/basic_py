import os

with open('config.yaml') as f:
    starter = dict(map(str.split, f.readlines()))
root_dir = starter.pop('root')

for dir, files in starter.items():
    os.makedirs(os.path.join(root_dir, dir), exist_ok=True)
    for file in files.split(','):
        with open(os.path.join(root_dir, dir, file), "w") as f:
            pass