#LEW JUN LONG
#TP059638

#Check patients have done registration before or not 
def searchPatient(fileName,patientName):
    fileHandler=open(fileName,"r")
    for line in fileHandler:                        #This is a for loop to run though each line in fileHandler
        if patientName in line:                     #If patient's name was found in the line, it will return False means that patient has done registration before 
            fileHandler.close()
            return False
    fileHandler.close()                             #If patient's name was not found in the line, it will return True means that patient has not done registration before 
    return True

#Patient registration and record in a text file
def patientRegistration():
    while True:
        patient=[]
        patientName=str(input("Patient Name,(x) to exit: ")).upper()
        if patientName == 'X':
            break
        if searchPatient("Patient_Detail.txt",patientName):
            #Collect patients information if patients didn't do registration before
            getID=open('Patient_Detail.txt','r+')
            count=0
            for line in getID:                                          #This is a for loop to run though each line in getID and each line represents 1 patient
                count+=1
            count=count+1                                               #A unique number for new patient
            getID.close()
            age=input("Age: ")
            try:                                                        #Age must be an integer
                age=str(int(age))
            except:
                print("Invalid age.")
                break
            print("Select a group:")
            print("ATO=Asymptomatic individuals with history of travelling overseas")
            print("ACC=Asymptomatic individuals with history of contact with known case of COVID-19")
            print("AEO=Asymptomatic individuals who had attended event associated with known COVID-19 outbreak")
            print("SID=Symptomatic individuals")
            print("AHS=Asymptomatic hospital staff")
            group=str(input("Group: ")).upper()
            if group=='ATO' or group=='ACC' or group=='AEO' or group=='SID' or group=='AHS':    #Group must be ATO, ACC, AEO, SID or AHS 
                pass
            else:
                print("Invalid group.")
                break
            print("Select a zone:")
            print("A-East")
            print("B-West")
            print("C-North")
            print("D-South")
            zone=str(input("Zone(A/B/C/D): ")).upper()
            if zone=='A' or zone=='B' or zone=='C' or zone=='D':        #Zone must be A, B, C or D
                pass
            else:
                print("Invalid zone.")
                break
            contactNumber=input("Contact Number: ")                 
            try:                                                        #Contact number must be an integer
                contactNumber=str('0')+str(int(contactNumber))
            except:
                print("Invalid contact number.")
                break
            emailAddress=str(input("Email Address: "))
            patientID=str(zone)+str(group)+str(count)                   #Join zone, group and count to form a unique patient ID
            patient.append(patientID)
            patient.append(patientName)
            patient.append(age)
            patient.append(group)
            patient.append(zone)
            patient.append(contactNumber)
            patient.append(emailAddress)
            print(patient)
            #Append one more patient to the txt file
            fileHandler=open("Patient_Detail.txt","a")
            for items in patient:                                       #This is a for loop to run though each items in patient and write them into fileHandler
                fileHandler.write(items)
                fileHandler.write('\t')
            fileHandler.write('\n')
            fileHandler.close()
        else:
            print("Patient Registered.")
        print()
    return 


#------------------------------------------------------------------------------------------------------------------------

#Check patients have done registration,test1 or test2 before or not 
def searchTest(fileName,patientID):
    fileHandler=open(fileName,"r")
    for line in fileHandler:                        #This is a for loop to run though each line in fileHandler
        if patientID in line:                       #If patient's ID was found in the line, it will return True 
            print(line)                             #In test1,patients must complete registration first
            fileHandler.close()                     #In test2,patients must complete test1 and the result is negative
            return True                             #In test3,patients must complete test2 and the result is negative
    fileHandler.close()                            
    return False                                    #If patient's ID was not found in the line, it will return False

#Check patients have done test1, test2 or test3 before or not
def searchTest1(fileName1,fileName2,patientID):
    fileHandler=open(fileName1,"r")
    for line in fileHandler:                        #This is a for loop to run though each line in fileHandler
        if patientID in line:                       #If patient's ID was found in the line, it will return False
            fileHandler.close()                     #In test1,patients who already done test1 cannot run test1 again
            return False                            #In test2,patients who already done test2 cannot run test2 again
    fileHandler.close()                             #In test3,patients who already done test3 cannot run test3 again
    fileHandler=open(fileName2,"r")
    for line in fileHandler:
        if patientID in line:
            fileHandler.close()
            return False
    fileHandler.close()  
    return True                                     #If patient's ID was not found in the line, it will return True 

