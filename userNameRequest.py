user_name=''
while len(user_name.strip())<1:
    print("Привет! Давай знакомиться! Как тебя зовут?")
    user_name = input()
print("Приятно познакомиться, " +  user_name + "!")