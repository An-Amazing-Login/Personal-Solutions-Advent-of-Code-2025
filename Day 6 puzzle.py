"""Trash Compactor: first half"""

with open("input puzzle 6", 'r', encoding="utf-8") as inputFile:
    autoInput= list(inputFile)



manualInput=['123 328  51 64 \n',' 45 64  387 23 \n','  6 98  215 314\n','*   +   *   +  \n']
#manualInput=['123 328  51',' 45 64  387','  6 98  215 ','*   +   *   ']
#print(autoInput)
cleanedInput=[string.split() for string in autoInput]
polishedInput=[]
for li in cleanedInput[:-1]:
    polishedInput.append([int(string) for string in li])
polishedInput.append(cleanedInput[-1])

#print(polishedInput)

#print([row[1] for row in polishedInput[:-1]])
result=0
for i in range(len(polishedInput[-1])):
    prob=[row[i] for row in polishedInput[:-1]]
    if polishedInput[-1][i]=='+':
        result+=sum(prob)
    if polishedInput[-1][i]=='*':
        tempResult=1
        for number in prob:
            tempResult*=number
        result+=tempResult

print(result)

"""second half: cephalod math is written funny"""

"""#problem=[row[1] for row in cleanedInput[:-1]]
#print(problem)
#size=max([len(string) for string in problem])
#print(max([len(string) for string in problem]))
#problem2=[(string+('0'*(size-len(string)))) for string in problem]
#print(problem2)

result=0

for i in range(len(cleanedInput[-1])):
    problem=[row[i] for row in cleanedInput[:-1]]
    size=max([len(string) for string in problem])
    problem2=[(string+(' '*(size-len(string)))) for string in problem]

    problem3=[]
    for j in range(size):
        number=''
        for string in problem2:
            number=number+string[j]
        problem3.append(number)
    problem4=[int(x) for x in problem3]
    
    if cleanedInput[-1][i]=='+':
        result+=sum(problem4)
    if cleanedInput[-1][i]=='*':
        tempResult=1
        for number in problem4:
            tempResult*=number
        result+=tempResult

print(cleanedInput[-1][2])
print(problem4)
#print(sum(problem4))
print(result)"""

rawInput=autoInput


cuttingPlaces=[]
counter=-1
for char in rawInput[-1]:
    if char==' ':
        counter+=1
    else:
        counter+=1
        cuttingPlaces.append(counter)

cuttingPlacesFixed=cuttingPlaces[:-1]
#print(cuttingPlaces[:-1])

processedInput=[]
for string in rawInput:
    row=[]
    for i in range(len(cuttingPlacesFixed)-1):
        row.append(string[cuttingPlacesFixed[i]:(cuttingPlacesFixed[i+1]-1)])
    row.append(string[cuttingPlacesFixed[i+1]:])
    processedInput.append(row)

#print(processedInput)

result=0

for i in range(len(processedInput[-1])):
    horizontalProblem=[row[i] for row in processedInput[:-1]]
    size=len(horizontalProblem[0])
    #print(horizontalProblem)
    #print(size)

    verticalProblem=[]
    for j in range(size):
        vnumber=''

        for string in horizontalProblem:
            vnumber=vnumber+string[j]
        verticalProblem.append(vnumber) #maybe use 'try' here to skip the next section

    #print(verticalProblem)
    finalProblem=[]
    for string in verticalProblem:
        if string[0]=='\n':
            continue
        else:
            finalProblem.append(int(string))

    if (processedInput[-1][i][0]=='+'):
        result+=sum(finalProblem)
    if (processedInput[-1][i][0]=='*'):
        tempResult=1
        for number in finalProblem:
            tempResult*=number
        result+=tempResult

#print(problem)
#print(verticalProblem)
print(result)