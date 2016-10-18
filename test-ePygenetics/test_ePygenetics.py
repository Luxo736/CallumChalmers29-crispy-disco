"""This is the testing script for the programme ePygenetics. For instructions on how to run the tests please see the README file. This programme is licensed under the MIT license. For more information on licensing see the LICENSE.md file.

Copyright (c) 2016 Callum Chalmers
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

from ePygenetics import * #import statements

def test_user_input_expected(): #testing user input checking function when input expected
	assert check_user_input(["1", "2", "3"], "3") == "3"

def test_user_input_expected1():
	assert check_user_input([1,2,3,4,5,6,7,8,9], 4) == 4

def test_user_input_unexpected(): #testing user input checking function when input not expected
	assert check_user_input([1,2,3,4,5,6,7,8,9], "2") == 0

def test_user_input_unexpected2():
	assert check_user_input(["1", 2, "3", 4], 3) == 0

def test_find_snp_in_database_mid(): #testing snp search function when snp is in the middle of the data blocks
	assert find_snp('10', '58247', 'CD34+-test-data.wig') == "42"

def test_find_snp_in_database_mid1():
	assert find_snp("10", "86145", 'FetalAdrenal-test-data.wig') == "67"

def test_find_snp_in_database_mid2():
	assert find_snp('10', '63726', 'FetalHeart-test-data.wig') == "32"

def test_find_snp_in_database_mid3():
	assert find_snp('10', '51102', 'FetalKidney-test-data.wig') == "21"

def test_find_snp_in_database_beginning(): #testing snp search function when snp is at the beginning of the data blocks
	assert find_snp('10', '92003', 'FetalLung-test-data.wig') == "84"

def test_find_snp_in_database_end(): #testing snp search function when snp is at the end of the data blocks
	assert find_snp('10', '61994', 'IMR90-test-data.wig') == "59"


def test_find_snp_not_in_database(): #testing snp search function when snp is not in the data file
	assert find_snp('10', '57247', 'CD34+-test-data.wig') == "NaN"

def test_find_snp_not_in_database1():
	assert find_snp("10", "91145", 'FetalAdrenal-test-data.wig') == "NaN"

def test_find_snp_not_in_database2():
	assert find_snp('10', '84726', 'FetalHeart-test-data.wig') == "NaN"

def test_find_snp_not_in_database3():
	assert find_snp('10', '56102', 'FetalKidney-test-data.wig') == "NaN"

def test_find_snp_not_in_database4():
	assert find_snp('10', '93003', 'FetalLung-test-data.wig') == "NaN"

def test_find_snp_not_in_database5():
	assert find_snp('10', '63994', 'IMR90-test-data.wig') == "NaN"

def test_generate_cell_line_file_list(): #testing file selecter function
        assert generate_cell_line_file_list(['IMR90' , 'CD34+', 'FetalAdrenal', 'FetalLung', 'FetalHeart', 'FetalKidney']) == ['IMR90-test-data.wig', 'CD34+-test-data.wig', 'FetalAdrenal-test-data.wig', 'FetalLung-test-data.wig', 'FetalHeart-test-data.wig', 'FetalKidney-test-data.wig']

def test_get_cell_line(monkeypatch): #testing user input function strips correctly
        monkeypatch.setitem(__builtins__, 'input', lambda x: "    IMR90rep2    ")
        assert get_cell_line() == "IMR90rep2"



        





