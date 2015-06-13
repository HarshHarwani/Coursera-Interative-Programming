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
    except NameError as exc:
        print(exc)
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
        word=word.replace("[^a-zA-Z0-9-]+","");
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
def getSortedList(wordDict):
    sortedWordList=sorted(wordDict,key=wordDict.get,reverse=True)
    return sortedWordList

def writeTop10intoFile(outputFilename,sortedWordList,wordDict):
    fileObject=open(outputFilename,'a')
    fileObject.write("\n")
    fileObject.write("The top 10 words are as follows:")
    count=0
    for i in range(len(sortedWordList)):
        if count>=10:
            break;
        fileObject.write("\n")
        fileObject.write(sortedWordList[i])
        fileObject.write("\t")
        fileObject.write(str(wordDict.get(sortedWordList[i])))
        count+=1
    fileObject.close()
    
def writeTotalWordsIntoFile(outputFilename,wordList):
    fileObject=open(outputFilename,'w')
    fileObject.write("The total no of words in the file are:")
    fileObject.write("\n")
    fileObject.write(str(len(wordList)))
    fileObject.write("\n")
    fileObject.close()


def buildCharDict(processedWordList):
    charDict={}
    for word in processedWordList:
        for char in word:
            keys=charDict.keys()
            if char in keys:
                value=charDict.get(char)
                value+=1
                charDict.update({char:value})
            else:
                charDict.update({char:1})
    return charDict

def getTotalNoChar(charDict):
    values=charDict.values()
    sum=0;
    for value in values:
        sum+=value
    return sum

def getFrequencyPerc(sortedCharList,charDict,totalNoOfChar):
    charFrequencyDict={}
    for char in sortedCharList:
        value=charDict.get(char)
        frequency=(value/totalNoOfChar)*100
        charFrequencyDict.update({char:frequency})
    return charFrequencyDict
    

##Declaration area
flag=True


##Main input loop
while flag:
    filename=input("Enter the path of the file to be read")
    outputFilename=input("Enter the path of the  output file")
    if filename!="" and len(filename)>4 and outputFilename!="":
        flag=False

        #retieving the lines from the file.
        lineList=openFile(filename)

        #retrieving the words from those lines.
        wordList=getWordsList(lineList)

        #processing the word list, removing trailing and leading whutespaces and lowercasing
        processedWordList=getProcessedWordsList(wordList)
        
        #writing total number of words in the file.
        writeTotalWordsIntoFile(outputFilename,wordList)

        #building the word dictionary
        wordDict=buildwordDict(processedWordList)

        #sorting the dictionary to get the top frequency words
        sortedWordList=getSortedList(wordDict)

        #writing the top 10 words in the file
        writeTop10intoFile(outputFilename,sortedWordList,wordDict)

        #building the character dictionary
        charDict=buildCharDict(processedWordList)

        #sorting the dictionary to get frequency of the characters as percentage
        sortedCharList=getSortedList(charDict)

        #getting the total no of non-white space characters.
        totalNoOfChar=getTotalNoChar(charDict)
        print(totalNoOfChar)

        #calculating the frequency as percentage for each of the characters
        charFrequencyDict=getFrequencyPerc(sortedCharList,charDict,totalNoOfChar)

        for item in charFrequencyDict.keys():
                print(item,str(charFrequencyDict.get(item)))
       
    else:
        print("Please enter a valid filename")
    
