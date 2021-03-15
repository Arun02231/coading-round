class Gym:
    def __init__(self):
        self.details_user={}
        self.regimen_list_18={}       
        self.regimen_list_25={}
        self.regimen_list_30={}
        self.regimen4={}
        self.user=input('Please choose who you are SUPER USER/MEMBER:')
        while self.user.casefold() not in ['superuser','super user','member']:
            print('***** Invalid option! please try again: *****')
            self.user=input('Please choose who you are USER/MEMBER:')
            continue
        self.user=self.user.casefold()
        if self.user.casefold=='superuser':
            self.user='super user'
        if self.user=='super user':
            self.super_user()
        if self.user=='member':
            self.member()    
    def member(self):
        print('***** please choose the following options *****')
        print('1. My Regimen')
        print('2. My profile')
        print('0. Switch as Super user')
        self.choice=input('please select the option from above:')
        while self.choice.isdigit==False or self.choice>'2':
            print('***** Invalid option *****')
            self.choice=input('please select the option from above:')
            continue
        self.choice=int(self.choice)
        if self.choice==0:
            self.super_user()
        elif self.choice==1:
            self.my_regimen()
        elif self.choice==2:
            self.my_profile()
        
        
    def super_user(self):
        print('****** Please choose the following options ***************')
        print('1. Create a member')
        print('2. View member')
        print('3. Delete member')
        print('4. Upadte member')
        print('5. Create Regimen')
        print('6. View Regimen')
        print('7. Delete Regimen')
        print('8. Update Regimen')
        print('0. Switch as member')
        self.choice=input('please select the option from above:')
        while self.choice.isdigit==False or self.choice>'8':
            print('***** Invalid option *****')
            self.choice=input('please select the option from above:')
            continue
        self.choice=int(self.choice)
        if self.choice==1:
            self.create_member()
        elif self.choice==2:
            self.view_member()
        elif self.choice==3:
            self.delete_member()
        elif self.choice==4:
            self.update_member()
        elif self.choice==5:
            self.create_regimen()
        elif self.choice==6:
            self.view_regimen()
        elif self.choice==7:
            self.delete_regimen()
        elif self.choice==8:
            self.update_regimen()
        elif self.choice==0:
            self.member()    
    def create_member(self):
        print('***** Enter 0 in any filed to get back to Main menu *****')
        self.name=input('Please enter your name:')
        if self.name=='0':
            self.super_user()
        while self.name.isdigit()==True:
            print('**** Invalid option *****')
            self.name=input('Please enter your name:')
            continue
        
        self.age=input('Please enter your age:')
        while self.age.isdigit()==False:
            print('**** Invalid option *****')
            self.age=input('Please enter your age:')
            continue
        if self.age=='0':
            self.super_user()
        self.gender=input('Please select your gender MALE/FEMALE/OTHER:')
        if self.gender=='0':
            self.super_user()
        while self.gender.isalpha()==False or self.gender.casefold() not in ['male','female','other']:
            print('**** Invalid option *****')
            self.gender=input('Please select your gender MALE/FEMALE/OTHER:')
            continue
        self.number=input('Please enter your phone number:')
        if self.number=='0':
            self.super_user()
        while self.number.isdigit()==False:
            print('***** Invalid option *****')
            self.number=input('Please enter your phone number:')
            continue
        self.mail=input('please enter yor email:')
        if self.mail=='0':
            self.super_user()
        while self.mail == ' ':
            print('Please enter the mail')
            self.mail=input('please enter yor email:')
            continue
        self.bmi=input('please enter the BMI(BODY MASS INDEX):')
        if self.bmi=='0':
            self.super_user()
        while self.bmi.isalpha()==True:
            print('**** Invalid option *****')
            self.bmi=input('please enter the BMI(BODY MASS INDEX):')
            continue
        self.duration=input('Please enter the duration in months:')
        if self.duration=='0':
            self.super_user()
        while self.duration.isdigit()==False:
            print('***** Invalid option *****')
            self.duration=input('Please enter the duration in months:')
            continue
        self.option=input('please confirm to add the mmber y/n:')
        while self.option.casefold() not in ['y','n','yes','no']:
            print('***** Invalid option *****')
            self.option=input('please confirm to add the mmber y/n:')
            continue
        if self.option in ['y','n','yes','no'] and self.number not in self.details_user:
            self.details_user[self.number]=[self.name,int(self.age),self.gender,self.number,self.mail,float(self.bmi),float(self.duration)]
        else:
            print('You are already a member of zym/you are phone number is already registered...!,please choose another number:')
            self.create_member()
        self.super_user()
    def delete_member(self):
        print('***** Enter 0 to get back to Main menu *****')
        self.contact=input('please enter the phone number/contatct that you want to remove:')
        if self.contact=='0':
            self.super_user()
        while self.contact.isdigit()==False:
            print('***** Invalid option *****')
    
            self.contact=input('please enter the phone number/contatct that you want to remove:')
            if self.contact=='0':
                self.super_user()
            else:
                continue
        try:
            self.details_user.pop(self.contact)
            self.super_user()
        except:
            print('*****Please choose proper contact it is not registered******')
            self.delete_member()
    def view_member(self):
        print('***** Enter 0 to get back to Main menu *****')
        self.contact=input('please enter the phone number/contatct that you want to see:')
        if self.contact=='0':
            self.super_user()
        while self.contact.isdigit()==False:
            print('***** Invalid option *****')
            self.contact=input('please enter the phone number/contatct that you want to see:')
            if self.contact=='0':
                self.super_user()
            else:
                continue
