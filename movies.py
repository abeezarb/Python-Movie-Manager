import re
class Movies:
 def __init__(self, name, cast, release_date, director,
 duration, description, sequels):
  
    self.name = name
    self.cast = cast
    self.release_date = release_date
    self.director = director
    self.duration = duration
    self.description = description
    self.sequels = sequels

    def details(self):
        """Returns details on the current Movie object as
        a string with all information that was used during
        the initialization process."""
        movie_details = list()
        movie_details.append("-=(+)=- Movie Details -=(+)=-")
        movie_details.append("Name: " + self.name)
        movie_details.append("Cast: " + self.cast)
        movie_details.append("Release Date: " + self.release_date)
        movie_details.append("Director: " + self.director)
        movie_details.append("Duration: " + self.duration)
        movie_details.append("Description: " + self.description)
        movie_details.append("Sequels: " + self.sequels)
        return movie_details

    def loadMovies(directory):
        """Goes to the directory where the movies.txt file is stored and
        creates the movie object for each individual movie by line.
        Then returning a list of movie objects for each movie."""
        movie_list = list()
        with open(directory + "/movies.txt", "r", encoding = "utf-8") as file:
            for line in file:
                movie_info = line.split("|")
                movie_list.append(Movies(movie_info[0],movie_info[1],movie_info[2],
                movie_info[3],movie_info[4],movie_info[5],
                movie_info[6]))

        return movie_list

    def findMovie(directory, search_term):
        """Goes through all the movies and sees if it can
        find a movie that includes the search_term anywhere
        in it's details (name, cast, director, description,
        etc.)"""
        search_results = list()
        search_results.append("-=(+)=- Results -=(+)=-")
        search_results.append("The following Movies included: \"" + search_term + "\"")
        with open(directory + "/movies.txt") as file:
            for line in file:
                search = re.search(search_term, line, flags = re.IGNORECASE)
            if search != None:
                count = (len(search_results)-1)
                movie_name = line.split("|")
                search_results.append(str(count) + ": " + movie_name[0])
            if len(search_results) == 2:
                search_results.clear()
                search_results.append("-=(+)=- Error -=(+)=-")
                search_results.append("No Results Found, please try another search term.")

        return search_results

    def addMovie(directory, name, cast, release_date, director,
    duration, description, sequels):
        """Adds a Movie to the Movies.txt file, and returns an output
        to print out regarding the movie details that were entered."""
        with open(directory + "/movies.txt", "a", encoding="utf-8") as file:
            new_movie = "\n" + name + "|" + cast + "|" + release_date + "|" + director + "|" + duration + "|" + description + "|" + sequels
            file.write(new_movie)
            file.close()
            output = list()
            output.append("-=(+)=- Movie Details -=(+)=-")
            output.append("Name: " + name)
            output.append("Cast: " + cast)
            output.append("Release Date: " + release_date)
            output.append("Director: " + director)
            output.append("Duration: " + duration)
            output.append("Description: " + description)
            output.append("Sequels: " + sequels)
        return output

    def addMovieVerify(directory):
        """Collects and verifies that all the information
        provided to create a new Movie object is accurate
        and valid."""
        while True:
            movie_name = input("-=(+)=- Add a Movie -=(+)=-\nPlease enter in a movie name\nTo exit type \"exit\"\n\nName: ")
            if "|" in movie_name:
                raise ValueError("You cannot use \"|\" in the name please tryagain.")
            elif movie_name == "exit":
                return False
            else:
                break

        while True:
            movie_cast = input("-=(+)=- Add a Movie -=(+)=-\nPlease enter in the cast of \"" + movie_name + "\"\nTo exit type \"exit\"\n\nCast: ")
            if "|" in movie_cast:
                raise ValueError("You cannot use \"|\" in the Cast please try again.")
            elif movie_cast == "exit":
                return False
            else:
                break

        while True:
            movie_release_date = input("-=(+)=- Add a Movie -=(+)=-\nPlease enter in the release date of \"" + movie_name + "\"\nTo exit type \"exit\"\n\nRelease Date: ")
            if "|" in movie_release_date:
                raise ValueError("You cannot use \"|\" in the release date please try again.")
            elif movie_release_date == "exit":
                return False
            else:
                break

        while True:
            movie_director = input("-=(+)=- Add a Movie -=(+)=-\nPlease enter in the Director(s) of \"" + movie_name + "\"\nTo exit type \"exit\"\n\nDirector(s): ")
            if "|" in movie_director:
                raise ValueError("You cannot use \"|\" in the Director(s) please try again.")
            elif movie_director == "exit":
                return False
            else:
                break

        while True:
            movie_duration = input("-=(+)=- Add a Movie -=(+)=-\nPlease enter in the Duration of \"" + movie_name + "\"\nTo exit type \"exit\"\n\nDuration: ")
            if "|" in movie_duration:
                raise ValueError("You cannot use \"|\" in the Duration please try again.")
            elif movie_duration == "exit":
                return False
            else:
                break

        while True:
            movie_description = input("-=(+)=- Add a Movie -=(+)=-\nPlease enter in the description of \"" + movie_name + "\"\nTo exit type \"exit\"\n\nDescription: ")
            if "|" in movie_description:
                raise ValueError("You cannot use \"|\" in the Description please try again.")
            elif movie_description == "exit":
                return False
            else:
                break

        while True:
            movie_sequels = input("-=(+)=- Add a Movie -=(+)=-\nPlease enter in any sequels of \"" + movie_name + "\"\nTo exit type \"exit\"\n\nSequels: ")
            if "|" in movie_sequels:
                raise ValueError("You cannot use \"|\" in the Description please try again.")
            elif movie_sequels == "exit":
                return False
            else:
                break
        return movie_name, movie_cast, movie_release_date, movie_director, movie_duration, movie_description, movie_sequels

    def delMovie(directory):
        """Deletes a movie out of the directory, returns
        Error or Success based on if the movie was deleted
        or not"""
        while True:
            movie_name = input("-=(+)=- Delete a Movie -=(+)=-\nPlease enter the name of the Movie you want to delete. \"\nTo exit type \"exit\"\n\nMovie Name: ")
            if "|" in movie_name:
                raise ValueError("You cannot use \"|\" in the Movie Name please try again.")
            elif movie_name == "exit":
                print("Now exiting...")
                return False
            else:
                delete_confirm = input("Are you sure you want to delete \"" + movie_name + "\"\n")
                delete_confirm = delete_confirm.lower()
                if delete_confirm == "yes":
                    line_pos = 0
                    with open(directory + "/movies.txt", encoding="UTF-8") as file:
                        lines = file.readlines()
                        for line in lines:
                            search = re.search(movie_name, line, flags =
                            re.IGNORECASE)
                            if search != None:
                                break
                            else:
                                line_pos += 1
                                file.close()

                    with open(directory + "/movies.txt", "r+", encoding="UTF-8") as file:
                        lines = file.readlines()
                        file.seek(0)
                        current_line_pos = 0
                        for line in lines:
                            if current_line_pos != line_pos:
                                file.write(line)
                                current_line_pos += 1
                                file.truncate()

                    return "-=(+)=- Delete a Movie -=(+)=-\n\"" + movie_name + "\" Successfully Deleted."

                elif delete_confirm == "no":
                    print("Delete Denied, now exiting...")
                    return False
 