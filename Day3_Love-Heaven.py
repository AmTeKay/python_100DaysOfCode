print('''
 _                                
| |                               
| |__   ___  __ ___   _____ _ __  
| '_ \ / _ \/ _` \ \ / / _ \ '_ \ 
| | | |  __/ (_| |\ V /  __/ | | |
|_| |_|\___|\__,_| \_/ \___|_| |_|
    
''')
print("Welcome to Love-Heaven Routine.")
print("Your mission is to find the Love-Heaven.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# print("Welcome to Love-Heaven Routine")
_1 = input("At the end of the road, where do you wanna go ? left or right?\n> ")
if _1 == "right" or _1 == "Right":

  _2 = input("Now you see a rose garden, what color will you choice? red? or white?\n> ")
  if _2 == "red" or _2 == "Red":

    _3 = input("Now, You are at the Love-Heaven Gate. There's a lock with password, what is your girlfriend fav-color.\n> ")
    _3_lower = _3.lower()
    ps = _3_lower.count('l' or 'v' or 'e' or 'u')
    # print(ps)
    if ps >= 1:
      print("Now you reach Love-Heaven. GOOD LUCK HAVE FUN!")
    else:
      print("Game Over!")  

  else:
    print("Game Over!")

else:
  print("Game Over!")
