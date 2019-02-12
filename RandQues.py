import random

x = [10,20,30]
y = [50,60,70]

def Switch_Question(NumQ):
    switcher = {
        1 : 'What is your best friend donig now ?' ,
        2 : 'What are things that people play ?',
        3 : 'What are things that people do ?',
        4 : 'What are things people go ?',
        5 : 'Do you play any sports ? Which sports do you play ?',
        6 : 'What kind of clothes do you like to buy ?',
        7 : 'What kind of clothes do you not like to buy ?',
        8 : 'What color do you like ?',
        9 : 'What color do you not like ?',
        10 : 'What do you want to do ?',
        11 : 'What do you need to do tomorrow ?',
        12 : 'What do you have to do when you go home ?',
        13 : 'How many seasons did we learn in class ?',
        14 : 'What are the seasons ?',
        15 : 'Which season usually has hot weather ?',
        16 : 'Which season usually has cold weather ?',
        17 : 'Which season usually has warm weather ?',
        18 : 'Which season usually has cool weather ?',
        19 : 'What is your favourite season ? Why ?',
        20 : 'How is the weather today ?',
        21 : 'What are you doing right now ?'
    }
    #print(str(NumQ) + " :  " + switcher.get(NumQ,"Invalid val"))
    print('{} : {}'.format(NumQ,switcher.get(NumQ,"Invalid")))

for i in range(10):
    rdmInt = random.randint(1,21)
    Switch_Question(rdmInt)

