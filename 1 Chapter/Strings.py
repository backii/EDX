import string

x = input("Give me a number ") # return a string value

print(" My favourite number is ", x, ".", "x=", x) # with spaces ,

print(" My favourite numer is " + x) # no spaces

varA = ""
varB = ""

if type(varA) == type(str) and type(varB) == type(str):
    print("string involved")

elif varA > varB:
    print("bigger")

elif varA == varB:
    print("equal")

else:
    print('smaller')



var = 10
poww = 0
iterations = var


while (iterations != 0):

    poww = var + poww
    iterations -= 1
print (poww)


iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1



string = "azcbobobegghakl12"
vowels = 0
for letter in string:
    if letter in "aeiou":
        vowels += 1


print (vowels)


s2 = 'azcbobobegghakl'
bob = 0
for i in range(0,len(s2)-3):
    s3 = s2[i:i+3]
    if s3 == 'bob':
        print("hell yeah")
        bob += 1

print(bob)



alphabet = 'abcdefghijklmnopqrstuvwxyz'
word = "beggh"
word2 = ""
for i in range(0, len(word)):
    j = i + 1
    while j <= len(word):
        if word[i:j] in alphabet:
            if len(word[i:j]) >= len(word2):
                word2 = word[i:j]
            j += 1
        else:
            break



print(word2)




