"""
"""

import sys
import os
import glob
from itertools import islice
from colorama import Fore, Style

def clear_screen(): #clears the screen for aesthetics
    os.system('clear')

def check_database_existance(): #checks if the output database is already present and if not, creates it
    if not os.path.exists("ePygenetics.csv"): #checking for database
        database = open("ePygenetics.csv", "w") #creating database
        database.write("snps,") #adding column label to new database
        database.close()

def check_user_input(expected_inputs, user_input): #takes user input and compares it to a #set of expected inputs to ensure the programme runs correctly
    if user_input not in expected_inputs:
        clear_screen()
        print(Fore.RED + "Illegal character entered") #prints in red to get user attention
        print(Style.RESET_ALL) #resets to white
        return 0
    else:
        return user_input

def return_to_menu(): #returns the user to the main menu
        clear_screen()
        welcome_to_ePygenetics()
        get_user_input_welcome()

def consume(iterator, n): #Advance the iterator n-steps ahead, downloaded from stack overflow
    if n is None: #skip to the end
        collections.deque(iterator, maxlen=0)
    else: #skip n steps in iterator
        next(islice(iterator, n, n), None)

def welcome_to_ePygenetics(): #welcome function that prints the menu of the programme
    clear_screen()
    print("Welcome to ePygenetics")
    print("1. Add a SNP")
    print("2. Exit")
    print() #for aesthetics
""" print("2. Add a cell line")
    print("3. Check the database")
    print("4. Help")
 
    print() #blank line for aesthetics """

def get_user_input_welcome(): #function which asks the user which menu option they would like to execute
    user_input = input("What would like to do?: ")
    print() #blank line for aesthetics
    user_input = user_input.strip()
    expected_inputs = ["1","2"] #expected inputs from the welcome function
    proceed = check_user_input(expected_inputs, user_input)
    proceed_with_chosen_path(proceed)

def proceed_with_chosen_path(user_input): #directs the user to the relevant function based on their input
    if user_input == "1":
        add_a_snp()    
    elif user_input == 0: #allows user to reinput a valid character
        clear_screen()
        print(Fore.RED + "Invalid character entered") #prints in red
        print(Style.RESET_ALL) #back to white
        get_user_input_welcome()
    else: #exits the programme
        quit()

""" elif user_input == "2":
        add_a_cell_line()
    elif user_input == "3":
        check_database()
    elif user_input == "4":
        run_help() """
 

def add_a_snp():
    clear_screen() #clears screens for aesthetics
    check_database_existance() #checks if there is already a database
    chromosome, snp = get_snp() #gets user input
    check_snp_in_database(chromosome, snp) #checks that SNP is not already in output database and if not adds it
    update_snp_database(chromosome, snp) #updates the database for the added snp

