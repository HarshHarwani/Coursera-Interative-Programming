import operator
##opening the input file and reading it
##returns the list of lines from the file which is read.
def openFile(filename):
    try:
        fileObject=open(filename,'r')
        listOfLines=fileObject.readlines()
    except FileNotFoundError as err:
        print(err)
        return
    except IOError as error:
        print(error)
        return
    else:
        return listOfLines
    finally:
        fileObject.close()

##returns the word-list from the line-list
def getWordsList(lineList):
    wordList=[]
    for line in lineList:
        wordList+=line.split()
    return wordList

##lowercases all the words and removes trailing and leading whitespaces
## returns the processed wordList
def getProcessedWordsList(wordList):
    processeWordList=[]
    for word in wordList:
        word=word.lower()
        word=word.strip()
        processeWordList.append(word)
    return processeWordList

##this function creates a dictionary of words
##words are keys and their occurences in the file as values
def buildwordDict(processedWordList):
    wordDict={}
    for word in processedWordList:
        words=wordDict.keys()
        if word in words:
            value=wordDict.get(word)
            value+=1
            wordDict.update({word:value})
        else:
            wordDict.update({word:1})
    return wordDict

#sorts the dictionary be values in descending order and returns it
def getTop10Words(wordDict):
    sortedWordList=sorted(wordDict,key=wordDict.get,reverse=True)
    return sortedWordList

##Declaration area
flag=True


##Main input loop
while flag:
    filename=input("Enter the path of the file to be read")
    if filename!="" and len(filename)>4:
        flag=False

        #retieving the lines from the file.
        lineList=openFile(filename)

        #retrieving the words from those lines.
        wordList=getWordsList(lineList)

        #processing the owrd list, removing trailing and leading whutespaces and lowercasing
        processedWordList=getProcessedWordsList(wordList)

        #building the word dictionary
        wordDict=buildwordDict(processedWordList)

        #sorting the dictionary to get the top frequency words
        sortedWordList=getTop10Words(wordDict)

        for i in range(10):
            print(sortedWordList[i])
    else:
        print("Please enter a valid filename")
    
