from argparse import ArgumentParser
from movies import Movies
from shows import Shows
import os
import sys



def printMovies():
    """Prints all the in the Movies.txt file including
    all the details regarding the show like name, cast
    duration, etc."""
    movies_list = Movies.loadMovies(directory)
    for movie in movies_list:
        movie_info = Movies.details(movie)
    for info in movie_info:
        print(info)
def printShows():
    """Prints all the in the Shows.txt file including
    all the details regarding the show like name, cast
    seasons, etc."""
    shows_list = Shows.loadShows(directory)
    for show in shows_list:
        show_info = Shows.details(show)
    for info in show_info:
        print(info)
def parse_args(arglist):
    """Parses through command-line arguments and verifies that
    the directory provided for the movies exists and is valid.
    """
    parser = ArgumentParser()
    parser.add_argument("directory", help = "Directory where all the movies and showed are stored")
    args = parser.parse_args()
    if os.path.exists(args.directory) == False:
        raise ValueError("Please enter in a valid directory.")
        return args
    if __name__ == "__main__":
        args = parse_args(sys.argv[1:])
        directory = args.directory
        while True:
            answer = input("-=(+)=- General -=(+)=-\n" +
            "All - List all Movies & Shows\n" +
            "Movies - Lists all Movies\n" +
            "Shows - Lists all Shows\n\n" +
            "-=(+)=- Add & Delete -=(+)=-\n" +
            "addMovie - Add a Movie\n" +
            "addShow - Add a Show\n" +
            "delMovie - Delete a Movie\n" +
            "delShow - Delete a Show\n\n" +
            "-=(+)=- Search -=(+)=-\n" +
            "searchMovies - Search all Movies\n" +
            "searchShows - Search all Shows\n\n")
            answer = answer.lower()
            if answer == "all":
                printMovies()
                printShows()
            elif answer == "movies" or answer == "movie":
                printMovies()
            elif answer == "shows" or answer == "shows":
                printShows()
            elif answer == "addmovie" or answer == "addmovies":
                output = Movies.addMovieVerify(directory)
                if output != False:
                    addMovie_output = Movies.addMovie(directory,
                    output[0],output[1],output[2],
                    output[3],output[4],output[5],
                    output[6])
                    for output in addMovie_output:
                        print(output)
                elif answer == "addshow" or answer == "addshows":
                    output = Shows.addShowVerify(directory)
                if output != False:
                    addShows_output = Shows.addShows(directory,
                    output[0],output[1],output[2],
                    output[3],output[4],output[5])
                    for output in addShows_output:
                        print(output)
                elif answer == "delmovie" or answer == "delmovies":
                    output = Movies.delMovie(directory)
                    if output != False:
                        print(output)
                elif answer == "delshow" or answer == "delshows":
                    output = Shows.delShow(directory)
                    if output != False:
                        print(output)
                elif answer == "searchmovies" or answer == "searchmovie":
                    while True:
                        search_term = input("Please enter in the search term to search through all movies\nTo go back type \"exit\"\n")
                        search_term = search_term.lower()
                        if "|" in search_term:
                            raise ValueError("You cannot use \"|\" in your search term, please try again.")
                        elif search_term == "exit":
                            break
                        else:
                            results = Movies.findMovie(directory, search_term)
                            for result in results:
                                print(result)
                elif answer == "searchshows" or answer == "searchshow":
                    while True:
                        search_term = input("Please enter in the search term to search through all movies\nTo go back type \"exit\"\n")
                        search_term = search_term.lower()
                        if "|" in search_term:
                            raise ValueError("You cannot use \"|\" in your search term, please try again.")
                        elif search_term == "exit":
                            break
                        else:
                            results = Shows.findShow(directory, search_term)
                            for result in results:
                                print(result)