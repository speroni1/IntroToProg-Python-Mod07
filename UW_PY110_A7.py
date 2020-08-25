# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# James Roefs, 2020-08-24 ,Modified code to complete assignment 7
# ---------------------------------------------------------------------------- #

import pickle

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
strBinFileName = "ToDoFile.dat" # The name of the binary data file
objFile = None   # An object that represents a file
binObjFile = None # An object that represents a binary file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        try:
            file = open(file_name, "r")
            for line in file:
                task, priority = line.split(",")
                row = {"Task": task.strip(), "Priority": priority.strip()}
                list_of_rows.append(row)
            file.close()
            return list_of_rows, 'Success'
        except FileNotFoundError as e:
            print("Invalid filename, file must exist before running this script!")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep = '\n')
            return list_of_rows, 'Fail'
        except Exception as e:
            print("Invalid filename, file must exist before running this script!")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
            return list_of_rows, 'Fail'

    @staticmethod
    def read_bin_data_from_file(bin_file_name, list_of_rows):
        try:
            binObjFile = open(bin_file_name, 'rb')
            list_of_rows = pickle.load(binObjFile)
            binObjFile.close()
            return list_of_rows, 'Success'
        except FileNotFoundError as e:
            print("Invalid filename, file must exist before running this script!")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep = '\n')
            return list_of_rows, 'Fail'
        except Exception as e:
            print("Invalid filename, file must exist before running this script!")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
            return list_of_rows, 'Fail'


    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        row={"Task":task,"Priority":priority}
        list_of_rows.append(row);
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        row_remove = {}
        for row in list_of_rows:
            if (row["Task"] ==task):
                row_remove = row

        list_of_rows.remove(row_remove)
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        objFile = open(file_name,"w")
        for row in list_of_rows:
            objFile.write(row["Task"]+","+row["Priority"]+"\n")
        objFile.close()
        return list_of_rows, 'Success'

    @staticmethod
    def pickle_data(bin_file_name, list_of_rows):
        binObjFile = open(bin_file_name,'ab' )
        pickle.dump(list_of_rows,binObjFile)
        binObjFile.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        6) Save Data as Binary
        7) Load Data from Binary
        8) Intentionally load a file that doesn't exist to test the exception
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 8] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        task = input("Enter a task: ")
        priority = input("Enter the task priority: ")
        return task, priority

    @staticmethod
    def input_task_to_remove():
        task = input("Enter a task to be removed: ")
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        strTask, strPriority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(strTask,strPriority,lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        strTask = IO.input_task_to_remove()
        lstTable, strResult = Processor.remove_data_from_list(strTask,lstTable)
        print(strResult)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstTable, strResult = Processor.write_data_to_file(strFileName,lstTable)
            print(strResult)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable, strResult = Processor.read_data_from_file(strFileName,lstTable)
            print(strResult)
            IO.input_press_to_continue(strStatus)

        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #  Exit Program
        print("Goodbye!")
        break   # and Exit

    elif strChoice == '6': #Pickle the File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            lstTable, strResult = Processor.pickle_data(strBinFileName,lstTable)
            print(strResult)
            IO.input_press_to_continue(strStatus)

    elif strChoice == '7': #Load Binary File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable, strResult = Processor.read_bin_data_from_file(strBinFileName,lstTable)
            print(strResult)
            IO.input_press_to_continue(strStatus)

        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue # to show the menu

    elif strChoice == '8': #Load a non-existant file
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            lstTable, strResult = Processor.read_bin_data_from_file('nope.dat',lstTable)
            print(strResult)
            IO.input_press_to_continue(strStatus)

        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue # to show the menu



