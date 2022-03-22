# Creating Class -- Library
class Library:
    def __init__(self,List_of_Books, User_Names):
        self.Books = List_of_Books
        self.UserNames = User_Names
    
     # Creating Function For listing the books Name
    def ListofBooks(self):
        print("AI: Book Available in Rudra's Library are: ")
        for Book in self.Books:
            print('>> '+Book) 
    
    # Creating Function To Borrow a book
    def Borrow_Book(self,Username):
        if Username in self.UserNames:
            BookName = input("AI: Enter a Name of Book Which You want to Borrow: ")
            if BookName in self.Books:
                print(f"AI: You borrowed {BookName} Book. Please keep it up safe and return within 30days")
                self.Books.remove(BookName)
            else:
                print(f"AI: {BookName} book is currently unavailable in Rudra's Library")
            
        if Username not in self.UserNames:
                print("==== Your are not registered ====")
                print("AI: Please Press 4: For Registration ")
     
     #  Creating Function To Return Book..
    def Return_Book(self,Book_Name):
        if Book_Name in self.Books:
            print(f"AI: {Book_Name} book is already present in Python's Library")
        else:
            print(f"AI: Thank You For Returning {Book_Name} Book to Rudra's Library")
            self.Books.append(Book_Name)
    
    # Creating Function For Registration..
    def Be_A_Member(self,User_Name):
        if User_Name in self.UserNames:
            print("AI: This User Name is already taken")
        else:
            self.UserNames.append(User_Name)
            print("AI: You are successfully Registered... ")

Students =  Library(["Python For Beginners","Advanced Python", "10th Maths NCERT","11th Maths NCERT","Algorithms", "Numpy","Data Science","C++ Programming","Complete <html>","Class-2 Maths"],[])

while True:
    Welcome = '''====== Welcome To Rudra's Library ======\n\tPlease Choose Any Option\n1.List of Books\n2.Request A Book\n3.Add/Return A Book\n4.Registration in Library \n5.Exit the Python's Library'''
    print(Welcome,'\n')
    User = input("AI: Enter Your Choice: ")
    
    if User == '1':
        Students.ListofBooks()        
    elif User == '2':
        Username = input("AI: Enter Your User Name: ")
        Students.Borrow_Book(Username)

    elif User == '3':
        Book = input("AI: Enter A Name of Book Which You want to return: ")
        Students.Return_Book(Book)
    elif User == '4':
        User_Name = input("AI: Enter Your User Name: ")        
        Students.Be_A_Member(User_Name)
    elif User == '5':
        print("AI: Thank You For Using Rudra's Library")
        exit()
    else:
        print ("AI: Enter Valid Choice") 