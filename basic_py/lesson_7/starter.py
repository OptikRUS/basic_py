import os

# зпустит one, two, tree по очереди

def one():
    os.makedirs('my_project/authapp/templates/authapp', exist_ok=True)
    os.chdir('my_project/authapp/templates/authapp')
    open('base.html', 'w', encoding='utf-8')
    open('index.html', 'w', encoding='utf-8')

def two():
    os.makedirs('my_project/settings', exist_ok=True)
    os.chdir('my_project/settings')
    open('__init__.py', 'w', encoding='utf-8')
    open('dev.py', 'w', encoding='utf-8')
    open('prod.py', 'w', encoding='utf-8')

def tree():
    os.makedirs('my_project/mainapp/templates/mainapp', exist_ok=True)
    os.chdir('my_project/mainapp/templates/mainapp')
    open('base.html', 'w', encoding='utf-8')
    open('index.html', 'w', encoding='utf-8')

#one()
#two()
#tree()