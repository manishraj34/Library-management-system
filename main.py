from crud import add_book

def main():
    print("************************")
    print("1. Add Book")
    print("2. View Book")
    print("************************")
    choice=input("Enter Your choice")

    if choice=='1':
        addNew
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        isbn = input("Enter book ISBN: ")
        count = int(input("Enter number of copies: "))
        add_book(title, author, isbn, count)
        print("> New Book added")
    
    elif choice==2:
        print("Code for View Book")


if __name__=="__main__":
    main()