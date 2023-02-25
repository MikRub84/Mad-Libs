import random


n = random.randint(1, 3)

if n == 1:
    word1 = input('Enter Number, press space, Measure of time of choice and press enter:')
    word2 = input('Enter Mode of Transportation of choice and press enter:')
    word3 = input('Enter Adjective of choice and press enter:')
    word4 = input('Enter Adjective, press space, Noun of choice and press enter:')
    word5 = input('Enter Color, press space, Part of the Body of choice and press enter:')
    word6 = input('Enter Verb of choice and press enter:')
    word7 = input('Enter Number, press space, Noun of choice and press enter:')
    word8 = input('Enter Noun of choice and press enter:')
    word9 = input('Enter Part of the Body of choice and press enter:')
    word10 = input('Enter Verb, press space, Noun of choice and press enter:')
    word11 = input('Enter Adjective of choice and press enter:')
    word12 = input('Enter Silly Word, press space, Noun of choice and press enter:')
    
    story1 = "It was about " + word1 + " ago when I arrived at the hospital in a/an " + word2 + ". The hospital is a/an " + word3 + " place, there are a lot of " + word4 + " here. There are nurses here, who have " + word5 + ". If someone wants to come into my room, I told them, that they have to " + word6 + " first. I've decorated my room with " + word7 + ". Today I talked to a doctor and they were wearing a/an " + word8 + " on their " + word9 + ". I heard, that all doctors " + word10 + " every day for breakfast. The most " + word11 + " thing about being in the hospital is the " + word12 + "!"
    print('\n')
    print(story1)
    
if n == 2:
    temp1 = input("Enter Proper Noun(Person's Name) of choice and press enter:")
    temp2 = input("Enter Noun of choice and press enter:")
    temp3 = input("Enter Adjective(Feeling) of choice and press enter:")
    temp4 = input("Enter Verb of choice and press enter:")
    temp5 = input("Enter Adjective(Feeling) of choice and press enter:")
    temp6 = input("Enter Animal of choice and press enter:")
    temp7 = input("Enter Verb of choice and press enter:")
    temp8 = input("Enter Color of choice and press enter:")
    temp9 = input("Enter Verb(ending in ing) of choice and press enter:")
    temp10 = input("Enter Adverb(ending in ly) of choice and press enter:")
    temp11 = input("Enter Number, press space, Measure of Time of choice and press enter:")
    temp12 = input("Enter Color, press space, Animal of choice and press enter:")
    temp13 = input("Enter Number, press space, Silly Word of choice and press enter:")
    temp14 = input("Enter Noun of choice and press enter:")
    
    story2 = "This weekend I am going camping with " + temp1 + ". I packed my lantern, sleeping bag and " + temp2 + ". I am so " + temp3 + " to " + temp4 + " in a tent. I am " + temp5 + " we might see a/an " + temp6 + ", I hear they're kind of dangerouse. While we're camping, we are going to hike, fish and " + temp7 + ". I have heard, that the " + temp8 + " lake is great for " + temp9 + ". Then we will " + temp10 +" hike through the forest for " + temp11 + ". If I see a/an " + temp12 + " while hiking, I am going to bring it home as a pet! At night we will tell " + temp13 + " stories and roast " + temp14 + " around the campfire!!"
    print('\n')
    print(story2)
    
if n == 3:
    text1 = input("Enter Proper Noun(Person's Name) of choice and press enter:")
    text2 = input("Enter Adjective of choice and press enter:")
    text3 = input("Enter Color, press space, Animal of choice and press enter:")
    text4 = input("Enter Place of choice and press enter:")
    text5 = input("Enter Adjective, press space, Magical Creature(Plural) of choice and press enter:")
    text6 = input("Enter Adjective, press space, Magical Creature(Plural) of choice and press enter:")
    text7 = input("Enter Room in a House of choice and press enter:")
    text8 = input("Enter Noun of choice and press enter:")
    text9 = input("Enter Noun of choice and press enter:")
    text10 = input("Enter Noun(Plural) of choice and press enter:")
    text11 = input("Enter Adjective, press space, Noun(Plural) of choice and press enter:")
    text12 = input("Enter Number, press space, Measure of Time of choice and press enter:")
    text13 = input("Enter Verb(ending in ing) of choice and press enter:")
    text14 = input("Enter Adjective, press space, Noun of choice and press enter:")
    
    story3 = "Dear " + text1 + ", I am writing to you from a/an " + text2 + " castle in an enchanted forest. I found myself here one day after going for a ride on a/an " + text3 + " in " + text4 + ". There are " + text5 + " and " + text6 + " here! In the " + text7 + " there is a pool full of " + text8 + ". I fall asleep each night on a/an " + text9 + " of " + text10 + " and dream of " + text11 + ". It feels as though I have lived here for " + text12 + ". I hope one day you can visit, although the only way to get here now is " + text13 + " on a/an " + text14 + "!!"
    print('\n')
    print(story3)
