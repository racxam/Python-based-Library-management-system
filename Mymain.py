


class Library:
    bookname= " "
    BorrowedList=[ ]
    UpcompingBooks=[ ]
    list_of_books=["Kamsutra","Ramayan","Mahabharat","loveislove","Karma"]

class Teacher(Library):
    space_of_books=7-len(Library.list_of_books)
    def addABook(self):
        print(f"We are having space of only 7 books!!, at this moment you can only add {Teacher.space_of_books} !!")
        for i in range(0,Teacher.space_of_books):
            inputbook=input("Input the book:  ")
            Library.list_of_books.append(inputbook)
            Teacher.space_of_books-=1

    def displayBooks(self):
        for i,item in enumerate(Teacher.list_of_books):
            i=i+1
            print("\t",i,"-",item)
    def issuedBoooks(self):
        for i,item in enumerate(Library.BorrowedList):
            i+=1
            print("\t",i,"-",item)

    def addUpcomingBooks(self):
        print("\nAdd upcoming books!!!\n")
        for i in range(1,6):
            newbook=input("Enter the upcoming books!!:\n")
            Library.UpcompingBooks.append(newbook)

        for i in Library.UpcompingBooks:
            print(i)
            
    


    



class Student(Library):
    def studentDetails(self):
        
        self.stu_name=input("Please Enter your name User!!\n")
        self.stu_age=input("Please Enter your age User!!\n")
        self.batchid=input("Enter your batch id\n")
        if(self.stu_name and self.stu_age and self.batchid):
            print("\n\nYou are registered successfully Now you can proceed further!!\n")
        else:
            print("You have to register yourself first!! then only you can use!\n")
            exit()
    def displayBooks(self):
        for i,item in enumerate(Teacher.list_of_books):
            i=i+1
            print("\t",i,"-",item)
    def borrowAbook(self):
        bookname=input("Enter the name of book you wants to borrow: \n")
        if bookname in Teacher.list_of_books:

            Teacher.list_of_books.remove(bookname)
            print(f"You have successfully borrowed the book named {bookname}")
            Library.BorrowedList.append(bookname)
        else:
            print("This book is not present our Library!!!")
    
    def Seeupcomingbooks(self):
        for i in Library.UpcompingBooks:
            print(i)

    def ReturningAbook(self):
        self.bookname=input("Enter the name of the book you wants to return !!\n")
        if self.bookname in Library.BorrowedList:
            Library.list_of_books.append(self.bookname)
            print("Thank you so much for returning the book!!\n Have a great day!!")
        else:
            print("We haven't issued this book to you !! please enter the correct name!!!")




        




#functions
def WelcomeForTeacher():
    welcomeMsgTeacher='''============Student Library Management System=============
    
    \t1.Press 1 to See the Available books
    \t2.Press 2 to Add a book
    \t3.Press 3 to see Issued books
    \t4.Press 4 to add upcoming books
    \t5.Press 5 to exit the system
    '''
    print(welcomeMsgTeacher)
def WelcomeForStudents():
    welcomeMsgStudents='''============Student Library Management System=============
    \t1.Press 1 to See the Available books
    \t2.Press 2 to Borrow a book.
    \t3.Press 3 to Return a book
    \t4.Press 4 to see the list of upcoming book
    \t5.Press 5 to exit the system
    '''
    print(welcomeMsgStudents)

def chooseforTeacher():
    while(True):
        try:

             teacherChoice=int(input("Select your choice Teacher!!\n"))
             if(teacherChoice==1):
                 t.displayBooks()
             elif(teacherChoice==2):
                 t.addABook()
             elif(teacherChoice==3):
                 t.issuedBoooks()
             elif(teacherChoice==4):
                 t.addUpcomingBooks()
             elif(teacherChoice==5):
                 print("Thanks Teacher for managing our library!!...........")
                 break
             else:
                 print("Please!! input appropriate choice Mr.")
        except Exception as e:
            print(f"Please!!! input only integer values ...\n program is showing expection as :  {e}")

def chooseforStudent():
    while(True):
        try:

    
             studentChoice=int(input(f"Select your choice !!{objname.stu_name}\n"))
             if(studentChoice==1):
                 objname.displayBooks()
             elif(studentChoice==2):
                 objname.borrowAbook()
             elif(studentChoice==3):
                 objname.ReturningAbook()
             elif(studentChoice==4):
                objname.Seeupcomingbooks()

             
             elif(studentChoice==5):
                print("\nThanks Bachhe for managing our library!!...........\n")
                break
             else:
                print("\nPlease!! input appropriate choice Mr.\n")
        except Exception as e:
            print(f"\nplease enter only integer value ....Program is getting this error : : {e}")

#object creations

objname=f"stu"
objname=Student()

t=Teacher()


while(True):

    print(f"1.If you are teacher then select 1 ")
    print(f"2.If you are Student then select 2 ")
    print("\n")
    print(f"To Exit the program plese enter 0")
    Who_is_user=int(input("\nSelect the appropriate option!!\n"))
    if(Who_is_user==1):
        WelcomeForTeacher()
        chooseforTeacher()


    elif(Who_is_user==2):
        WelcomeForStudents()
        print("\nfirst Register youself to use these options!!\n")
        objname.studentDetails()
        chooseforStudent()
    elif(Who_is_user==0):
        print("Thanks for using our program !!!")
        exit()

    else:
        print("OOPS!!!!Enter the appropriate Choice!!!")

        

