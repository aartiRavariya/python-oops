class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedIn = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatbook"
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to msg a frnd
                           5. Press any other key to exit 
                           
                           
                           """
                            )
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.send_msg()
        else:
            exit()

    def signup(self):
        email = input("enter ur email here: ")
        password = input("Set your password: ")
        self.username = email
        self.password = password
        print("Sign up successfull")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == '' and self.password == '':
            print("Please Sign up")
        else:
            uname = input("Username: ")
            pswd = input("Password: ")
            if uname == self.username and pswd == self.password:
                print("Successfully signed-in")
                self.loggedIn = True
            else:
                print("Invalid Credentials. Try again")

        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedIn == True:
            txt = input("Write your message here: ")
            print(f"following {txt} has been posted")
        else:
            print("Please signin")
        
        print("\n")
        self.menu()

    def send_msg(self):
        if self.loggedIn == True:
            txt = input("Write your message here: ")
            frnd = input("whome to send the message: ")
            print(f"Your message has been sent to {frnd}")
        else:
            print("Please signin")
        
        print("\n")
        self.menu()

# obj = chatbook()