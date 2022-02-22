"""
This code is desinged to visit the movie page of your liking and download 
all still frames images of the movie
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# from webdriver_manager.chrome import EdgeChromiumDriverManager -> if Browser is Edge
# from webdriver_manager.firefox import GeckoDriverManager -> if Browser is Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import os
from Manager import Manager


class ImageScraper(webdriver.Chrome, Manager):
    """
    this is the class that deals with all IMDB related stuff
    """

    def __init__(self):
        # This is made to ignore the annoying "Devtools listening" terminal messages
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        webdriver.Chrome.__init__(
            self,
            executable_path=ChromeDriverManager(log_level=1).install(),
            options=options,
        )

    # the EdgeChromiumDriverManager is replaced with the above commented importes
    # if the used browser is not edge

    def land_first_page(self):
        self.get("https://www.imdb.com/")

    def search_for_movie(self, movie_name):
        search_field = self.find_element(By.ID, "suggestion-search")
        search_field.clear()
        search_field.send_keys(movie_name)
        search_field.send_keys(Keys.ENTER)

    def reach_the_imgs(self):
        try:
            movie_link_element = self.find_element(
                By.XPATH, '//*[@id="main"]/div/div[2]/table/tbody/tr[1]/td[2]/a'
            )
            link = movie_link_element.get_attribute("href")  # open the movie page
            self.get(link)
        except:
            print("Movie Not Found")
            quit()
        # -------------------------------------------------------------
        self.get_movie_name()  # get the movie name to use it later
        # --------------------------------------------------------------
        images_link = self.find_element(
            By.CSS_SELECTOR, "a[data-testid='photos-title']"
        )  # Reach to the images page
        images_link.click()
        # ------------------------------------------------------------
        Filter = self.find_element(
            By.LINK_TEXT, "Still Frame"
        )  # select only still frames
        Filter.click()

    def download_image_scheme(self, download_path, url, file_name, num=0):
        """
        Function that downloads the given src url of an image (single image)
        """
        num += 1
        res = requests.get(url)
        with open(download_path + "\\" + file_name, "wb") as f:
            f.write(res.content)

    def download_all_images(self, MAIN_FOLDER, number=1):
        big_element = self.find_element(By.ID, "media_index_thumbnail_grid")
        elements = big_element.find_elements(By.TAG_NAME, "a")
        # ------------------------------------------------------------------
        # This part is present in both classes and made so that each class is independent of it's own
        # and can create the project dir if not exist
        if os.path.exists(os.path.join(MAIN_FOLDER, self._movie_name)):
            pass
        else:
            Manager.create_dirs(
                self, MAIN_FOLDER=MAIN_FOLDER, movie_name=self._movie_name
            )
        # ------------------------------------------------------------------
        # Iterate over each image and download
        for element in elements:
            try:
                img = element.find_element(By.TAG_NAME, "img")
            except:
                self.quit()
            img_src = img.get_attribute("src")
            complete_img_src = (
                img_src[: len(img_src) - 28] + img_src[len(img_src) - 4 :]
            )
            self.download_image_scheme(
                os.path.join(MAIN_FOLDER, f"{self._movie_name}\Material"),
                complete_img_src,
                f"img{number}.jpg",
            )
            number += 1
        try:
            next_button = self.find_element(By.XPATH, '//*[@id="right"]/a')
            next_button.click()

        except:
            self.quit()
        self.download_all_images(number=number)

    def get_movie_name(self):
        self._movie_name = self.find_element(
            By.XPATH,
            '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[1]/div[1]/h1',
        ).get_attribute("innerHTML")


class PosterScraper(webdriver.Chrome, Manager):
    """
    This is the class that deals with all IMB AWARDS related stuff
    """

    def __init__(self) -> None:
        # --------------------------------------------------------------
        # this block is made to ignore the annoying Devtools message of selenium
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # ---------------------------------------------------------------
        webdriver.Chrome.__init__(
            self,
            executable_path=ChromeDriverManager(log_level=1).install(),
            options=options,
        )

    def land_first_page(self):
        self.get("http://www.impawards.com/")

    def search_for_movie(self, movie_name):
        self.movie_name = movie_name
        search_bar = self.find_element(By.XPATH, '//*[@id="myNavbar"]/form/div/input')
        search_bar.clear()
        search_bar.send_keys(self.movie_name)
        search_bar.send_keys(Keys.ENTER)

    def download_images(self, MAIN_FOLDER):
        imgs = self.find_element(By.CSS_SELECTOR, "div[class='col-sm-12']")
        imgs_elements = imgs.find_elements(By.TAG_NAME, "a")
        num_for_iteration = 0
        num_for_posters = -2
        # -------------------------------------------------------------------
        for element in imgs_elements:
            num_for_iteration += 1
            num_for_posters += 1
            # -----------------------------------------------------------------
            if (
                num_for_iteration <= 2
            ):  # This is done because there is always 2 duplicates of the first element
                # so did what first come to my mind to try and igonre them
                self.get_movie_name_(href=element.get_attribute("href"))
                continue
            # -----------------------------------------------------------------
            # This block is responsilbe for extracting the complete src url for the image from the href of the web page element
            self.src1 = element.get_attribute("href")
            self.src2 = self.src1.replace("html", "jpg")
            complete_url = f"{self.src2[:30]+'posters/'+self.src2[30:]}"
            # ----------------------------------------------------------------
            # This part is present in both classes and made so that each class is independent of it's own
            # and can create the project dir if not exist
            if os.path.exists(os.path.join(MAIN_FOLDER, self._movie_name_)):
                pass
            else:
                Manager.create_dirs(
                    self, MAIN_FOLDER=MAIN_FOLDER, movie_name=self._movie_name_
                )
            # ------------------------------------------------------------------
            self.download_image_scheme(
                os.path.join(MAIN_FOLDER, f"{self._movie_name_}\Previous Posters"),
                complete_url,
                f"poster{num_for_posters}.jpg",
            )

    def download_image_scheme(self, download_path, url, file_name):
        res = requests.get(url)
        with open(download_path + "\\" + file_name, "wb") as f:
            f.write(res.content)

    def get_movie_name_(self, href):
        self._movie_name_ = href[30 : len(href) - 5].replace("_", " ").title()
