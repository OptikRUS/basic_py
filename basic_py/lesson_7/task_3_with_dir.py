import os, shutil

for root, dirs, files in os.walk('my_project'):
    if root.find('templates') > 0 and len(files) == 0:
        shutil.copytree(root, 'my_project/templates', dirs_exist_ok=True)