This is a documentation file for the programme ePygenetics.

**Programme requirements**:
 - The programme was scripted using Python 3.5.2 so can only be run in versions compatible with this version, alternatively the user can manually alter the script so it runs on their particular Python version
 - Accordingly a Python interpreter is needed to run the programme
 - The programme was scripted for Ubuntu 16.04 LTS, it is yet to be tested for compatibility issues with other operating systems
 - The programme can only read .wig files with a fixed step of 20 in their standard format, see https://genome.ucsc.edu/goldenpath/help/wiggle.html
 - For the programme to read the files, both the script and the files need to be in the same directory
 - At least one .wig file is needed to run the programme
 - For the output to be valid, all files must use the same genome build
 - Files must contain a "-" in their name to be read by the programme, whatever text is before the dash will be the column heading in the database output so bear this in mind when naming files

**Programme implementation**:
Upon opening the programme you will be greeted with a menu with 5 options: 
1. Add a cell line
2. Add a SNP
3. Help
4. Exit
You will then be asked to enter which of the 5 options you would like to do via a user input

If you choose 1:
 - You will be asked to enter the name of a cell line to add to the database or 0 to return to the menu
 - This refers to loading a file into the database 
 - For this action to work the corresponding file must be in the same directory as the python script
 - The file must be named [cell line]-[any text] and it must be a .wig file
 - If you enter a cell line that does not have a corresponding file in the directory an error message will pop up thats asks you to move the file into the directory and then press enter
 - If you enter a cell line that is already in the database, an error message will pop up asking you how you would like to proceed (see below)
 - If you enter 0 you will returned to the menu
 - If you enter a valid cell line, the programme will add a column to the database and search the file for any SNPs that have been entered into the file
 - Once this is complete, the programme will notify you that your cell line was added and ask if you would like to add another cell line, return to the main menu or exit the programme
 - If you press 1, the cycle will repeat
 - If you press 2, the programme will return to the menu
 - If you press 3, the programme will exit

If you choose 2:
 - You will be asked to enter the number of the chromosome the desired SNP is on
 - If you enter a number that is not 0-23, you will be notified your input is invalid and will be asked to press enter before entering a valid input
 - If you enter 0 you will returned to the main menu
 - Then you will be asked to enter the position of the SNP on that chromosome. The position is the location of that SNP in base pairs.
 - If you enter 0 you will be returned to main menu
 - If you enter a SNP that is already in the database, you will be asked how you would like to proceed (see below)
 - At this point the programme will add a row to the database for that SNP
 - The programme will then take the user parameters and use them to search for that SNP in all the files that have been loaded into the database
 - If no files have been loaded, it will simply notify you that your SNP has been added and ask how you want to proceed (see below)
 - The programme will then return the number of contigs that aligned to the section of the genome that covers that SNP for each file. If the region of the genome that contains your SNP is not in the file, the programme will return NaN.
 - The programme will then populate the row of the database using the values it extracted from each file
 - The programme will then notify you that your SNP was added
 - The programme will then ask if you want to add another SNP, want to return to the main menu or exit the programme
 - If you press 1, this cycle will repeat
 - If you press 2, the programme will return to the menu
 - If you press 3, the programme will exit

If you choose 3:
 - You will be redirected to a brief manual that explains what each function does
 - You will then be asked to press enter to continue and you will be redirected to the main menu 

If you choose 4:
 - The programme will close

