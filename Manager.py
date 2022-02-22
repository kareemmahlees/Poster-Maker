"""
This code is desinged to create a full working directory for the movie you want to 
make a poster
"""
import os
from gui import Gui


class Manager(Gui):
    """
    class responsible for creating the dirs and psd file in the project folder
    """

    def create_dirs(self, movie_name, MAIN_FOLDER):
        self.movie_name = movie_name
        os.chdir(
            MAIN_FOLDER
        )  # changing the current working direcory to make our lifes easier
        os.makedirs(
            f".\{self.movie_name}\Material",
        )
        os.makedirs(
            f".\{self.movie_name}\Final",
        )
        os.makedirs(f".\{self.movie_name}\Previous Posters")
        os.chdir(os.path.join(MAIN_FOLDER, self.movie_name))
        os.system(
            f'type nul > "{self.movie_name}.psd"'
            if os.name == "nt"
            else f"touch {self.movie_name}"
        )
