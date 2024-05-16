"""pytest will execute all tests in all files 
whose names follow the form:
test_*.py or \*_test.py
in the current directory and its subdirectories"""
import re
def clean_abv(raw_abv: str)-> str:
    abv_final = re.match(pattern = "[0-9]+[.]*[0-9]*",
                               string = raw_abv).group(0)
    return abv_final

# Run the following within the command line
# pytest test_brew_functions.py::test_clean_abv
def test_clean_abv():
    assert clean_abv('9.5% ABV') == '9.5'
    assert clean_abv('4.7 %') == '4.7'
    assert clean_abv('5.2 % abv') == '5.2'
