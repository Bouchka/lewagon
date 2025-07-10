"""
This module defines the EngStudent class, which represents a student in the Data
Engineering course at Le Wagon.

Classes
-------
EngStudent
    A class representing a student with attributes for name and age, and
    methods for speaking and creating instances based on birth year.
"""

from datetime import date
from typing_extensions import Self


class EngStudent:
    """
    A class to represent an engineering student.

    Attributes
    ----------
    language : str
        The class' language.

    Methods
    -------
    __init__(name, age):
        Initializes the EngStudent instance with name and age.
    says(quote):
        Returns a string with the student's name and the given quote.
    from_birth_year(name, birth_year):
        Class method to create an EngStudent instance using the birth year to
        calculate age.
    """

    language = "Python"

    def __init__(self, name, age):
        """
        Initializes a new instance of the class.
        Parameters
        ----------
        name : str
            The name of the student.
        age : int
            The age of the student.
        """
        self.name = name.capitalize()
        self.age = age

    def says(self, quote):
        """
        Returns a formatted string with the student's name and the given quote.

        Parameters
        ----------
        quote : str
            The quote that the student says.

        Returns
        -------
        str
            A string in the format "{name} says: {quote}".
        """
        return f"{self.name} says: {quote}"

    @classmethod
    def from_birth_year(cls, name: str, birth_year: int | str) -> Self:
        """
        Create an instance of the class using the birth year.

        Parameters
        ----------
        cls : type
            The class itself.
        name : str
            The name of the student.
        birth_year : int
            The birth year of the student.

        Returns
        -------
        object
            An instance of the class with the calculated age.
        """
        birth_year = int(birth_year)
        age = date.today().year - birth_year
        return cls(name=name, age=age)



# Remember: first we need to add simple prints to check that th code beahves
# But say if we added a print() to check while writing in VS code
# But someone imported the function in notebook ... 
# THe print() might run accidentally on the python notebook and cause errors
# Hence - we use if __name__ == "__main__": block still check that the code behaves properly
# but in a clear way
# This runs only with python school/engstudent.py
# Tests are for correctness (require pylint, separate files ...)
# This is different: it's for demonstrating behavior 
# # or printing something out manually for debugging - in a clean way.
if __name__ == "__main__":  # Runs this block only if script is executed directly (python school/student.py)
    paul = EngStudent("paul", 34)  # Creates a student named Paul, age 34
    print(paul.name)  # Prints capitalized name
    print(paul.age)  # Prints age
    print(paul.language)  # Prints class language attribute
    print(paul.says("I was a student of batch 1769!"))  # Prints a custom message
    paul = EngStudent.from_birth_year("paul", "2000")  # Creates a new student with age from birth year
