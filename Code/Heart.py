# Project 5: The Happy Heart Program
# This is a heart function monitoring system that will raise an alarm if there is something seriously wrong. 
# It will be monitoring Pulse Rate, Blood pressure, and Blood oxygen level. This is a simulation so the data
# will be imported or typed in.
from time import sleep


def pulseRate(pulse): #first input 10 second checking

    nPulse = int(pulse)
    #checking where the pulse number lands on scale from 0 to 210 and raising according alert
    if nPulse <= 20: 
        return("Pulse Extremly Low: {}".format(nPulse))
    elif nPulse >= 20 and nPulse < 40:
        return("Pulse Below Normal: {}".format(nPulse))
    elif nPulse >= 40 and nPulse < 110:
        return("None")
    elif nPulse >= 110 and nPulse < 130:
        return("Pulse Slightly Above Normal: {}".format(nPulse))
    elif nPulse >= 130 and nPulse <= 170:
        return("Pulse Above Normal: {}".format(nPulse))
    elif nPulse > 170 and nPulse <= 210:
        return("Pulse Extremly High: {}".format(nPulse))     
    elif nPulse > 210:
        return("Incorrect Data")   

def bloodOxygenLevel(level,oxygenTracker): #second input 10 seconds
  
    oxygenTracker.append(level)
    add = 0
    if len(oxygenTracker) <= 6: #if less than 6 add all together for average
        for ind in oxygenTracker:
            add = add + int(ind)
            nLevel = add / len(oxygenTracker)
    else:
        lastFive = oxygenTracker[-6::]
        for ind in lastFive: #if greater than 6 add up last 6 for average
            add = add + int(ind)
            nLevel = add / len(lastFive)
    nLevel = nLevel / 100
    if nLevel < .50:
        return("Oxygen Extreemly Low: {}".format(round(nLevel*00,1))) 
    elif nLevel < .80 and nLevel >=.5:
        return("Oxygen Really Low: {}".format(round(nLevel*100,1))) 
    elif nLevel < .85 and nLevel >=.8:
        return("Oxygen Low: {}".format(round(nLevel*100,1))) 
    elif nLevel < 1 and nLevel >= .85:
        return("None")
    elif nLevel >= 1 or nLevel <=0:
        return("Incorrect Data") 
             

def bloodPressure(pressure): #third input random checking

    nPressure = pressure.split('/') #splitting up number
    systolic = int(nPressure[0]) #upper number
    diastolic = int(nPressure[1]) #lower number
    #checking where the blood pressure fits
    if systolic > 200 or diastolic > 120:
        return("Pressure Dangerously High: {}".format(pressure))
    elif systolic > 150 and systolic <= 200:
        return("Pressure Somewhat High: {}".format(pressure))
    elif systolic <= 150 and systolic >= 70:
        if diastolic > 90 and diastolic <= 120:
            return('Pressure Somewhat High: {}'.format(pressure))
        elif diastolic < 40 and diastolic >= 33:
            return("Pressure Somewhat Low: {}".format(pressure))
        elif diastolic < 33:
            return("Pressure Dangerously Low: {}".format(pressure))
        elif diastolic <= 90 and diastolic >= 40:
            return("None") 

    elif systolic < 70 and systolic >= 50: #and 
        return("Pressure Somewhat Low: {}".format(pressure))
    elif systolic > 50 or diastolic < 33:
        return("Pressure Dangerously Low: {}".format(pressure))


def printStatement(sec,min,pul,blOx,blPr):
    alertDesc, medAlert = alertLevel(pul,blOx,blPr)
    if sec == 0:
        str = "0{}:0{}  {:<12}{:<40}".format(min,sec,medAlert,alertDesc)
        print(str)
    else:
        str = "0{}:{}  {:<12}{:<40}".format(min,sec,medAlert,alertDesc)
        print(str)

