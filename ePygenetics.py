"""
This programme is called ePygenetics. It was designed and built by Callum Chalmers with assistance from Kreshnik Pireva. This code is for extracting the epigenetic status of SNPs from wiggle files and storing the data in a database. For more information see the documentation in the README.md file.
"""

import sys
import os
import glob
import csv
from itertools import islice
from colorama import Fore, Style

def clear_screen(): #clears the screen for aesthetics
    os.system('clear')

def check_database_existance(): #checks if the output database is already present and if not, creates it
    if not os.path.exists("ePygenetics.csv"): #checking for database
        database = open("ePygenetics.csv", "w") #creating database
        database.write("snps" + '\n') #adding column label to new database
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
    print("1. Add a cell line (load a file)")
    print("2. Add a SNP")
    print("3. Help")
    print("4. Exit")
    print() #for aesthetics

""" print("3. Check the database")
 
    print() #blank line for aesthetics """

def get_user_input_welcome(): #function which asks the user which menu option they would like to execute
    user_input = input("What would like to do?: ")
    print() #blank line for aesthetics
    user_input = user_input.strip()
    expected_inputs = ["1","2","3","4"] #expected inputs from the welcome function
    proceed = check_user_input(expected_inputs, user_input)
    proceed_with_chosen_path(proceed)

def proceed_with_chosen_path(user_input): #directs the user to the relevant function based on their input
    if user_input == "2": #allows user to add a snp
        add_a_snp()    
    elif user_input == 0: #allows user to reinput a valid character
        clear_screen()
        print(Fore.RED + "Invalid character entered") #prints in red
        print(Style.RESET_ALL) #back to white
        get_user_input_welcome()
    elif user_input == "1": #allows user to add a cell line
        add_a_cell_line()
    elif user_input == "3": #runs help
        run_help()
    else: #exits the programme
        quit()
 

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
    chromosome = check_user_input(["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","X","M", "Y"], chromosome) #ensures chromosome entry is valid
    if chromosome == 0:
        input(Fore.RED + "Invalid chromosome entered, only numbers 1-23 are valid, press enter to continue: ") #makes sure user enters a valid chromosome, message in red
        print(Style.RESET_ALL) #resets to white
        add_a_snp()
    snp = input("Enter SNP position: ") #gets user input for SNP position
    snp = snp.strip()
    if snp == "0": #allows user to return if they got here by accident
        return_to_menu()
    else:
        return chromosome, snp

def check_snp_in_database(chromosome, snp): #function which checks that SNP is not already in output database
    finder = 0
    with open("ePygenetics.csv", "r") as f:
        for line in f: #goes through the file line by line
            finder = line.find("chr" + chromosome + "-" + snp + "*" + ",") #looks for snp in each line
            if finder != -1: #if snp is found
                duplicate_snp() #notifies the user the snp is already in the database
        if finder == -1: #if the SNP is not present
            add_snp_database("chr" + chromosome + "-" + snp + "*" + "," + '\n') #adds the snp to the database
	
def duplicate_snp(): #tells the user they entered a SNP already in the database
    clear_screen()
    print(Fore.RED + "SNP already entered")  #prints in red to get user attention
    print(Style.RESET_ALL) #resets to white
    print() #blank line for aesthetics
    user_input = input("Would like to add a different SNP?, enter 1 for yes, 2 to return to the main menu or 3 to exit the programme: ") #gets user input
    user_input = user_input.strip()
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
    database.write(snp_code) #adds new row to the database with the snp code as the label
    database.close()

def update_snp_database(chromosome, snp): #updates the database for the snp that was added
    cell_line_list = generate_cell_line_list() #makes a list of all the cell lines that are in the database
    file_list = generate_cell_line_file_list(cell_line_list) #makes sure the cell line files are opened in the right order
    for file in file_list: #for the cell line files
        append_snp(chromosome, snp, file) #look for the SNP contig value and add it to the database
    snp_added() #passes the user to a function which asks how they want to proceed

def generate_cell_line_list(): #makes a list of all the cell lines that are in the database
    database = open("ePygenetics.csv", "r")
    cell_line_list = database.readline() #reads top row
    end = cell_line_list.find("\n")
    cell_line_list = cell_line_list[:end] #removes new line character
    cell_line_list = cell_line_list.split(",") #splits into list of cell lines
    cell_line_list.pop(0) #removes snp column label
    database.close()
    return cell_line_list

