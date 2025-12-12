"""first half: Cafeteria"""
with open("input puzzle 5", 'r', encoding="utf-8") as inputFile:
    autoInput= list(inputFile)
manualInput= ['3-5','10-14','16-20','12-18','','1','5','8','11','17','32']

#print(autoInput)
#Ranges=manualInput[:manualInput.index('')]
Ranges=autoInput[:autoInput.index('\n')]
#print(Ranges)
#Items=manualInput[manualInput.index('')+1:]
Items=autoInput[autoInput.index('\n')+1:]
#print(Items)

cleanedItems=[int(ID) for ID in Items]
cleanedRanges=[(int(interval.split('-')[0]),int(interval.split('-')[1])) for interval in Ranges]
#print(cleanedRanges)

result=0
for ID in cleanedItems:
    for interval in cleanedRanges:
        if ((interval[0]<=ID) and (ID<=interval[1])):
            result+=1
            break

print(result)

"""second half"""

Points=[]
for i in range(len(cleanedRanges)):
    Points.append((cleanedRanges[i][0],0,i+1))
    Points.append((cleanedRanges[i][1],1,i+1))

#print(Points)
line=sorted(Points)
#print(line)

nonOverlapPoints=[]
inInterval=0
for p in line:
    if inInterval==0:
        nonOverlapPoints.append(p[0])
    if p[1]==0:
        inInterval+=p[2]
    if p[1]==1:
        inInterval-=p[2]
    if inInterval==0:
        nonOverlapPoints.append(p[0])    

#print(nonOverlapPoints)
result=0
for i in range(0,len(nonOverlapPoints),2):
    result+=((nonOverlapPoints[(i+1)]-nonOverlapPoints[i])+1)

print(result)

"""def overlapRemover(interval1=tuple,interval2=tuple):
    smallest=min(interval1[0],interval2[0])
    largest=max(interval1[1],interval2[1])
    smallLarge=min(interval1[1],interval2[1])
    largeSmall=max(interval1[0],interval2[0])
    if (smallLarge<=largeSmall):
        return ((smallest, largest), ())
    else:
        return (interval1, interval2)

changingRanges=cleanedRanges
changes=1
while (changes>0):
    newRanges=[]
    changes=0
    for (low, high) in changingRanges:
        for (l,h) in changingRanges:
            if ((l<=high) and (high<=h) and (low, high)!=(l,h)):
                newRanges.append((min(low, l), h))
                changes+=1

    changingRanges=newRanges

print(changingRanges)"""