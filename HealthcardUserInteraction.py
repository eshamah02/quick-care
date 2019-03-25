from HealthcardClasses import *

#We're beginners at coding and didn't really know how to incorporate whole datasets into our code. The code has been
#done with certain inputs that you have to press to make it work (e.g. full name, health card number, etc.)

patientHealthcardInput = input("Input your healthcard number.") #Must write '0000-000-001-YM'
look = patientHealthcardInput
for patient in patientList:
    if look in patient.healthcardNumber:
        confirmNumber = input("Type out your name to confirm.") #Must write 'Kathryn Grace Chow'
        while confirmNumber == patientList[0].fullName:
            print (patientList[0].fullName)
            print (patientList[0].birthYear)
            print (patientList[0].gender)
            print (patientList[0].healthcardNumber)
            break
        else:
            while confirmNumber != patientList[0].fullName:
                patientHealthcardInput = input("Sorry, wrong name. Input your healthcard number.")
                look = patientHealthcardInput
                for patient in patientList:
                    if look in patient.healthcardNumber:
                        confirmNumber = input("Type out your name to confirm.")


familyDoctorInput = input("What is the name of your family doctor?") #Must input 'Irene Lee' or 'Elbert Chen'
while familyDoctorInput not in familyDoctorList:
    familyDoctorInput = input("Check spelling please. What is the name of your family doctor?")
else:
    print("Currently gathering your health history from your family doctor records.")

patientSymptomList = []

patientSymptoms = input("Input your symptoms one at a time.") #must include symptoms from lists in HealthcardClasses.py
patientSymptomList.append(patientSymptoms)
moreSymptoms = input("If you have more symptoms, enter them one at a time and press enter. If you're done, enter 'No'.")
if moreSymptoms != "No":
    patientSymptomList.append(moreSymptoms)
while moreSymptoms != "No":
    moreSymptoms=input("To input more symptoms, enter them one at a time and press enter. If you're done, enter 'No'.")
    if moreSymptoms != "No":
        patientSymptomList.append(moreSymptoms)
else:
    for item in patientSymptomList:
        print (item)
    confirmSymptoms = input("Confirm that the following are your symptoms. Write 'Confirm' or 'Not Confirmed'.")
    while confirmSymptoms != "Confirm":
        patientSymptomList.clear()
        patientSymptoms = input("Input your symptoms one at a time.")
        patientSymptomList.append(patientSymptoms)
        moreSymptoms=input("To input more symptoms, type them one at a time and press enter. If you're done, type 'No'.")
        if moreSymptoms != "No":
            patientSymptomList.append(moreSymptoms)
        while moreSymptoms != "No":
            moreSymptoms=input("To input more symptoms, type them one at a time and press enter. "
                            "If you're done, type 'No'.")
            if moreSymptoms != "No":
                patientSymptomList.append(moreSymptoms)
        else:
            for item in patientSymptomList:
                print (item)
            confirmSymptoms = input("Confirm that the following are your symptoms. Write 'Confirm' or 'Not Confirmed'.")

brokenBoneCount = 0
commonColdCount = 0
if confirmSymptoms == "Confirm":
    for i in brokenBone.keys():
        for j in commonCold.keys():
            for k in patientSymptomList:
                if k in i:
                    brokenBoneCount = brokenBoneCount + 1
                if k in j:
                    commonColdCount = commonColdCount + 1

if brokenBoneCount > commonColdCount:
    print("There is a chance you may have a broken bone.")
    postalCodeInput = input("What is your postal code? Don't separate with a space.") #Must use 'L6T3R5'
    if postalCodeInput == "L6T3R5":
        print("We recommend you go to one of the following places right away.")
        print(emergencyCare)
elif brokenBoneCount < commonColdCount:
    print("There is a chance you may have a common cold.")
    postalCodeInput = input("What is your postal code? Don't separate with a space.") #Must use 'L6T3R5'
    if postalCodeInput == "L6T3R5":
        print(walkInClinic)
        whichWalkIn = input("Which walk in do you want to book an appointment with? Type exactly as shown.")
        if whichWalkIn == "Bramalea & Bovaird Walk-In Clinic":
            print(bramAndBov)
            timeCommit = input("Pick a time to commit to for today. Type exactly as written above")
            if timeCommit in bramAndBov:
                print(timeCommit + " time has been committed to you. Get to the medical "
                                    "centre 15 minutes in advance.")
        if whichWalkIn == "Cornerstone Medical Centre Walk In/Urgent Care":
            print(cornStoneMedical)
            timeCommit = input("Pick a time to commit to for today. Type exactly as written above.")
            if timeCommit in cornStoneMedical:
                print(timeCommit + " time has been committed to you. Get to the medical "
                                    "centre 15 minutes in advance.")