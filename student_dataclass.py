# Import the dataclass module
from dataclasses import dataclass

# Define the dataclass
@dataclass
class Student:
    # Set the class attributes
    name: str
    school_id: str
    gpa: float

    # Define the method that prints the class's information
    def __str__(self):
        return f'Student name: {self.name}, ID: {self.school_id}, GPA: {self.gpa}'

# Define the main function
def main():

    # Set up some example classes
    alex = Student('Alex', 'abcdef', 3.8)
    print(alex.name)
    print(alex.school_id)
    print(alex)

    sam = Student('Sam', 'qwerty', 3.5)
    print(sam)

# Call the main function
if __name__ == '__main__':
    main()