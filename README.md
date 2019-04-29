# Movie Recommender

## Introduction

This project is designed to help individuals who struggle to decide on picking movies, especially movie lovers who are looking for some new content, by recommending three choices based on their preference of genre.

This project features information such as title and description from The Movie DataBase (TMDB), a massive data source across a wide variety of different movies. 

It is crucial for the user to input a correct genre or the system will quit out and the user will have to restart the program.


## Installation

Prerequisites: Install Python 3.6.

Install source code:

```sh
git clone https://github.com/chenmi1997/movie_recommender.git
cd movie_project/ # all commands below assume you are running them from this repository's root directory
```


## Setup

Obtain a [TMDB API Key](https://www.themoviedb.org/documentation/api) and store the result in an environment variable called `API_KEY_V3`. 

This key is stored locally to ensure security.

## Usage

Run the app locally:

```
Run `movie_project.py` if you wish to run this app via command line only.


## Testing

To test the functions in this app, import `pytest` package and run the pytest command line from within the `test` directory.

The 5 unit tests covers the 5 functions defined in this app. 