#Choice for user to run test1, test2 or test3
def testResults():
    choice=0
    while (choice!=4):
        print('Select a test')
        print('1. Test 1')
        print('2. Test 2')
        print('3. Test 3')
        print('4. Exit')
        choice=input('Enter selection: ')
        try:                                        #'choice' must be a number(1,2,3,4)  
            choice=int(choice)
            if choice==1:
                test1()
            elif choice==2:
                test2()
            elif choice==3:
                test3()
            elif choice==4:
                break
            else:                                   #If 'choice' is not a number between 1-4, it will go to 'else'
                print('Invalid input')
        except:                                     #If 'choice' is not a number, it will go to 'except'
            print('Non-numeric value entered.')
        print()

#Test1
def test1():
    positive=[]                                                             #'positive' and 'negative' will reset when run the function
    negative=[]
    while True:                                                             #The program will run/continue only the statement is 'True'
        patient=[]
        testNumber='T1'
        patientID=input("Enter Patient ID,(x) to exit:").upper()
        patient.append(patientID)
        if patientID=='X':
            break
        if searchTest1("Test1_negative.txt","Test1_positive.txt",patientID): #To check whether patients done test1 before or not
            if searchTest("Patient_Detail.txt",patientID):                   #To check whether patients done registration before or not
                zone=input("Zone(A/B/C/D):").upper()
                patient.append(zone)
                if zone=='A' or zone=='B' or zone=='C' or zone=='D':        #Zone must be A, B, C or D
                    testResult=input("Enter Test result,negative or positive:").lower()
                    patient.append(testNumber)
                    patient.append(testResult)
                    if testResult=='negative':
                        group=str(input("Group(ATO/ACC/AEO/SID/AHS): ")).upper()
                        patient.append(group)
                        if group=='AHS':                                    #Group must be ATO, ACC, AEO, SID or AHS 
                            actionTaken='CWFR'
                            print('Continue Working')
                            print("Pls come back for second test.")
                        elif group=='SID':
                            actionTaken='HQFR'
                            print('Home Quarantine')
                            print("Pls come back for second test.")
                        elif group=='ATO' or group=='ACC' or group=='AEO':
                            actionTaken='QDFR'
                            print('Quarantine in Designated Centres')
                            print("Pls come back for second test.")
                        else:
                            print("Invalid group.")
                            break
                        patient.append(actionTaken)
                        print(patient)
                        negative.append(patient)
                        fileHandler=open('Test1_negative.txt','a')
                        for items in negative:                              #This is a for loop to run though each item in negative for writing item into fileHandler
                            for item in items:
                                fileHandler.write(item)
                                fileHandler.write('\t')
                            fileHandler.write('\n')
                        fileHandler.close()
                    elif testResult=='positive':
                        positivePatientData=[]                              #'positivePatientData' will reset when run test result becomes positive
                        patientStatus='ACTIVE'
                        group=str(input("Group(ATO/ACC/AEO/SID/AHS): ")).upper()
                        patient.append(group)
                        getID=open('Patient_Status.txt','r+')
                        count=0
                        for line in getID:                                  #This is a for loop to run though each line in getID and each line represents 1 patient
                            count+=1
                        count=count+1                                       #A unique number for new patient
                        getID.close()
                        caseID=str("C")+str(zone)+str(group)+str(count)     #join 'C',zone,group and count to form a unique case ID
                        positivePatientData.append(caseID)
                        positivePatientData.append(patientID)
                        positivePatientData.append(zone)
                        positivePatientData.append(group)
                        positivePatientData.append(patientStatus)
                        if group=='AHS':
                            actionTaken='HQNF'
                            place=""
                            print("Test Result is positive.")
                            print("Home Quarantine")
                        elif group=='ATO' or group=='ACC' or group=='AEO'or group=='SID':
                            actionTaken='QHNF'
                            place=input('WARD or ICU:').upper()
                            if place=='WARD':                               #Place must be WARD or ICU
                                print("Test Result is positive.")
                                print('Quarantine in Hospital Normal Ward.')
                            elif place=='ICU':
                                print("Test Result is positive.")
                                print('Quarantine in Hospital ICU.')
                            else:
                                print("Invalid quarantine place.")
                                break
                        else:
                            print("Invalid group.")
                            break
                        positivePatientData.append(place)
                        fileHandler=open('Patient_Status.txt','a')
                        for items in positivePatientData:
                            fileHandler.write(items)
                            fileHandler.write('\t')
                        fileHandler.write('\n')
                        fileHandler.close()
                        patient.append(actionTaken)
                        patient.append(place)
                        print(patient)
                        positive.append(patient)
                        fileHandler=open("Test1_positive.txt","a")
                        for items in positive:
                            for item in items:
                                fileHandler.write(item)
                                fileHandler.write('\t')
                            fileHandler.write('\n')
                        fileHandler.close()
                    else:
                        print("Invalid test result.")
                else:
                    print("Invalid zone")
            else:
                print("Patient not found.")
        else:
            print("Patient already done test1")
        print()
        break

