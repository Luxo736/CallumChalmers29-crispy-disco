#ePygenetics

This programme extracts data from .wig files based on user input. The output of the programme is a database called ```ePygenetics.csv``` which contains all data extracted by the user.

##Project Description

This programme was designed as part of Medsci 736, a course on Digital Research Skills at the University of Auckland, New Zealand. 

The project was designed by Dr Justin O'Sullivan from the Liggins Institute who wanted to add the epigenetic status of single nucleotide polymorphisms to his genetic data analysis. 

In simple terms, this programme allows scientists to get extra information about person to person genetic variation. This information can then be used to better understand how genetics is related to disease and to look for treatments for diseases with a genetic component.

The programme was designed using data from the [NIH Roadmap Epigenomics Repository](https://www.ncbi.nlm.nih.gov/geo/roadmap/epigenomics/?search=DNAse+hypersensitivity&display=50) which is open access. A subset of 5 modified files has been included in the ```test-data``` folder for testing the programme.

##Contributors

1. Callum Chalmers
2. Kreshnik Pireva
3. Luis Miguel
4. Bibiana Lee

##Licensing

All code and associated documentation in this repository is under the MIT license. Data in the ```test-data file``` was downloaded from [here](http://nihroadmap.nih.gov/epigenomics/) is covered by the [NIH Epigenomic Data Policy](https://www.drugabuse.gov/funding/funding-opportunities/nih-common-fund/epigenomics-data-access-policies). All other files are licensed under CC-BY-SA 4.0 International. For more information see the [LICENSE file](https://github.com/UOA-MEDSCI-736/CallumChalmers29-crispy-disco/blob/master/LICENSE.txt).

##Prerequisites
1. Python
  - To run the software you will need Python 3.5.2 or a compatible version
  - Follow [this link](https://www.python.org/downloads/release/python-352/) to download Python 3.5.2 
  - Alternatively under the CC BY-SA 4.0 license you can update the code to be compatible with your own version of python 

2. Operating System
 - The programme was scripted for Ubuntu 16.04 LTS, it is yet to be tested for compatibility issues with other operating systems
 - If you are using the file on Windows, on line 13 of ePygenetics.py you will need to change the code to read os.system('cls')

##Input Data Requirements
 - The programme can only read Wiggle (.wig) files with a fixed step of 20, see [this link](https://genome.ucsc.edu/goldenpath/help/wiggle.html) for more information about this file type
 - **For the programme to read the files, both the script and the files need to be in the same directory**
 - **At least one .wig file is needed to run the programme**
 - Files must contain a "-" in their name to be read by the programme, whatever text is before the dash will be the column heading in the output database so bear this in mind when naming files

##Limitations
 - The last 1000 base pairs of each chromosome cannot be read due to a change in the file structure at this point, any SNP in this range will be treated as if it is not in the file and return NaN
 - For the output to be valid, all files must use the same genome build, see [this link](https://genome.ucsc.edu/FAQ/FAQreleases.html) for more information about genome releases

## Running the programme using the test data

1. Download ```test-data``` and transfer the contents to the same directory as the ```ePygenetics.py``` script
2. Open the command line to folder containing the ```ePygenetics.py``` script
3. Type the command ```python ePygenetics.py```
4. You will be greeted with a menu with 4 options:

	```
	1. Add a cell line (loading a file)
	2. Add a SNP
	3. Help
	4. Exit
	```

###Loading the test data files

5. Start by typing ```1``` and pressing enter

 - You will be transferred to the Add a Cell Line function and a message will appear saying ```Enter the cell line name (the characters before the '-' in the file name) or 0 to return to the main menu```

6. Type ```CD34+``` and press enter

 - A message will appear which says ```Cell line added``` and you will be asked what you would like to do next

7. Type ```1``` and press enter

8. Repeat the last two steps to add the following cell lines: 
	```
	IMR90
	FetalLung
	FetalKidney
	FetalHeart
	FetalAdrenal
	```

 - If you enter something incorrectly, red text saying ```Cell line file not in folder``` will appear, press enter to continue and re-enter the cell line correctly

 - If you enter one that you have already entered, red text saying ```Cell line already entered``` will appear, enter ```1``` to continue and re-enter a different cell line

9. Once this is complete and you have added all the cell lines, type ```2``` and press enter to return to the main menu

###Adding SNPs

10. Type ```2``` and press enter

 - You will be transferred to the Add a SNP function and a message will appear saying ```Enter the chromosome and position of the SNP you wish to add or enter 0 to return to the main menu```

11. Type ```10``` for the chromosome and press enter

12. Type ```58247``` for the SNP position and press enter

 - The programme will then pause briefly while it searches through the loaded files

 - Once the data has been added, a message will appear saying ```SNP added``` and the programme will ask what you want to do next

13. Type ```1``` and press enter

14. Repeat the last three steps using the following chromosome, SNP pairs:

	```
	chromosome = 10 SNP = 86145
	chromosome = 10 SNP = 63726
	chromosome = 10 SNP = 51102
	chromosome = 10 SNP = 92003
	chromosome = 10 SNP = 61994
	```

 - If you enter one that you have already entered, red text saying ```SNP already entered``` will appear, enter ```1``` to continue and re-enter a different SNP

15. Once this is complete exit the programme by typing ```3``` and pressing enter

###Expected output

1. Go to the file containing the ```ePygenetics.py``` script and find the output database ```ePygenetics.csv```

2. If you open it with a text editor it should look like this:

	```
	snps,CD34+,IMR90,FetalLung,FetalHeart,FetalAdrenal,FetalKidney
	chr10-58247*,42,NaN,NaN,NaN,NaN,NaN,
	chr10-86145*,1,2,0,0,67,0,
	chr10-63726*,NaN,NaN,2,32,2,1,
	chr10-51102*,NaN,0,0,NaN,NaN,21,
	chr10-92003*,NaN,NaN,84,0,0,NaN,
	chr10-61994*,NaN,59,NaN,NaN,NaN,NaN,
	```

3. If you open it with a Spreadsheet application it should look like this:

	snps        |CD34+|IMR90|FetalLung|FetalHeart|FetalAdrenal|FetalKidney
	------------|-----|-----|---------|----------|------------|-----------
	chr10-58247*|42   |NaN  |NaN      |NaN       |NaN         |NaN
	chr10-86145*|1    |2    |0        |0         |67          |0
	chr10-63726*|NaN  |NaN  |2        |32        |2           |1
	chr10-51102*|NaN  |0    |0        |NaN       |NaN         |21
	chr10-92003*|NaN  |NaN  |84       |0         |0           |NaN
	chr10-61994*|NaN  |59   |NaN      |NaN       |NaN         |NaN

4. Alternatively, there is a file in the ```test-data``` folder called ```ePygenetics-sample-output.csv``` which was generated by following these instructions and can be used as a comparison

##Running the programme using your own data

1. Open the command line to folder containing the Python script called ```ePygenetics.py```
2. Type the command ```python ePygenetics.py```
3. You will be greeted with a menu with 4 options: 

	```
	1. Add a cell line (loading a file)
	2. Add a SNP
	3. Help
	4. Exit
	```

You will then be asked to choose which of the 4 options you would like to do. Type the number corresponding to the action you would like to perform and press enter.

###Adding a cell line (loading a file)
 - A message will pop up saying ```Enter the cell line name (the characters before the '-' in the file name) or 0 to return to the main menu```
 - If the output database ```ePygenetics.csv``` does not exist, it will be created as part of this process
 - For this action to work the corresponding file must be in the same directory as the ```ePygenetics.py``` script
 - The file must be named ```[cell line]-[any text].wig```
 - Type the cell line name and press enter
 - If you enter a valid cell line, the programme will add a column to the database and search the file for any SNPs that have been entered into the file
 - If you enter a cell line that does not have a corresponding file in the directory an error message will pop up saying ```Cell line file not in folder```, to clear move the file into the directory and then press enter
 - If you enter a cell line that is already in the database, an error message will pop up saying ```Cell line already entered```, see below for how to proceed
 - If you enter ```0``` you will returned to the menu
 - Once this is complete, the programme will notify you ```Cell line added``` and ask if you would like to add another cell line, return to the main menu or exit the programme
 - Type the character corresponding to how you would like to proceed and press enter
 - If you press ```1```, the you can add another file
 - If you press ```2```, the programme will return to the menu
 - If you press ```3```, the programme will exit

###Adding a SNP
 - A message will pop up saying ```Enter the chromosome and position of the SNP you wish to add or enter 0 to return to the main menu```
 - Type the chromosome your SNP is on and press enter
 - If you enter a value that is not the number 0-23 or the letters M, X or Y, an error message will pop up saying ```Illegal character entered``` and you will be asked to press enter before entering a valid input
 - If you enter ```0``` you will returned to the main menu
 - Then you will be asked to enter the position of the SNP on that chromosome. The position is the location of that SNP in base pairs.
 - Type the SNP position and press enter
 - If you enter ```0``` you will be returned to main menu
 - If the output database ```ePygenetics.csv``` does not exist then it will be created at this point
 - If you enter a SNP that is already in the database, an error message will appear saying ```SNP already entered```, see below for how to proceed
 - At this point the programme will add a row to the database for that SNP
 - The programme will then take the user parameters and use them to search for that SNP in all the files that have been loaded into the database
 - If no files have been loaded, it will simply notify you that your SNP has been added and ask how you want to proceed (see below)
 - The programme will then return the number of contigs that aligned to the section of the genome that covers that SNP for each file. If the region of the genome that contains your SNP is not in the file, the programme will return NaN.
 - The programme will then populate the row of the database using the values it extracted from each file
 - A message will then appear saying ```SNP added```
 - The programme will then ask if you want to add another SNP, want to return to the main menu or exit the programme
 - Type the number corresponding to how you want to proceed and press enter
 - If you press ```1```, this cycle will repeat
 - If you press ```2```, the programme will return to the menu
 - If you press ```3```, the programme will exit

###Help
 - You will be redirected to a brief manual that explains what each function does
 - You will then be asked to press enter to continue and you will be redirected to the main menu 

###Exit
 - The programme will close

###Expected Output
 - Once you are finished, all the data you have added can be visualised in the output database ```ePygenetics.csv``` which can be found in the same directory as the ```ePygenetics.py``` script.
 - This file can be opened in almost any text editor but is best visualised in Google Docs, Libre or Open Office Calc or Microsoft Excel. 
 - The output database should have all the added cell lines as column headings and all the added SNPs as row headings. All the cells within these columns and rows should be filled with data values or NaN

##Testing the programme
1. Download ```test-data``` and transfer the contents to the same directory as the ```ePygenetics.py``` script
2. Download the ```test-ePygenetics``` folder and move the entire folder to the same directory as the ```ePygenetics.py``` script
3. In the ```ePygenetics.py``` script, delete the last line ```main()``` and save the file
4. To install pytest, open the command line in the directory containing the ```ePygenetics.py``` script and run the command ```pip install -U pytest```
5. To check this worked correctly type the command ```python -m pytest --version``` and it should return a message similar to this, depending on your version and directory pathway:

	```
	This is pytest version 2.9.2, imported from /home/admin736/anaconda3/lib/python3.5/site-packages/pytest.py
	```
6. Once this is complete, type the command ```python -m pytest```
7. This will collect all the tests in the ```test-ePygenetics``` folder and run them
8. The output should be similar to this, depending on your Python and pytest versions and your rootdir, the most important thing is there are **18 tests** and they all pass:

	```
	============================= test session starts ==============================
	platform linux -- Python 3.5.2, pytest-2.9.2, py-1.4.31, pluggy-0.3.1
	rootdir: /home/admin736/Desktop/Assignments/CallumChalmers29-crispy-disco, inifile: 
	collected 18 items 

	test-ePygenetics/test_ePygenetics.py ..................

	========================== 18 passed in 0.03 seconds ===========================
	```

9. This confirms the programme is working correctly, if you do not get this screen, delete and redownload the contents of the GitHub repo and try again
10. Once this is complete, in the ```ePygenetics.py``` script add the last line ```main()``` back in and save the file to run the programme properly




