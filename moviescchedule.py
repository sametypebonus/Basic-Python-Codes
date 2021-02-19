current_movies = {'The Haunted House' : "6:00 pm",
                  "Night at the Museum": "8.30 pm"}

print("The following movies are previewing tonight\n")

for i in current_movies:
    print(i)

inp = input("WHat movie would you like to watch? \n")

time = current_movies.get(inp)
if time == None:
    print("pick a correct one\n")

else :
    print(inp, 'is playing at', time)
    