#Test2
def test2():
    positive=[]                                                             #'positive' and 'negative' will reset when run the function
    negative=[]
    while True:                                                             #The program will run/continue only the statement is 'True'
        patient=[]
        testNumber='T2'
        patientID=input("Enter Patient ID,(x) to exit:").upper()
        patient.append(patientID)
        if patientID=='X':
            break
        if searchTest1("Test2_positive.txt","Test2_negative.txt",patientID): #To check whether patients done test2 before or not
            if searchTest("Test1_negative.txt",patientID):                   #To check whether patients done test1 before or not and the result must be negative
                zone=input("Zone(A/B/C/D):").upper()
                patient.append(zone)
                if zone=='A' or zone=='B' or zone=='C' or zone=='D':        #Zone must be A, B, C or D
                    testResult=input("Enter Test result,negative or positive:").lower()
                    patient.append(testNumber)
                    patient.append(testResult)
                    if testResult=='negative':
                        group=str(input("Group(ATO/ACC/AEO/SID/AHS): ")).upper()
                        patient.append(group)
                        if group=='AHS':                                    #Group must be ATO, ACC, AEO, SID or AHS 
                            actionTaken='CWFR'
                            print('Continue Working')
                            print("Pls come back for third test.")
                        elif group=='SID':
                            actionTaken='HQFR'
                            print('Home Quarantine')
                            print("Pls come back for third test.")
                        elif group=='ATO' or group=='ACC' or group=='AEO':
                            actionTaken='QDFR'
                            print('Quarantine in Designated Centres')
                            print("Pls come back for third test.")
                        else:
                            print("Invalid group.")
                            break
                        patient.append(actionTaken)
                        print(patient)
                        negative.append(patient)
                        fileHandler=open('Test2_negative.txt','a')
                        for items in negative:                              #This is a for loop to run though each item in negative for writing item into fileHandler
                            for item in items:
                                fileHandler.write(item)
                                fileHandler.write('\t')
                            fileHandler.write('\n')
                        fileHandler.close()
                    elif testResult=='positive':
                        positivePatientData=[]                              #'positivePatientData' will reset when run test result becomes positive
                        patientStatus='ACTIVE'
                        group=str(input("Group(ATO/ACC/AEO/SID/AHS): ")).upper()
                        patient.append(group)
                        getID=open('Patient_Status.txt','r+')
                        count=0
                        for line in getID:                                  #This is a for loop to run though each line in getID and each line represents 1 patient
                            count+=1
                        count=count+1                                       #A unique number for new patient
                        getID.close()
                        caseID=str("C")+str(zone)+str(group)+str(count)     #join 'C',zone,group and count to form a unique case ID
                        positivePatientData.append(caseID)
                        positivePatientData.append(patientID)
                        positivePatientData.append(zone)
                        positivePatientData.append(group)
                        positivePatientData.append(patientStatus)
                        if group=='AHS':
                            actionTaken='HQNF'
                            place=""
                            print("Test Result is positive.")
                            print('Home Quarantine')
                        elif group=='ATO' or group=='ACC' or group=='AEO'or group=='SID':
                            actionTaken='QHNF'
                            place=input('WARD or ICU:').upper()
                            if place=='WARD':                               #Place must be WARD or ICU
                                print("Test Result is positive.")
                                print('Quarantine in Hospital Normal Ward.')
                            elif place=='ICU':
                                print("Test Result is positive.")
                                print('Quarantine in Hospital ICU.')
                            else:
                                print("Invalid quarantine place.")
                                break
                        else:
                            print("Invalid group.")
                            break
                        positivePatientData.append(place)
                        fileHandler=open('Patient_Status.txt','a')
                        for items in positivePatientData:
                            fileHandler.write(items)
                            fileHandler.write('\t')
                        fileHandler.write('\n')
                        fileHandler.close()
                        patient.append(actionTaken)
                        patient.append(place)
                        print(patient)
                        positive.append(patient)
                        fileHandler=open('Test2_positive.txt','a')
                        for items in positive:
                            for item in items:
                                fileHandler.write(item)
                                fileHandler.write('\t')
                            fileHandler.write('\n')
                        fileHandler.close()
                    else:
                        print("Invalid test result.")
                else:
                    print("Invalid zone")
            else:
                print('Pls completed registration or test1 first.')
                print('Positive patients did not need to run test2')
        else:
            print("Patient already done test2")
        print()
        break

