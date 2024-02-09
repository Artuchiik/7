class chair:
    def __init__(self, legs, size, material):
       self.legs = legs
       self.size = size
       self.material = material

    def __str__(self):
        return f'Стул(Материал: {my_chair.material}, Кол-во ножек: {my_chair.legs}, Размер сидалища: {my_chair.size})'

my_chair = chair(5, 44, 'Осина')
print(my_chair)
