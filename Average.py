average = 0
total = 0
howManyEntered = 0
howMany = int(input('How Many test scores would you like to avarage?\n'))
while howManyEntered < howMany:
    testScores = int(input('Enter test score:\n'))
    total += testScore
    howManyEntered += 1
average = total / howMany
print('The Avarge fo the test scores you entered is:')
print(average)
