"""pytest will execute all tests in all files 
whose names follow the form:
test_*.py or *_test.py
in the current directory and its subdirectories"""
import re
import pytest
def clean_abv(raw_abv: str)-> str:
    abv_final = re.match(pattern = "[0-9]+[.]*[0-9]*",
                               string = raw_abv).group(0)
    return abv_final

# Run the following within the command line
# pytest test_brew_functions.py::test_clean_abv
@pytest.mark.parametrize("raw_abv, expected_abv",  
  [("9.5% ABV", "9.5"),  
   ("4.7 %", "4.7"),
   ("5.2 % abv","5.2")])
def test_clean_abv(raw_abv, expected_abv):
    cleaned_abv = clean_abv(raw_abv)
    assert cleaned_abv == expected_abv
