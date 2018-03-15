import pyautogui as pg
import time
import webbrowser

points = 0
gender = ""

# Question 1

answer = pg.prompt(
"""
Are you a boy or girl?

a)girl
b)boy

"""
    )

# Give points

if answer == "a":
    points += 1
    gender = "girl"
elif answer == "b":
    points += 2
    gender = "boy"


# Question 2

answer = pg.prompt(
"""
Which would you rather eat?

a) protein shake
b) healthy foods
c) junk food and sweets/whatever I want

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# Question 3

answer = pg.prompt(
"""
Which would you rather wear?

a) day dress and sandals
b) t-shirt and jeans
c) my own unique style

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

# Question 4

answer = pg.prompt(
"""
Which would do you do as a hobby/sport?

a) cheerleading
b) football
c) dance/sing

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3


# Question 5

answer = pg.prompt(
"""
What would your role be as a performer?

a)background singer
b)lead singer
c)dancer

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

    # Question 6

answer = pg.prompt(
"""
What is your best quality?

a) Looks
b) Determination
c) Causing trouble

"""
    )

# Give points

if answer == "a":
    points += 1
elif answer == "b":
    points += 2
elif answer == "c":
    points += 3

#Finn
if points < 11 and gender == "boy": 
    pg.alert("Finn")
    webbrowser.open("https://www.google.com/search?q=which+glee+character+are+you+finn&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiPm7quxZbZAhWSjlkKHU_9AHMQ_AUICygC&biw=1366&bih=637#imgrc=bHUxL_4aLnqMOM:")
    
#Mike Chang
elif points > 14 and gender == "boy":
    pg.alert("Mike")
    webbrowser.open("") 
#Puck
elif points < 13 and gender == "boy":
    pg.alert("Puck")
    webbrowser.open("")    
#Mercedes
elif points > 15 and gender == "girl":
    pg.alert("Mercedes")
    webbrowser.open("https://www.google.com/search?q=which+glee+character+are+you+mercedes&rlz=1C1GCEA_enUS751US751&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjyyqCsxpbZAhUFuVkKHfeMCyUQ_AUICygC&biw=1366&bih=637#imgrc=vxfWF8JtYozI4M:")    
#Quinn
elif points < 9 and gender == "girl":
    pg.alert("Quinn")
    webbrowser.open("https://www.google.com/search?q=which+glee+character+are+you+finn&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiPm7quxZbZAhWSjlkKHU_9AHMQ_AUICygC&biw=1366&bih=637#imgdii=5GMpcbAGQYw9mM:&imgrc=ryA12X8roUpFmM:")    
#Rachel
elif points < 12 and gender == "girl":
    pg.alert("Rachel")
    webbrowser.open("https://www.google.com/search?q=which+glee+character+are+you+finn&tbm=isch&tbs=rimg:CWx1MS_1-Gi56Ijjr8kSd-8XN8zrulTYEKAkMkql2YdrGtLVxeB5odkvZHwAxmpNMBUZcOzKeC1UUs6QH6xNSe8nJiyoSCevyRJ37xc3zEf1vneYMBQeXKhIJOu6VNgQoCQwRxcnF9TsuxtcqEgmSqXZh2sa0tRFT3IzUtb9YzSoSCXF4Hmh2S9kfEVEW27NR9REjKhIJADGak0wFRlwRLTud6ftuEDIqEgk7Mp4LVRSzpBFT3IzUtb9YzSoSCQfrE1J7ycmLEcHxksEVww1M&tbo=u&sa=X&ved=2ahUKEwiC5rvyxZbZAhUswVkKHfrwCv0Q9C96BAgAEBs&biw=1366&bih=637&dpr=1#imgrc=be5YO_dIIgDhnM:")
