#if you are on 32 bit OS:
#import Image

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
import time
from collections import Counter

#i = Image.open('images/numbers/0.1.png')
#iar = np.asarray(i)

#print (iar)

#plt.imshow(iar)
#plt.show()

def createExamples():
    numberArrayExamples = open('numArEx.txt','a')
    numbersWeHave = range(0,10)
    versionsWeHave = range(1,10)

    for eachNum in numbersWeHave:
        for eachVer in versionsWeHave:
           # print (str(eachNum) + '.' + str(eachVer))
           imgFilePath = 'images/numbers/'+str(eachNum)+'.'+str(eachVer)+'.png'
           ei = Image.open(imgFilePath)
           eiar = np.array(ei)
           eiar1 = str(eiar.tolist())

           lineToWrite = str(eachNum)+ '::' +eiar1+'\n'
           numberArrayExamples.write(lineToWrite)

def threshold(imageArray):
    balanceAr = []
    newAr = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            # print(eachPix)

            # time.sleep(2)
            avgNum = reduce(lambda x, y: x+y, eachPix[:3])/len(eachPix[:3])
            balanceAr.append(avgNum)

    balance = reduce(lambda x, y: x+y, balanceAr)/len(balanceAr)

    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x+y, eachPix[:3])/len(eachPix[:3])>balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255
                eachPix[3] = 255
            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0
                eachPix[3] = 255
    return newAr
'''
i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)

'''
'''
threshold(iar3)
#threshold(iar2)
threshold(iar4)


fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)

ax1.imshow(iar)
ax2.imshow(iar2)
ax3.imshow(iar3)
ax4.imshow(iar4)

plt.show()
'''

def what(filepath):
    matchedAr = []
    loadExamps = open('numArEx.txt','r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filepath)
    iar = np.array(i)
    iarl = iar.tolist()

    inQue = str(iarl)

    for each in loadExamps:
        if len(each) > 3:
            splitEx = each.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            eachPixEx = currentAr.split('],')

            eachPixInQ = inQue.split('],')

            x=0
            
            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append(int(currentNum))

                    x +=1

    print(matchedAr)
    x = Counter(matchedAr)
    print (x)

    graphX = []
    graphY = []
    for eachThing in x:
        print (eachThing)
        graphX.append(eachThing)
        print(x[eachThing])
        graphY.append(x[eachThing])

    fig = plt.figure()
    ax1 =plt.subplot2grid((4,4), (0,0), rowspan=1, colspan=4)
    ax2 =plt.subplot2grid((4,4), (1,1), rowspan=3, colspan=4)

    ax1.imshow(iar)
    ax2.bar(grpahX, graphY, aligh='center')
    plt.ylim(400)
    xloc = plt.MaxNLocator(12)

    ax2.xaxis.set_major_locator(xloc)

    plt.show()
    
what('images/test.png')
