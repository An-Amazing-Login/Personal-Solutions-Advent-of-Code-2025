"""first half"""
with open("input puzzle 3", 'r', encoding="utf-8") as inputFile:
    autoInput= list(inputFile)

manualInput=['987654321111111\n','811111111111119\n','234234234234278\n','818181911112111\n']

cleanedInput= [x[:-1] for x in autoInput]

def biggestSizeTwoSubsequence(string):
    bigCandidate=string[-2:]
    for char in string[-3::-1]:
        if (char>=bigCandidate[0]):
            bigCandidate=char+str(max(int(bigCandidate[0]),int(bigCandidate[1])))

    return bigCandidate

result=[int(biggestSizeTwoSubsequence(string)) for string in cleanedInput]
#print(result) #debugging
print(sum(result))

"""second half"""

def biggestSizeNSubsequence(string, n):
    bigCandidate=string[-n:]
    for char in string[-(n+1)::-1]:
        if (char>=bigCandidate[0]):
            newCandidate = char
            for i in range(n-1):
                if (int(bigCandidate[i])<int(bigCandidate[i+1])):
                    newCandidate=newCandidate+bigCandidate[i+1:]
                    break
                else:
                    newCandidate=newCandidate+bigCandidate[i]
            bigCandidate=newCandidate

    return bigCandidate

result=[int(biggestSizeNSubsequence(string, 12)) for string in cleanedInput]
#print(result) #debugging
print(sum(result))