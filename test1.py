from module import recruiter
from validataion1 import *
import database1 as db
import maskpass

print('*****Welcome to candidate Management system*****')

choice=0

while(choice!=4):
    print('1,Login')
    print('2,Signup')
    print('3,Exit')

    choice=int(input("Enter your choice:"))
    if choice==1:
        print('Login')
        
        print('\n-----<Login SEction>-----\n')
        print()
        while True:
            print('1,Admin Login')
            print('2,Candidate Login')
            print('3,Exist')
            print()
            choice=input('Enter your Login Choice:')
            #-----------Admin Login---------------------------
            if choice=='1':
                print('\n---------<Admin Login Section>--------\n')
                print()
                #Email validation
                while True:
                    Email=input('Enter  your email:')
                    if EmailValidation(Email):
                        break
                    else:
                        print('\n-----------Invalid Email-----------\n')
                #Password validation
                while True:
                    Password=maskpass.askpass('Enter your Password:',mask='*')
                    if PasswordValidationi(Password)==True:
                        break
                    else:
                        print('\n------Invalid Password-------\n')
                
                data=db.Admin_Login(Email,Password)
                if data==True:
                    print('\n------<Admin Login Successfully>-------\n')
                    print()
                    while True:
                        print('\n--------<Admin Choice>-------------')
                        print()

                        print('1,search Candidate')
                        print('2,Display Candidates Names')
                        print('3,selected Candidate')
                        print('4,Rejected candidate')
                        print('5,Delete candidate')
                        print('6,Download data')
                        print('7,Enter Candidate feedback')
                        print('8,Exit')
                        print()
                        choice=input('enter your Choice')
                        #add new candidate
                        if choice=='1':
                            print()
                            #email validation
                            while True:                            
                                candname=input('Enter email id')
                                break
                            db.search_candidate(candname)
                        elif choice=='2':
                            db.display_candidated_names()
                        elif choice=='3':
                            db.selected_candidate()
                        elif choice=='4':
                            db.rejected_candidate()
                        elif choice=='5':
                            deleteid=input('Enter candidate email ID:')
                            db.delete_candidate(deleteid)
                            print('candidate deleted successfully')
                        elif choice=='6':
                            db.download_data()
                            print('data downloaded successfully')
                        elif choice=='7':
                            email1=input('Enter candidate email')
                            cfeedback=input('Enter your feedback')
                            f=(cfeedback,email1)
                            db.candidate_feedback(f)
                            print()
                            print('---feedback updated-----')
                            print()
                        elif choice=='8':
                            print('\n==========<Back in login page>============\n')
                            break
                        else:
                            print("\n---------invalid choice--------\n")        
                else:
                    print('------<Admin email or Password Wrong>-------')

            #-----------Candidate Login---------------------------
            if choice=='2':
                print('\n---------<candidate Login Section>--------\n')
                print()
                #Email validation
                while True:
                    Email=input('Enter  your email:')
                    if EmailValidation(Email):
                        break
                    else:
                        print('\n-----------Invalid Email-----------\n')
                #Password validation
                while True:
                    Password=maskpass.askpass('Enter your Password:',mask='*')
                    if PasswordValidationi(Password)==True:
                        break
                    else:
                        print('\n------Invalid Password-------\n')
                
                data=db.candidate_Login(Email,Password)
                if data==True:
                    print('\n------<Candidate Login Successfully>-------\n')
                    while True:
                        print('1,Add/Edit details')
                        print('2,show data')
                        print('3,Exist')
                        print()
                        choice=input("Enter your choice:")
                        if choice=='1':
                            print('\n---------<Candidate Details>--------\n')
                            print()
                            #email validation
                            while True:
                                email=input('Enter your Email:')
                                if EmailValidation(email):
                                    break
                                else:
                                    print('\n-------Invalid Email--------\n')
                            #Qualification validation
                            while True:
                                Qualification=input('Enter  your qualification:')
                                if AddressValidation(Qualification):
                                    break
                                else:
                                    print('\n-----------Invalid qualification-----------\n')
                            #work experience validation
                            while True:
                                workexp=input('Enter your work experience')
                                if AddressValidation(workexp):
                                    break
                                else:
                                    print("Enter valid work experience")
                            #Last Salary validation
                            while True:
                                lastsalary=input('Enter your Last Salary per month')
                                if AddressValidation(lastsalary):
                                    break
                                else:
                                    print("Enter valid salary")
                            #Source validation
                            while True:
                                source=input('Enter reference name')
                                if AddressValidation(source):
                                    break
                                else:
                                    print('\n-----------Invalid source-----------\n')
                            #last designation validation
                            while True:
                                lastdesignation=input('Enter your last designation')
                                if AddressValidation(lastdesignation):
                                    break
                                else:
                                    print('\n-----------Invalid designation-----------\n')
                            #designation applied for validation
                            while True:
                                designationapply=input('Enter designation you want to apply for')
                                if AddressValidation(designationapply):
                                    break
                                else:
                                    print('\n-----------Invalid designation applied-----------\n')
                            #Notice Period validation
                            while True:
                                noticeperiod=input('Enter your notice period')
                                if AddressValidation(noticeperiod):
                                    break
                                else:
                                    print("Enter valid details")
                            #Gender validation
                            while True:
                                gender=input('Enter your Gender')
                                if NameValidation(gender):
                                    break
                                else:
                                    print("Enter valid details")
                            #DOB validation
                            while True:
                                dob=input('Enter your date of birth')
                                if AddressValidation(dob):
                                    break
                                else:
                                    print("Enter valid details")
                            #Date validation
                            while True:
                                date=input('Enter date')
                                if AddressValidation(date):
                                    break
                                else:
                                    print("Enter valid details")
                            y=(email,Qualification,workexp,lastsalary,source,lastdesignation,designationapply,noticeperiod,gender,dob,date)
                            db.details(y)
                            print()
                            print('-----------<Details submitted Successfully>-------')
                            print()
                        elif choice=='2':
                            db.show_data(Email)
                        elif choice=='3':
                            print('\n---------back to login page-------\n')
                            break
                                            
                else:
                    print('------<Candidate email or Password Wrong>-------')
            if choice=='3':
                print('Home Page')
                break
            else:
                print('enter correct choice')

    elif choice==2:
        print('signup')
        #email validation
        while True:
            Email=input('Enter your Email:')
            if EmailValidation(Email):
                break
            else:
                print('\n-------Invalid Email--------\n')
        #Password validation
        while True:
            Password=maskpass.askpass('Enter your Password: ',mask='*')
            if PasswordValidationi(Password)==True:
                break
            else:
                print('\n-------Invalid Password------\n')
        #Name Validate
        while True:
            Name=input('Enter  your Name')
            if NameValidation(Name):
                break
            else:
                print('Please type valid name')
        #Address validation
        while True:
            Address=input("Enter your Address")
            if AddressValidation(Address):
                break
            else:
                print("please enter valid address")
        #Contact Validation
        while True:
            Contact=input('Enter you contact number')
            if ConatactValidation(Contact):
                break
            else:
                print("Enter valid contact number")
                
        x= (Email,Password,Name,Address,Contact)
        db.register(x)
        print()
        print('-----------<Account Created Successfully>-------')
        print()

    elif choice==3:
        print('See you soon')
    else:
        break