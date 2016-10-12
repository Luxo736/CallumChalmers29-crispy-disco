#ePygenetics

This programme extracts data from .wig files based on user input. The output of the programme is a database called ePygenetics.csv which contains all data extracted by the user.

##Project Description

This programme was designed as part of Medsci 736, a course on Digital Research Skills at the University of Auckland, New Zealand. 

The project was designed by Dr Justin O'Sullivan from the Liggins Institute who wanted to add the epigenetic status of single nucleotide polymorphisms to his genetic data analysis. 

In simple terms, this programme allows scientists to get extra information about person to person genetic variation. This information can then be used to better understand how genetics is related to disease and to look for treatments for diseases with a genetic component.

The programme was designed using data from the [NIH Roadmap Epigenomics Repository](https://www.ncbi.nlm.nih.gov/geo/roadmap/epigenomics/?search=DNAse+hypersensitivity&display=50) which is open access. A subset of 5 files has been included in the sample data folder for testing the programme.

##Prerequisites:
1. **Python**
  - To run the software you will need Python 3.5.2 or a compatible version
  - Follow [this link](https://www.python.org/downloads/release/python-352/) to download Python 3.5.2 
  - Alternatively under the CC BY-SA 4.0 license you can update the code to be compatible with your own version of python 

2. **Operating System**
 - The programme was scripted for Ubuntu 16.04 LTS, it is yet to be tested for compatibility issues with other operating systems
 - If you are using the file on Windows, on line 13 of ePygenetics.py you will need to change the code to read os.system('cls')

3. **Data File Requirements**
 - The programme can only read Wiggle (.wig) files with a fixed step of 20, see [this link](https://genome.ucsc.edu/goldenpath/help/wiggle.html) for more information about this file type
 - **For the programme to read the files, both the script and the files need to be in the same directory**
 - **At least one .wig file is needed to run the programme**
 - For the output to be valid, all files must use the same genome build see [this link](https://genome.ucsc.edu/FAQ/FAQreleases.html) for more information about genome releases
 - Files must contain a "-" in their name to be read by the programme, whatever text is before the dash will be the column heading in the output database so bear this in mind when naming files

##Running the programme

###To run the programme:

1. Open the command line to folder containing the Python script called ePygenetics
2. Type the command ```python ePygenetics.py```

You will be greeted with a menu with 4 options: 

1. Add a cell line (loading a file)
2. Add a SNP
3. Help
4. Exit

You will then be asked to choose which of the 4 options you would like to do.

###Adding a cell line:
 - You will be asked to enter the name of a cell line to add to the database or 0 to return to the menu
 - This refers to loading a file into the database 
 - For this action to work the corresponding file must be in the same directory as the python script
 - The file must be named ``[``cell line``]``-``[``any text``]`` and it must be a .wig file
 - If you enter a cell line that does not have a corresponding file in the directory an error message will pop up thats asks you to move the file into the directory and then press enter
 - If you enter a cell line that is already in the database, an error message will pop up asking you how you would like to proceed (see below)
 - If you enter 0 you will returned to the menu
 - If you enter a valid cell line, the programme will add a column to the database and search the file for any SNPs that have been entered into the file
 - Once this is complete, the programme will notify you that your cell line was added and ask if you would like to add another cell line, return to the main menu or exit the programme
 - If you press 1, the cycle will repeat
 - If you press 2, the programme will return to the menu
 - If you press 3, the programme will exit

###Adding a SNP:
 - You will be asked to enter the chromosome the desired SNP is on
 - If you enter a value that is not the number 0-23 or the letters M, X or Y, you will be notified your input is invalid and will be asked to press enter before entering a valid input
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

###Help:
 - You will be redirected to a brief manual that explains what each function does
 - You will then be asked to press enter to continue and you will be redirected to the main menu 

###Exit:
 - The programme will close

##Running the tests

