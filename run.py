"""
Developed By Kareem Mahlees
"""

from multiprocessing import Process
from Poster_Maker import ImageScraper
from Poster_Maker import PosterScraper
from gui import Gui


def Process_1(movie, MAIN_FOLDER):
    inst1 = ImageScraper()
    inst1.land_first_page()
    inst1.search_for_movie(movie)
    inst1.reach_the_imgs()
    inst1.download_all_images(MAIN_FOLDER=MAIN_FOLDER)


def Process_2(movie, MAIN_FOLDER):
    inst2 = PosterScraper()
    inst2.land_first_page()
    inst2.search_for_movie(movie)
    inst2.download_images(MAIN_FOLDER=MAIN_FOLDER)


def main_function(movie_name, MAIN_FOLDER):
    if __name__ == "__main__":

        p1 = Process(target=Process_1, args=[movie_name, MAIN_FOLDER])
        p2 = Process(target=Process_2, args=[movie_name, MAIN_FOLDER])

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        inst3.when_finished()


# this is done so as tkinter doens't open 2 additional windows
if __name__ == "__main__":
    inst3 = Gui()
    inst3.splash_screen(main_function=main_function)
