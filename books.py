# import doctest
import pandas
import json
from typing import Union
from time import sleep


class Book:
    """
    This class represents a Book.
    """

    def __init__(self, author: str, title: str, publisher: str, shelf: Union[int, str], category: str, subject: str):
        """Create an instance of the Book class.

        :param author: a string
        :param title: a string
        :param publisher: a string
        :param shelf: an integer or string
        :param category: a string
        :param subject: a string

        >>> my_book = Book('Author One', 'Book One', 'Publisher One', 1, 'Category One', 'Subject One')
        >>> my_book.author
        'Author One'
        >>> my_book.title
        'Book One'
        >>> my_book.publisher
        'Publisher One'
        >>> my_book.shelf
        1
        >>> my_book.category
        'Category One'
        >>> my_book.subject
        'Subject One'
        """
        self.author = author
        self.title = title
        self.publisher = publisher
        self.shelf = shelf
        self.category = category
        self.subject = subject

    def __repr__(self) -> str:
        """Provide the information stored in each attribute of this Book object.

        :return: a string

        >>> my_book = Book('Author One', 'Book One', 'Publisher One', '1', 'Category One', 'Subject One')
        >>> my_book.__repr__()
        "Book('Author One', 'Book One', 'Publisher One', '1', 'Category One', 'Subject One')"
        """
        return f"Book('{self.author}', '{self.title}', '{self.publisher}', '{self.shelf}', '{self.category}', " \
               f"'{self.subject}')"

    def __str__(self) -> str:
        """Provide an informal description of this Book object with the attributes currently stored.

        :return: a string

        >>> my_book = Book('Author One', 'Book One', 'Publisher One', '1', 'Category One', 'Subject One')
        >>> my_book.__str__()
        "This book is named 'Book One', written by 'Author One', published by 'Publisher One', category of \
'Category One', subject of 'Subject One', and currently sits on shelf: 1."
        """
        return f"This book is named '{self.title}', written by '{self.author}', published by '{self.publisher}', " \
               f"category of '{self.category}', subject of '{self.subject}', and currently sits on shelf: {self.shelf}."


def get_json_data() -> list:
    """Open or create a 'somebooks.json' file with the contents of the 'somebooks.xlsx' file.

    :precondition: 'somebooks.xlsx' must be located in current directory
    :precondition: 'somebooks.xlsx' must have Author, Title, Publisher, Shelf, Category, Subject columns
    :postcondition: opens/creates 'somebooks.json' and returns a list of Book objects for each book in 'somebooks.xlsx'
    :return: a list of Book objects
    """
    try:
        with open('somebooks.json', 'r') as file_object:
            content = json.load(file_object)
    except FileNotFoundError:
        excel_data = pandas.read_excel('somebooks.xlsx')
        converted = excel_data.to_json(orient='records')
        with open('somebooks.json', 'w+') as file_object:
            file_object.write(converted)
        with open('somebooks.json', 'r') as file_object:
            content = json.load(file_object)
    else:
        print('Library is ready to load.')
    finally:
        return create_book_objects(content)


def create_book_objects(content):
    """Create a Book object for each dictionary in the content list.

    :param content: a list of dictionaries in JSON format
    :precondition: content must be a list of dictionaries
    :precondition: each dictionary in content must have Author, Title, Publisher, Shelf, Category, and Subject keys
    :postcondition: create a Book object for each dictionary in content and return them all in one list
    :return: a list which stores each Book object that was created

    >>> create_book_objects([{'Author': 'Auth1', 'Title': 'Book1', 'Publisher': 'Publish1', 'Shelf': '1', \
'Category': 'Category1', 'Subject': 'Subject1'}, {'Author': 'Auth2', 'Title': 'Book2', \
'Publisher': 'Publish2', 'Shelf': '2', 'Category': 'Category2', 'Subject': 'Subject2'}])
    Your Library has been loaded.
    [Book('Auth1', 'Book1', 'Publish1', '1', 'Category1', 'Subject1'), Book('Auth2', 'Book2', 'Publish2', \
'2', 'Category2', 'Subject2')]
    """
    library = []
    for book in content:
        library.append(Book(book['Author'], book['Title'], book['Publisher'], book['Shelf'], book['Category'],
                            book['Subject']))
    print('Your Library has been loaded.')
    return library


