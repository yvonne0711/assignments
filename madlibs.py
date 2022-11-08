#series of inputs from user
#eg noun, adjective etc
#then place them into a premade story template

name = input("What's your name? ") #yvonne
pet = input('Think of an pet: ') #dog
colour = input('Think of a colour: ') #purple
country = input('Enter a country: ') #japan
food = input('Think of a food: ') #burger
noun = input('Enter a noun: ') #book
adjective = input('Enter an adjective: ') #heavy
verb = input('Enter a verb (past tense): ') #walked
adverb = input('Enter an adverb: ') #quickly

story = name + ' flew to ' + country + ' forgetting that she had left her ' + pet + ' behind. She needed some space after sitting on the aeroplane for a long time so she ' + adverb + ' ' + verb + ' in her ' + colour + ' flowing dress to the nearest convenience store and bought a ' + food + '. She sat down exhausted, her ' + adjective + ' luggage by her side and pulled out her ' + noun + '. The day went by ' + adverb + ' and as the sun starts to set, she ' + verb + ' back to her hotel.'

print(story)