# Create and define the Author class
class Author:
    def __init__(self, name):
        self.name = name
        self.books = set()

    # Define mthods that the Author class can perform
    # This method adds a book title to the Author's published books list
    def publish(self, title):
        # Count the number of books before trying to add another
        starting_book_count = len(self.books)
        
        # Add the title to the list
        self.books.add(title)

        # Get the new length of the set and compare it to the starting value
        end_book_count = len(self.books)

        # Compare the starting book list length to the end
        # If the lengths are the same, let the user know that it has already been published
        if starting_book_count == end_book_count:
            print(f'{title} has already been published.')

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