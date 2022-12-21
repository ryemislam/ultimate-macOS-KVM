# GPU-CHECK v0.1 BY COOPYDOOD
import os
import time
import subprocess
import re 
import json
detectChoice = 1
latestOSName = "Ventura"
latestOSVer = "13"
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def startup():
    global detectChoice
    print("Welcome to"+color.BOLD+color.YELLOW,"gpu-check v0.1"+color.END)
    print("Created by",color.BOLD+"Coopydood\n"+color.END)
    print("\nThe purpose of this script is to check your exact system's GPU model against a compatibility list created and provided by"+color.BOLD,"Dortania.\n"+color.END)
    print("\nI can attempt to check what GPU you have automatically, or you can manually enter it. Which would you prefer?")
    print(color.BOLD+"\n1. Detect automatically (recommended)")
    print(color.END+"2. Enter manually")
    print(color.END+"3. Exit\n")
    detectChoice = int(input(color.BOLD+"Select> "+color.END))

startup()
#debug

def clear(): print("\n" * 150)


def autoRun():
    print("Running auto detection script...")
    time.sleep(1)
    clear()

    output_stream = os.popen('lspci -v | grep "VGA"')
    vgaGrep = output_stream.read().splitlines()
   # print(vgaGrep)

    output_stream1 = os.popen('lspci | grep "VGA" | cut -d" " -f 1')
    vgaGrepIDs = output_stream1.read().splitlines()
   # print(vgaGrepIDs)


    vgaGrepT = []

    for x in vgaGrep:
        #val = x.split('[', 1)[1].split(']')
        
        val = re.findall('\[.*?\]', x)
        vgaGrepT.append(val)
    #print(vgaGrepT)
    gpuList = open("./gpuList.json")
    data = json.load(gpuList)
    #for x in vgaGrepT:
    model = str(vgaGrepT)
    gpus = [y for y in data['gpuList']]
    gpuCount = -1
    for gpu in gpus:
       # print("trying to find",gpu["name"])
       # print("seeing if",gpu["name"],"is contained within",model)
        if (gpu["name"]) in model:
            gpuCount = gpuCount + 1
            gpuName = gpu["fullName"]
            gpuSupport = gpu["supported"]
            gpuVendor = gpu["vendor"]
            gpuMinOS = gpu["minOS"]
            gpuMaxOS = gpu["maxOS"]
            gpuQuirks = gpu["quirks"]

           # if gpuSupport == False:
           #     gpuSupport = "Supported"
           # else:
            #    gpuSupport = "Unsupported"


            if gpuMinOS == "-1":
                gpuMinOS = "N/A"

            

            if gpuQuirks == "0":
                gpuQuirks = "This GPU should work fine as-is under macOS!"
            elif gpuQuirks == "-1":
                gpuQuirks = "This GPU is NOT supported in macOS at all. Sorry :["

            gpuMaxOSF = "N/A"
            if gpuMaxOS in "10.2":
                gpuMaxOSF = "Jaguar ("+gpuMaxOS+")"
            elif gpuMaxOS in "10.3":
                gpuMaxOSF = "Panther ("+gpuMaxOS+")"
            elif gpuMaxOS in "10.4":
                gpuMaxOSF = "Tiger ("+gpuMaxOS+")"
            elif gpuMaxOS in "10.5":
                gpuMaxOSF = "Leopard ("+gpuMaxOS+")"
            elif gpuMaxOS in "10.6":
                gpuMaxOSF = "Snow Leopard ("+gpuMaxOS+")"
            elif gpuMaxOS in "10.7":
                gpuMaxOSF = "Lion ("+gpuMaxOS+")"
            elif gpuMaxOS in "10.8":
                gpuMaxOSF = "Mountain Lion ("+gpuMaxOS+")"
            elif gpuMaxOS in "10.9":
                gpuMaxOSF = "Mavericks ("+gpuMaxOS+")"
            elif gpuMaxOS in "10.10":
                gpuMaxOSF = "Yosemite ("+gpuMaxOS+")"
            elif gpuMaxOS in "10.11":
                gpuMaxOSF = "El Capitan ("+gpuMaxOS+")"
            elif "10.12" in gpuMaxOS:
                gpuMaxOSF = "Sierra ("+gpuMaxOS+")"
            elif "10.13" in gpuMaxOS:
                gpuMaxOSF = "High Sierra ("+gpuMaxOS+")"
            elif gpuMaxOS in "10.14":
                gpuMaxOSF = "Mojave ("+gpuMaxOS+")"
            elif gpuMaxOS in "10.15":
                gpuMaxOSF = "Catalina ("+gpuMaxOS+")"
            elif gpuMaxOS in "11":
                gpuMaxOSF = "Big Sur ("+gpuMaxOS+")"
            elif gpuMaxOS in "12":
                gpuMaxOSF = "Monterey ("+gpuMaxOS+")"
            elif gpuMaxOS in "13":
                gpuMaxOSF = "Ventura ("+gpuMaxOS+")"
            
            gpuMinOSF = "N/A"
            if gpuMinOS in "10.2":
                gpuMinOSF = "Jaguar ("+gpuMinOS+")"
            elif gpuMinOS in "10.3":
                gpuMinOSF = "Panther ("+gpuMinOS+")"
            elif gpuMinOS in "10.4":
                gpuMinOSF = "Tiger ("+gpuMinOS+")"
            elif gpuMinOS in "10.5":
                gpuMinOSF = "Leopard ("+gpuMinOS+")"
            elif gpuMinOS in "10.6":
                gpuMinOSF = "Snow Leopard ("+gpuMinOS+")"
            elif gpuMinOS in "10.7":
                gpuMinOSF = "Lion ("+gpuMinOS+")"
            elif gpuMinOS in "10.8":
                gpuMinOSF = "Mountain Lion ("+gpuMinOS+")"
            elif gpuMinOS in "10.9":
                gpuMinOSF = "Mavericks ("+gpuMinOS+")"
            elif gpuMinOS in "10.10":
                gpuMinOSF = "Yosemite ("+gpuMinOS+")"
            elif gpuMinOS in "10.11":
                gpuMinOSF = "El Capitan ("+gpuMinOS+")"
            elif "10.12" in gpuMinOS:
                gpuMinOSF = "Sierra ("+gpuMinOS+")"
            elif gpuMinOS in "10.13":
                gpuMinOSF = "High Sierra ("+gpuMinOS+")"
            elif gpuMinOS in "10.14":
                gpuMinOSF = "Mojave ("+gpuMinOS+")"
            elif gpuMinOS in "10.15":
                gpuMinOSF = "Catalina ("+gpuMinOS+")"
            elif gpuMinOS in "11":
                gpuMinOSF = "Big Sur ("+gpuMinOS+")"
            elif gpuMinOS in "12":
                gpuMinOSF = "Monterey ("+gpuMinOS+")"
            elif gpuMinOS in "13":
                gpuMinOSF = "Ventura ("+gpuMinOS+")"

            #print("it was!")
            #print("GPU"+str(gpuCount),gpuName)
            print(color.BOLD+gpuName+color.END)
            print("───────────────────────────────")
            if gpuSupport == True:
                print(color.BOLD+color.GREEN+"●",color.END+"Supported\n")
            else:
                print(color.BOLD+color.RED+"●",color.END+"Unsupported\n")
            
            if gpuMaxOS == "9999":
                print(color.BOLD+"Maximum macOS:"+color.END,"Latest /",latestOSName,"("+latestOSVer+")")
            elif gpuMaxOS == "-1":
                print(color.BOLD+"Maximum macOS:"+color.END,"N/A")
            else:
                print(color.BOLD+"Maximum macOS:"+color.END,gpuMaxOSF)

            if gpuMinOS == "-1":
                print(color.BOLD+"Minimum macOS:"+color.END,"N/A")
            else:
                print(color.BOLD+"Minimum macOS:"+color.END,gpuMinOSF)
            
            print("\n"+color.BOLD+"Additional Information"+color.END)
            print(gpuQuirks)

            print("\n")



        



def manualRun():
    exit
print("choice was ",detectChoice)

if detectChoice == 1:
    autoRun()
elif detectChoice == 2:
    manualRun()
else:
    exit


