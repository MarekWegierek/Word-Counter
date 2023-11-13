url = './test2.txt'

def wordCounter(url, textEncoding = 'utf8', minWordLength = 0, maxWordLength = 99, numOfEntities = 10, inConsole = True):
    """ Takes .txt file and return list of most often occurring words.
        url                 url of the file
        minWordLength       minimal length of a word, by default 0
        maxWordLength       maximal length of a word, by default 99
        numOfEntities       how many words you want to return 
        inConsole           if True,    returns curated for console version of output
                            if False,   returns list of key-value pairs
    """
    fhand =  open(url, encoding=textEncoding, errors='ignore')
    counts = dict()
    result = []
    for line in fhand:
        words = line.split()
        for word in words:
            if (len(word) > minWordLength) and (len(word) < maxWordLength):
                counts[word] = counts.get(word, 0) + 1
    lst = list()
    for key, val in counts.items():
        lst.append((val, key))
    lst = sorted(lst, reverse=True)
    if inConsole:
        for val, key in lst[:numOfEntities]:
            result.append([f'{key}', (15 - len(key))*' ', 'appears', (6 - len(str(val)))*'' ,f'{val} times'])
    elif inConsole != True:
        for val, key in lst[:numOfEntities]:
            result.append([key, val])
    if inConsole:
        tempStr = ''
        for x in range(0, len(result)):
            for part in result[x]:
                tempStr = tempStr +' '+ part
            tempStr = tempStr + '\n'
        return tempStr
    if inConsole !=True:
        return result

