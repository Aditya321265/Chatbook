class user:
    def __init__(self, name, email, password):
        self.name= name 
        self.email= email
        self.__password= password

    def send_message(self, message):
        print(self.name,"sent:", message )

    def get_profile(self):
        print('Name:', self.name)
        print('email:', self.email)  

    def set_password(self, password):
        if len(password)>=8:
            self.__password = password    
            print('Password has been updated')
        else:
            print('The password should contain atleast 8 characters')
            
        

user1=user('Aditya','aditya@gmail.com','sasas')
user2=user('Barsha','barsha@gmail.com','asadd')
user3=user('prabhat','pravat@gmail.com','adsfrgrds')

user1.send_message('Hello! Barsha')
user1.get_profile()
#Setter
user1.set_password('xyz')

print('')
user2.send_message('Hello! Adi how are you?')
user2.get_profile()
#Setter
user2.set_password('cygfeg3r24r')

print('')
user3.send_message('Hello! All, hope you are doing good.')
user3.get_profile()
#Setter
user3.set_password('hgbkjrnaefe')

#static method
@staticmethod
def validate_email(email):
    return '@' in email

# dunder method 
def __str__(self):
    return f"user: {self.name}"
