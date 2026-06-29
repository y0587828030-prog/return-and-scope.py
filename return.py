#Question 1
score = 10

def update_score():
    score = 5
    score = score + 3
    print(score)

update_score() # Print 8 because we only access what in the function
print(score) # Print 10 because accessed outside the function

#question 2
name = "Agent"
level = 2

def show_info():
    name = "Spy"
    level = 4
    power = level * 10
    print(name)
    print(power)

show_info()
print(name)
print(level)

#When the function is run,
# it will print what is inside "spy" and 4*10- 40.
#  print -(name & level) prints the global name and level -"agent" 2

##question 3
coins = 20
def mission_reward(coins):
    coins = coins + 10
    coins = coins * 2
    print(coins)

mission_reward(5)
print(coins)
##When the function is run,
#  it will print 30 (5 +10 then multiplied by 2)
#in the printing of print (coins) - print 20 - the global

##question 4
health = 100

def take_damage(damage):
    health = 100
    health = health - damage
    damage = damage + 5
    print(health)
    print(damage)

take_damage(30)
print(health)
##when printing the function in health it will print 70 (100 - 30)
#and in damage it will print 35 (30+5)
#print health will print 100, the global value.

##question 5
items = ["map", "key"]

def add_item():
    items.append("torch")
    items.append("coin")
    print(items)

add_item()
print(items)