def generate_cell_line_file_list(cell_line_list):#makes sure the cell line files required are opened in the right order 
    file_list = glob.glob('*.wig') #selects all the wig files in the current working directory
    sorted_cell_line_file_list = []
    for element in file_list:
        end_of_cell_line = element.find("-") #finds the dash in the file
        cell_line = element[:end_of_cell_line] #slices till the dash which is the cell line name
        order = cell_line_list.index(cell_line) if cell_line in cell_line_list else None#uses cell line name to determine if cell line is loaded in the database
        if order == None: #If the cell line is not loaded in the database
            pass #do nothing
        elif order > len(sorted_cell_line_file_list): #If the cell line is in a column greater than the length of the list
            sorted_cell_line_file_list.append(element) #Add it to the list
        else: #If the cell line is in a column less than the length of the list
            sorted_cell_line_file_list.insert(order, element) #Add it in the right position

def append_snp(chromosome, snp, file):
    contigs = find_snp(chromosome, snp, file) #searchs the file for the right value
    input_database = open("ePygenetics.csv", "r")
    data = input_database.read()
    data = data.split('\n')
    for element in data:
        data += '\n'
    end = element.find("\n")
    element = element[:end]
    element += (contigs + ',')
    database.close()
    output_database = open("ePygenetics.csv", "r")
    output_database.writelines(data)
    output_database.close()

