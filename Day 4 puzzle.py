"""first half"""
with open("input puzzle 4", 'r', encoding="utf-8") as inputFile:
    autoInput= list(inputFile)

manualInput= ['..@@.@@@@.','@@@.@.@.@@','@@@@@.@.@@','@.@@@@..@.','@@.@@@@.@@','.@@@@@@@.@',
'.@.@.@.@@@','@.@@@.@@@@','.@@@@@@@@.','@.@.@@@.@.']

cleanedInput= []
for string in autoInput:
    newString=''
    for char in string:
        if (char=='@'):
            newString=newString+'1'
        else:
            newString=newString+'0'
    cleanedInput.append(newString)

gridSize=[len(cleanedInput), len(cleanedInput[0])]
h=gridSize[0]
l=gridSize[1]

def isAccessible(pos0, pos1, grid):
    adjacencies=-1 #avoids counting the input tile itself
    for i in range(3):
        for j in range(3):
            adjacencies+=int(grid[(pos0-1+i)][(pos1-1+j)])

    if (adjacencies<4):
        adjacencies=-1
        return True
    else:
        adjacencies=-1
        return False

calcGrid=['0'*(gridSize[1]+2)]
for string in cleanedInput:
    calcGrid.append('0'+string+'0')
calcGrid.append('0'*(gridSize[1]+2))

result=0
for i in range(1,h+1):
    for j in range(1,l+1):
        if (calcGrid[i][j]=='1'):
            result+=int(isAccessible(i,j,calcGrid))

#print(calcGrid)
#print(isAccessible(1,3,calcGrid))
print(result)

"""second half"""

changingGrid=calcGrid

result=0
previousChanges=True
while previousChanges:
    onepassSum=0
    changePoints=[]
    for i in range(1,h+1):
        for j in range(1,l+1):
            if (calcGrid[i][j]=='1'):
                if (isAccessible(i,j,changingGrid)==True):
                    onepassSum+=1
                    changePoints.append((i,j))


    result+=onepassSum
    for tuple in changePoints:
        changingGrid[tuple[0]]=changingGrid[tuple[0]][:tuple[1]]+'0'+changingGrid[tuple[0]][(tuple[1]+1):]
    if (onepassSum==0):
        previousChanges=False

print(result)
