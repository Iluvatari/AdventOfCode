

fileH = open('input.txt','r')
fileText = fileH.readlines()
fileText = fileText[0]
for idx, currChar in enumerate(fileText):
    if idx < 14:
        continue
    if len(set(fileText[idx-13:idx + 1])) == 14:
        print(idx)
        break