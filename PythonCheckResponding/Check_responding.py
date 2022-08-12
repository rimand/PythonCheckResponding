import os
from datetime import datetime
import time
import math

from linenotipy import Line
line = Line(token='4nQRXaFFmESdQTv1dU0ItnPSpwuQBmggtDGsVg3ZbVe')  #G5UrvYGMVkFuRpDad7YXALaxMwlxwpqIlAcugAuWDpP

datetime1 = datetime.now().second
datetime2 = datetime.now().second

print("========[ Check_responding ]========")

def getTasks(name):
    r = os.popen('tasklist /v').read().strip().split('\n')
    print('# of tasks is %s' % (len(r)))
    for i in range(len(r)):
        s = r[i]
        if name in r[i]:
            print('%s in r[i]' % (name))
            return r[i]
    return []


if __name__ == '__main__':
    '''
    This code checks tasklist, and will print the status of a code
    '''

    imgName = 'TouchDesigner.exe'

    notResponding = 'Not Responding'

    num = 0

    while True:
        if(abs(datetime.now().second - datetime2) >= 1.0):
            print("Check ", datetime.now().second, " " , datetime.now().second - datetime1 )
            num += 1
            datetime2 = datetime.now().second

        if(abs(datetime.now().second - datetime1) >= 3.0):

            r = getTasks(imgName)

            if not r:
                print('%s - No such process' % (imgName))

            elif 'Not Responding' in r:
                print('%s is Not responding' % (imgName))
                # line.post(message='%s is Not responding!!! Check It' % (imgName))
                line.post(message='%s is Not responding!!! Check It' %
                          (imgName), stickerPackageId=446, stickerId=2011)

            else:
                print('%s is Running or Unknown' % (imgName))
                # line.post(message='%s is Running or Unknown' % (imgName))
                # line.post(message='%s is Running' % (imgName),
                #           stickerPackageId=789, stickerId=10858)

            datetime1 = datetime.now().second
            num = 0
