#Напишите программу, которая генерирует новый список из первого
#списка, заменяя все отрицательные числа на ноль.

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
new_prices = [price if price > 0 else 0 for price in original_prices]
print("Результат:\n", new_prices)

