class healthcard:
    def __init__(self, fullName = None, birthYear = None, gender = None, healthcardNumber = None):
        self.fullName = fullName
        self.birthYear = birthYear
        self.gender = gender
        self.healthcardNumber = healthcardNumber

patientList = []
patientList.append(healthcard("Kathryn Grace Chow", "2003", "F", "0000-000-001-YM"))

familyDoctorList = []
familyDoctorList.append("Irene Lee")
familyDoctorList.append("Elbert Chen")

brokenBone = {("discolouration", "swelling", "bruising", "pain") : "Broken Bone"}
commonCold = {("runny nose", "stuffy nose", "cough", "body aches", "sore throat", "mild fever") : "Common Cold"}

emergencyCare = {"Brampton Civic Hospital" : "2100 Bovaird Dr. E, Brampton, L6R3J7",
                 "Sajjad Ebrahim & Family Urgent Care Centre" : "20 Lynch St, Brampton, L6S 2Z8",
                 "Cornerstone Medical Centre Walk In/Urgent Care" : "8990 Chinguacousy Rd #9, Brampton L6R0K1",
                 "Pulse Urgent Care Centre" : "55 Dusk Dr #1, Brampton L6Y5Z6"}

walkInClinic = {"Bramalea & Bovaird Walk-In Clinic" : "10095 Bramalea Rd. #107, Brampton L6R0K1",
                "Cornerstone Medical Centre Walk In/Urgent Care" : "8990 Chinguacousy Rd. #9, Brampton L6Y5X6"}

bramAndBov = ["2:00PM", "5:00PM"]
cornStoneMedical = ["11:00AM", "3:30PM"]