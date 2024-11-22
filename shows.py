import re
class Shows:
    def __init__(self, name, cast, release_date, director, seasons, episodes):
        self.name = name
        self.cast = cast
        self.release_date = release_date
        self.director = director
        self.seasons = seasons
        self.episodes = episodes

    def details(self):
        """Returns details on the current Show object as
        a string with all information that was used during
        the initialization process."""
        show_details = list()
        show_details.append("-=(+)=- Show Details -=(+)=-")
        show_details.append("Name: " + self.name)
        show_details.append("Cast: " + self.cast)
        show_details.append("Release Date: " + self.release_date)
        show_details.append("Director: " + self.director)
        show_details.append("Seasons: " + self.seasons)
        show_details.append("Episodes: " + self.episodes)
        return show_details
    
    def loadShows(directory):
        """Goes to the directory where the shows.txt file is stored and
        creates the show object for each individual show by line.
        Then returning a list of show objects for each show."""
        show_list = list()
        with open(directory + "/shows.txt") as file:
            for line in file:
                show_info = line.split("|")
                show_list.append(Shows(show_info[0],show_info[1],show_info[2],
                show_info[3],show_info[4],show_info[5]))
        return show_list
    
    def findShow(directory, search_term):
        """Goes through all the shows and sees if it can
        find a shows that includes the search_term anywhere
        in it's details (name, cast, director, description,
        etc.)"""
        search_results = list()
        search_results.append("-=(+)=- Results -=(+)=-")
        search_results.append("The following Shows included: \"" + search_term + "\"")
        with open(directory + "/shows.txt") as file:
            for line in file:
                search = re.search(search_term, line, flags = re.IGNORECASE)
            if search != None:
                count = (len(search_results)-1)
                show_name = line.split("|")
                search_results.append(str(count) + ": " + show_name[0])
            if len(search_results) == 2:
                search_results.clear()
                search_results.append("-=(+)=- Error -=(+)=-")
                search_results.append("No Results Found, please try another search term.")
        return search_results
    
    def addShows(directory, name, cast, release_date, director, seasons, episodes):
        """Adds a Show to the Show.txt file, and returns an output
        to print out regarding the movie details that were entered."""
        with open(directory + "/shows.txt", "a", encoding="utf-8") as file:
            new_show = "\n" + name + "|" + cast + "|" + release_date + "|" + director + "|" + seasons + "|" + episodes
            file.write(new_show)
            file.close()
            output = list()
            output.append("-=(+)=- Show Details -=(+)=-")
            output.append("Name: " + name)
            output.append("Cast: " + cast)
            output.append("Release Date: " + release_date)
            output.append("Director: " + director)
            output.append("Seasons: " + seasons)
            output.append("Episodes: " + episodes)
        return output
    
    def addShowVerify(directory):
        """Collects and verifies that all the information
        provided to create a new Movie object is accurate
        and valid."""
        while True:
            show_name = input("-=(+)=- Add a Show -=(+)=-\nPlease enter in a show_name name\nTo exit type \"exit\"\n\nName: ")
            if "|" in show_name:
                raise ValueError("You cannot use \"|\" in the name please try again.")
            elif show_name == "exit":
                return False
            else:
                break

        while True:
            show_cast = input("-=(+)=- Add a Show -=(+)=-\nPlease enter in the cast of \"" + show_name + "\"\nTo exit type \"exit\"\n\nCast: ")
            if "|" in show_cast:
                raise ValueError("You cannot use \"|\" in the Cast please try again.")
            elif show_cast == "exit":
                return False
            else:
                break

        while True:
            show_release_date = input("-=(+)=- Add a Show -=(+)=-\nPlease enter in the release date of \"" + show_name + "\"\nTo exit type \"exit\"\n\nRelease Date:")
            if "|" in show_release_date: raise ValueError("You cannot use \"|\" in the release date please try again.")
            elif show_release_date == "exit":
                return False
            else:
                break

        while True:
            show_director = input("-=(+)=- Add a Show -=(+)=-\nPlease enter in the Director(s) of \"" + show_name + "\"\nTo exit type \"exit\"\n\nDirector(s): ")
            if "|" in show_director:
                raise ValueError("You cannot use \"|\" in the Director(s) please try again.")
            elif show_director == "exit":
                return False
            else:
                break
        while True:
            show_seasons = input("-=(+)=- Add a Show -=(+)=-\nPlease enter in the Seasons of \"" + show_name + "\"\nTo exit type \"exit\"\n\nSeasons: ")
            if "|" in show_seasons:
                raise ValueError("You cannot use \"|\" in the Seasons please try again.")
            elif show_seasons == "exit":
                return False
            else:
                break
        while True:
            show_episodes = input("-=(+)=- Add a Show -=(+)=-\nPlease enter in the total episodes of \"" + show_name + "\"\nTo exit type \"exit\"\n\nTotal Episodes:")
            if "|" in show_episodes:
                raise ValueError("You cannot use \"|\" in the Episodes please try again.")
            elif show_episodes == "exit":
                return False
            else:
                break
        
        return show_name, show_cast, show_release_date, show_director, show_seasons, show_episodes
            
    def delShow(directory):
        """Deletes a show out of the directory, returns
        Error or Success based on if the show was deleted
        or not"""
        while True:
            show_name = input("-=(+)=- Delete a Show -=(+)=-\nPlease enter the name of the Show you want to delete. \"\nTo exit type \"exit\"\n\nShow Name: ")
            if "|" in show_name:
                raise ValueError("You cannot use \"|\" in the Show Name please try again.")
            elif show_name == "exit":
                print("Now exiting...")
                return False
            else:
                delete_confirm = input("Are you sure you want to delete \"" + show_name + "\"\n")
                delete_confirm = delete_confirm.lower()
            if delete_confirm == "yes":
                line_pos = 0
                with open(directory + "/shows.txt", encoding="UTF-8") as file:
                    lines = file.readlines()
                    for line in lines:
                        search = re.search(show_name, line, flags=re.IGNORECASE)
                        if search != None:
                            break
                        else:
                            line_pos += 1
                            file.close()
                with open(directory + "/shows.txt", "r+", encoding="UTF-8") as file:
                    lines = file.readlines()
                    file.seek(0)
                    current_line_pos = 0
                    for line in lines:
                        if current_line_pos != line_pos:
                            file.write(line)
                            current_line_pos += 1
                            file.truncate()
                            return "-=(+)=- Delete a Show -=(+)=-\n\"" + show_name + "\" Successfully Deleted."
                        elif delete_confirm == "no":
                            print("Delete Denied, now exiting...")
                            return False