#         self.contact=int(self.contact)
        try:
            print('Name:',self.details_user[self.contact][0])
            print('Age:',self.details_user[self.contact][1])
            print('Gender:',self.details_user[self.contact][2])
            print('Number:',self.details_user[self.contact][3])
            print('E-Mail:',self.details_user[self.contact][4])
            print('BMI:',self.details_user[self.contact][5])
            print('Duration:',self.details_user[self.contact][6])
            self.super_user()
        except KeyError:
            print('*****Please choose proper contact it is not registered******')
            self.view_member()
    def update_member(self):
        print('***** Enter 0 in any filed to get back to Main menu *****')
        print('**** This section for extending and revoking the memberdhip ****')
        self.contact=input('please enter the phone number/contatct that you want to see:')
        if self.contact=='0':
            self.super_user()
        while self.contact.isdigit()==False:
            print('***** Invalid option *****')
            print('Number not in list please enter 0 to getback to menu menu or enter number to continue:')
            self.contact=input('please enter the phone number/contatct that you want to see:')
            if self.contact=='0':
                self.super_user()
            continue
        try:
            print('Your membership is:',self.details_user[self.contact][6],'months')

            self.um=input('Please enter the E for extending or R for the revoking:')
            if self.um=='0':
                self.super_user()
            while self.um.isalpha()==False or self.um.casefold() not in ['e','r','extend','revoke']:
                print('**** Invalid option')
                self.um=input('Please enter the E for extending or R for the revoking:')
                continue
            self.um=self.um
        
            if self.um.casefold() in ['e','extend']:
                self.du=input('please enter no of months do you want to extend:')
                if self.du=='0':
                    self.super_user()
                while self.du.isdigit()==False:
                    print('**** Invalid option ****')
                    self.du=input('please enter no of months do you want to extend:')
                    continue
                self.details_user[self.contact][6]=self.details_user[self.contact][6]+float(self.du)
                print('Your duration has ectended to',self.du,'months')
            elif self.um.casefold() in ['r','revoke']:
                self.details_user.pop(self.contact)
                print('**** Yor mebership has been terminated ****')

            self.super_user()
        except KeyError:
            print('*****Please choose proper contact it is not registered******')
            self.update_member()
    def create_regimen(self):
    
        print('***** Enter 0 in any filed to get back to Main menu *****')
        self.regimen1={}
        self.mon=input('Please enter the work regimen for Monday!:')
        if self.mon=='0':
            self.super_user()
        while self.mon.isalpha == False or self.mon not in ['legs','chest','biceps','rest','back','cardio','cardio/abs']:
            print('***** Invalid option *****')
            self.mon=input('Please enter the work regimen for Monday!:')
            continue
        self.regimen1['Mon']=self.mon
        self.tue=input('Please enter the work regimen for Tuesday!:')
        if self.tue=='0':
            self.super_user()
        while self.tue.isalpha == False or self.tue not in ['legs','chest','biceps','rest','back','cardio','cardio/abs']:
            print('***** Invalid option *****')
            self.tue=input('Please enter the work regimen for Tuesday!:')
            continue
        self.regimen1['Tue']=self.tue
        self.wed=input('Please enter the work regimen for wednesday!:')
        if self.wed=='0':
            self.super_user()
        while self.wed.isalpha == False or self.wed not in ['legs','chest','biceps','rest','back','cardio','cardio/abs']:
            print('***** Invalid option *****')
            self.wed=input('Please enter the work regimen for wednesday!:')
            continue
        self.regimen1['Wed']=self.wed
        self.thur=input('Please enter the work regimen for Thursday!:')
        if self.thur=='0':
            self.super_user()
        while self.thur.isalpha == False or self.thur not in ['legs','chest','biceps','rest','back','cardio','cardio/abs']:
            print('***** Invalid option *****')
            self.thur=input('Please enter the work regimen for Thursday!:')
            continue
        self.regimen1['Thur']=self.thur
        self.fri=input('Please enter the work regimen for Friday!:')
        if self.fri=='0':
            self.super_user()
        while self.fri.isalpha == False or self.fri not in ['legs','chest','biceps','rest','back','cardio','cardio/abs']:
            print('***** Invalid option *****')
            self.fri=input('Please enter the work regimen for Friday!:')
            continue
        self.regimen1['Fri']=self.fri
        self.sat=input('Please enter the work regimen for Saturday!:')
        if self.sat=='0':
            self.super_user()
        while self.sat.isalpha == False or self.sat not in ['legs','chest','biceps','rest','back','cardio','cardio/abs']:
            print('***** Invalid option *****')
            self.sat=input('Please enter the work regimen for Saturday!:')
            continue
        self.regimen1['Sat']=self.sat
        self.sun=input('Please enter the work regimen for Sunnday!:')
        if self.sun=='0':
            self.super_user()
        while self.sun.isalpha == False or self.sun not in ['legs','chest','biceps','rest','back','cardio','cardio/abs']:
            print('***** Invalid option *****')
            self.sun=input('Please enter the work regimen for Sunnday!:')
            continue
        self.regimen1['Sun']=self.sun
        try:
            if float(self.bmi)<18.5 or self.number not in self.regimen_list_18:
                self.regimen_list_18[self.number]=self.regimen1
            elif float(self.bmi)<25 or self.number not in self.regimen_list_25:
                self.regimen_list_25[self.number]=self.regimen1
            elif float(self.bmi)<30 or self.number not in self.regimen_list_30:
                self.regimen_list_30[self.number]=self.regimen1
            elif float(self.bmi)>30 or self.number not in self.regimen4:
                self.regimen4[self.number]=self.regimen1
            else:
                print('***** The number is already in list please choose another number *****')
                self.super_user()
            self.super_user()
        except AttributeError:
            print('*****Please choose proper contact it is not registered******')
            self.create_regimen
            
            
        
    def view_regimen(self):
        print('***** Enter 0 in any filed to get back to Main menu *****')
        self.b=input('Please enter the bmi of the person you want to see:')
        if self.b=='0':
            self.super_user()
        
        while self.b.isalpha == True:
            print('***** Invalid option *****')
            print('Number not in list please enter 0 to getback to menu menu or enter number to continue:')
            self.b=input('Please enter the bmi of the person you want to see:')
            if self.b=='0':
                self.super_user()
            else:
                continue
        
        self.c=input('please enter the contact of the person you wnat to see:')
        if self.c=='0':
            self.super_user()
        while self.c.isdigit==False:
            print('***** Invalid option *****')
            print('Number not in list please enter 0 to getback to menu menu or enter number to continue:')
            self.c=input('please enter the contact of the person you wnat to see:')
            if self.c=='0':
                self.super_user()
            else:
                continue
        try:
        
            self.days=['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
            if float(self.b)<18.5:

                for i in self.days:
                    print(i+':'+self.regimen_list_18[self.c][i])
                self.super_user()
            elif float(self.b)<25:
                for i in self.days:
                    print(i+':'+self.regimen_list_25[self.c][i])
                self.super_user()
            elif float(self.b)<30:
                for i in self.days:
                    print(i+':'+self.regimen_list_30[self.c][i])
                self.super_user()
            elif float(self.b)>30:
                for i in self.days:
                    print(i+':'+self.regimen4[self.c][i])
                self.super_user()
            else:
                print('**** Please choose the correct option ****')
                self.super_user()
        except KeyError:
            print('*****Please choose proper contact it is not registered******')
            self.view_regimen()
            
    def delete_regimen(self):
        print('***** Enter 0 in any filed to get back to Main menu *****')
        self.b=input('Please select the bmi of person which yo want to delete:')
        if self.b=='0':
            self.super_user()
        while self.b.isalpha==True:
            print('***** Invalid option *****')
            self.b=input('Please select the bmi of person which yo want to delete:')
            continue
        self.c=input('please enter the contact of the person which you wnat to delete:')
        if self.c=='0':
            self.super_user()
        while self.c.isdigit==False:
            print('***** Invalid option *****')
            print('Number not in list please enter 0 to getback to menu menu or enter number to continue:')
            self.c=input('please enter the contact of the person which you wnat to selete:')
            if self.c=='0':
                self.super_user()
            else:
                continue
        try:
            if float(self.b)<18.5:
                self.regimen_list_18.pop(self.c)
                print('***** The regimen has deleted *****')
                self.super_user()
            elif float(self.b)<25:
                self.regimen_list_25.pop(self.c)
                print('***** The regimen has deleted *****')
                self.super_user()
            elif float(self.b)<30:
                self.regimen_list_30.pop(self.c)
                print('***** The regimen has deleted *****')
                self.super_user()
            elif float(self.b)>30:
                self.regimen4.pop(self.c)
                print('***** The regimen has deleted *****')
                self.super_user()
        except KeyError:
            print('*****Please choose proper contact it is not registered******')
            self.delete_regimen()
            
    def update_regimen(self):
        print('***** Enter 0 in any filed to get back to Main menu *****')
        while True:
            self.b=input('Please select the bmi of person which yo want to Upadte:')
            if self.b=='0':
                self.super_user()
            while self.b.isalpha==True:
                print('***** Invalid option *****')
                self.b=input('Please select the bmi of person which yo want to update:')
                continue
            self.c=input('please enter the contact of the person which you wnat to Upadte:')
            if self.c=='0':
                self.super_user()
            while self.c.isdigit==False:
                print('***** Invalid option *****')
                self.c=input('please enter the contact of the person which you wnat to update:')
                if self.c=='0':
                    self.super_user()
                else:
                    continue
            self.day=input('Please enter the day which you wnat to update:')
            if self.day=='0':
                self.super_user()
            while self.day.title() not in ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']:
                print('***** Invalid option *****')
                self.day=input('Please enter the day which you wnat to update:')
                continue
            self.day=self.day.title()
            self.update=input('please enter what you want to update:')
            if self.update=='0':
                self.super_user()
            while self.update.isalpha == False or self.update not in ['legs','chest','biceps','rest','back','cardio','cardio/abs']:
                print('***** Invalid option *****')
                self.update=input('please enter what you want to update:')
                continue
            try:
                if float(self.b)<18.5:
                    self.regimen_list_18[self.c][self.day]=self.update
                    print('**** Your regimen updated *****')

                elif float(self.b)<25:
                    self.regimen_list_25[self.c][self.day]=self.update
                    print('**** Your regimen updated *****')
                elif float(self.b)<30:
                    self.regimen_list_30[self.c][self.day]=self.update
                    print('**** Your regimen updated *****')
                elif float(self.b)>30:
                    self.regimen4[self.c][self.day]=self.update

                    print('**** Your regimen updated *****')
                self.o=input('Please enter 1 to update further or enter 0 to quit')
                while self.o.isdigit==False or self.o not in ['0','1']:
                    print('***** Invalid option *****')
                    self.o=input('Please enter 1 to update further or enter 0 to quit')
                    continue
                if self.o=='1':
                    continue
                else:
                    self.super_user()
            except KeyError:
                print('*****Please choose proper contact it is not registered******')
                self.update_regimen()
                
                
    def my_regimen(self):
        print('***** Enter 0 in any filed to get back to Main menu *****')
        self.days=['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
        self.b=input('Please enter your bmi:')
        if self.b=='0':
                self.member()
        
        while self.b.isalpha == True:
            print('***** Invalid option *****')
            self.b=input('Please enter your bmi:')
            continue
        self.con=input('please enter your contact:')
        if self.con=='0':
                self.member()
        while self.con.isdigit==False:
            print('***** Invalid option *****')
            self.con=input('please enter your contact:')
            if self.con=='0':
                self.member()
            else:
                continue
        try:
            self.con=str(self.con)
            if float(self.b)<18.5: 
                for i in self.days:
                    print(i+':'+self.regimen_list_18[self.con][i])
                self.member()
            elif float(self.b)<25:
                for i in self.days:
                    print(i+':'+self.regimen_list_25[self.con][i])
                self.member()
            elif float(self.b)<30:
                for i in self.days:
                    print(i+':'+self.regimen_list_30[self.con][i])
                self.member()
            elif float(self.b)>30:
                for i in self.days:
                    print(i+':'+self.regimen4[self.con][i])
                self.member()
            else:
                print('**** Please choose the correct option ****')
                self.member()
        except KeyError:
            print('*****Please choose proper contact it is not registered******')
            self.my_regimen()
            
    def my_profile(self):
        print('***** Enter 0 in any filed to get back to Main menu *****')
        self.conta=input('Please enter your contact number:')
        if self.conta=='0':
                self.member()
        while self.conta.isdigit==False or self.conta not in self.details_user:
            print('***** Invalid option *****')
            rint('***** Contact is not registered please Enter 0 to get back to menu or enter number to continue:')
            self.conta=input('please enter your contact:')
            if self.conta=='0':
                self.member()
            else:
                continue
        try:
            print('Name:',self.details_user[self.conta][0])
            print('Age:',self.details_user[self.conta][1])
            print('Gender:',self.details_user[self.conta][2])
            print('Number:',self.details_user[self.conta][3])
            print('E-Mail:',self.details_user[self.conta][4])
            print('BMI:',self.details_user[self.conta][5])
            print('Duration:',self.details_user[self.conta][6])
            self.member()
        except:
            print('*****Please choose proper contact it is not registered******')
            self.my_profile()
g=Gym()