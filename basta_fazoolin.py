# Making the Menus
class Menu:

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f"{self.name} menu available from {self.start_time} to {self.end_time}"

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      if item in self.items:
        total += self.items[item]
    return total

brunch_dict = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

early_bird_dict = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

dinner_dict = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

kids_dict = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

arepas_menu_dict = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

brunch = Menu('brunch', brunch_dict, 1100, 1600)
early_bird = Menu('early_bird', early_bird_dict, 1500, 1800)
dinner = Menu('dinner', dinner_dict, 1700, 2300)
kids = Menu('kids', kids_dict, 1100, 2100)
arepas_menu = Menu("Take a' Arepa", arepas_menu_dict, 1000, 2200)

print(brunch)
print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))
print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))
print(arepas_menu.calculate_bill(['arepa pabellon', 'jamon arepa']))

# Creating the Franchises
class Franchise:
  def __init__(self,address, menus):
    self.address = address
    self.menus = menus

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    available = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available.append(menu)
    return available

flagship_store = Franchise('1232 West End Road', [brunch, early_bird, dinner, kids, arepas_menu])
new_installment = Franchise('12 East Mulberry Street', [brunch, early_bird, dinner, kids, arepas_menu])
arepas_place = Franchise('189 Fitzgerald Avenue', [brunch, early_bird, dinner, kids, arepas_menu])
print(flagship_store.available_menus(1200))
print(new_installment.available_menus(1700))
print(arepas_place.available_menus(2200))

# Creating Businesses
class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
  
  def __repr__(self):
    return self.name

Business("Basta Fazoolin' with my heart", (flagship_store, new_installment, arepas_place))
Business("Take a' Arepa", (flagship_store, new_installment, arepas_place))
