print("yay! It's quiz time")

playing = input("Hop into quiz challenge? ")
if playing != "yes":
    print("Bye bye,see you another time!")

print("quiz challenge accepted")
score = 0

answer = input("what is the name the flag with a dark double faced Eagle inscription? ")
if answer.lower() == "alabania":
    print("perfect, you got that right!")
    score += 1
else:
    print("ooppss! that's wrong.")

answer = input("what is the name of the Flag with green and white stripes? ")
if answer.lower() == "nigeria":
    print("Great job there!")
    score += 1
else:
    print("ooppss! that's wrong.")

answer = input("what is the name of  the flag with grey crowned crane inscription ")
if answer.lower() == "turkey":
    print("perfect, you got that right!")
    score += 1
else:
    print("ooppss! that's wrong.")

answer = input("Name the flag with half of a yellow sun inscription? ")
if answer.lower() == "biafra":
    print("perfect, you got that right!")
    score += 1

else:
    print("ooppss! that's wrong.")

answer = input("Name the flag with blue inscribed cross? ")
if answer.lower() == "finland":
    print("perfect, you got that right!")
    score += 1

else:

    print("ooppss! that's wronccg.")

answer = input("Name the flag with a dark double faced Eagle inscription? ")
if answer.lower() == "alabania":
    print("perfect, you got that right!")
    score += 1
else:
    print("ooppss! that's wrong.")
print("rounds up " + str(score) + " questions valid!")
print("rounds up " + str((score / 6) * 100) + "%.")