#Test3       
def test3():
    positive=[]                                                             #'positive' and 'negative' will reset when run the function
    negative=[]
    while True:                                                             #The program will run/continue only the statement is 'True'
        patient=[]
        testNumber='T3'
        patientID=input("Enter Patient ID,(x) to exit:").upper()
        patient.append(patientID)
        if patientID=='X':
            break
        if searchTest1("Test3_positive.txt","Test3_negative.txt",patientID): #To check whether patients done test3 before or not
            if searchTest("Test2_negative.txt",patientID):                   #To check whether patients done test2 before or not and the result must be negative
                zone=input("Zone(A/B/C/D):").upper()
                patient.append(zone)
                if zone=='A' or zone=='B' or zone=='C' or zone=='D':        #Zone must be A, B, C or D
                    testResult=input("Enter Test result,negative or positive:").lower()
                    patient.append(testNumber)
                    patient.append(testResult)
                    if testResult=='negative':
                        group=str(input("Group(ATO/ACC/AEO/SID/AHS): ")).upper()
                        patient.append(group)
                        if group=='AHS':                                    #Group must be ATO, ACC, AEO, SID or AHS 
                            actionTaken='CW'
                            print('Continue Working')
                            print("Congratulation!Your last test result is negative.")
                        elif group=='ATO' or group=='ACC' or group=='AEO' or group=='SID':
                            actionTaken='RU'
                            print('Allow to reunion with family.')
                            print("Congratulation!Your last test result is negative.")
                        else:
                            print("Invalid group.")
                            break
                        patient.append(actionTaken)
                        print(patient)
                        negative.append(patient)
                        fileHandler=open('Test3_negative.txt','a')      
                        for items in negative:                              #This is a for loop to run though each item in negative for writing item into fileHandler
                            for item in items:
                                fileHandler.write(item)
                                fileHandler.write('\t')
                            fileHandler.write('\n')
                        fileHandler.close()
                    elif testResult=='positive':
                        positivePatientData=[]                              #'positivePatientData' will reset when run test result becomes positive
                        patientStatus='ACTIVE'
                        group=str(input("Group(ATO/ACC/AEO/SID/AHS): ")).upper()
                        patient.append(group)
                        getID=open('Patient_Status.txt','r+')
                        count=0
                        for line in getID:                                  #This is a for loop to run though each line in getID and each line represents 1 patient
                            count+=1
                        count=count+1                                       #A unique number for new patient
                        getID.close()
                        caseID=str("C")+str(zone)+str(group)+str(count)     #join 'C',zone,group and count to form a unique case ID
                        positivePatientData.append(caseID)
                        positivePatientData.append(patientID)
                        positivePatientData.append(zone)
                        positivePatientData.append(group)
                        positivePatientData.append(patientStatus)
                        if group=='AHS':
                            actionTaken='HQNF'
                            place=""
                            print("Test Result is positive.")
                            print('Home Quarantine')
                        elif group=='ATO' or group=='ACC' or group=='AEO'or group=='SID':
                            actionTaken='QHNF'
                            place=input('WARD or ICU:').upper()
                            if place=='WARD':                               #Place must be WARD or ICU
                                print("Test Result is positive.")
                                print('Quarantine in Hospital Normal Ward.')
                            elif place=='ICU':
                                print("Test Result is positive.")
                                print('Quarantine in Hospital ICU.')
                            else:
                                print("Invalid quarantine place.")
                                break
                        else:
                            print("Invalid group.")
                            break
                        positivePatientData.append(place)   
                        fileHandler=open('Patient_Status.txt','a')
                        for items in positivePatientData:
                            fileHandler.write(items)
                            fileHandler.write('\t')
                        fileHandler.write('\n')
                        fileHandler.close()
                        patient.append(actionTaken)
                        patient.append(place)
                        print(patient)
                        positive.append(patient)
                        fileHandler=open('Test3_positive.txt','a')
                        for items in positive:
                            for item in items:
                                fileHandler.write(item)
                                fileHandler.write('\t')
                            fileHandler.write('\n')
                        fileHandler.close()
                    else:
                        print("Invalid test result.")
                else:
                    print("Invalid zone")
            else:
                print('Pls completed test2 first.')
                print('Positive patients did not need to run test3')
        else:
            print("Patient already done test3")
        print()
        break
    
