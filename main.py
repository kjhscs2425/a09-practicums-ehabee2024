def choose_practicum():
   choice = input("sign up for a practicum (lighting, sound, scenery, or costumes): ")
   if choice == "lighting" or choice == "sound" or choice == "scenery" or choice == "costumes":
    return choice
   #returns choice
   else:
    return choose_practicum()
   #run the function choose practium and returns the result
   
name = input("what is your name? ")
practicum = choose_practicum()
print(f"Congratulations, {name}, you are signed up for {practicum}")