def get_snp(): #function which gets the SNP data from the user and returns a tuple of this data
    print("Enter the chromosome and position of the SNP you wish to add or enter 0 to return to the main menu")
    print() #blank line for aesthetics
    chromosome = input("Enter chromosome number: ")
    chromosome = chromosome.strip()
    if chromosome == "0": #allows user to return if they got here by accident
        return_to_menu()
    chromosome = check_user_input(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"], chromosome) #ensures chromosome entry is valid
    if chromosome == 0:
        input(Fore.RED + "Invalid chromosome entered, only numbers 1-23 are valid, press enter to continue: ") #makes sure user enters a valid chromosome, message in red
        print(Style.RESET_ALL) #resets to white
        add_a_snp()
    snp = input("Enter SNP position: ")
    snp = snp.strip()
    if snp == "0": #allows user to return if they got here by accident
        return_to_menu()
    else:
        return chromosome, snp

def check_snp_in_database(chromosome, snp): #function which checks that SNP is not already in output database
    finder = 0
    with open("ePygenetics.csv", "r") as f:
        for line in f: #goes through the file line by line
            finder = line.find("chr" + chromosome + "-" + snp + "*") #looks for snp in each line
            if finder != -1: #if snp is found
                duplicate_snp() #notifies the user the snp is already in the database
        if finder == -1: #if the SNP is not present
            add_snp_database("chr" + chromosome + "-" + snp + "*") #adds the snp to the database
	
def duplicate_snp(): #tells the user they entered a SNP already in the database
    clear_screen()
    print(Fore.RED + "SNP already entered")  #prints in red to get user attention
    print(Style.RESET_ALL) #resets to white
    print() #blank line for aesthetics
    user_input = input("Would like to add a different SNP?, enter 1 for yes, 2 to return to the main menu or 3 to exit the programme: ") #gets user input
    user_input.strip()
    expected_inputs = ["1","2","3"] #expected inputs
    proceed = check_user_input(expected_inputs, user_input)
    proceed_with_chosen_path2(proceed)

def proceed_with_chosen_path2(user_input):
    if user_input == "1": #allows user to enter another snp
        add_a_snp()
    elif user_input == "2": #allows user to return to menu
        return_to_menu()
    elif user_input == 0:
        duplicate_snp() #allows user to enter a valid input
    else:
        quit()

def add_snp_database(snp_code): #adds snp to database
    database = open("ePygenetics.csv", "a")
    database.write(snp_code + ",") #adds new row to the database with the snp code as the label
    database.close()

def update_snp_database(chromosome, snp): #updates the database for the snp that was added
    cell_line_list = generate_cell_line_list() #makes a list of all the cell lines that are in the database
    file_list = generate_cell_line_file_list(cell_line_list) #makes sure the cell line files are opened in the right order
    for file in file_list: #for the cell line files
        append_snp(chromosome, snp, file) #look for the SNP contig value and add it to the database

def generate_cell_line_list(): #makes a list of all the cell lines that are in the database
    database = open("ePygenetics.csv", "r")
    cell_line_list = database.readline() #reads top row
    end = cell_line_list.find("\n")
    cell_line_list = cell_line_list[:end] #removes new line character
    cell_line_list = cell_line_list.split(",") #splits into list of cell lines
    cell_line_list.pop(0) #removes snp column label
    database.close()
    if len(cell_line_list) == 0: #checks that a cell line has been added and if not, prompts the user to add a cell line
        no_cell_lines_added() #prompts user to add a cell line
    else:
        return cell_line_list

def generate_cell_line_file_list(cell_line_list):#makes sure the cell line files required are opened in the right order 
    file_list = glob.glob('*.wig') #selects all the wig files in the current working directory
    sorted_cell_line_file_list = []
    for element in file_list:
        end_of_cell_line = element.find("-") #finds the dash in the file
        cell_line = element[:end_of_cell_line] #slices till the dash which is the cell line name
        if cell_line in cell_line_list: #uses cell line name to determine if cell line is loaded in the database
            sorted_cell_line_file_list += [element] #adds the cell lines in order
    return sorted_cell_line_file_list

def no_cell_lines_added(): #prompts the user to add a cell line because none have been loaded
    clear_screen()
    print(Fore.RED + "No cell lines added")  #prints in red to get user attention
    print(Style.RESET_ALL) #resets to white
    print()
    print("Please move a .wig file into the current working directory in the format [cell line]-*.wig")
    print()
    input("Once this is complete press enter to continue")
    print()
    print("Function currently unavailable") #coming soon
    quit()
#    add_cell_line() #passes the user to the the add cell line function

def append_snp(chromosome, snp, file):
    contigs = find_snp(chromosome, snp, file) #searchs the file for the right value
    database = open("ePygenetics.csv", "a")
    database.write(contigs + "," + "\n") #adds value to the row
    database.close()
    snp_added() #passes the user to a function which asks how they want to proceed


def find_snp(chromosome, snp, file):#finds the SNP within the wig file and returns the contigs value
    count = 0
    snp_position = int(snp)
    snp_position_rounded = ((snp_position // 1000) * 1000) + 1 #works out what block the data is in
    snp_position_rounded = "start=" + str(snp_position_rounded) + " "
    iterations = ((snp_position % 1000) // 20) #works out what line the correct value is on
    if iterations == 0: #ensures that multiples of 1000 are found on the right line
        iterations = 50
    chromosome_pos = -1 #initialises variable
    snp_pos = -1 #initialises variable
    with open(file) as f: 
        next(f)
        for line in f: #goes through the file line by line
            chromosome_pos = line.find(chromosome) #finds right block
            snp_pos = line.find(snp_position_rounded) #finds right block
            if chromosome_pos != -1 and snp_pos != -1: #in right block
                consume(f, (iterations-1)) #move to right line
                return next(f).strip() #return it
            consume(f, 50) #skip to next block
        return "NaN" #if not in then return Not a number



def snp_added(): #asks user what they want to do next
    print()
    print("SNP added")
    print()
    print("What do you want to do next?")
    print()
    user_input = input("Enter 1 to add another SNP, 2 to return to main menu or 3 to exit: ")
    user_input.strip()
    expected_inputs = ["1", "2", "3"]
    proceed = check_user_input(expected_inputs, user_input) #checks user input is as expected
    proceed_with_chosen_path3(proceed)
    
def proceed_with_chosen_path3(user_input):
    if user_input == "1": #allows user to enter another snp
        add_a_snp()
    elif user_input == "2": #allows user to return to menu
        return_to_menu()
    elif user_input == 0:
        print(Fore.RED + "Invalid character added")  #prints in red to get user attention
        print(Style.RESET_ALL) #reset to white
        snp_added() #allows user to enter a valid input
    else:
        quit()		
		
def main():
    welcome_to_ePygenetics()
    get_user_input_welcome()

main()


