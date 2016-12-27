from datetime import datetime

def ifOpen():
    timeNowS = datetime.now().strftime('%H')
    timeNow = int(timeNowS)
    if timeNow>=9 and timeNow<=20:
        print('Portland HQ: Open')
    else:
        print('Portland HQ: Closed')
    if (timeNow+3)>=9 and (timeNow+3)<=20:
        print('NYC Office: Open')
    else:
        print('NYC Office: Closed')
    if (timeNow+8)>=9 and (timeNow+8)<=20:
        print('London Office: Open')
    else:
        print('London Office: Closed')


ifOpen()
