from ePygenetics import *

def test_user_input_expected():
	assert check_user_input(["1", "2", "3"], "3") == "3"
	assert check_user_input([1,2,3,4,5,6,7,8,9], 4) == 4

def test_user_input_unexpected():
	assert check_user_input([1,2,3,4,5,6,7,8,9], "2") == 0
	assert check_user_input(["1", 2, "3", 4], 3) == 0

def test_find_snp_in_database():
	assert find_snp('10', '103284', 'IMR90rep2-DNAse-hypersensitivity-GSM468801.wig') == "4"
	assert find_snp("10", "80018084", 'IMR90rep2-DNAse-hypersensitivity-GSM468801.wig') == "45"

def test_find_snp_not_in_database():
	assert find_snp('10', '49000', 'IMR90rep2-DNAse-hypersensitivity-GSM468801.wig') == "NaN"
	assert find_snp("10", "53424", 'IMR90rep2-DNAse-hypersensitivity-GSM468801.wig') == "NaN"


