"""first half"""
inputFile = open("input puzzle 1", 'r', encoding="utf-8")
combination=list(inputFile)
#manualInput= ['L68', 'L30', 'R48','L5','R60','L55','L1','L99','R14','L82']
#combination=manualInput
dialPos = 50
password=0
for x in (combination):
    if (x[0]=='L'):
        dialPos=dialPos-(int(x[1:]))
    else:
        dialPos=dialPos+(int(x[1:]))
    dialPos=dialPos%100
    if (dialPos==0):
        password+=1
print(password)

"""second half"""

#manualInput= ['L68', 'L30', 'R48','L5','R60','L55','L1','L99','R14','L82']
#combination=manualInput

dialPos=50
password=0
for x in (combination):
    if (dialPos==0 and x[0]=='L'):
        password-=1
    if (x[0]=='L'):
        dialPos=dialPos-(int(x[1:]))
    else:
        dialPos=dialPos+(int(x[1:]))
        
    password=password+abs(dialPos//100)
    dialPos=dialPos%100
    if (dialPos==0 and x[0]=='L'):
        password+=1
    

print(password)