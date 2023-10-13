#Welcome to my ChatBot, cuz why not
import pickle
user_info={}

while True:
    qCount=0

    ask_name=input("Hey, I'm KuttiBot. What's your name?")
    user_info['name']=ask_name

    print('Hey',ask_name,', what do you want to ask me?')
    ask_chat=input()
    qCount+=1

    user_info[qCount]=ask_chat

    lenQ=len(user_info[qCount])

    ask_chat=input("What's next?")
    qCount+=1
    list_user=user_info[qCount].split(' ')
    for i in list_user:
        if i in ask_chat:
            print("A similar question was asked")
