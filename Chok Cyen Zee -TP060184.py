#CHOK CYEN ZEE
#TP060184

def CounterATO(): #generates patient ID for ATO
    filehandler = open('Patient_Detail.txt','r')
    ID = 100
    for line in filehandler: #checks if ID already exist in file
        line = line.rstrip()
        if str(ID) in line:
            ID = ID+1
    return ID

def CounterACC(): #generates patient ID for ACC
    filehandler = open('Patient_Detail.txt','r')
    ID = 200
    for line in filehandler:
        line = line.rstrip()
        if str(ID) in line:
            ID = ID+1
    return ID

def CounterAEO(): #generates patient ID for AEO
    filehandler = open('Patient_Detail.txt','r')
    ID = 300
    for line in filehandler:
        line = line.rstrip()
        if str(ID) in line:
            ID = ID+1
    return ID

def CounterSID(): #generates patient ID for SID
    filehandler = open('Patient_Detail.txt','r')
    ID = 400
    for line in filehandler:
        line = line.rstrip()
        if str(ID) in line:
            ID = ID+1
    return ID

def CounterAHS(): #generates patient ID for AHS
    filehandler = open('Patient_Detail.txt','r')
    ID = 500
    for line in filehandler:
        line = line.rstrip()
        if str(ID) in line:
            ID = ID+1
    return ID

def PatientsReg(): #for registering patients
    Registration = []
    PatientIDATO = CounterATO()
    PatientIDACC = CounterACC()
    PatientIDAEO = CounterAEO() #assign counters as variables
    PatientIDSID = CounterSID()
    PatientIDAHS = CounterAHS()
    reg = []
    PatientName = input("Enter patient's name: ")
    NameLabel = ('Name    :'+PatientName)
    Email = input("Enter patient's email: ")
    EmailLabel = ('Email   :'+Email)
    Contact = input("Enter patient's contact number: ")
    ContactLabel = ('Contact :'+Contact)
    Zone = input("Enter patient's Zone(A/B/C/D): ")
    while Zone != 'A' and Zone != 'B' and Zone != 'C' and Zone != 'D':
        print("Zone doesn't exist\n")
        menu()
    ZoneLabel = ('Zone    :'+Zone)
    print()
    print('Asymptomatic individuals with history of traveling overseas(ATO)')
    print('Asymptomatic individuals with history of contact with known case of COVID19(ACC)')
    print('Asymptomatic individuals who has attended event associated with known COVID-19 outbreak(AEO)')
    print('Symptomatic individuals(SID)')
    print('Asymptomatic hospital staff(AHS)')
    print()
    Group = input("Enter patient's Group(ATO/ACC/AEO/SID/AHS): ")
    GroupLabel = ('Group   :'+Group)
    if Group == "ATO": #registered patients saved to list according to their group
        print('Patient ID number is: '+'ATO'+str(PatientIDATO))
        print('Patient registered...')
        IDLabel = ('ID      :'+'ATO'+str(PatientIDATO))
        reg.append(IDLabel)
        reg.append(GroupLabel) 
        reg.append(NameLabel)
        reg.append(EmailLabel)
        reg.append(ContactLabel)
        reg.append(ZoneLabel)
        
    elif Group == "ACC": #every option gets to store on their own list so it doesnt get registered if wrong group is written
        print('Patient ID number is: '+'ACC'+str(PatientIDACC))
        print('Patient registered...')
        IDLabel = ('ID      :'+'ACC'+str(PatientIDACC))
        reg.append(IDLabel)
        reg.append(GroupLabel)
        reg.append(NameLabel)
        reg.append(EmailLabel)
        reg.append(ContactLabel)
        reg.append(ZoneLabel)
        
    elif Group == "AEO":
        print('Patient ID number is: '+'AEO'+str(PatientIDAEO))
        print('Patient registered...')
        IDLabel = ('ID      :'+'AEO'+str(PatientIDAEO))
        reg.append(IDLabel)
        reg.append(GroupLabel)
        reg.append(NameLabel)
        reg.append(EmailLabel)
        reg.append(ContactLabel)
        reg.append(ZoneLabel)
        
    elif Group == "SID":
        print('Patient ID number is: '+'SID'+str(PatientIDSID))
        print('Patient registered...')
        IDLabel = ('ID      :'+'SID'+str(PatientIDSID))
        reg.append(IDLabel)
        reg.append(GroupLabel)
        reg.append(NameLabel)
        reg.append(EmailLabel)
        reg.append(ContactLabel)
        reg.append(ZoneLabel)

    elif Group == "AHS":
        print('Patient ID number is: '+'AHS'+str(PatientIDAHS))
        print('Patient registered...')
        IDLabel = ('ID      :'+'AHS'+str(PatientIDAHS))
        reg.append(IDLabel)
        reg.append(GroupLabel)
        reg.append(NameLabel)
        reg.append(EmailLabel)
        reg.append(ContactLabel)
        reg.append(ZoneLabel)

    else:
        print("Group doesn't exist") #if wrong group is typed this gets printed and no information is saved in file
    print()
    Registration.append(reg)
    return Registration
    menu()

def SavePatientsInfo(): #saves registered info in a file
    fileHandler = open('Patient_Detail.txt','a')
    Registration = PatientsReg()

    for reg in Registration:
        for x in reg:
            fileHandler.write(str(x))
            fileHandler.write('\n') #so it'll store information vertically
        fileHandler.write('\n')
    fileHandler.close()

    menu()

def CounterTest1(): #generates case id for those who was positive in test 1
    filehandler = open('Test1_positive.txt','r')
    ID = 1000
    for line in filehandler: 
        line = line.rstrip() #checks the file if number already exists and
        if str(ID) in line:  #rstrip makes sure counter ignores numbers of lines and instead focuses on only number of id that exists
            ID = ID+1
    return ID

