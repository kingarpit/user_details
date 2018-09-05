#ask user for name

name=raw_input('What is your name : ')
#print(name)

#ask user for age

age=raw_input('How old are you : ')
#print(age)

#ask user for city

city=raw_input('What city do you live in : ')
#print(city)

#ask user what they enjoy

love=raw_input('What do you love doing : ')
#print(love)

#create output text

string="Your name is {} and you are {} years old.You live in {} and you love {}."
output=string.format(name,age,city,love)

#print output to screen

print(output)
