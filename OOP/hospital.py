# a Patient class which gets instantiated in the admit() method of the Hospital class

class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies

class Hospital(object):
    def __init__(self, name, capacity):
        self.bed_num = 0
        self.patients_list = [] 
        self.name = name
        self.capacity = capacity
        self.empty_beds = capacity
        #create list of bed numbers based on capacity
        self.bed_nums = []
        while self.capacity > 0:
            self.bed_nums.append(self.capacity)
            self.capacity -= 1          
    
    def admit(self, id, name, allergies):
        # if there are empty beds
        if self.bed_nums:
            # assign a bed number from list of bed numbers
            self.bed_num = self.bed_nums[0]
            #a dict to hold all the new patient info and hospital bed number
            new_patient = {
                'patient' : Patient(id, name, allergies), #creating a new instance of Patient here
                'bed_num' : self.bed_num
                }
            self.patients_list.append(new_patient)
            # remove bed num from list of available because just used it
            self.bed_nums.pop(0)
            self.empty_beds -= 1
        else:
            print '* *'* 40
            print self.name, 'is at capacity and cannot admit any more patients at this time'
            print '* *'* 40
        return self

    def discharge(self, name):
        for patient in self.patients_list:
            if patient['patient'].name == name:
                idx = self.patients_list.index(patient) #grab index in list of patients of patient to be removed
                self.bed_nums.append(patient['bed_num'])
                self.empty_beds += 1
        self.patients_list.pop(idx)
        return self

    def display(self):
        print ' '
        print 'Currently at', self.name
        print ' - -' * 10
        for patient in self.patients_list:
            print 'patient name:', patient['patient'].name
            print 'bed #:', patient['bed_num']
            print 'allergies:', patient['patient'].allergies
            print ' - -' *10
        print '{} empty bed(s) until {} is at capacity'.format(self.empty_beds, self.name)
        print '=='* 40



#tests:
x = Hospital('Portland General', 3)
print 'admiting 3 new patients'
x.admit(1, 'J R', 'none').admit(2,'G W', 'penicillin').admit(3, 'M J', "none").display()  #capicity full now
print ' '
x.admit(4, 'H C', 'glocouse') #puts out message that at capicity and cant admit more patients
print ' '
print 'discharging patient'
x.discharge('G W').display()  #now a bed vacency
print ' '
print 'admiting 1 patient'
x.admit(4, 'H C', 'glocouse').display() #notice here that the new patient gets assigned to bed 2 because that is the only one available