#-----------------------------------------------------------------------------------------------------------------------------

#Modify active patients' status 
def modifyPatientStatus():
    fileHandler=open('Patient_Status.txt','r')
    caseID=input("Enter Patient's Case ID,(x) to exit: ").upper()
    fileData=fileHandler.readlines()                                #Read fileHandler and store information in fileData temporarily 
    for index,line in enumerate(fileData):                          #Give a specific representation in each line in fileData
        line=line.strip()
        if caseID in line:
            print(line)                                             #Print patient status if case ID was found in the line of fileData or it will automatically back to main menu
            patientStatus=input("Patient Status(ACTIVE/RECOVERED/DECEASED):").upper()
            line=line.replace("ACTIVE",patientStatus)+"\n"          #Replace 'ACTIVE' with entered patient status
            fileData[index]=line                                    #Renew index in fileData after modifying patient's status
            print(line)
    fileHandler.close()    
    file=open('Patient_Status.txt','w')
    for line in fileData:                                           #This is a for loop to run though each line in fileData for writing line into file
        file.write(line)
    file.close()
    
#-----------------------------------------------------------------------------------------------------------------------------

#Total number of patients in each test 
def testCarriedOut():
    #All counts start from 0
    count1=0
    count2=0
    count3=0
    fileHandler = open('Test1_negative.txt','r')
    for items in fileHandler:                   #This is a for loop to run though each item in fileHandler
        count1 += 1                             #Each line represents 1 patient 
    fileHandler.close()
    fileHandler = open('Test1_positive.txt','r')
    for items in fileHandler:                   
        count1 += 1
    fileHandler.close()   
    fileHandler = open('Test2_negative.txt','r')
    for items in fileHandler:                   
        count2+=1
    fileHandler.close()
    fileHandler = open('Test2_positive.txt','r')
    for items in fileHandler:                   
        count2+=1
    fileHandler.close()
    fileHandler = open('Test3_negative.txt','r')
    for items in fileHandler:                   
        count3+=1
    fileHandler.close()
    fileHandler = open('Test3_positive.txt','r')
    for items in fileHandler:                   
        count3+=1
    fileHandler.close()
    print("Total number of Test1 carried out is",count1)
    print("Total number of Test2 carried out is",count2)
    print("Total number of Test3 carried out is",count3)

#Total number of tested patients     
def patientsTested():
    #Count starts from 0
    count=0
    fileHandler = open('Test1_negative.txt','r')
    for items in fileHandler:                       #This is a for loop to run though each item in fileHandler
        count += 1                                  #Each line represents 1 patient 
    fileHandler.close()
    fileHandler = open('Test1_positive.txt','r')
    for items in fileHandler:                       
        count += 1
    fileHandler.close()
    print("Total number of patients tested is",count)

#Total number of recovered patients    
def recoveredCases():
    count=0
    status="RECOVERED"
    fileHandler = open('Patient_Status.txt','r')
    for items in fileHandler:                       #This is a for loop to run though each item in fileHandler
        if status in items:
            count+=1
    fileHandler.close()
    print("Total number of recovered cases is",count)

