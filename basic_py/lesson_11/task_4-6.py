from warehouse import Warehouse

base_1 = Warehouse(2000, True)
print(base_1)
deliver = base_1.receive('Первое', 'Принтеры', 'Canon', 200)
print(deliver)
print(base_1)
sale = base_1.sale('Первое', 'Принтеры', 'Canon', 50)
print(sale)