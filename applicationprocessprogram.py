class application_process:
    
    def __init__ (self, name,current_number_of_students = 1000, management_space = 1500,business_information_management_space = 1500, information_technology_space = 1500, application_limit = 5000, number_of_applications_received = 0):
        self.name = name
        self.current_number_of_students = current_number_of_students
        self.application_limit = application_limit
        self.number_of_applications_received = number_of_applications_received
        self.management_space = management_space
        self.business_information_management_space = business_information_management_space
        self.information_technology_space = business_information_management_space
        
    #Check the number of applications received thus far   
    def current_students(self):
        print(f"Hi {self.name}, the current number of student is {self.current_number_of_students}")
     
    def business_managament(self, business_management_received):
        if business_management_received <= self.management_space:
            self.current_number_of_students += business_management_received
            return(f"You have added {business_management_received} new student for Business Management and the current student is {self.current_number_of_students}")
            
        if self.management_space < 1501:
            result = self.management_space - business_management_received
            return(f"Business management space left is {result}")

        else:
            return("Application limit exceeded")
     
    def business_information_managament(self, business_information_management_received):
        if business_information_management_received <= self.management_space:
            self.current_number_of_students += business_information_management_received
            return(f"You have added {business_information_management_received} new student for Business Information Management and the current student is {self.current_number_of_students}")
            
        if self.business_information_management_space < 1501:
            result = self.management_space - business_information_management_received
            return(f"Business Information Management space left is {result}")

        else:
            return("Application limit exceeded")

    def information_technology(self, information_technology_received):
        if information_technology_received <= self.information_technology_space:
            self.current_number_of_students += information_technology_received
            return(f"You have added {information_technology_received} new student for Information Technology and the current student is {self.current_number_of_students}")
    
        if self.information_technology_space < 1501:
            result = self.business_information_management_space - information_technology_received
            return(f"Information Technology space left is {result}")
            
        else:
            return("Application limit exceeded")
            
    def application_received(self, number_of_application_received):
        if number_of_application_received <= self.application_limit:
            self.current_number_of_students += number_of_application_received
            return(f"Hi {self.name.upper()} you have successfully added number of new application which is {number_of_application_received} and the Current number of student is {self.current_number_of_students}")
            
        if self.current_number_of_students < 5001:
            result = self.application_limit - self.current_number_of_students
            return(f"Application space left is {result}") 
                
        else:
            return("Application limit exceeded")
        
                           
def main():
    print("Welcome to DUT")
    name = input("Enter your name:   ")
    
    while True:
        user = input("Press 1 if you want to check number of application received, Press 2 if you want to see expected number of applications, Press 3 if you want more information about DUT faculties, Press 0 to exit:     ")
        
        ap = application_process(name)
        if user == '0':
            break
        
        elif user =="1":
            ap.current_students()
    
        elif user =="2":
           number_of_application_received = int(input("Enter number of application received:  "))
           ap.application_received(number_of_application_received)
        
        elif user == "3":
            faculty = input("Press 1 if you want Business Management, Press 2 if you want Business Information management(BIM), Press 3 if you want Information Technology(IT)")

            if faculty =="1":
                business_management_received = int(input("Enter number of application received:   "))
                ap.business_managament(business_management_received)

            elif faculty == "2":
                business_information_management_received = int(input("Enter number of application received:   "))
                ap.business_information_managament(business_information_management_received)
        
            elif faculty == "3":
                information_technology_received = int(input("Enter number of application received:    "))
                ap.information_technology(information_technology_received)
        
if __name__ =="__main__":
    main() 