def CounterTest2(): #generates case id for those who was positive in test 2
    filehandler = open('Test2_positive.txt','r')
    ID = 2000
    for line in filehandler:
        line = line.rstrip()
        if str(ID) in line:
            ID = ID+1
    return ID

def CounterTest3(): #generates case id for those who was positive in test 3
    filehandler = open('Test3_positive.txt','r')
    ID = 3000
    for line in filehandler:
        line = line.rstrip()
        if str(ID) in line:
            ID = ID+1
    return ID
    
def PatientsTest1Pos(): #registers results for positive patients in test 1
    Test1Pos = []
    PatientCaseID = CounterTest1()
    NWard = ('Ward    :NW')
    ICU = ('Ward    :ICU')            
    Status = ('Case has been set to ACTIVE')
    flag = 0
    TestedGroup = input("The Patient is from which Group(ATO/ACC/AEO/SID/AHS): ")
    if TestedGroup == "ATO":
        grouplabelATO = ('Group   :ATO')
        AdviceATOPos = ('Advice  :QHNF')
        data = str(input("Enter ID: ATO"))
        idfind = ('ID      :ATO'+data)
        IDLabel = ('ID      :ATO'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Patient_Detail.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)): #checks if patient is registered
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient couldn't be found")
            print()
        else:
            fileCheck = open("Test1_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1 

            fileCheck2 = open("Test1_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    #checks if patient is already tested
            if flag == 1:
                print('Patient already tested')
                print() #after both files are checks these get printed to the user
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ATOTest1Pos = [] #stores positive patients in a list
                ATOTest1Pos.append(IDLabel)
                ATOTest1Pos.append(grouplabelATO)
                ATOTest1Pos.append(AdviceATOPos)
                print('Test 1 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    ATOTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    ATOTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print('Please go to Set Status menu to change status of this patient')
                print()
                Test1Pos.append(ATOTest1Pos)
                return Test1Pos 
    elif TestedGroup == "ACC": #function is repeated for each group
        grouplabelACC = ('Group   :ACC')
        AdviceACCPos = ('Advice  :QHNF')
        data = str(input("Enter ID: ACC"))
        idfind = ('ID      :ACC'+data)
        IDLabel = ('ID      :ACC'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Patient_Detail.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient couldn't be found")
            print()
        else:
            fileCheck = open("Test1_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test1_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ACCTest1Pos = [] 
                ACCTest1Pos.append(IDLabel)
                ACCTest1Pos.append(grouplabelACC)
                ACCTest1Pos.append(AdviceACCPos)
                print('Test 1 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    ACCTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    ACCTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(ACCTest1Pos)
                return Test1Pos
    elif TestedGroup == "AEO":
        grouplabelAEO = ('Group   :AEO')
        AdviceAEOPos = ('Advice  :QHNF')
        data = str(input("Enter ID: AEO"))
        idfind = ('ID      :AEO'+data)
        IDLabel = ('ID      :AEO'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Patient_Detail.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient couldn't be found")
            print()
        else:
            fileCheck = open("Test1_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test1_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AEOTest1Pos = []
                AEOTest1Pos.append(IDLabel)
                AEOTest1Pos.append(grouplabelAEO)
                AEOTest1Pos.append(AdviceAEOPos)
                print('Test 1 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    AEOTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    AEOTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(AEOTest1Pos)
                return Test1Pos
    elif TestedGroup == "SID":
        grouplabelSID = ('Group   :SID')
        AdviceSIDPos = ('Advice  :QHNF')
        data = str(input("Enter ID: SID"))
        idfind = ('ID      :SID'+data)
        IDLabel = ('ID      :SID'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Patient_Detail.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient couldn't be found")
            print()
        else:
            fileCheck = open("Test1_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test1_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                SIDTest1Pos = []
                SIDTest1Pos.append(IDLabel)
                SIDTest1Pos.append(grouplabelSID)
                SIDTest1Pos.append(AdviceSIDPos)
                print('Test 1 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    SIDTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    SIDTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(SIDTest1Pos)
                return Test1Pos
    elif TestedGroup == "AHS":
        grouplabelAHS = ('Group   :AHS')
        AdviceAHSPos = ('Advice  :HQNF')
        data = str(input("Enter ID: AHS"))
        idfind = ('ID      :AHS'+data)
        IDLabel = ('ID      :AHS'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Patient_Detail.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient couldn't be found")
            print()
        else:
            fileCheck = open("Test1_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test1_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AHSTest1Pos = []
                AHSTest1Pos.append(IDLabel)
                AHSTest1Pos.append(grouplabelAHS)
                AHSTest1Pos.append(AdviceAHSPos)
                print('Test 1 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Home Quarantine (HQNF)')
                print('No follow-up test required')
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(AHSTest1Pos)
                return Test1Pos
    else:
        print("Group doesn't exist. Please try again.")#if wrong group gets types this gets printed
        print("Returning to menu...")
        print()
       
    menu()

def SaveTest1ResultsPos(): #saves information for those who are positive in test1 in text file
    fileHandler = open('Test1_positive.txt','a') #only stores test 1 patients
    fileHandler2 = open('All_Positive_Patients.txt','a') #used to store all patients from all tests
    Test1Pos = PatientsTest1Pos()

    for PatTest1Pos in Test1Pos:
        for t1 in PatTest1Pos:
            fileHandler.write(str(t1))
            fileHandler.write('\n')
        fileHandler.write('\n')
    fileHandler.close()

    for PatTest2Pos in Test1Pos:
        for t2 in PatTest2Pos:
            fileHandler2.write(str(t2))
            fileHandler2.write('\n')
        fileHandler2.write('\n')
    fileHandler2.close()

    menu()

def PatientsTest1Neg(): #copy of PatientsTest2Pos() but with different condition according to what is entered and is for negative patient
    Test1Pos = []
    flag = 0
    TestedGroup = input("The Patient is from which Group(ATO/ACC/AEO/SID/AHS): ")
    if TestedGroup == "ATO":
        grouplabelATO = ('Group   :ATO')
        AdviceATOPos = ('Advice  :QDFR')
        data = str(input("Enter ID: ATO"))
        datalabel = ('ID      :ATO'+data)
        Registered = 0
        fileHandler = open("Patient_Detail.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient couldn't be found")
            print()
        else:
            fileCheck = open("Test1_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test1_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ATOTest1Pos = []
                ATOTest1Pos.append(datalabel)
                ATOTest1Pos.append(grouplabelATO)
                ATOTest1Pos.append(AdviceATOPos)
                print('Test 1 recorded...')
                print('Patient required to be Quarantine in Designated Centres(QDFR)')
                print('Follow-up test required')
                print()
                Test1Pos.append(ATOTest1Pos)
                return Test1Pos
    elif TestedGroup == "ACC":
        grouplabelACC = ('Group   :ACC')
        AdviceACCPos = ('Advice  :QDFR')
        data = str(input("Enter ID: ACC"))
        datalabel = ('ID      :ACC'+data)
        Registered = 0
        fileHandler = open("Patient_Detail.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient couldn't be found")
            print()
        else:
            fileCheck = open("Test1_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test1_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ACCTest1Pos = []
                ACCTest1Pos.append(datalabel)
                ACCTest1Pos.append(grouplabelACC)
                ACCTest1Pos.append(AdviceACCPos)
                print('Test 1 recorded...')
                print('Patient required to be Quarantine in Designated Centres(QDFR)')
                print('Follow-up test required')
                print()
                Test1Pos.append(ACCTest1Pos)
                return Test1Pos
    elif TestedGroup == "AEO":
        grouplabelAEO = ('Group   :AEO')
        AdviceAEOPos = ('Advice  :QDFR')
        data = str(input("Enter ID: AEO"))
        datalabel = ('ID      :AEO'+data)
        Registered = 0
        fileHandler = open("Patient_Detail.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient couldn't be found")
            print()
        else:
            fileCheck = open("Test1_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test1_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AEOTest1Pos = []
                AEOTest1Pos.append(datalabel)
                AEOTest1Pos.append(grouplabelAEO)
                AEOTest1Pos.append(AdviceAEOPos)
                print('Test 1 recorded...')
                print('Patient required to be Quarantine in Designated Centres(QDFR)')
                print('Follow-up test required')
                print()
                Test1Pos.append(AEOTest1Pos)
                return Test1Pos
    elif TestedGroup == "SID":
        grouplabelSID = ('Group   :SID')
        AdviceSIDPos = ('Advice  :HQFR')
        data = str(input("Enter ID: SID"))
        datalabel = ('ID      :SID'+data)
        Registered = 0
        fileHandler = open("Patient_Detail.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient couldn't be found")
            print()
        else:
            fileCheck = open("Test1_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test1_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                SIDTest1Pos = []
                SIDTest1Pos.append(datalabel)
                SIDTest1Pos.append(grouplabelSID)
                SIDTest1Pos.append(AdviceSIDPos)
                print('Test 1 recorded...')
                print('Patient required to be Home Quarantine(HQFR)')
                print('Follow-up test required')
                print()
                Test1Pos.append(SIDTest1Pos)
                return Test1Pos
    elif TestedGroup == "AHS":
        grouplabelAHS = ('Group   :AHS')
        AdviceAHSPos = ('Advice  :CWFR')
        data = str(input("Enter ID: AHS"))
        datalabel = ('ID      :AHS'+data)
        Registered = 0
        fileHandler = open("Patient_Detail.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient couldn't be found")
            print()
        else:
            fileCheck = open("Test1_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test1_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AHSTest1Pos = []
                AHSTest1Pos.append(datalabel)
                AHSTest1Pos.append(grouplabelAHS)
                AHSTest1Pos.append(AdviceAHSPos)
                print('Test 1 recorded...')
                print('Patient allowed to Continue Working(CWFR)')
                print('Follow-up test required')
                print()
                Test1Pos.append(AHSTest1Pos)
                return Test1Pos
    else:
        print("Group doesn't exist. Please try again.")
        print("Returning to menu...")
        print()
       
    menu()

def SaveTest1ResultsNeg(): #saves information for those who are negative in test1 in text file
    fileHandler = open('Test1_negative.txt','a') #Negative patient from test1 gets stored here
    fileHandler2 = open('All_Negative_Patients.txt','a') #all Negative patients get stored here
    Test1Pos = PatientsTest1Neg()

    for PatTest1Pos in Test1Pos:
        for t1 in PatTest1Pos:
            fileHandler.write(str(t1))
            fileHandler.write('\n')
        fileHandler.write('\n')
    fileHandler.close()

    for PatTest2Pos in Test1Pos:
        for t2 in PatTest2Pos:
            fileHandler2.write(str(t2))
            fileHandler2.write('\n')
        fileHandler2.write('\n')
    fileHandler2.close()

    menu()
    
def PatientsTest2Pos(): #registers positive patients for test 2
    Test1Pos = []
    PatientCaseID = CounterTest2()
    NWard = ('Ward    :NW')
    ICU = ('Ward    :ICU')
    flag = 0
    Status = ('Case has been set to ACTIVE')
    TestedGroup = input("The Patient is from which Group(ATO/ACC/AEO/SID/AHS): ")
    if TestedGroup == "ATO":
        grouplabelATO = ('Group   :ATO')
        AdviceATOPos = ('Advice  :QHNF')
        data = str(input("Enter ID: ATO"))
        idfind = ('ID      :ATO'+data)
        IDLabel = ('ID      :ATO'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Test1_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test2_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test2_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ATOTest1Pos = []
                ATOTest1Pos.append(IDLabel)
                ATOTest1Pos.append(grouplabelATO)
                ATOTest1Pos.append(AdviceATOPos)
                print('Test 2 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    ATOTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    ATOTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(ATOTest1Pos)
                return Test1Pos
    elif TestedGroup == "ACC":
        grouplabelACC = ('Group   :ACC')
        AdviceACCPos = ('Advice  :QHNF')
        data = str(input("Enter ID: ACC"))
        idfind = ('ID      :ACC'+data)
        IDLabel = ('ID      :ACC'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Test1_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test2_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test2_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ACCTest1Pos = []
                ACCTest1Pos.append(IDLabel)
                ACCTest1Pos.append(grouplabelACC)
                ACCTest1Pos.append(AdviceACCPos)
                print('Test 2 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    ACCTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    ACCTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(ACCTest1Pos)
                return Test1Pos
    elif TestedGroup == "AEO":
        grouplabelAEO = ('Group   :AEO')
        AdviceAEOPos = ('Advice  :QHNF')
        data = str(input("Enter ID: AEO"))
        idfind = ('ID      :AEO'+data)
        IDLabel = ('ID      :AEO'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Test1_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test2_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test2_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AEOTest1Pos = []
                AEOTest1Pos.append(IDLabel)
                AEOTest1Pos.append(grouplabelAEO)
                AEOTest1Pos.append(AdviceAEOPos)
                print('Test 2 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    AEOTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    AEOTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(AEOTest1Pos)
                return Test1Pos
    elif TestedGroup == "SID":
        grouplabelSID = ('Group   :SID')
        AdviceSIDPos = ('Advice  :QHNF')
        data = str(input("Enter ID: SID"))
        idfind = ('ID      :SID'+data)
        IDLabel = ('ID      :SID'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Test1_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test2_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test2_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                SIDTest1Pos = []
                SIDTest1Pos.append(IDLabel)
                SIDTest1Pos.append(grouplabelSID)
                SIDTest1Pos.append(AdviceSIDPos)
                print('Test 2 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    SIDTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    SIDTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(SIDTest1Pos)
                return Test1Pos
    elif TestedGroup == "AHS":
        grouplabelAHS = ('Group   :AHS')
        AdviceAHSPos = ('Advice  :HQNF')
        data = str(input("Enter ID: AHS"))
        idfind = ('ID      :AHS'+data)
        IDLabel = ('ID      :AHS'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Test1_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test2_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test2_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AHSTest1Pos = []
                AHSTest1Pos.append(IDLabel)
                AHSTest1Pos.append(grouplabelAHS)
                AHSTest1Pos.append(AdviceAHSPos)
                print('Test 2 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Home Quarantine (HQNF)')
                print('No follow-up test required')
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(AHSTest1Pos)
                return Test1Pos
    else:
        print("Group doesn't exist. Please try again.")
        print("Returning to menu...")
        print()
       
    menu()

def SaveTest2ResultsPos(): #saves information for those who are positive in test2 in text file
    fileHandler = open('Test2_positive.txt','a')
    fileHandler2 = open('All_Positive_Patients.txt','a')
    Test1Pos = PatientsTest2Pos()

    for PatTest1Pos in Test1Pos:
        for t1 in PatTest1Pos:
            fileHandler.write(str(t1))
            fileHandler.write('\n')
        fileHandler.write('\n')
    fileHandler.close()

    for PatTest2Pos in Test1Pos:
        for t2 in PatTest2Pos:
            fileHandler2.write(str(t2))
            fileHandler2.write('\n')
        fileHandler2.write('\n')
    fileHandler2.close()

    menu()

def PatientsTest2Neg(): #Register negative patients for test 2
    Test1Pos = []
    flag = 0
    TestedGroup = input("The Patient is from which Group(ATO/ACC/AEO/SID/AHS): ")
    if TestedGroup == "ATO":
        grouplabelATO = ('Group   :ATO')
        AdviceATOPos = ('Advice  :QDFR')
        data = str(input("Enter ID: ATO"))
        datalabel = ('ID      :ATO'+data)
        Registered = 0
        fileHandler = open("Test1_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test2_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test2_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ATOTest1Pos = []
                ATOTest1Pos.append(datalabel)
                ATOTest1Pos.append(grouplabelATO)
                ATOTest1Pos.append(AdviceATOPos)
                print('Test 2 recorded...')
                print('Patient required to be Quarantine in Designated Centres(QDFR)')
                print('Follow-up test required')
                print()
                Test1Pos.append(ATOTest1Pos)
                return Test1Pos
    elif TestedGroup == "ACC":
        grouplabelACC = ('Group   :ACC')
        AdviceACCPos = ('Advice  :QDFR')
        data = str(input("Enter ID: ACC"))
        datalabel = ('ID      :ACC'+data)
        Registered = 0
        fileHandler = open("Test1_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test2_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test2_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ACCTest1Pos = []
                ACCTest1Pos.append(datalabel)
                ACCTest1Pos.append(grouplabelACC)
                ACCTest1Pos.append(AdviceACCPos)
                print('Test 2 recorded...')
                print('Patient required to be Quarantine in Designated Centres(QDFR)')
                print('Follow-up test required')
                print()
                Test1Pos.append(ACCTest1Pos)
                return Test1Pos
    elif TestedGroup == "AEO":
        grouplabelAEO = ('Group   :AEO')
        AdviceAEOPos = ('Advice  :QDFR')
        data = str(input("Enter ID: AEO"))
        datalabel = ('ID      :AEO'+data)
        Registered = 0
        fileHandler = open("Test1_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test2_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test2_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AEOTest1Pos = []
                AEOTest1Pos.append(datalabel)
                AEOTest1Pos.append(grouplabelAEO)
                AEOTest1Pos.append(AdviceAEOPos)
                print('Test 2 recorded...')
                print('Patient required to be Quarantine in Designated Centres(QDFR)')
                print('Follow-up test required')
                print()
                Test1Pos.append(AEOTest1Pos)
                return Test1Pos
    elif TestedGroup == "SID":
        grouplabelSID = ('Group   :SID')
        AdviceSIDPos = ('Advice  :HQFR')
        data = str(input("Enter ID: SID"))
        datalabel = ('ID      :SID'+data)
        Registered = 0
        fileHandler = open("Test1_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test2_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test2_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                SIDTest1Pos = []
                SIDTest1Pos.append(datalabel)
                SIDTest1Pos.append(grouplabelSID)
                SIDTest1Pos.append(AdviceSIDPos)
                print('Test 2 recorded...')
                print('Patient required to be Home Quarantine(HQFR)')
                print('Follow-up test required')
                print()
                Test1Pos.append(SIDTest1Pos)
                return Test1Pos
    elif TestedGroup == "AHS":
        grouplabelAHS = ('Group   :AHS')
        AdviceAHSPos = ('Advice  :CWFR')
        data = str(input("Enter ID: AHS"))
        datalabel = ('ID      :AHS'+data)
        Registered = 0
        fileHandler = open("Test1_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test2_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test2_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AHSTest1Pos = []
                AHSTest1Pos.append(datalabel)
                AHSTest1Pos.append(grouplabelAHS)
                AHSTest1Pos.append(AdviceAHSPos)
                print('Test 2 recorded...')
                print('Patient allowed to Continue Working(CWFR)')
                print('Follow-up test required')
                print()
                Test1Pos.append(AHSTest1Pos)
                return Test1Pos
    else:
        print("Group doesn't exist. Please try again.")
        print("Returning to menu...")
        print()
       
    menu()

def SaveTest2ResultsNeg(): #saves information for those who are negative in test2 in text file
    fileHandler = open('Test2_negative.txt','a')
    fileHandler2 = open('All_Negative_Patients.txt','a')
    Test1Pos = PatientsTest2Neg()

    for PatTest1Pos in Test1Pos:
        for t1 in PatTest1Pos:
            fileHandler.write(str(t1))
            fileHandler.write('\n')
        fileHandler.write('\n')
    fileHandler.close()

    for PatTest2Pos in Test1Pos:
        for t2 in PatTest2Pos:
            fileHandler2.write(str(t2))
            fileHandler2.write('\n')
        fileHandler2.write('\n')
    fileHandler2.close()

    menu()

def PatientsTest3Pos(): #Registers Positive Patient for test 3
    Test1Pos = []
    PatientCaseID = CounterTest3()
    NWard = ('Ward    :NW')
    ICU = ('Ward    :ICU') 
    flag = 0
    Status = ('Case has been set to ACTIVE')
    TestedGroup = input("The Patient is from which Group(ATO/ACC/AEO/SID/AHS): ")
    if TestedGroup == "ATO":
        grouplabelATO = ('Group   :ATO')
        AdviceATOPos = ('Advice  :QHNF')
        data = str(input("Enter ID: ATO"))
        idfind = ('ID      :ATO'+data)
        IDLabel = ('ID      :ATO'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Test2_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test3_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test3_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ATOTest1Pos = []
                ATOTest1Pos.append(IDLabel)
                ATOTest1Pos.append(grouplabelATO)
                ATOTest1Pos.append(AdviceATOPos)
                print('Test 3 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    ATOTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    ATOTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(ATOTest1Pos)
                return Test1Pos
    elif TestedGroup == "ACC":
        grouplabelACC = ('Group   :ACC')
        AdviceACCPos = ('Advice  :QHNF')
        data = str(input("Enter ID: ACC"))
        idfind = ('ID      :ACC'+data)
        IDLabel = ('ID      :ACC'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Test2_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test3_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test3_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ACCTest1Pos = []
                ACCTest1Pos.append(IDLabel)
                ACCTest1Pos.append(grouplabelACC)
                ACCTest1Pos.append(AdviceACCPos)
                print('Test 3 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    ACCTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    ACCTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(ACCTest1Pos)
                return Test1Pos
    elif TestedGroup == "AEO":
        grouplabelAEO = ('Group   :AEO')
        AdviceAEOPos = ('Advice  :QHNF')
        data = str(input("Enter ID: AEO"))
        idfind = ('ID      :AEO'+data)
        IDLabel = ('ID      :AEO'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Test2_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test3_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test3_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AEOTest1Pos = []
                AEOTest1Pos.append(IDLabel)
                AEOTest1Pos.append(grouplabelAEO)
                AEOTest1Pos.append(AdviceAEOPos)
                print('Test 3 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    AEOTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    AEOTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(AEOTest1Pos)
                return Test1Pos
    elif TestedGroup == "SID":
        grouplabelSID = ('Group   :SID')
        AdviceSIDPos = ('Advice  :QHNF')
        data = str(input("Enter ID: SID"))
        idfind = ('ID      :SID'+data)
        IDLabel = ('ID      :SID'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Test2_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test3_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test3_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                SIDTest1Pos = []
                SIDTest1Pos.append(IDLabel)
                SIDTest1Pos.append(grouplabelSID)
                SIDTest1Pos.append(AdviceSIDPos)
                print('Test 3 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Quarantine in Hospital Normal Ward or ICU(QHNF)')
                print('No follow-up test required\n')
                print('Will the patient be admitted to Normal Ward or Intensive care Unit?')
                WChoice = input('Write NW or ICU: ')
                if WChoice == 'NW':
                    SIDTest1Pos.append(NWard)
                elif WChoice == 'ICU':
                    SIDTest1Pos.append(ICU)
                else:
                    print("invalid input\n")
                    menu()
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(SIDTest1Pos)
                return Test1Pos
    elif TestedGroup == "AHS":
        grouplabelAHS = ('Group   :AHS')
        AdviceAHSPos = ('Advice  :HQNF')
        data = str(input("Enter ID: AHS"))
        idfind = ('ID      :AHS'+data)
        IDLabel = ('ID      :AHS'+data+',Case ID :'+'C'+str(PatientCaseID))
        Registered = 0
        fileHandler = open("Test2_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(idfind)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test3_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(idfind)):
                   flag = 1

            fileCheck2 = open("Test3_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(idfind)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AHSTest1Pos = []
                AHSTest1Pos.append(IDLabel)
                AHSTest1Pos.append(grouplabelAHS)
                AHSTest1Pos.append(AdviceAHSPos)
                print('Test 3 recorded...')
                print('Patient Case ID number is: '+'C'+str(PatientCaseID))
                print('Patient required to be Home Quarantine (HQNF)')
                print('No follow-up test required')
                print()
                print(Status)
                print("Please go to 'Set Status' section to change status of this patient")
                print()
                Test1Pos.append(AHSTest1Pos)
                return Test1Pos
    else:
        print("Group doesn't exist. Please try again.")
        print("Returning to menu...")
        print()
       
    menu()

def SaveTest3ResultsPos(): #saves information for those who are positive in test3 in text file
    fileHandler = open('Test3_positive.txt','a')
    fileHandler2 = open('All_Positive_Patients.txt','a')
    Test1Pos = PatientsTest3Pos()

    for PatTest1Pos in Test1Pos:
        for t1 in PatTest1Pos:
            fileHandler.write(str(t1))
            fileHandler.write('\n')
        fileHandler.write('\n')
    fileHandler.close()

    for PatTest2Pos in Test1Pos:
        for t2 in PatTest2Pos:
            fileHandler2.write(str(t2))
            fileHandler2.write('\n')
        fileHandler2.write('\n')
    fileHandler2.close()

    menu()

def PatientsTest3Neg(): #registers negative patients for test 3
    Test1Pos = []
    flag = 0
    TestedGroup = input("The Patient is from which Group(ATO/ACC/AEO/SID/AHS): ")
    if TestedGroup == "ATO":
        grouplabelATO = ('Group   :ATO')
        AdviceATOPos = ('Advice  :RU')
        data = str(input("Enter ID: ATO"))
        datalabel = ('ID      :ATO'+data)
        Registered = 0
        fileHandler = open("Test2_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test3_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test3_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ATOTest1Pos = []
                ATOTest1Pos.append(datalabel)
                ATOTest1Pos.append(grouplabelATO)
                ATOTest1Pos.append(AdviceATOPos)
                print('Test 3 recorded...')
                print('Patient Allowed to reunion with family(RU)')
                print()
                Test1Pos.append(ATOTest1Pos)
                return Test1Pos
    elif TestedGroup == "ACC":
        grouplabelACC = ('Group   :ACC')
        AdviceACCPos = ('Advice  :RU')
        data = str(input("Enter ID: ACC"))
        datalabel = ('ID      :ACC'+data)
        Registered = 0
        fileHandler = open("Test2_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test3_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test3_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                ACCTest1Pos = []
                ACCTest1Pos.append(datalabel)
                ACCTest1Pos.append(grouplabelACC)
                ACCTest1Pos.append(AdviceACCPos)
                print('Test 3 recorded...')
                print('Patient Allowed to reunion with family(RU)')
                print()
                Test1Pos.append(ACCTest1Pos)
                return Test1Pos
    elif TestedGroup == "AEO":
        grouplabelAEO = ('Group   :AEO')
        AdviceAEOPos = ('Advice  :RU')
        data = str(input("Enter ID: AEO"))
        datalabel = ('ID      :AEO'+data)
        Registered = 0
        fileHandler = open("Test2_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test3_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test3_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AEOTest1Pos = []
                AEOTest1Pos.append(datalabel)
                AEOTest1Pos.append(grouplabelAEO)
                AEOTest1Pos.append(AdviceAEOPos)
                print('Test 3 recorded...')
                print('Patient Allow to reunion with family(RU)')
                print()
                Test1Pos.append(AEOTest1Pos)
                return Test1Pos
    elif TestedGroup == "SID":
        grouplabelSID = ('Group   :SID')
        AdviceSIDPos = ('Advice  :RU')
        data = str(input("Enter ID: SID"))
        datalabel = ('ID      :SID'+data)
        Registered = 0
        fileHandler = open("Test2_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test3_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test3_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                SIDTest1Pos = []
                SIDTest1Pos.append(datalabel)
                SIDTest1Pos.append(grouplabelSID)
                SIDTest1Pos.append(AdviceSIDPos)
                print('Test 3 recorded...')
                print('Patient Allow to reunion with family(RU)')
                print()
                Test1Pos.append(SIDTest1Pos)
                return Test1Pos
    elif TestedGroup == "AHS":
        grouplabelAHS = ('Group   :AHS')
        AdviceAHSPos = ('Advice  :CW')
        data = str(input("Enter ID: AHS"))
        datalabel = ('ID      :AHS'+data)
        Registered = 0
        fileHandler = open("Test2_negative.txt","r")
        for line in fileHandler:
            if(line.startswith(datalabel)):
                Registered = 1
        if(Registered == 0):
            print('Test not recorded')
            print("Patient is not found or eligible for testing")
            print()
        else:
            fileCheck = open("Test3_positive.txt","r") 
            for check in fileCheck:
                if(check.startswith(datalabel)):
                   flag = 1

            fileCheck2 = open("Test3_negative.txt","r")
            for check2 in fileCheck2:
                if(check2.startswith(datalabel)):
                    flag = 2
                    
            if flag == 1:
                print('Patient already tested')
                print()
            elif flag == 2:
                print('Patient already tested')
                print()
            else:
                AHSTest1Pos = []
                AHSTest1Pos.append(datalabel)
                AHSTest1Pos.append(grouplabelAHS)
                AHSTest1Pos.append(AdviceAHSPos)
                print('Test 3 recorded...')
                print('Patient allowed to Continue Working(CW)')
                print()
                Test1Pos.append(AHSTest1Pos)
                return Test1Pos
    else:
        print("Group doesn't exist. Please try again.")
        print("Returning to menu...")
        print()
       
    menu()

def SaveTest3ResultsNeg(): #saves information for those who are negative in test3 in text file
    fileHandler = open('Test3_negative.txt','a')
    fileHandler2 = open('All_Negative_Patients.txt','a')
    Test1Pos = PatientsTest3Neg()

    for PatTest1Pos in Test1Pos:
        for t1 in PatTest1Pos:
            fileHandler.write(str(t1))
            fileHandler.write('\n')
        fileHandler.write('\n')
    fileHandler.close()

    for PatTest2Pos in Test1Pos:
        for t2 in PatTest2Pos:
            fileHandler2.write(str(t2))
            fileHandler2.write('\n')
        fileHandler2.write('\n')
    fileHandler2.close()

    menu()

def StatusDeceased():
    Stat = []
    ID = input('Please enter Patient ID to change patient status(e.g.ATO***): ')
    cid = input('Please enter Case ID of Patient: C')
    File = ('ID :'+ID+',Case ID :C'+cid+',DECEASED')
    FileCheck = ('ID      :'+ID+',Case ID :C'+cid)
    fileHandler = open("All_Positive_Patients.txt","r")
    flag = 0
    check = 0
    for line in fileHandler:
        if (line.startswith(FileCheck)):
            flag = 1
    if flag == 1:
        fileHandler2 = open("Deceased_patient.txt","r")
        for line2 in fileHandler2:
            if(line2.startswith('ID :'+ID)):
                check = 1
                
        fileHandler3 = open("Recovered_patient.txt","r")
        for line3 in fileHandler3:
            if(line3.startswith('ID :'+ID)):
                check = 2
                
        if check == 1:
            print('Change failed')
            print('Patient status has already changed to DECEASED\n')
        elif check == 2:
            print('Change failed')
            print('Patient status has already changed to RECOVERED\n')
        else:
            print('Status successfully changed to DECEASED\n')
            Dec = []
            Dec.append(File)
            Stat.append(Dec)
            return Stat
    else:
        print("Patient doesn't exist or Case ID isn't related to Patient ID\n")
    menu()
    
def StatusRecovered():
    Stat = []
    ID = input('Please enter Patient ID to change patient status(e.g.ATO***): ')
    cid = input('Please enter Case ID of Patient: C')
    File = ('ID :'+ID+',Case ID :C'+cid+',RECOVERED')
    FileCheck = ('ID      :'+ID+',Case ID :C'+cid)
    fileHandler = open("All_Positive_Patients.txt","r")
    flag = 0
    check = 0
    for line in fileHandler:
        if (line.startswith(FileCheck)):
            flag = 1
    if flag == 1:
        fileHandler2 = open("Deceased_patient.txt","r")
        for line2 in fileHandler2:
            if(line2.startswith('ID :'+ID)):
                check = 1
        fileHandler3 = open("Recovered_patient.txt","r")
        for line3 in fileHandler3:
            if(line3.startswith('ID :'+ID)):
                check = 2
        if check == 1:
            print('Change failed')
            print('Patient status has already changed to DECEASED\n')
        elif check == 2:
            print('Change failed')
            print('Patient status has already changed to RECOVERED\n')
        else:
            print('Status successfully changed to RECOVERED\n')
            Dec = []
            Dec.append(File)
            Stat.append(Dec)
            return Stat
    else:
        print("Patient doesn't exist or Case ID isn't related to Patient ID\n")
    menu()

def saveDeceased():
    fileHandler = open('Deceased_patient.txt','a')
    Stat = StatusDeceased()

    for Dec in Stat:
        for x in Dec:
            fileHandler.write(str(x))
            fileHandler.write('\n')
        fileHandler.write('\n')
    fileHandler.close()

    menu()

def saveRecovered():
    fileHandler = open('Recovered_patient.txt','a')
    Stat = StatusRecovered()

    for Dec in Stat:
        for x in Dec:
            fileHandler.write(str(x))
            fileHandler.write('\n')
        fileHandler.write('\n')
    fileHandler.close()

    menu()

def countTotal():
    fileHandler = open('All_Positive_Patients.txt','r')
    fileHandler2 = open('All_Negative_Patients.txt','r')
    with fileHandler as f:
        with fileHandler2 as f2:
            testedP = f.read()
            testedN = f2.read()
            print('Tests carried out:')
            print(testedP.count('ID      :')+testedN.count('ID      :'))
            print()
            print('Number of positive results:')
            print(testedP.count('ID      :'))
            print()
            print('Number of negative results:')
            print(testedN.count('ID      :'))
            print()
    fileHandler3 = open('Test1_negative.txt','r')
    fileHandler4 = open('Test1_positive.txt','r')
    with fileHandler3 as f3:
        with fileHandler4 as f4:
            PtestedN = f3.read()
            PtestedP = f4.read()
            print('Patients tested:')
            print(PtestedN.count('ID      :')+PtestedP.count('ID      :'))
            print()
    fileHandler5 = open('Deceased_patient.txt','r')
    fileHandler6 = open('Recovered_patient.txt','r')
    fileHandler7 = open('All_Positive_Patients.txt','r')
    with fileHandler5 as f5:
        with fileHandler6 as f6:
            with fileHandler7 as f7:
                Dpatient = f5.read()
                Rpatient = f6.read()
                Apatient = f7.read()
                print('Active patients:')
                print(Apatient.count('ID      :')-Dpatient.count('DECEASED')-Rpatient.count('RECOVERED'))
                print()
                print('Deceased patients:')
                print(Dpatient.count('DECEASED'))
                print()
                print('Recovered patients:')
                print(Rpatient.count('RECOVERED'))
                print()
                print('ATO group positives:')
                print(Apatient.count('ID      :ATO'))
                print()
                print('ACC group positives:')
                print(Apatient.count('ID      :ACC'))
                print()
                print('AEO group positives:')
                print(Apatient.count('ID      :AEO'))
                print()
                print('SID group positives:')
                print(Apatient.count('ID      :SID'))
                print()
                print('AHS group positives:')
                print(Apatient.count('ID      :AHS'))
                print()
    fileHandler8 = open('Patient_Detail.txt','r')
    with fileHandler8 as f8:
        Zpatient = f8.read()
        print('Patients from Zone A:')
        print(Zpatient.count('Zone    :A'))
        print()
        print('Patients from Zone B:')
        print(Zpatient.count('Zone    :B'))
        print()
        print('Patients from Zone C:')
        print(Zpatient.count('Zone    :C'))
        print()
        print('Patients from Zone D:')
        print(Zpatient.count('Zone    :D'))
        print()
         
def SearchPatientsInfo():#for searching patients record
    ID = input('Please enter ID of patient(ATO***): ')
    fileHandler = open("Patient_Detail.txt", "r")
    searchPatients = fileHandler.readlines()
    fileHandler.close()
    for i, line in enumerate(searchPatients):
        if ("ID      :"+ID) in line: 
            for l in searchPatients[i:i+6]:
                print (l)
                print()
    menu()

def searchStatus():
    ID = input('Please enter ID of patient(ATO***): ')
    cid = input('Case ID of patient: C')
    fileHandler = open('Deceased_patient.txt','r')
    fileHandler2 = open('Recovered_patient.txt','r')
    fileHandler3 = open('All_Positive_Patients.txt','r')
    flag = 0
    for line in fileHandler:
        if (line.startswith('ID :'+ID+',Case ID :C'+cid+',DECEASED')):
            flag = 1
    for line2 in fileHandler2:
        if (line2.startswith('ID :'+ID+',Case ID :C'+cid+',RECOVERED')):
            flag = 2

    if flag == 1:
        print('Status: DECEASED\n')
    elif flag == 2:
        print('Status: RECOVERED\n')
    else:
        for line3 in fileHandler3:
            if (line3.startswith('ID      :'+ID+',Case ID :C'+cid)):
                flag = 3
        if flag == 3:
            print('Status: ACTIVE\n')
        else:
            print("Patient doesn't exist or Case ID isn't related to Patient ID\n")
    menu()

def deceasedRecord():
    fileHandler = open("Deceased_patient.txt",'r')
    
    for line in fileHandler:
        print(line)
        
    fileHandler.close()
    menu()

def recoveredRecord():
    fileHandler = open("Recovered_patient.txt",'r')
    
    for line in fileHandler:
        print(line)
        
    fileHandler.close()
    menu()
    
def searchMenu():
    print()
    print('Select the operation that you want to perform')
    print('1. Search patient record')
    print('2. Search Status of patient')
    print('3. All Deceased Patients')
    print('4. All Recovered Patients')
    searchChoice = input('What do you wanna search?: ')

    if searchChoice == '1':
        SearchPatientsInfo()
    elif searchChoice == '2':
        searchStatus()
    elif searchChoice == '3':
        deceasedRecord()
    elif searchChoice == '4':
        recoveredRecord()
    else:
        print('Invalid input')
        menu()

def TestMenu(): #menu for choosing test 1 test 2 test 3
    print()
    print('Pick which test to perform:')
    print('1. Test 1')
    print('2. Test 2')
    print('3. Test 3')
    testchoice = input('Enter selection: ')
    if testchoice == '1': #for test 1
        open("Test1_positive.txt","a")#creates file so it can be checked
        open("Test1_negative.txt","a")
        print('Is the patient Positive or Negative?')
        Result = input("Write P or N: ")
        if Result == 'P': #prompts test1 positive patients function
            SaveTest1ResultsPos()
        elif Result == 'N': #prompts test1 negative patients function
            SaveTest1ResultsNeg()
        else: #if other letters not P or N are typed in
            print('Invalid input\n')
            menu()
    if testchoice == '2': #for test2
        open("Test2_positive.txt","a")
        open("Test2_negative.txt","a")
        print('Is the patient Positive or Negative?')
        Result = input("Write P or N: ")
        if Result == 'P':
            SaveTest2ResultsPos()
        elif Result == 'N':
            SaveTest2ResultsNeg()
        else:
            print('Invalid input\n')
            menu()
    if testchoice == '3': #for test3
        open("Test3_positive.txt","a")
        open("Test3_negative.txt","a")
        print('Is the patient Positive or Negative?')
        Result = input("Write P or N: ")
        if Result == 'P':
            SaveTest3ResultsPos()
        elif Result == 'N':
            SaveTest3ResultsNeg()
        else:
            print('Invalid input\n')
            menu()
    else:
        print('Invalid input\n')
        menu()

def setStatusMenu():
    print()
    print('Would you like to change patient status to Deceased or Recovered?: ')
    statusChoice = input('Write D or R: ')
    if statusChoice == 'D':
        open('Recovered_patient.txt','a')
        open('Deceased_patient.txt','a')
        saveDeceased()
    elif statusChoice == 'R':
        open('Recovered_patient.txt','a')
        open('Deceased_patient.txt','a')
        saveRecovered()
    else:
        print('Invalid input\n')
    menu()
        
def menu(): #main menu
    print('Select the operation that you want to perform')
    print('1. Register Patients')#for registering patients
    print('2. Test Patients')
    print('3. Set Status')
    print('4. Statistical information')
    print('5. Search')
    print('6. Exit')

    choice = input('Enter selection: ')

    if (choice=='1'):
        SavePatientsInfo() #if typing in 1 this executes register patients function
    elif (choice=='2'):
        TestMenu() #executes program that run tests
    elif (choice=='3'):
        setStatusMenu()
    elif (choice=='4'):
        open('Patient_Detail.txt','a')
        open('Deceased_patient.txt','a')
        open('Recovered_patient.txt','a')
        open('All_Positive_Patients.txt','a')
        open('All_Negative_Patients.txt','a')
        open('Test1_negative.txt','a')
        open('Test1_positive.txt','a')
        countTotal()
        menu()
    elif (choice=='5'):
        searchMenu()
    elif (choice=='6'):
        print('Have a nice day')#exiting prints this line
        exit()
    else:
        print('Invalid input\n') #if any other data is being input on choice this displays
        menu()

menu()


