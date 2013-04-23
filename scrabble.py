import itertools
import string

def isWord(word, dic):
    try:
        return dic[word.lower()]>=0
    except KeyError:
        return False

def wordScore(word):
    score = 0
    for letter in word:
        score += tiles[letter]
    return score

def createDict():
    words = {}
    for x in open('TWL06.txt'):
        length=len(x)
        x=x.lower().split('\n')[0]
        words[x] = wordScore(x)
    return words

def createBoard():
    board = []
    for i in range(0,15):
        board.append([])
        for j in range(0,15):
            board[i].append('0')
    return board

def goThrough(letters, dic):
    for perm in itertools.permutations(letters):
        w = ''
        for l in perm:
            w+=l
        if isWord(w, dic):
            print(w)

def bingoCheck(word, dic):
    letters = []
    blankInd = [0,0]
    count = 0
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(0,len(word)):
        if word[i]=='?':
            blankInd[count]=i
            count+=1
        letters.append(word[i])
    if count>0:
        for a in alpha:
            for j in range(0,count):
                letters[blankInd[j]]=a
            letCopy=list(letters)
            goThrough(letCopy, dic)
    else:
        goThrough(letters, dic)

def stackCheck(dic, length): #see which words of size length can be stacked
    lst = []
    found = []
    for word in dic:
        if(len(word)==length):
            lst.append(word)
    for word1 in lst:
        if(isIn(word1, 'c', 'v')):
            continue
        for word2 in lst:
            if(stackCompare(word1, word2, dic)):
                print(word1, word2)

def stackCompare(word, word2, dic): #check if 2 words can be stacked
    #print("%s %s", word, word2)
    i=0
    for i in range(0, len(word)):
        if(not isWord(str(word[i]+word2[i]), dic)):
            return False
    return True

def isIn(word, let1, let2):
    for let in word:
        if(let==let1 or let==let2):
            return True
    return False
    
        
tiles = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

words = createDict()
while True:
    print("Check: ")
    lets = input()
    if(lets[0:5]=="bingo"): #check all combinations for bingo
        print(bingoCheck(lets[6:], words))
    else: #check if in dictionary
        print(isWord(lets, words))
