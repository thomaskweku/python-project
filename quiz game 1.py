print("welcome to my computer quiz")

playing=input("do you want to play my game? ")

print(playing)

if playing.lower() != "yes":
    quit()

print("okay! let's play :")

score=0

answer= input("what does CPU stand for? ").lower()
if answer=="central processing unit":
    print('correct!')
    score +=1
else:
    print('incorrect!')
 
answer= input("what does GPU stand for? ").lower()
if answer=="graphics processing unit":
    print('correct!')
    score +=1

else:
    print('incorrect!')
 
answer= input("what does RAM stand for? ").lower()
if answer=="random access memory":
    print('correct!')
    score +=1

else:
    print('incorrect!')

answer= input("what does UMaT stand for? ").lower()
if answer=="university of mines and technology":
    print('correct!')
    score +=1

else:
    print('incorrect!')


print("Please you got " + str(score) + " questions correct")

print("Please you got " + str((score/4)*100) + "%")