#Total number of positive patients in each group
def positiveGroup():
    #All counts start from 0
    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    fileHandler = open('Test1_positive.txt','r')
    for item in fileHandler:                        #This is a for loop to run though each item in fileHandler
        if item[1:4]=='ATO':                        #First 5 alphabet is the patient ID, and alphabet 1-3 is the abbreviations of group 
            count1+=1
        elif item[1:4]=='ACC':
            count2+=1
        elif item[1:4]=='AEO':
            count3+=1
        elif item[1:4]=='SID':
            count4+=1
        elif item[1:4]=='AHS':
            count5+=1
    fileHandler.close()
    fileHandler = open('Test2_positive.txt','r')
    for item in fileHandler:                       
        if item[1:4]=='ATO':
            count1+=1
        elif item[1:4]=='ACC':
            count2+=1
        elif item[1:4]=='AEO':
            count3+=1
        elif item[1:4]=='SID':
            count4+=1
        elif item[1:4]=='AHS':
            count5+=1
    fileHandler.close()
    fileHandler = open('Test3_positive.txt','r')
    for item in fileHandler:                     
        if item[1:4]=='ATO':
            count1+=1
        elif item[1:4]=='ACC':
            count2+=1
        elif item[1:4]=='AEO':
            count3+=1
        elif item[1:4]=='SID':
            count4+=1
        elif item[1:4]=='AHS':
            count5+=1
    fileHandler.close()
    print("Total number of positive patients in ATO",count1)
    print("Total number of positive patients in ACC",count2)
    print("Total number of positive patients in AEO",count3)
    print("Total number of positive patients in SID",count4)
    print("Total number of positive patients in AHS",count5)

#Total number of positive patients in each zone    
def positiveZone():
    #All counts start from 0
    count1=0
    count2=0
    count3=0
    count4=0
    fileHandler = open('Test1_positive.txt','r')
    for item in fileHandler:                        #This is a for loop to run though each item in fileHandler
        if item[0]=='A':                            #First 5 alphabet is the patient ID, and alphabet 0 is the abbreviations of zone
            count1+=1
        elif item[0]=='B':
            count2+=1
        elif item[0]=='C':
            count3+=1
        elif item[0]=='D':
            count4+=1
    fileHandler.close()
    fileHandler = open('Test2_positive.txt','r')
    for item in fileHandler:                        
        if item[0]=='A':
            count1+=1
        elif item[0]=='B':
            count2+=1
        elif item[0]=='C':
            count3+=1
        elif item[0]=='D':
            count4+=1
    fileHandler.close()
    fileHandler = open('Test3_positive.txt','r')
    for item in fileHandler:                    
        if item[0]=='A':
            count1+=1
        elif item[0]=='B':
            count2+=1
        elif item[0]=='C':
            count3+=1
        elif item[0]=='D':
            count4+=1
    fileHandler.close()
    print("Total number of positive patients in Zone A",count1)
    print("Total number of positive patients in Zone B",count2)
    print("Total number of positive patients in Zone C",count3)
    print("Total number of positive patients in Zone D",count4)

#Statistical information on tests carried out       
def statisticalInformation():
    choice=0
    while (choice!=6):
        print('Total number of')
        print('1. Tests carried out')
        print('2. Patients tested')
        print('3. Recovered cases')
        print('4. Patients test positive for COVID-19 group wise')
        print('5. Active cases zone wise')
        print('6. Exit')
        choice=input('Enter selection: ')
        try:                                        #'choice' must be a number(1,2,3,4,5,6)
            choice=int(choice)
            if choice==1:
                testCarriedOut()
            elif choice==2:
                patientsTested()
            elif choice==3:
                recoveredCases()
            elif choice==4:
                positiveGroup()
            elif choice==5:
                positiveZone()
            elif choice==6:
                break
            else:                                   #If 'choice' is not a number between 1-6, it will go to 'else'
                print('Invalid input')
        except:                                     #If 'choice' is not a number, it will go to 'except'
            print('Non-numeric value entered.')
        print()
    
#------------------------------------------------------------------------------------------------------------------------

