import os
import json
import pprint as pp # see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/pprint.md
import random
import pytest

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY_V3 = os.environ.get("API_KEY_V3")

output_length = 3

genres = [
    {"id": 28,"name": "Action"},
    {"id": 12,"name": "Adventure"},
    {"id": 16,"name": "Animation"},
    {"id": 35,"name": "Comedy"},
    {"id": 80,"name": "Crime"},
    {"id": 99,"name": "Documentary"},
    {"id": 18,"name": "Drama"},
    {"id": 10751,"name": "Family"},
    {"id": 14,"name": "Fantasy"},
    {"id": 36,"name": "History"},
    {"id": 27,"name": "Horror"},
    {"id": 10402,"name": "Music"},
    {"id": 9648,"name": "Mystery"},
    {"id": 10749,"name": "Romance"},
    {"id": 878,"name": "Science Fiction"},
    {"id": 10770,"name": "TV Movie"},
    {"id": 53,"name": "Thriller"},
    {"id": 10752,"name": "War"},
    {"id": 37,"name": "Western"}
]

    #
    # USER SELECTS GENRE
    #

    # inferring these from https://developers.themoviedb.org/3/genres/get-movie-list

genre_list = []

for x in genres:
    genre_list.append(x["name"]) 

    # genre_list = ["action", "adventure", "documentary", "horror", "mystery", "science fiction"]


def random_movie_generator(movie = ""):

    if(movie == ""): 
        print("GENRES:" + str(genre_list))
        genre_input = input("Enter the name of the genre you want: ")
        print("SELECTED GENRE:" + genre_input)
    else:
        genre_input = movie
  

      # if genre_input.lower() in genre_list:
          
      # else:
          # ("Please enter a valid genre")

      # h/t: https://www.themoviedb.org/talk/59fcec1fc3a368689300071d?language=en-US

      # for genre_input in request_url:
              # = [p for p in genres if str(p["name"]) == str(genre_input)]


      # GENRE MATCHING PROCESS
    matching_genres = [p for p in genres if str(p["name"].lower()) == str(genre_input).lower()]
    matching_genre = matching_genres[0]
    genre_id = matching_genre["id"]



      # RANDOMIZATION PROCESS
  #number_of_movies_available = 85000 # todo: lookup id matching the selected genre (see genres.json or make a request to https://developers.themoviedb.org/3/genres/get-movie-list):
  #movie_ids = list(range(number_of_movies_available))
  #random.shuffle(movie_ids) # sort randomly, which will introduce randomness into the request process. see: https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/random.md
  #print("SOME RANDOM MOVIE IDS:", movie_ids[0:7])

      # print(genre_id)

          # for collection in range(genre_id):
          #    data = requests.get("https://api.themoviedb.org/3/movie/" + str(genre_id) + f"?api_key={API_KEY_V3}")

    request_url = f"https://api.themoviedb.org/3/discover/movie?api_key=859ad25d111a2a5246f618512a63e567&language=en-US&sort_by=popularity.desc&with_genres={genre_id}"
        # print(request_url)
    data = requests.get(request_url)


    get_request_attempts = 0
    max_data_get_request_attempts = 25

    while data.status_code != 200 and get_request_attempts < max_data_get_request_attempts:
        data = requests.get(request_url)
        get_request_attempts += 1

    if get_request_attempts == max_data_get_request_attempts:
        raise Exception("Failed to get data from server")




    if data.status_code == 200:
        json_string = data.text
        parsed_response = json.loads(json_string)

            # breakpoint()
            # (Pdb) type(parsed_response)
            # <class 'dict'>
            # (Pdb) parsed_response.keys()
            # dict_keys(['page', 'total_results', 'total_pages', 'results'])

        matching_movies = parsed_response["results"]

            # print(type(matching_movies))

        movie_list = []


            # ENSURES THERE ARE ONLY 3 OUPUTS

        while len(movie_list) != output_length:
            random_int = random.randint(0, len(matching_movies) - 1)
            if matching_movies[random_int] not in movie_list:
                movie_list.append(matching_movies[random_int])

        
            # PRINTING PROCESS OF THE MOVIES 

        print("-------------------")
        print("Random " +  str(matching_genres[0]['name']) + " Movies: ")
        for movie in movie_list:
            print(movie['original_title'])
            print(movie['overview'])  
            print()
        print("---------")
        return len(movie_list)

random_movie_generator() 
