from movie_project import random_movie_generator
import pytest

def test_outputLenIs3():
    output_len = 0
    for p in range(300):
        output_len += random_movie_generator("comedy")
    if (output_len == 900):
        print("Assertion Succeeded")
    assert output_len == 900 
    
    # WORKED WITH ERIK FOK ON THIS

test_outputLenIs3()