def get_user_choice(options: list, prompt: str) -> str:
    """Ask user to choose an option out of the given options.

    :param options: a list
    :param prompt: a string
    :precondition: options must be a list of strings
    :precondition: options must have a length equal to or greater than 1
    :precondition: prompt must be a string
    :postcondition: gets the user's choice of one of the valid options given
    :return: a string of the user's input
    """
    choice = False
    while not validate_user_choice(choice, options):
        print(prompt)
        for num, option in enumerate(options, 1):
            print(f"{num} - {option}")
        choice = input('\nPlease enter the number corresponding to your choice here: ')
    return choice


def validate_user_choice(choice: str, options: list) -> bool:
    """Evaluate whether choice is a valid option from given options.

    :param choice: a string
    :param options: a list
    :precondition: options must be a list of strings
    :precondition: options must have a length equal to or greater than 1
    :precondition: choice must be a string
    :postcondition: returns True if choice is a valid choice from options else False
    :return: True or False

    >>> validate_user_choice('0', ['Author', 'Title'])
    False
    >>> validate_user_choice('1', ['Author', 'Title'])
    True
    >>> validate_user_choice('one', ['Author', 'Title'])
    False
    """
    return True if choice in [f'{num}' for num, option in enumerate(options, 1)] else False


def book_search(library: list) -> None:
    """Search for books in the library by user's choice of search options and input.

    :param library: a list of Book objects
    :precondition: library must be a list of Book objects
    :precondition: library must have a length equal to or greater than 1
    :postcondition: displays the correct results from the user's search
    :return: None
    """
    options = ['Author', 'Title', 'Publisher', 'Shelf', 'Category', 'Subject']
    prompt = '\nWhat option would you like to search by?'
    choice = get_user_choice(options, prompt)
    if choice == '1':
        search_by_chosen_option(library, options[0])
    elif choice == '2':
        search_by_chosen_option(library, options[1])
    elif choice == '3':
        search_by_chosen_option(library, options[2])
    elif choice == '4':
        search_by_shelf(library)
    elif choice == '5':
        search_by_chosen_option(library, options[4])
    elif choice == '6':
        search_by_chosen_option(library, options[5])


def search_by_shelf(library: list) -> None:
    """Search for books in the library by shelf value and user's input.

    :param library: a list of Book objects
    :precondition: library must be a list of Book objects
    :precondition: library must have a length equal to or greater than 1
    :postcondition: displays the correct results from the user's search
    :return: None
    """
    user_input = input(f'What is the number/name of the shelf you want to search for?')
    found_books = []
    for book in library:
        if user_input.lower() == str(getattr(book, 'shelf')).lower():
            found_books.append(book)
    print(f'We found {len(found_books)} book(s) that matched this search in your library.\n')
    for num, book in enumerate(found_books, 1):
        print(f'{num} - {book.__repr__()}')
    if len(found_books) > 0 and not return_to_main_menu():
        move_book(library, found_books)


def search_by_chosen_option(library: list, chosen_option: str) -> None:
    """Search for books in the library by the chosen_option and user's input.

    :param library: a list of Book objects
    :param chosen_option: a string
    :precondition: library must be a list of Book objects
    :precondition: library must have a length equal to or greater than 1
    :precondition: chosen_option must be a string
    :precondition: chosen_option must be a valid attribute of the Book object
    :postcondition: displays the correct results from the user's search
    :return: None
    """
    user_input = input(f'What is the name of the {chosen_option} you want to search for?')
    found_books = []
    for book in library:
        if user_input.lower() in str(getattr(book, chosen_option.lower())).lower():
            found_books.append(book)
    print(f'We found {len(found_books)} book(s) that matched this search in your library.\n')
    for num, book in enumerate(found_books, 1):
        print(f'{num} - {book.__repr__()}')
    if len(found_books) > 0 and not return_to_main_menu():
        move_book(library, found_books)


