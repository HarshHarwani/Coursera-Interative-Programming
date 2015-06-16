# @author hharwani
import re
##opening the input file and reading it
##returns the list of lines from the file which is read.
def openFile(filename):
    try:
        fileObject = open(filename, 'r')
    except OSError:
        print("file path is invalid")
        return
    except FileNotFoundError as err:
        print("File is not found at the given path",err)
        return
    except IOError as error:
        print("Some Error occured in Inpout-Output",error)
        print(error)
        return
    except NameError as exc:
        print(exc)
        return
    else:
        listOfLines = fileObject.readlines()
        fileObject.close()
        return listOfLines



##returns the word-list from the line-list
def getWordsList(lineList):
    wordList = []
    for line in lineList:
        wordList += line.split()
    return wordList


##lowercases all the words and removes trailing and leading whitespaces
## returns the processed wordList
def getProcessedWordsList(wordList):
    processeWordList = []
    for word in wordList:
        word = word.lower()
        word = word.strip()
        #word = re.sub("[,]", "", word);
        if word is not "":
            processeWordList.append(word)
    return processeWordList


##this function creates a dictionary of words
##words are keys and their occurences in the file as values
def buildwordDict(processedWordList):
    wordDict = {}
    for word in processedWordList:
        words = wordDict.keys()
        word = re.sub("[,:;#.$]", "", word);
        if word in words:
            value = wordDict.get(word)
            value += 1
            wordDict.update({word: value})
        else:
            wordDict.update({word: 1})
    return wordDict


# sorts the dictionary be values in descending order and returns it
def getSortedList(wordDict):
    sortedWordList = sorted(wordDict, key=wordDict.get, reverse=True)
    return sortedWordList



# builds the character dictionary with char as key and their occurences as value
def buildCharDict(processedWordList):
    charDict = {}
    for word in processedWordList:
        for char in word:
                keys = charDict.keys()
                if char in keys:
                    value = charDict.get(char)
                    value += 1
                    charDict.update({char: value})
                else:
                    charDict.update({char: 1})
    return charDict


# counts the total number of characters in the file
def getTotalNoChar(charDict):
    values = charDict.values()
    sum = 0;
    for value in values:
        sum += value
    return sum


# calculates the frequency as percentage of various characters in the file.
def getFrequencyPerc(sortedCharList, charDict, totalNoOfChar):
    charFrequencyDict = {}
    for char in sortedCharList:
        value = charDict.get(char)
        frequency = (value / totalNoOfChar) * 100
        charFrequencyDict.update({char: frequency})
    return charFrequencyDict


##writing functions for writing various stastics in the file
def writeTop10intoFile(outputFilename, sortedWordList, wordDict):
    fileObject = open(outputFilename, 'a')
    fileObject.write("\n")
    fileObject.write("The top 10 words are as follows:")
    fileObject.write("\n")
    count = 0
    for i in range(len(sortedWordList)):
        if count == 10:
            break;
        fileObject.write(sortedWordList[i])
        fileObject.write("\t")
        fileObject.write(str(wordDict.get(sortedWordList[i])))
        fileObject.write("\n")
        count += 1
    fileObject.close()


def writeTotalWordsIntoFile(outputFilename, wordList):
    fileObject = open(outputFilename, 'a')
    fileObject.write("\n")
    fileObject.write("The total no of words in the file are:")
    fileObject.write("\n")
    fileObject.write(str(len(wordList)))
    fileObject.write("\n")
    fileObject.close()


def writeTotalCharIntoFile(outputFilename, totalNoOfChar):
    fileObject = open(outputFilename, 'a')
    fileObject.write("\n")
    fileObject.write("The total no of non-whitespace characters in the file are:")
    fileObject.write("\n")
    fileObject.write(str(totalNoOfChar))
    fileObject.write("\n")
    fileObject.close()


def writeCharFrequency(outputFilename, charFrequencyDict,charDict):
    charList=[]
    for i in range(97,123):
        charList.append(chr(i))
    sortedList=sorted(charFrequencyDict)
    fileObject = open(outputFilename, 'w')
    fileObject.write("Various stastics of the file are as follows:")
    fileObject.write("\n\n")
    fileObject.write("The characters,their counts and their frequency are as follows:")
    fileObject.write("\n")
    for item in sortedList:
        if ord(item)>=97 and ord(item)<=122:
            charList.remove(item)
            fileObject.write(item)
            fileObject.write("\t")
            fileObject.write(str(charDict.get(item)))
            fileObject.write("\t")
            fileObject.write(str(charFrequencyDict.get(item))+"%")
            fileObject.write("\n")
    for char in charList:
            fileObject.write(char)
            fileObject.write("\t")
            fileObject.write(str("0"))
            fileObject.write("\t")
            fileObject.write(str("0.00%"))
            fileObject.write("\n")


##

##Declaration area
flag = True


##Main input loop
while flag:
    filename = input("Enter input filename\n")
    outputFilename = input("Enter output file name\n")
    if filename==outputFilename:
        print("Input and output file can't be same")

    if filename != "" and outputFilename != "" and filename!=outputFilename:
        flag = False

        # retieving the lines from the file.
        lineList = openFile(filename)
        if lineList is None:
            flag=True

        if not flag:
            # retrieving the words from those lines.
            wordList = getWordsList(lineList)

            # processing the word list, removing trailing and leading whutespaces and lowercasing
            processedWordList = getProcessedWordsList(wordList)

            # building the word dictionary
            wordDict = buildwordDict(processedWordList)

            # sorting the dictionary to get the top frequency words
            sortedWordList = getSortedList(wordDict)

            # building the character dictionary
            charDict = buildCharDict(processedWordList)

            # sorting the dictionary to get frequency of the characters as percentage
            sortedCharList = sorted(charDict)

            # getting the total no of non-white space characters.
            totalNoOfChar = getTotalNoChar(charDict)

            # calculating the frequency as percentage for each of the characters
            charFrequencyDict = getFrequencyPerc(sortedCharList, charDict, totalNoOfChar)

            # writing the frequency of different characters in the file
            writeCharFrequency(outputFilename, charFrequencyDict,charDict)

            # writing the top 10 words in the file
            writeTop10intoFile(outputFilename, sortedWordList, wordDict)

            # writing total number of words in the file.
            writeTotalWordsIntoFile(outputFilename, wordList)

            # writing the total no of non-whitespace characters in the file.
            writeTotalCharIntoFile(outputFilename, totalNoOfChar)

            print("Output file created successfully:"+outputFilename)

        else:
            print("Please enter a valid filename")
