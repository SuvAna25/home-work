class Potato:
    states = {0: 'Отсутсвует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}\n'.format(
            self.index, Potato.states[self.state]
        ))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index)
                         for index in range(1, count+1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
            print('Картошка ещё не созрела!\n')
            return False
        else:
            print('Вся картошка созрела. Можно собирать!\n')
            return True

    def print_all_states(self):
        for i_potato in self.potatoes:
            i_potato.print_state()


my_garden = PotatoGarden(5)

for _ in range(3):
    my_garden.grow_all()

my_garden.are_all_ripe()


