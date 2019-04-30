# testing-123/my_test.py

from my_script import enlarge # load the `enlarge()` function to avoid NameError: name 'enlarge' is not defined

def test_outputLenIs3():
    output_len = 0
    for x in range(300):
        output_len += random_movie_generator("comedy")
    if (output_len == 900):
        print("Assertion Succeeded")
    assert output_len == 900 
