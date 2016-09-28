from ePygenetics import *

def test_user_input_expected():
	assert check_user_input(["1", "2", "3"], "3") == "3"

def test_user_input_expected1():
	assert check_user_input([1,2,3,4,5,6,7,8,9], 4) == 4

def test_user_input_unexpected():
	assert check_user_input([1,2,3,4,5,6,7,8,9], "2") == 0

def test_user_input_unexpected2():
	assert check_user_input(["1", 2, "3", 4], 3) == 0

def test_find_snp_in_database():
	assert find_snp('10', '103284', 'IMR90rep2-DNAse-hypersensitivity-GSM468801.wig') == "4"

def test_find_snp_in_database1():
	assert find_snp("10", "80018084", 'IMR90rep2-DNAse-hypersensitivity-GSM468801.wig') == "45"

def test_find_snp_not_in_database():
	assert find_snp('10', '49000', 'IMR90rep2-DNAse-hypersensitivity-GSM468801.wig') == "NaN"

def test_find_snp_not_in_database1():
	assert find_snp("10", "53424", 'IMR90rep2-DNAse-hypersensitivity-GSM468801.wig') == "NaN"

def test_generate_cell_line_file_list():
        assert generate_cell_line_file_list(['IMR90rep2' , 'CD34+']) == ['IMR90rep2-DNAse-hypersensitivity-GSM468801.wig' , 'CD34+-DNAse-Hypersensitivity-DS12734.wig']

def test_get_cell_line(monkeypatch):
        monkeypatch.setitem(__builtins__, 'input', lambda x: "    IMR90rep2    ")
        assert get_cell_line() == "IMR90rep2"

def test_generate_cell_line_list():
        assert generate_cell_line_list() == ['IMR90rep2','CD34+']

        





