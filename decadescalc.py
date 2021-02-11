inp_age = input("How old are you?\n")
inp_age = int(inp_age)
years = inp_age%10
decades = int(inp_age/10)
print("You are " + str(decades)+ " decades and " + str(years) + " year(s) old")
print("You are", decades, "decades and", years, "year(s) old")