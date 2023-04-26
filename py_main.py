# Author : maxus_red
# License : maxus_universe
# Date : 26/04/23
# Third miniproject on python
# Student Library Management Systems

class Book:

    __author = 'Not mentioned'
    __name = 'Not mentioned'
    __id = 'Not mentioned'
    # _count = 0

    def __init__(self, name, aut='Not mentioned'):
        self.__name = name
        # self.__id = id
        self.__author = aut
        # Book._count += 1

    def setAuthor(self, auth):
        self.__author = auth

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id
    # @staticmethod
    # def getBookCount():
    #     return Book._count

    def getInfo(self):
        print(
            f"\t* Book name : {self.__name}\n\t* Author name : {self.__author}\n\t* Id no. : {self.__id}")

    def __str__(self):
        return f"\t* Book name : {self.__name}\n\t* Author name : {self.__author}\n\t* Id no. : {self.__id}"


count = 0


class Library:
    __bookList = []
    __borrowedList = []

    def __init__(self):
        pass

    def __str__(self):
        return "This is Library Class"

    def addBook(self, name, author):
        item = Book(name, author)
        global count
        count = count + 1
        item.setId(count)
        self.__bookList.append(item)
        

    def getList(self):
        if len(self.__bookList) == 0:
            print("No books available to borrow!!!\n")
            return
        print("List of books available: ")
        ind = 1
        for item in self.__bookList:
            print('______________________________________________\n')
            print(f"##{ind}")
            ind += 1
            print(item)
        print('______________________________________________\n')
        # print('\n')

    def getBorrowList(self):
        if len(self.__borrowedList) == 0:
            print("No books in the Borrowed list!!!\n")
            return
        print("List of books borrowed: ")
        ind = 1
        for item in self.__borrowedList:
            print('______________________________________________\n')
            print(f"##{ind}")
            ind += 1
            print(item)
            # print('\n')
        print('______________________________________________\n')

    def borrowBook(self, id):
        idFound = False
        for item in self.__bookList:
            # print(item.getId())
            if (item.getId() == id):
                self.__borrowedList.append(item)
                self.__bookList.remove(item)
                idFound = True
                break
        if idFound:
            print(f"Successfully borrowed book with id: {id}")
        else:
            print("ID not found")

    def returnBook(self, id):
        idFound = False
        for item in self.__borrowedList:
            # print(item.getId())
            if (item.getId() == id):
                self.__bookList.append(item)
                self.__borrowedList.remove(item)
                idFound = True
                break
        if idFound:
            print(f"Successfully returned book with id: {id}")
        else:
            print("ID not found")


class Students:
    pass


def main():
    print("WELCOME TO LIBRARY MANAGEMENT SYSTEM")
    print("====================================")
    lib = Library()
    lib.addBook('Alice in Wonderland', 'Lewis Carrol')
    lib.addBook('Animal Farm', 'George Orwell')
    lib.addBook("Ben Hur","Lewis Wallace")
    lib.addBook('Baburnama','Babur')
    lib.addBook('Mein Kampf','Adolf Hitler')
    lib.addBook('Time Machine',' H.G. Wells')
    lib.addBook('Origin of Species', 'Charles Darwin')
    while (True):
        print("       MENU")
        print("********************")
        print("1. Borrow Book")
        print("2. List available books")
        print("3. List of borrowed books")
        print("4. Donate a book")
        print("5. Return Book")
        print("6. Quit")
        try:
            choice = int(input("Enter your choice option number: "))
            print('\n')
        except ValueError:
            print("Please enter a valid option number")
        except Exception:
            print("Error occured. Try again!!")
        else:
            
            if choice == 6:
                print('Thanks for using Library Management System\nVisit Again!')
                break
            elif choice == 1:
                try:
                    id = int(input("Please enter id of the book to borrow: "))
                except ValueError:
                    print("Please enter a valid option number")
                except Exception:
                    print("Error occured. Try again!!")
                else:
                    lib.borrowBook(id)
            elif choice == 2:
                lib.getList()
            elif choice == 3:
                lib.getBorrowList()
            elif choice == 4:
                bookName = input("Enter book name: ")
                bookAuthor = input("Enter book Author: ")
                lib.addBook(bookName,bookAuthor)
                print("Successfully added Book!!!")
            elif choice == 5:
                try:
                    id = int(input("Please enter id of the book to return: "))
                except ValueError:
                    print("Please enter a valid option number")
                except Exception:
                    print("Error occured. Try again!!")
                else:
                    lib.returnBook(id)
            elif choice > 6:
                print("Please enter a valid option number")
            print("**********************************************")

        

if __name__=="__main__":
    main()



