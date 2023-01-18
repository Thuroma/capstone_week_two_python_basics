# Create and define the Author class
class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    # Define mthods that the Author class can perform
    # This method adds a book title to the Author's published books list
    def publish(self, title):
        for book in self.books:
            if book == title:
                print(f'{title} has already been published')
                return

        self.books.append(title)

    # This method prints a formatted string with the Author's name and published book list
    def __str__(self):
        book_list = ', '.join(self.books) or 'no books'
        return f'{self.name} has published {book_list}'

# Define the main function
def main():
    # Create Authors and "publish" their books
    shakespeare = Author('William Shakespeare')
    shakespeare.publish('Hamlet')
    shakespeare.publish('Richard III')
    print(shakespeare)

    thurman = Author('Thurman')
    thurman.publish('My First Book')
    thurman.publish('The Sequal')
    thurman.publish('The Sequal')
    print(thurman)

# Call the main function
if __name__ == '__main__':
    main()