def return_to_main_menu() -> bool:
    """Determine if user wants to return to main menu.

    :return: True or False
    """
    choice = get_user_choice(['Return to main menu', 'Move a book to another shelf'],
                             '\nWould you like to return to the main menu or move a book?')
    return True if choice == '1' else False


def move_book(library: list, found_books: list) -> None:
    """Change value of user's chosen book's shelf attribute to value desired by user.

    :param library: a list
    :param found_books: a list
    :precondition: library and books must be a list of Book objects
    :precondition: library and books must have a length equal to or greater than 1
    :postcondition: change user's chosen book's shelf value to user's desired value
    :return: None
    """
    book_to_move = get_user_choice(found_books, '\nWhich book would you like to move?')
    destination_shelf = input('\nWhat shelf would you like to move this book to?')
    for book in library:
        if book == found_books[int(book_to_move) - 1]:
            book.shelf = destination_shelf
    print(f"Success! {found_books[int(book_to_move) - 1].title} has been moved to shelf '{destination_shelf}'.")


def convert_library_to_json(library: list) -> list:
    """Convert contents of library to JSON format.

    :param library: a list
    :precondition: library and books must be a list of Book objects
    :precondition: library and books must have a length equal to or greater than 1
    :postcondition: converts each Book object in library to a dictionary and returns those dictionaries in a list
    :return: a list of dictionaries

    >>> my_library = [Book('Author One', 'Book One', 'Publisher One', '1', 'Category One', 'Subject One'), \
Book('Author Two', 'Book Two', 'Publisher Two', '2', 'Category Two', 'Subject Two')]
    >>> convert_library_to_json(my_library)
    [{'Author': 'Author One', 'Title': 'Book One', 'Publisher': 'Publisher One', 'Shelf': '1', 'Category': \
'Category One', 'Subject': 'Subject One'}, {'Author': 'Author Two', 'Title': 'Book Two', 'Publisher': \
'Publisher Two', 'Shelf': '2', 'Category': 'Category Two', 'Subject': 'Subject Two'}]
    """
    books_to_save = []
    for book in library:
        book_dict = book.__dict__
        books_to_save.append(dict((key.title(), value) for key, value in book_dict.items()))
    return books_to_save


def save_to_json(library: list, json_file_name) -> None:
    """Write JSON formatted contents of library to 'somebooks.json'.

    :param library: a list
    :param json_file_name: a string
    :precondition: library and books must be a list of Book objects
    :precondition: library and books must have a length equal to or greater than 1
    :precondition: json_file_name must be a string of 'somebooks.json'
    :postcondition: overwrites the contents of 'somebooks.json' with the JSON formatted contents of library
    :return: None
    """
    contents = convert_library_to_json(library)
    with open(json_file_name, 'w') as file_object:
        json.dump(contents, file_object)


def library_organizer() -> None:
    """Act as user interface for user to search or move books within their library.

    :return: None
    """
    print("Hidey-ho, book lover! Welcome to Brian's Totally Tubular Library Organizer!"
          "\nPlease wait while we load your book library...")
    library = get_json_data()
    keep_reading = False
    while not keep_reading:
        choice = get_user_choice(['Search for a book', 'Move a book to another shelf', 'Save and Exit'],
                                 '\nWhat would you like to do within your library?')
        if choice == '1':
            book_search(library)
        elif choice == '2':
            print("Let's find you a book to move!")
            sleep(1.5)
            book_search(library)
        elif choice == '3':
            keep_reading = True
            save_to_json(library, 'somebooks.json')
            print("\nYour library has been saved successfully."
                  "\nThank you for using Brian's Totally Tubular Library Organizer! Come again soon!")


def main():
    # doctest.testmod(verbose=True)
    library_organizer()


if __name__ == '__main__':
    main()
