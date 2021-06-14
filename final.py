from PIL import Image
print ("Oh hi you're awake! I was a bit worried there.")
choice= ['yes','no']
directions= 'Would you like to first go to the safe, the bookcase, exit, or the paintings?\n'
location= ['safe' , 'bookcase', 'painting','exit']
d= ['6824', 'Wheat', 'wheat', 'yellow']
e= ['code','cipher', 'continue']
numbers= Image.open('1432.jpg')
ciph= Image.open('Cipher.png')
pigpen= Image.open('code.png')
books=Image.open('books.png')
lock=Image.open('lock.png')
p=['echo','Echo']
end= ['cmy','CMY']

name= input ('What is your name? \n')
print ('I would say nice to meet you,' + name + ', but we are currently stuck in the basement of a serial killer!')

q1= input ('Would you like to escape with me?\n')
if q1== 'no':
    print ('Very sorry to hear that, I guess we will be dying down here. Goodbye' + name)
elif q1== 'yes':
    print('Amazing! How would you like to proceed?')
    b= input(directions)
else:
    a= input("I'm sorry, please enter 'yes', or 'no' \n")
    if a== 'no':
        print ('Very sorry to hear that, I guess we will be dying down here. Goodbye' + name)
    elif a== 'yes':
        print ('Amazing! How would you like to proceed?')
        b= input (directions)
        
while b not in location:
    b= input ("I'm sorry,I didn't get that. Please enter 'safe', 'bookcase', or 'painting'\n")

if b== 'safe':
    print ("Awesome, let's go check out the safe!")
    print ('Looks like it requires a 4 digit code. Wonder what it could be')
    print ('Look at this peice of paper! We might be able to figure out the code.')
    numbers.show()
    code= input('What do you think the code is?\n')
    while code not in d:
        code = input('hmmm its not working. Got a different code?\n')
    else:
        print ('Woah! It opened! Looks like theres a peice of paper inside')
        print ("It says the letter 'c' I'll save it for now, we might need it later")
        b= input ("Where should we go now? The painting, exit, or the bookcase?\n")
    
if b== 'bookcase':
    print ('To the bookcase we go!')
    books.show()
    book= input ('Look, there are three books here. Which one should we open first?\n')
    while book not in d:
        book = input ('Nope nothing here! Want to check a different one?')
    else:
        print ('Look theres a peice of paper inside! It says, "enter your answer in the box beside the bookshelf." Looks like a word puzzle?')
        print ('I am a five-letter word and people eat me. If you remove the first letter I become an energy form. If you remove the first two letters, I am needed to live. Scramble the last three letters and I am a drink. What word am I?')
        riddle= input ('What do you think the answer is?\n')
        while riddle not in d:
            riddle=input ("Sorry, the light turned red. I don't think its correct. Got anything else?")
        else:
            print ("The light turned green! It worked!Look the letter 'm'!")
            b= input ('Where to now? The safe, exit, or painting?\n')
            if b== 'safe':
                print ("Awesome, let's go check out the safe!")
                print ('Looks like it requires a 4 digit code. Wonder what it could be')
                print ('Look at this peice of paper! We might be able to figure out the code.')
                code= input('What do you think the code is?')
                while code not in d:
                    code = input('hmmm its not working. Got a different code?')
                else:
                    print ('Woah! It opened! Looks like theres a peice of paper inside')
                    print ("It says the letter 'c' I'll save it for now, we might need it later")
                    b= input ("Where should we go now? The painting, safe, or the exit?\n")
if b== 'exit':
    print ('Look a door! Its locked though')
    print ('looks like a 3 letter code! The first digit has the first 10 letters as choice, the second has the next 10, and the last one is the last 6 letters! What do you think the code can be?')
    lock.show()
    final=input ('Please put in the code')
    if final not in end:
        print ("Let's go do all the puzzles and come back")
    else:
        print ('The code is correct The door is unlocked. We can finally escape. Thank you for your help. We did it!')
        
if b== 'painting':
    print ("Good choice. Let's go see!")
    print ('Hm whats so special about this painting?')
    print ('Oh look theres something behind it! Theres a lock and a peice of paper. Look like a pigpen cipher! Know how to solve these?')
    print ('Wait look the back of the painting opens up! Look its a cipher!')
    print ("Let's solve this thing")
    paint= input ("(type 'code' if you would like to see the code and 'cipher' for the cipher. Type 'continue' when you think you've gotten the answer)")
    while paint in e:
        if paint== 'code':
            pigpen.show()
            paint= input ('Would you like to see the cipher or continue?')
        elif paint== 'cipher':
            ciph.show()
            paint= input ('Would you like to see the code or continue?')
        elif paint== 'continue':
            answer= input ("What do you think the answer is? Let's see if the lock opens!")
            while answer not in p:
                answer= input ("Oh no that doesn't seem to be the answer. Try again?")
            else:
                print(name+ "! It worked!Look! The letter 'y'!")
                b= input ('Where would you like to go next?')
                if b== 'safe':
                    print ("Awesome, let's go check out the safe!")
                    print ('Looks like it requires a 4 digit code. Wonder what it could be')
                    print ('Look at this peice of paper! We might be able to figure out the code.')
                    numbers.show()
                    code= input('What do you think the code is?\n')
                    while code not in d:
                        code = input('hmmm its not working. Got a different code?\n')
                    else:
                        print ('Woah! It opened! Looks like theres a peice of paper inside')
                        print ("It says the letter 'c' I'll save it for now, we might need it later")
                        b= input ("Where should we go now? The painting or the bookcase?\n")
                if b== 'bookcase':
                    print ('To the bookcase we go!')
                    books.show()
                    book= input ('Look, there are three books here. Which one should we open first?\n')
                    while book not in d:
                        book = input ('Nope nothing here! Want to check a different one?')
                    else:
                        print ('Look theres a peice of paper inside! It says, "enter your answer in the box beside the bookshelf." Looks like a word puzzle?')
                        print ('I am a five-letter word and people eat me. If you remove the first letter I become an energy form. If you remove the first two letters, I am needed to live. Scramble the last three letters and I am a drink. What word am I?')
                        riddle= input ('What do you think the answer is?\n')
                        while riddle not in d:
                            riddle=input ("Sorry, the light turned red. I don't think its correct. Got anything else?")
                        else:
                            print ("The light turned green! It worked!Look the letter 'm'!")
                            b= input ('Where to now? The safe, exit, or painting?\n')
                            if b== exit:
                                print ('Look a door! Its locked though')
                                print ('looks like a 3 letter code! The first digit has the first 9 letters as choice, the second has the next 9, and the last one is the last 8 letters! What do you think the code can be?')
                                final=input ('Please put in the code')
                                if final not in end:
                                    print ("Let's go do all the puzzles and come back")
                                else:
                                    print ('The code is correct The door is unlocked. We can finally escape. Thank you for your help. We did it!')
                if b== 'exit':
                    print ('Look a door! Its locked though')
                    print ('looks like a 3 letter code! The first digit has the first 9 letters as choice, the second has the next 9, and the last one is the last 8 letters! What do you think the code can be?')
                    lock.show()
                    final=input ('Please put in the code')
                    if final not in end:
                        print ("Let's go do all the puzzles and come back")
                    else:
                        print ('The code is correct The door is unlocked. We can finally escape. Thank you for your help. We did it!')
    
