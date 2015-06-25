import os
from compiler.ast import flatten
from datetime import datetime
import commands
def getIdenticalFiles():
	fileList=[]
	AllFilesList=[]
	for dirname,dirnames,filenames in os.walk('./'):
	    for file in filenames:
	    	filePath = os.path.join(dirname, file)
	        AllFilesList.append(filePath)
	
	finalFileList=flatten(AllFilesList)
	identicalFileList=[]
	for i in range(0,len(finalFileList)):
		x=finalFileList.__getitem__(i)
		for j in range(i,len(finalFileList)):
			result=""
			y=finalFileList.__getitem__(j)
			if x!=y:
				str="diff"+" "+x+" "+y
				result=commands.getoutput(str)
				if result=="" or result is None:
					filetuple=(x,y)
					identicalFileList.append(filetuple)
			j+=1
		i+=1
	if len(identicalFileList)!=0:
		print "List of identical files in the current directory:\n",identicalFileList
	else:
		print "There are no identical files in the current directory"	
	print "\n\n"


def getFilesAfterModifiedDate(dateString):
        AllFilesList=[]
        modifyfileList=[]
	for dirname, dirnames, filenames in os.walk('./'):
		for filename in filenames:
			filePath = os.path.join(dirname, filename)
			AllFilesList.append(filePath)

        for i in range(0,len(AllFilesList)):
                result=""
                x=AllFilesList.__getitem__(i)
                x.replace("'","")
                str="stat"+" "+x
                result=commands.getoutput(str)
                list1=result.split()
                if "Modify:" in list1:
                        i=list1.index("Modify:")
                #extracting file's modified date
                        date1=list1.__getitem__(i+1)
                        datelist=date1.split("-")
                        year=datelist.__getitem__(0)
                        month=datelist.__getitem__(1)
                        day=datelist.__getitem__(2)
                        fileDate=month+"-"+day+"-"+year

                #formatting the inputDate
                        inputDate=datetime.strptime(dateString, "%m-%d-%Y")
                        fd=datetime.strptime(fileDate, "%m-%d-%Y")
                        b=fd > inputDate
                        if b:
                                modifyfileList.append(x)
                i+=1

	if len(modifyfileList)!=0:
        	print "The list of files which have been modified after the given date "+dateString+" are :\n",modifyfileList
	else:
		print "There are no files which have been modified after the given date "+dateString
	print "\n\n"




flag=True
while flag:
	print("\n")
	print("Enter a choice from the following options(1-3):")
	print("1. List of identical files in the current directory")
	print("2. List of files modified after a given date")
	print("3. Exit")
	try:
		i=int(raw_input("Enter a valid choice 1 or 2 or 3\n"))
		if i in range(1,4):
			if i==1:
				getIdenticalFiles()
			elif i==2:
				try:
					dateString=raw_input("Enter a date(mm-dd-yyyy)\n")
					getFilesAfterModifiedDate(dateString)
				except ValueError as err:
					print "Enter a valid date in the mm-dd-yyyy format"
					print "\n\n"
					
			elif i==3:
				flag=False
			else:
				print("Please enter a valid choice 1 or 2 or 3")
				print("\n\n")
	except ValueError as err:
		print "Please enter a number  1 or 2 or 3" 