#Information of registered patient data
def searchPatientRecord():
    try:
        fileHandler = open('Patient_Detail.txt','r')
    except:
        print ('File cannot be opened:')
        exit()
    search_key = input('Enter patient ID or name: ')    
    for line in fileHandler:                        #This is a for loop to run though each line in fileHandler
        line = line.rstrip()
        if search_key.upper() in line:              #If 'search_key'(in upper case) is not in the line, it will go to next line and find 'search_key'
            print(line)
            return                                  #When 'search_key' is found, program will print the information and return to function searchPatientData()
    print("Data not found.")   
    print()
    fileHandler.close()                             

#Information of COVID-19 positive result patient data
def searchCaseStatus():
    try:
        fileHandler = open('Patient_Status.txt','r')
    except:
        print ('File cannot be opened:')
        exit()
    search_key = input('Enter case ID: ')           
    for line in fileHandler:                        #This is a for loop to run though each line in fileHandler
        line = line.rstrip()
        if search_key.upper() in line:              #If 'search_key'(in upper case) is not in the line, it will go to next line and find 'search_key'
            print(line)
            return                                  #When 'search_key' is found, program will print the information and return to function searchPatientData()
    print("Data not found.")
    print()
    fileHandler.close()                             

#Information of deceased patients
def deceasedPatient():
    try:
        fileHandler = open('Patient_Status.txt','r')
    except:
        print ('File cannot be opened:')
        exit()
    search_key = 'DECEASED'   
    for line in fileHandler:                        #This is a for loop to run though each line in fileHandler
        line = line.rstrip()
        if search_key in line:                      #If 'search_key' is not in the line, it will go to next line and find 'search_key'
            print(line)
    print()
    fileHandler.close()                             

#Choice for user to search each particular patient data    
def searchPatientData():
    choice=0
    while (choice!=4):
        print('1. Patient Record')
        print('2. Status of Case')
        print('3. Patient Record of all Deceased Patients')
        print('4. Exit')
        choice=input('Enter selection: ')
        try:                                        #'choice' must be a number(1,2,3,4)
            choice=int(choice)
            if choice==1:
                searchPatientRecord()
            elif choice==2:
                searchCaseStatus()
            elif choice==3:
                deceasedPatient()
            elif choice==4:
                break
            else:                                   #If 'choice' is not a number between 1-4, it will go to 'else'
                print('Invalid input')
        except:                                     #If 'choice' is not a number, it will go to 'except'
            print('Non-numeric value entered.')
        print()
        
#-------------------------------------------------------------------------------------------------

#Create file for storing information        
def createFile():
    fileHandler=open("Patient_Detail.txt",'a')      #Store registered patient information 
    fileHandler.close()
    fileHandler=open('Test1_negative.txt','a')      #Store negative Test1 result patient information 
    fileHandler.close()
    fileHandler=open('Test1_positive.txt','a')      #Store positive Test1 result patient information 
    fileHandler.close()
    fileHandler=open('Test2_negative.txt','a')      #Store negative Test2 result patient information 
    fileHandler.close()
    fileHandler=open('Test2_positive.txt','a')      #Store positive Test2 result patient information 
    fileHandler.close() 
    fileHandler=open('Test3_negative.txt','a')      #Store negative Test3 result patient information 
    fileHandler.close()
    fileHandler=open('Test3_positive.txt','a')      #Store positive Test3 result patient information 
    fileHandler.close()
    fileHandler=open("Patient_Status.txt",'a')      #Store patient information who test positive for COVID-19
    fileHandler.close()
    
#Main Menu
def menu():
    choice=0
    while choice!=6:
        print('----------COVID-19 Patient Management System----------')
        print('Select the operation that you want to perform:')
        print('1. New Patient Registration')
        print('2. Test Result and Action Taken')
        print('3. Changing Patient Status')
        print('4. Statistical Information on Tests Carried Out')
        print('5. Searching Functionalities')
        print("6. Exit")
        choice =input('Enter selection: ')
        print()
        createFile()
        try:                                        #'choice' must be a number(1,2,3,4,5,6)
            choice=int(choice)
            if choice==1:
                patientRegistration()       
            elif choice==2:
                testResults()
            elif choice==3:
                modifyPatientStatus()
            elif choice==4:
                statisticalInformation()
            elif choice==5:
                searchPatientData()
            elif choice==6:
                break
            else:                                   #If 'choice' is not a number between 1-6, it will go to 'else'
                print('Invalid input')
        except:                                     #If 'choice' is not a number, it will go to 'except'
            print("Non-numeric value entered.")
        print()

menu()
