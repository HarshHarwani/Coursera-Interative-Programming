# @author hharwani

import operator
import re

##opening the input file and reading it
##returns the list of lines from the file which is read.
def openFile(filename):
    try:
        fileObject = open(filename, 'r')
        listOfLines = fileObject.readlines()
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
        word = re.sub("[^a-zA-Z]", "", word);
        processeWordList.append(word)
    return processeWordList


##this function creates a dictionary of words
##words are keys and their occurences in the file as values
def buildwordDict(processedWordList):
    wordDict = {}
    for word in processedWordList:
        words = wordDict.keys()
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
        fileObject.write("\t\t")
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


def writeCharFrequency(outputFilename, charFrequencyDict):
    sortedList=getSortedList(charFrequencyDict)
    fileObject = open(outputFilename, 'w')
    fileObject.write("\n")
    fileObject.write("The characters and their frequency are as follows:")
    fileObject.write("\n")
    for item in sortedList:
        fileObject.write(item)
        fileObject.write("\t")
        fileObject.write(str(charFrequencyDict.get(item))+"%")
        fileObject.write("\n")

##

##Declaration area
flag = True


##Main input loop
while flag:
    filename = input("Enter the path of the file to be read")
    outputFilename = input("Enter the path of the  output file")
    if filename != "" and len(filename) > 4 and outputFilename != "":
        flag = False

        # retieving the lines from the file.
        lineList = openFile(filename)

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
        sortedCharList = getSortedList(charDict)

        # getting the total no of non-white space characters.
        totalNoOfChar = getTotalNoChar(charDict)

        # calculating the frequency as percentage for each of the characters
        charFrequencyDict = getFrequencyPerc(sortedCharList, charDict, totalNoOfChar)

        # writing the frequency of different characters in the file
        writeCharFrequency(outputFilename, charFrequencyDict)

        # writing the top 10 words in the file
        writeTop10intoFile(outputFilename, sortedWordList, wordDict)

        # writing total number of words in the file.
        writeTotalWordsIntoFile(outputFilename, wordList)

        # writing the total no of non-whitespace characters in the file.
        writeTotalCharIntoFile(outputFilename, totalNoOfChar)

    else:
        print("Please enter a valid filename")