def alertLevel(pul,blOx,blPr): #find alert level to display

    pel = "Pulse Extremly Low:"
    pbn = "Pulse Below Normal:"
    psan = "Pulse Slightly Above Normal:"
    pan = "Pulse Above Normal:"
    peh = "Pulse Extremly High:"

    oel = "Oxygen Extremly Low:"
    orl = "Oxygen Really Low:"
    ol = "Oxygen Low:"

    pdh = "Pressure Dangerously High:"
    psh = "Pressure Somewhat High:"
    psl = "Pressure Somewhat Low:"
    pdl = "Pressure Dangerously Low:"

    extreem = [pel,peh,oel,pdl]
    medium = [pbn,pan,orl,psh,psl,pdh]
    low = [psan,ol]

    for i in extreem:
        if str(i) in pul:
            return pul,'Med Alert'
        elif str(i) in blOx:
            return blOx,'Med Alert'
        elif str(i) in blPr:
            return blPr,'Med Alert'
    for i in medium:
        if str(i) in pul:
            return pul,'Med Alert'
        elif str(i) in blOx:
            return blOx,'Med Alert'
        elif str(i) in blPr:
            return blPr,'Med Alert'
    for i in low:
        if str(i) in pul:
            return pul,'Med Alert'
        elif str(i) in blOx:
            return blOx,'Med Alert'
        elif str(i) in blPr:
            return blPr,'Med Alert'

    if pul == "None" and blOx == "None" and blPr == "None":
        return "None","None"
    elif pul == "Incorrect Data" and blOx == "Incorrect Data" and blPr == "Incorrect Data":
        return "Incorrect Data","Incorrect Data"
    
def readInData(oxygenTracker): #reads in inputs from text file
    with open('inputs.txt') as f:
        sec = 0
        min = 0
        for line in f: #seperating by line
            if sec == 60:
                sec = 0
                min = min +1
            seperated = line.split(',')#breaking line up by comma's
            seperated[0] = seperated[0].replace('\n','') #Getting rid of \n 
            seperated[1] = seperated[1].replace('\n','')
            seperated[2] = seperated[2].replace('\n','')

            if len(seperated) == 3: #if all 3 inputs
                pul = pulseRate(int(seperated[0]))
                blOx = bloodOxygenLevel(float(seperated[1]),oxygenTracker)
                blPr = bloodPressure(seperated[2])
            elif len(seperated) == 2: # if 2 imputs
                    pul = pulseRate(int(seperated[0]))
                    blOx = bloodOxygenLevel(float(seperated[1]),oxygenTracker)
            elif len(seperated) == 1:
                    pul = pulseRate(int(seperated[0]))
            else: 
                print('No inputs')

            printStatement(sec,min,pul,blOx,blPr)
            sec = sec + 10
            sleep(10)
def manualInput(oxygenTracker):
    answer = ''
    seperated = []
    sec = 0
    min = 0
    while answer != 'stop':
        if sec == 60:
            sec = 0
            min = min +1
        while True:
            print("\nInput values as asked:\n")
            print("Range from 0 to  210")
            pul = int(input("Pulse level: "))
            if pul >= 0 and pul <= 210:
                break
        seperated.append(pul)
        while True:
            print("Range from 0 to  100")
            blOx = int(input("Blood Oxygen level: "))
            if blOx >=0 and blOx <= 100:
                break
        seperated.append(blOx)
        while True:
            print("Enter as _/_  : systolic(upper) Range:0-230 / diastolic(lower) Range:0-150")
            blPr = input("Blood Pressure level: ")
            nPressure = blPr.split('/') #splitting up number
            if(len(nPressure) == 2):
                systolic = int(nPressure[0]) #upper number
                diastolic = int(nPressure[1]) #lower number
            else:
                systolic = -1
                diastolic = -1

            if systolic >=0 and systolic <= 230 and diastolic >= 0 and diastolic <= 150:
                break
        seperated.append(blPr)
        
        if len(seperated) == 3: #if all 3 inputs
            pul = pulseRate(int(seperated[0]))
            blOx = bloodOxygenLevel(float(seperated[1]),oxygenTracker)
            blPr = bloodPressure(seperated[2])
        elif len(seperated) == 2: # if 2 imputs
                pul = pulseRate(int(seperated[0]))
                blOx = bloodOxygenLevel(float(seperated[1]),oxygenTracker)
        elif len(seperated) == 1:
                pul = pulseRate(int(seperated[0]))
        else: 
            print('No inputs')
        print("{}  {:<12}{:<40}".format("\nTime:", "Alarm:","Description:"))
        printStatement(sec,min,pul,blOx,blPr)
        sec = sec + 10
    #    sleep(10)
        



def main():
    print("\nProject 5: The Happy Heart Program\n")
    oxygenTracker = [] #array to hold oxygen levels for moving average
    answer = ''
    while (True):
        print("Do you want to read from file? Or Input data?")
        answer = input("Type yes to read from file or no to manually input: ")
        if answer == 'yes' or answer == 'no':
            break
    if answer == "yes":
        print("{}  {:<12}{:<40}".format("\nTime:", "Alarm:","Description:"))
        readInData(oxygenTracker)
    elif answer == "no":
        manualInput(oxygenTracker)


if __name__ == "__main__":
    main()