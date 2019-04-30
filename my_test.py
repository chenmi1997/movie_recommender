# testing-123/my_test.py

from my_script import enlarge # load the `enlarge()` function to avoid NameError: name 'enlarge' is not defined

def test_enlarge(): # note the function name is prefixed with "test_"
    result = len(movie_list) # directly invoke the function we want to test
    assert result == 300 # describe expectations for desired behavior
