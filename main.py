class Person:
  height = 170
  name = "Name"
  is_sad = True
  
  def __init__(self, name , height):
    self.name = name
    self.height = height


class Cat:
  color = "Black"

  def __init__(self, name):
    self.name = name
  def play_w_hooman(self, human):
    human.is_sad = False



me = Person('Deenis', 179)
me_pet = Cat("Barsik")

you = Person('Macsim', 176)


print(me.is_sad)
me_pet.play_w_hooman(me)
print("Сумний - ",me.is_sad)


print(you.is_sad)
me_pet.play_w_hooman(you)
print("Сумний - ",you.is_sad)



