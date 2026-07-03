# #Question 1
# score = 10

# def update_score():
#     score = 5
#     score = score + 3
#     print(score)

# update_score() # Print 8 because we only access what in the function
# print(score) # Print 10 because accessed outside the function

# #question 2
# name = "Agent"
# level = 2

# def show_info():
#     name = "Spy"
#     level = 4
#     power = level * 10
#     print(name)
#     print(power)

# show_info()
# print(name)
# print(level)

# #When the function is run,
# # it will print what is inside "spy" and 4*10- 40.
# #  print -(name & level) prints the global name and level -"agent" 2

# ##question 3
# coins = 20
# def mission_reward(coins):
#     coins = coins + 10
#     coins = coins * 2
#     print(coins)

# mission_reward(5)
# print(coins)
# ##When the function is run,
# #  it will print 30 (5 +10 then multiplied by 2)
# #in the printing of print (coins) - print 20 - the global

# ##question 4
# health = 100

# def take_damage(damage):
#     health = 100
#     health = health - damage
#     damage = damage + 5
#     print(health)
#     print(damage)

# take_damage(30)
# print(health)
# ##when printing the function in health it will print 70 (100 - 30)
# #and in damage it will print 35 (30+5)
# #print health will print 100, the global value.

# ##question 5
# items = ["map", "key"]

# def add_item():
#     items.append("torch")
#     items.append("coin")
#     print(items)

# add_item()
# print(items)
# #will print the entire list twice
# #because it is  a list so in the function
# #it is a pointer and not  a buplicate of the list.

# ##question 6
# items = ["map", "key"]

# def replace_items():
#     items = ["potion"]
#     items.append("shield")
#     print(items)

# replace_items()
# print(items)
# #In this function it will print ['potion', 'shield']
# #  because it overwrites and creates a new list.
# #  print(items) - it will print ['map', 'key']


# #question 7
# points = 3

# def add_points():
#     global points
#     points = points + 7
#     points = points * 2
#     print(points)

# add_points()
# print(points)
# # will print 20 in both because global is updating its number

# #question 8
# status = "waiting"

# def outer():
#     status = "ready"

#     def inner():
#         status = "running"
#         print(status)

#     inner()
#     print(status)

# outer()
# print(status)
##Print

#running- internal function
#ready- external function
#waiting- global variable


# # # questions 9
# coins = 10

# def outer():
#     coins = 5

#     def inner():
#         nonlocal coins
#         coins = coins + 3
#         coins = coins * 2
#         print(coins)

#     inner()
#     print(coins)

# outer()
# print(coins)
#
#16-From the inner function (because it changed its previous value because of nonlocal)
#16-From the outer function
#10- Global variable

# # questionn 10
# score = 1
# bag = ["key"]

# def outer():
#     score = 10
#     bag.append("map")

#     def inner():
#         nonlocal score
#         score = score + 5
#         bag.append("coin")
#         print(score)
#         print(bag)

#     score = score * 2
#     inner()
#     print(score)
#     print(bag)

# outer()
# print(score)
# print(bag)

##25: (20 from outer variable +5 from inner variable)
#['key', 'map', 'coin']- Because there was no variable with that name in the functions,
#  the change was made globally

#25- nonlocal created a change in the outer function
#['key', 'map', 'coin']- Same as above

#1- Global variable not changed
#['key', 'map', 'coin']- Same as above







# #part 2
# ##1

# def meters_to_sm(metar):
#     centimets = metar * 100
#     return centimets


# def format_movement_message(centimets):
#     return f"Robot moved {centimets} centimeters"

# result = format_movement_message(meters_to_sm(1))
# print(result)



# ##2
## foo-1
# def Add_a_shipping_price(price):
#     return price + 10

# # foo 2
# def Doubling_the_price(price):
#     return price* 2

# Initial_price = 45
# Price_with_surcharge = Add_a_shipping_price(Initial_price)
# Price_with_doubling = Doubling_the_price(Price_with_surcharge)
# print(Price_with_doubling)


# # ##3
# def Returning_a_first_name(first_name , sceand_name):
#     return f"{first_name} - {sceand_name}"

# def Converts_to_uppercase(name_string):
#     return name_string.upper()

# name1 = "yehoshua"
# nami2 = "zalts"

# add_nam = Returning_a_first_name(name1, nami2)
# big_name = Converts_to_uppercase(add_nam)

# print(big_name)

##4
# def celsius_to_fahrenhit(celsius):
#     return(celsius * 9/5)+32

# def temperture_repotr(fahrenheit):
#     return f"the temperature is {fahrenheit} degrees: "

# celsius_num = 25
# fahr_value = celsius_to_fahrenhit(celsius_num)
# report = temperture_repotr(fahr_value)

# print(report)

# ##5
# def apply_damage(health, damage):
#     return health - damage

# def apply_healing(damaged_health, healing):
#     return damaged_health + healing

# start = 100
# damage_amount = 30
# healing_amount = 15

# current_health = apply_damage(start, damage_amount)

# final_health = apply_healing(current_health, healing_amount)
# print(final_health)


##6
# def Price_calculation(price1, price2, price3):
#     return price1 + price2 + price3

# def disconunt(price_orgunal):
#     return price_orgunal * 0.8

# def crate_message(final_price):
#     message = f"the final price 20% discount is: {final_price}"
#     return message 

# product1 = 50
# product2 = 100
# product3 = 50

# price_total = Price_calculation(product1, product2, product3)
# after_discount = disconunt(price_total)
# messge_customer = crate_message(after_discount)

# print(messge_customer)

# ##7
# def clean_password(password):
#     cleaned = password.strip()
#     return cleaned 

# def get_password_length(cleaned_password):
#     length = len(cleaned_password)
#     return length

# def is_password_valid(password_length):
#     if password_length >= 8:
#         return True
#     else:
#         return False

# user = "   yehoshya1234   "
# clean = clean_password(user)
# final_length = get_password_length(clean)
# valisation = is_password_valid(final_length)

# print(valisation)
# # print(clean)

##8
def add_flat_bonus(base_grade):
    new_grade = base_grade + 5
    return new_grade

def apply_factor(current_grade):
    factored_grade = current_grade * 1.1
    return factored_grade

def cap_at_maximum(final_calculation):
    capped_grade = min(final_calculation, 100)
    return capped_grade

student_starting_grade = 90
grade_after_flat = add_flat_bonus(student_starting_grade)
grade_after_factor = apply_factor(grade_after_flat)
final_student_grade = cap_at_maximum(grade_after_factor)
print(final_student_grade)