while True:
    word = 0
    char = 0
    he = 0
    she = 0
    file = open("STORY.txt")
    text = file.read()
    textSplit = text.split()
    for i in textSplit:
        if "he" == i.lower():
            he+=1
        elif "she" == i.lower():
            she +=1
        char += len(i)
    print(textSplit)
    print('He count:', he)
    print('She count:', she)
    print('Word count:', len(textSplit))
    print('Character count:', char)
    if input('Continue:[Y/N]') == 'N':
        break
