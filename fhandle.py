import pickle

class Employee():
    def __init__(self, name, designation, noHours, payRate):
        self.name = name
        self.designation = designation
        self.noHours = noHours
        self.payRate = payRate

    def __str__(self):
        return """\n\nName : %s\nDesignation : %s \nNo. of hours worked in a week : %s\nHourly pay rate : %s """ % (self.name, self.designation, self.noHours, self.payRate)

def existCount(name):
    suc = 1
    count = 0
    while True:
            checkfile = name.lower()+ str(suc) +'.pkl'
            try:
                with open(checkfile,'rb') as check:
                    count += 1
            except:
                break
                
            suc += 1
    return count

while True:
    choice = (input("""
        \t1. Add employee record
        \t2. Show details
        \t3. Exit application
                """))

    if choice == '1':
        name = input("\nEnter the employee's name : ")
        designation = input("Enter Designation : ")
        noHours = input("No of hours worked in a week : ")
        payRate = input("Hourly pay rate : ")
       
        if not name or not designation or not noHours or not payRate:
            print('Details missing, Please try again !')
            continue
        
        emp = Employee(name, designation, noHours, payRate)
        filename = emp.name.lower().strip().replace(' ','_') + '.pkl'
        try:
            with open(filename, 'xb') as save:
                pickle.dump(emp, save)
                print('\nRecorded successfully')

        except:
            enter = input(emp.name+"'s Details already exist.\n1.Update exisiting record\n2.Create new record  :")
            count = existCount(emp.name)
            count += 1
            if enter == '1':
                with open(filename, 'wb') as save:
                    pickle.dump(emp, save)
                    print('\nRecorded successfully')

            elif enter == '2':
                filename = emp.name.lower().strip().replace(' ','_') + str(count) +'.pkl'
                with open(filename, 'wb') as save:
                    pickle.dump(emp, save)
                    print('\nRecorded successfully')
                
            else:
                print('\nWrong input, try again !\n')   

    elif choice == '2':
        name = input("\nEnter the employee's name to search : ")
        filename = name.lower().strip().replace(' ','_') + '.pkl'
        try:
                with open(filename, 'rb') as retreive:
                    emp = pickle.load(retreive)
                    print(emp)
                        
        except:
                print('\nEmployee details not found !')
        
        count = 0
        count = existCount(name)
        if count != 0:
           
            for x in range(1,count+1):
                filename = name.lower()+ str(x) + '.pkl' 
                with open(filename, 'rb') as retreive:
                    emp = pickle.load(retreive)
                    print(emp)
                        
            
    elif choice == '3':
        print('Thank you')
        break
    
    else:
        print('Wrong input, try Again')
        

