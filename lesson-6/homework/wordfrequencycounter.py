
filename="sample.txt"
filename2="word_count_report.txt"
def fileInput():
    global filename
    try:
        file=open(filename)
        file.close()
        
    except IOError:
        try:
            file=open(filename,'w')
            while(True):
                content=input("Enter a paragraph or article: ")
                if(content!=""):
                    break
            file.write(content)
            file.close()
        except IOError:
            print("There was an error with working files")
# fileInput()

def synth(word):
    while(True):
        if(',' in word):
            word1=word.split(",")
            # word=word1.join()
        elif('.' in word):
            word1=word.split(".")
            # word1.join()
        elif('\n' in word):
            word1=word.split("\n")
            # word1.join()
        else:
            break
        
        word=word1.join()
    return word

def countWordFrequency():
    global filename
    try:
        counts=list()
        fileInput()
        with open(filename) as file_handler:
            all = file_handler.read()
            all=all.lower()
            arrAll=all.split(" ")
            # print(arrAll)
            newArr=list()
            for arr in arrAll:
                if(arr!=""):
                    if("," in arr):
                        arr1=arr.split(",")
                        # print(arr1)
                        # n=arr1[0]
                        arr=arr1[0]
                    if("." in arr):
                        arr1=arr.split(".")
                        arr=arr1[0]
                        # newArr.append(n)
                        # print(arr1)
                    if("\n" in arr):
                        arr1=arr.split("\n")
                        arr=arr1[0]
                    newArr.append(arr)
                # m=synth(arr)
                # print(arr)
                # newArr.append(m)
                # if("," in arr):
                #     arr1=arr.split(",")
                #     print(arr1)
                #     # newArr.append(arr1[0])
                # if("." in arr):
                #     arr1=arr.split(".")
                #     newArr.append(arr1[0])
                # if("\n" in arr):
                #     arr1=arr.split("\n")
                #     newArr.append(arr1[0])
            # print(newArr)
            counts.append(len(newArr))
            newSet=set(newArr)
            newCount=list()
            newList1=list(newSet)
            newDict=dict()
            for item in newSet:
                num=newArr.count(item)
                newCount.append(num)
                # newDict[item]=num

            for i in range(len(newCount)):
                for j in range(len(newCount)-1):
                    if(newCount[j]<newCount[j+1]):
                        num=newCount[j]
                        newCount[j]=newCount[j+1]
                        newCount[j+1]=num
                        n=newList1[j]
                        newList1[j]=newList1[j+1]
                        newList1[j+1]=n
            for i in range(len(newList1)):
                num=newCount[i]
                item=newList1[i]
                # newCount.append(num)
                newDict[item]=num
            counts.append(newDict)
            # print(counts)
        file_handler.close()
        return counts
                
    except:
        print("An error occured with working on files")




def outputAll(counts,a):
    wordList=counts[1]
    total=counts[0]
    content=""
    content=(f"""Total words: {total}\nTop {a} most common words:\n""")
    c=0
    for item in wordList.items():
        content+=f"""{item[0]} - {item[1]} times\n"""
        if(c>=a):
            break
        c+=1

    return content

def writeFile(counts,a):
    try:
        wordList=counts[1]
        total=counts[0]
        content="Word Count Report\n"
        content=f"""Total words: {total}\nTop {a} words:\n"""
        c=0
        for item in wordList.items():
            content+=f"""{item[0]} - {item[1]}\n"""
            if(c>=a):
                break
            c+=1


        file=open(filename2,'w')
        file.write(content)
        file.close()
    except IOError:
        print("Error happened")

counts=countWordFrequency()
# print(counts)
a=int(input('Enter how many top words you want to see: '))
content=outputAll(counts,a)
print(content)
writeFile(counts,a)

