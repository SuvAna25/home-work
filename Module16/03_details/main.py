shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Название детали: ')
count = 0
total = 0

for i in shop:
        if i[0] == detail:
                count += 1
                total += i[1]
if count == 0:
        print('Деталь не найдена')
else:
        print('Количество деталей: ', count)
        print('Общая стоимость: ', total)