def find_snp(chromosome, snp, file):#"""finds the SNP within the wig file and returns the contigs value"""
    snp_position = int(snp)
    snp_position_rounded = ((snp_position // 1000) * 1000) + 1 #works out what block the data is in
    if ((snp_position % 1000) == 0): #ensures that multiples of 1000 are found on the right line
        snp_position_rounded = snp_position - 999
    snp_position_rounded = "start=" + str(snp_position_rounded) + " "
    chromosome_string = "chrom=chr" + chromosome + " "
    iterations = ((snp_position % 1000) // 20) #works out what line the correct value is on
    if (snp_position % 20) != 0:
        iterations += 1
    if ((snp_position % 1000) == 0):
        iterations = 49
    chromosome_pos = -1 #initialises variable
    snp_pos = -1 #initialises variable
    with open(file) as f: 
        next(f) #skips first line
        for line in f: #goes through the file line by line
            chromosome_pos = line.find(chromosome_string) #finds right block
            snp_pos = line.find(snp_position_rounded) #finds right block
            if chromosome_pos != -1 and snp_pos != -1: #in right block   
                consume(f, (iterations-1)) #move to right line
                return next(f).strip() #return i
            if line[0] == "f":
                consume(f, 50)
            else:
                consume(f, 1)
  
                 #skip to next block
        return "NaN" #if not in then return Not a number

def snp_added(): #asks user what they want to do next
    print()
    print("SNP added")
    print()
    print("What do you want to do next?")
    print()
    user_input = input("Enter 1 to add another SNP, 2 to return to main menu or 3 to exit: ")
    user_input = user_input.strip()
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

def add_a_cell_line(): #allows user to load a file into the programme
    clear_screen() #clears screens for aesthetics
    check_database_existance() #checks if there is already a database
    cell_line = get_cell_line() #gets user input for the cell line
    check_cell_line(cell_line)
    add_cell_line_database(cell_line) #adds a new column to the database for that cell line
    cell_line_added() #asks the user what they would like to do next
    
def get_cell_line(): #asks user to input the name of the cell line they want to add
    print("Enter the cell line name (the characters before the '-' in the file name) or 0 to return to the main menu")
    print() #blank line for aesthetics
    cell_line = input("Enter cell line name: ") #gets user input
    cell_line = cell_line.strip() #cleans input
    if cell_line == "0": #allows user to return if they got here by accident
        return_to_menu()
    else:
        return cell_line #returns input

def check_cell_line(cell_line):
    database = open("ePygenetics.csv", "r")
    cell_line_list = database.readline() #reads top row
    end = cell_line_list.find("\n")
    cell_line_list = cell_line_list[:end]
    cell_line_list = cell_line_list.split(",") #splits into list of cell lines
    cell_line_list.pop(0) #removes snp column label
    database.close()
    file_list = glob.glob('*.wig')
    cell_line_file_list = []
    for element in file_list:
        end_of_cell_line = element.find("-") #finds the dash in the file
        cell_line_file = element[:end_of_cell_line] #slices till the dash which is the cell line name
        cell_line_file_list.append(cell_line_file)
    if cell_line not in cell_line_file_list:
        cell_line_not_added()
    elif cell_line in cell_line_list:
        duplicate_cell_line()


def cell_line_not_added():
    clear_screen()
    print(Fore.RED + "Cell line file not in folder")  #prints in red to get user attention
    print(Style.RESET_ALL) #resets to white
    print()
    print("Please move the .wig file corresponding to the cell line you wish to add into the current working directory in the format [cell line]-*.wig")
    print()
    input("Once this is complete press enter to continue")
    add_a_cell_line()

def duplicate_cell_line(): #tells the user they entered a cell line already in the database
    clear_screen()
    print(Fore.RED + "Cell line already entered")  #prints in red to get user attention
    print(Style.RESET_ALL) #resets to white
    print() #blank line for aesthetics
    user_input = input("Would like to add a different cell line?, enter 1 for yes, 2 to return to the main menu or 3 to exit the programme: ") #gets user input
    user_input = user_input.strip()
    expected_inputs = ["1","2","3"] #expected inputs
    proceed = check_user_input(expected_inputs, user_input)
    proceed_with_chosen_path4(proceed)
    
def proceed_with_chosen_path4(user_input):
    if user_input == "1": #allows user to enter another snp
        add_a_cell_line()
    elif user_input == "2": #allows user to return to menu
        return_to_menu()
    elif user_input == 0:
        print(Fore.RED + "Invalid character added")  #prints in red to get user attention
        print(Style.RESET_ALL) #reset to white
        snp_added() #allows user to enter a valid input
    else:
        quit()	

def add_cell_line_database(cell_line): #adds cell line to database
    input_database = open('ePygenetics.csv', 'r') #opens database
    data = input_database.read() #stores database
    data = data.split('\n')
    for num in range(len(data)):
        if data[num] == "":
            data.pop(num)
    columns_list = data[0] #stores first line
    columns_list += (',' + cell_line + '\n') #adds cell line from user input to first line
    data[0] = columns_list #replaces first line
    filename = [cell_line]
    full_filename = generate_cell_line_file_list(filename)
    print(full_filename)
    full_filename = full_filename[0]
    print(full_filename)
    for num in range(1, len(data)):
        line = data[num]
        print(line)
        split = line.find("-")
        split1 = line.find("*")
        chromosome = line[3:split]
        snp = line[split+1:split1]
        print(chromosome)
        print(snp)
        contigs = find_snp(chromosome, snp, full_filename)
        line += (contigs + ",")  
        if num == len(data):
            end = line.find("\n")
            line = line[:end]
        data[num] = line + '\n'
    input_database.close()
    output_database = open('ePygenetics.csv', 'w')
    output_database.writelines(data) #writes to database
    output_database.close() 

def cell_line_added(): #asks user what they want to do next
    print()
    print("Cell line added")
    print()
    print("What do you want to do next?")
    print()
    user_input = input("Enter 1 to add another cell line, 2 to return to main menu or 3 to exit: ")
    user_input = user_input.strip()
    expected_inputs = ["1", "2", "3"]
    proceed = check_user_input(expected_inputs, user_input) #checks user input is as expected
    proceed_with_chosen_path4(proceed)

def proceed_with_chosen_path4(user_input):
    if user_input == "1": #allows user to enter another cell line
        add_a_cell_line()
    elif user_input == "2": #allows user to return to menu
        return_to_menu()
    elif user_input == 0:
        print(Fore.RED + "Invalid character added")  #prints in red to get user attention
        print(Style.RESET_ALL) #reset to white
        cell_line_added() #allows user to enter a valid input
    else:
        quit()  
    
def run_help():
    clear_screen() #for aesthetics
    print()
    print("1. Add a SNP") #help statements
    print()
    print("This function allows you to add a SNP to the database so that its status can be analysed in all the currently loaded cell lines")
    print()
    print("2. Add a cell line")
    print()
    print("This function allows you add a cell line to the database so that the status of all its SNPs can be analysed")
    print()
#    print("3. Check the database")
#    print()
#    print("This function allows you to view data that has already been loaded")
#    print()
    input("Press enter to continue")
    print()
    return_to_menu()	
	

def main():
    welcome_to_ePygenetics()
    get_user_input_welcome()


