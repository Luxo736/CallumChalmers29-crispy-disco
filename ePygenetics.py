"""
This programme is called ePygenetics. It was designed and built by Callum Chalmers with assistance from Kreshnik Pireva. This code is for extracting the epigenetic status of SNPs from wiggle files and storing the data in a database. For more information on the programme see the documentation in the README.md file. This programme is licensed under the MIT license. For more information on licensing see the LICENSE.md file.

Copyright (c) 2016 Callum Chalmers
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import sys #import statements
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
        database.close() #closing database

def check_user_input(expected_inputs, user_input): #takes user input and compares it to a set of expected inputs to ensure the programme runs correctly
    if user_input not in expected_inputs: #if user inputs something unexpected
        clear_screen() #clears screen for aesthetics
        print(Fore.RED + "Illegal character entered") #prints warning message in red to get user attention
        print(Style.RESET_ALL) #resets to white
        return 0 #returns a unique character
    else: #if user enters expected input
        return user_input #returns user input

def return_to_menu(): #returns the user to the main menu
        clear_screen() #clears screen for aesthetics
        welcome_to_ePygenetics() #prints welcome message
        get_user_input_welcome() #asks user what they want to do

def consume(iterator, n): #Advance the iterator n-steps ahead, downloaded from stack overflow http://stackoverflow.com/questions/11113803/pythonic-solution-to-drop-n-values-from-an-iterator
    if n is None: #skip to the end
        collections.deque(iterator, maxlen=0)
    else: #skip n steps in iterator
        next(islice(iterator, n, n), None)

def welcome_to_ePygenetics(): #welcome function that prints the menu of the programme
    clear_screen() #clears screen for aesthetics
    print("Welcome to ePygenetics") #print programme options
    print("1. Add a cell line (load a file)")
    print("2. Add a SNP")
    print("3. Help")
    print("4. Exit")
    print() #blank line for aesthetics

def get_user_input_welcome(): #function which asks the user which menu option they would like to execute
    user_input = input("What would like to do?: ") #gets user input
    print() #blank line for aesthetics
    user_input = user_input.strip() #cleans user input
    expected_inputs = ["1","2","3","4"] #expected inputs from the welcome function
    proceed = check_user_input(expected_inputs, user_input) #checks user input
    proceed_with_chosen_path(proceed) #passes user input to function which pipes them to the right function

def proceed_with_chosen_path(user_input): #directs the user to the relevant function based on their input
    if user_input == "2": #allows user to add a snp
        add_a_snp()    
    elif user_input == 0: #allows user to reinput a valid character
        clear_screen() #clears screen for aesthetics
        print(Fore.RED + "Invalid character entered") #prints in red
        print(Style.RESET_ALL) #back to white
        get_user_input_welcome() #asks user to reenter an input
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
    chromosome = input("Enter chromosome number: ") #gets user input
    chromosome = chromosome.strip() #cleans user input
    if chromosome.isalpha(): #if user enters a letter
       chromosome = chromosome.upper() #make sure it is capital
    if chromosome == "0": #allows user to return if they got here by accident
        return_to_menu()
    expected_inputs = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","X","M", "Y"] 
    chromosome = check_user_input(expected_inputs, chromosome) #ensures chromosome entry is valid
    if chromosome == 0: #if user entry is invalid
        input(Fore.RED + "Invalid chromosome entered, only numbers 1-23 and characters X, Y and M are valid, press enter to continue: ") #makes sure user enters a valid chromosome, message in red
        print(Style.RESET_ALL) #resets to white
        add_a_snp() #asks user again
    snp = input("Enter SNP position: ") #gets user input for SNP position
    snp = snp.strip() #cleans user input
    if snp == "0": #allows user to return to menu if they got here by accident
        return_to_menu()
    else:
        return chromosome, snp #returns clean user inputs

def check_snp_in_database(chromosome, snp): #function which checks that SNP is not already in output database
    finder = 0 #initialises variable
    with open("ePygenetics.csv", "r") as f: #opens file
        for line in f: #goes through the file line by line
            finder = line.find("chr" + chromosome + "-" + snp + "*" + ",") #looks for snp in each line
            if finder != -1: #if snp is found
                duplicate_snp() #notifies the user the snp is already in the database
        if finder == -1: #if the SNP is not present
            add_snp_database("chr" + chromosome + "-" + snp + "*" + "," + '\n') #adds the snp to the database
	
def duplicate_snp(): #tells the user they entered a SNP already in the database
    clear_screen() #clears screen for aesthetics
    print(Fore.RED + "SNP already entered")  #prints in red to get user attention
    print(Style.RESET_ALL) #resets to white
    print() #blank line for aesthetics
    user_input = input("Would like to add a different SNP?, enter 1 for yes, 2 to return to the main menu or 3 to exit the programme: ") #gets user input
    user_input = user_input.strip() #cleans user input
    expected_inputs = ["1","2","3"] #expected inputs
    proceed = check_user_input(expected_inputs, user_input) #checks user input
    proceed_with_chosen_path2(proceed) #passes user input to function which pipes them to the right function

def proceed_with_chosen_path2(user_input):
    if user_input == "1": #allows user to enter another snp
        add_a_snp()
    elif user_input == "2": #allows user to return to menu
        return_to_menu()
    elif user_input == 0:
        duplicate_snp() #allows user to enter a valid input
    else: #allows user to exit the programme
        quit()

def add_snp_database(snp_code): #adds snp to database
    database = open("ePygenetics.csv", "a") #opens database
    database.write(snp_code) #adds new row to the database with the snp code as the label
    database.close() #closes database

def update_snp_database(chromosome, snp): #updates the database for the snp that was added
    cell_line_list = generate_cell_line_list() #makes a list of all the cell lines that are in the database
    file_list = generate_cell_line_file_list(cell_line_list) #makes sure the cell line files are opened in the right order
    for file in file_list: #for the cell line files
        append_snp(chromosome, snp, file) #look for the SNP contig value and add it to the database
    snp_added() #passes the user to a function which asks how they want to proceed

def generate_cell_line_list(): #makes a list of all the cell lines that are in the database
    database = open("ePygenetics.csv", "r") #opens database
    cell_line_list = database.readline() #reads top row
    end = cell_line_list.find("\n") #finds new line character
    cell_line_list = cell_line_list[:end] #removes new line character
    cell_line_list = cell_line_list.split(",") #splits into list of cell lines
    cell_line_list.pop(0) #removes snp column label
    database.close() #closes databases
    return cell_line_list #returns list of cell lines

def generate_cell_line_file_list(cell_line_list):#makes sure the cell line files required are opened in the right order 
    file_list = glob.glob('*.wig') #selects all the wig files in the current working directory
    sorted_cell_line_file_list = [] #initialises variable
    for element in file_list: #goes through files
        end_of_cell_line = element.find("-") #finds the dash in the file
        cell_line = element[:end_of_cell_line] #slices till the dash which is the cell line name
        order = cell_line_list.index(cell_line) if cell_line in cell_line_list else None#uses cell line name to determine if cell line is loaded in the database
        if order == None: #If the cell line is not loaded in the database
            pass #do nothing
        else: #If the cell line is loaded
           sorted_cell_line_file_list += [[order, element]] #create a new list with the correct order as a tuple
    sorted_cell_line_file_list.sort() #sort into the correct order
    for num in range(0,len(sorted_cell_line_file_list)): #for all the cell lines
        element = sorted_cell_line_file_list[num]
        element = element[1] #remove the order from the tuple
        sorted_cell_line_file_list[num] = element #reset the list to just the file names in order
    return sorted_cell_line_file_list #return ordered file list

def append_snp(chromosome, snp, file): #adds the snp data to the database
    contigs = find_snp(chromosome, snp, file) #searchs the data file for the snp contig value
    input_database = open("ePygenetics.csv", "r") #opens database
    data = input_database.read() #reads database
    data = data.split('\n') #splits into lines
    for num in range(len(data)): #for lines in database
        if data[num] == "": #if empty
            data.pop(num) #remove line
    for num in range(len(data)):
        if num < (len(data) - 1): #for all but the last element
            data[num] += '\n'#restores new lines
        else: #for the last element
            data[num] += (contigs + ',' + '\n') #appends snp data to line
    input_database.close() #closes database
    output_database = open("ePygenetics.csv", "w") #reopens database for writing
    output_database.writelines(data) #writes changes to database
    output_database.close() #closes database

def find_snp(chromosome, snp, file): #finds the SNP within the wig file and returns the contigs value"""
    snp_position = int(snp) #converts to integer for manipulation
    snp_position_rounded = ((snp_position // 1000) * 1000) + 1 #calculates which block the data is in
    if ((snp_position % 1000) == 0): #ensures that multiples of 1000 are found on the right line
        snp_position_rounded = snp_position - 999
    snp_position_rounded = "start=" + str(snp_position_rounded) + " " #converts to string for searching
    chromosome_string = "chrom=chr" + chromosome + " " #converts to string for searching
    iterations = ((snp_position % 1000) // 20) #works out what line within the block the correct value is on
    if (snp_position % 20) != 0: #ensures multiples of 20 are found on the the right line
        iterations += 1
    if ((snp_position % 1000) == 0): #ensures that multiples of 1000 are found on the right line
        iterations = 49
    chromosome_pos = -1 #initialises variable
    snp_pos = -1 #initialises variable
    with open(file) as f: 
        next(f) #skips first line
        for line in f: #goes through the file line by line
            chromosome_pos = line.find(chromosome_string) #finds right block
            snp_pos = line.find(snp_position_rounded) #finds right block
            if chromosome_pos != -1 and snp_pos != -1: #if in right block   
                consume(f, (iterations-1)) #move to right line
                return next(f).strip() #return contig value
            elif line[0] == "f":#if not in the right block
               consume(f, 50) #skip to next block
            else: #if stuck mid block
                while line[0] != "f": #while stuck
                    consume(f, 1) #keep moving line by line till unstuck
        return "NaN" #if not in then return Not a number

def snp_added(): # notifies user snp was added and asks user what they want to do next
    print() #blank line for aesthetics
    print("SNP added")
    print() #blank line for aesthetics
    print("What do you want to do next?")
    print() #blank line for aesthetics
    user_input = input("Enter 1 to add another SNP, 2 to return to main menu or 3 to exit: ") # gets user input
    user_input = user_input.strip() #cleans user input
    expected_inputs = ["1", "2", "3"] #expected user inputs
    proceed = check_user_input(expected_inputs, user_input) #checks user input is as expected
    proceed_with_chosen_path3(proceed) #pipes user to desired function based on their input
    
def proceed_with_chosen_path3(user_input):
    if user_input == "1": #allows user to enter another snp
        add_a_snp()
    elif user_input == "2": #allows user to return to menu
        return_to_menu()
    elif user_input == 0: #if user input is invalid
        print(Fore.RED + "Invalid character added")  #prints warning in red to get user attention
        print(Style.RESET_ALL) #reset to white
        snp_added() #allows user to enter a valid input
    else: #quits the programme
        quit()	

def add_a_cell_line(): #allows user to load a file into the programme
    clear_screen() #clears screens for aesthetics
    check_database_existance() #checks if there is already a database
    cell_line = get_cell_line() #gets user input for the cell line
    check_cell_line(cell_line) #checks user input
    add_cell_line_database(cell_line) #adds a new column to the database for that cell line
    cell_line_added() #asks the user what they would like to do next
    
def get_cell_line(): #asks user to input the name of the cell line they want to add
    print("Enter the cell line name (the characters before the '-' in the file name) or 0 to return to the main menu")
    print() #blank line for aesthetics
    cell_line = input("Enter cell line name: ") #gets user input
    cell_line = cell_line.strip() #cleans input
    if cell_line == "0": #allows user to return to menu if they got here by accident
        return_to_menu()
    else:
        return cell_line #returns input

def check_cell_line(cell_line): #checks if corresponding file is in folder or if cell line is already entered
    database = open("ePygenetics.csv", "r") #opens database
    cell_line_list = database.readline() #reads top row
    end = cell_line_list.find("\n") #finds new line character
    cell_line_list = cell_line_list[:end] #removes new line character
    cell_line_list = cell_line_list.split(",") #splits into list of cell lines
    cell_line_list.pop(0) #removes snp column label
    database.close() #closes database
    file_list = glob.glob('*.wig') #selects all files
    cell_line_file_list = []  #initialises list
    for element in file_list: #for cell line files
        end_of_cell_line = element.find("-") #finds the dash in the file
        cell_line_file = element[:end_of_cell_line] #slices till the dash which is the cell line name
        cell_line_file_list.append(cell_line_file) #adds to cell line file list
    if cell_line not in cell_line_file_list: #if file not in folder
        cell_line_not_added() #notify user
    elif cell_line in cell_line_list: #if cell line already added
        duplicate_cell_line() #notify user


def cell_line_not_added(): #notifies user the file they are trying to add is not in the right folder
    clear_screen() #clears screen for aesthetics
    print(Fore.RED + "Cell line file not in folder")  #prints in red to get user attention
    print(Style.RESET_ALL) #resets to white
    print() #blank line for aesthetics
    print("Please move the .wig file corresponding to the cell line you wish to add into the current working directory in the format [cell line]-*.wig") #instructs user
    print() #blank line for aesthetics
    input("Once this is complete press enter to continue") #waits for user to move file
    add_a_cell_line() #allows user to continue once they move the file

def duplicate_cell_line(): #tells the user they entered a cell line already in the database
    clear_screen() #clears screen for aesthetics
    print(Fore.RED + "Cell line already entered")  #prints in red to get user attention
    print(Style.RESET_ALL) #resets to white
    print() #blank line for aesthetics
    user_input = input("Would like to add a different cell line?, enter 1 for yes, 2 to return to the main menu or 3 to exit the programme: ") #gets user input
    user_input = user_input.strip() #cleans user input
    expected_inputs = ["1","2","3"] #expected inputs
    proceed = check_user_input(expected_inputs, user_input) #checks user input
    proceed_with_chosen_path4(proceed) #pipes user to correct function based on their input
    
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
    data = input_database.read() #reads database
    data = data.split('\n') #splits into lines
    for num in range(len(data)): #for lines in database
        if data[num] == "": #if empty
            data.pop(num) #remove line
    columns_list = data[0] #stores first line
    columns_list += (',' + cell_line + '\n') #adds cell line from user input to first line
    data[0] = columns_list #replaces first line
    filename = [cell_line] #converts cell name to list so it can be passed to generate_cell_line_file_list function
    full_filename = generate_cell_line_file_list(filename) #turns cell line into filename
    full_filename = full_filename[0] #ensures only filename is returned
    for num in range(1, len(data)): #for all lines except the first line
        line = data[num] #select line
        split = line.find("-") #find '-' in snp code
        split1 = line.find("*") #find * in snp code
        chromosome = line[3:split] #extract chromosome number
        snp = line[split+1:split1] #extract snp position
        contigs = find_snp(chromosome, snp, full_filename) #gets snp data
        line += (contigs + ",")  #adds snp data
        data[num] = line + '\n' #readds new line character
    input_database.close() #closes database
    output_database = open('ePygenetics.csv', 'w') #opens database to write
    output_database.writelines(data) #writes to database
    output_database.close() #closes database

def cell_line_added(): #notifies user cell line added and asks user what they want to do next
    print() #blank line for aesthetics
    print("Cell line added") #user notification
    print() #blank line for aesthetics
    print("What do you want to do next?")
    print() #blank line for aesthetics
    user_input = input("Enter 1 to add another cell line, 2 to return to main menu or 3 to exit: ") #get user input
    user_input = user_input.strip() #cleans user input
    expected_inputs = ["1", "2", "3"] #expected input
    proceed = check_user_input(expected_inputs, user_input) #checks user input is as expected
    proceed_with_chosen_path4(proceed) #pipes user to correct function based on their input

def proceed_with_chosen_path4(user_input): #directs user based on their input
    if user_input == "1": #allows user to enter another cell line
        add_a_cell_line()
    elif user_input == "2": #allows user to return to menu
        return_to_menu()
    elif user_input == 0: #if user enters invalid 
        print(Fore.RED + "Invalid character added")  #prints warning in red to get user attention
        print(Style.RESET_ALL) #reset to white
        cell_line_added() #allows user to enter a valid input
    else: #exits programme
        quit()  
    
def run_help():
    clear_screen() #clears screen for aesthetics
    print() #blank line for aesthetics
    print("1. Add a cell line") #help statements
    print() #blank line for aesthetics
    print("This function allows you add a cell line to the database so that the status of all its SNPs can be analysed")
    print() #blank line for aesthetics
    print("2. Add a SNP")
    print() #blank line for aesthetics
    print("This function allows you to add a SNP to the database so that its status can be analysed in all the currently loaded cell lines")
    print() #blank line for aesthetics
    input("Press enter to continue")
    print() #blank line for aesthetics
    return_to_menu()	
	

def main(): #initialises programme
    welcome_to_ePygenetics()
    get_user_input_welcome()

main()


