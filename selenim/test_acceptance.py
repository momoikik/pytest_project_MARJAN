from selenium.webdriver.common.by import By
import pytest
import time

from BaseClass import BaseClass
@pytest.mark.usefixtures("setup")
@pytest.mark.acceptance
class Testsecurity(BaseClass):
    # 1111111111
    def test_Home_page_button(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Clicking on the home page icon takes the user back to the home page")
        setup.find_element(By.NAME, "Email").send_keys("marjanik@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("123456")
        # button[type='submit']
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        # return into homepage by click in the homepageicon
        # number of image on home page
        number_image_in_homepage = len(setup.find_elements(By.XPATH, "//a[starts-with(@href,'/movie_info/')]"))
        setup.find_element(By.XPATH, "//a[starts-with(@href,'/movie_info/6')]").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/acceptance_test/movie_page.png")
        # after click on a movie
        time.sleep(2)
        # back to home page
        setup.find_element(By.CSS_SELECTOR, "a[href='/Home_page']").click()
        number_imagepage = len(setup.find_elements(By.XPATH, "//a[starts-with(@href,'/movie_info/')]"))
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/acceptance_test/home_page.png")
        assert number_image_in_homepage == number_imagepage,\
            self.getLooger().error("user not in the homepage")
        self.getLooger().info("Pass:user in the homepage")

    def test_search_exist_movie_open_image(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("check if the search result open page"
                              " appear image of the movie")
        # search movie that is in the movie list
        ##to check if the search apper the image of the specific movie
        # 1111111
        setup.find_element(By.NAME, "Email").send_keys("marjanik@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("123456")
        # button[type='submit']
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        setup.find_element(By.CSS_SELECTOR, "input[name='search_string']").send_keys("HAROLD AND MAUDE")
        setup.find_element(By.XPATH, "//input[@type='image']").click()
        setup.get_screenshot_as_file("screenshot/acceptance_test/movie_image.png")
        assert setup.find_element(By.XPATH, "//input[@type='image']").is_displayed(),\
            self.getLooger().error("the image is not appear")
        self.getLooger().info("Pass:movie image after search is appear")

    def test_serch_exist_movie_open_movie(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("check if the search result open page"
                              " appear in it a movie image and clicking in the "
                              "image open the movie information page")
        setup.find_element(By.NAME, "Email").send_keys("marjanik@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("123456")
        # button[type='submit']
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        setup.find_element(By.CSS_SELECTOR, "input[name='search_string']").send_keys("BOOKSMART")
        setup.find_element(By.XPATH, "//input[@type='image']").click()
        assert setup.find_element(By.XPATH, "//input[@type='image']").is_displayed(),\
            self.getLooger().error("the image is not appear")
        self.getLooger().info("Pass:movie image after search is appear")
        time.sleep(3)
        setup.find_element(By.XPATH, "//a[starts-with(@href,'/movie_info/')]").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/acceptance_test/movie_page.png")
        assert setup.find_element(By.TAG_NAME, "h1").text == "BOOKSMART",self.getLooger().error("clicking in the "
                              "image did not open the movie information page")
        self.getLooger().info("Pass:click in the image after search the movie open movie page ")

    def test_unexistmovie(self, setup):
        self.getLooger ().info("movie name that is not in the site")
        setup.get("http://127.0.0.1:5000/")
        setup.find_element(By.NAME, "Email").send_keys("marjanik@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("123456")

        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        setup.find_element(By.CSS_SELECTOR, "input[name='search_string']").send_keys("marjan movie")
        setup.find_element(By.XPATH, "//input[@type='image']").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/acceptance_test/non_page.png")
        assert len(setup.find_elements(By.XPATH,"//a[starts-with(@href,'/movie_info/')]")) == 0, \
            self.getLooger().error("shold not return a movie image")
        self.getLooger().info("Pass:return empty page")

    def test_sign_in_button_working(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Check if pressing the register button opens the sign in page")
        setup.find_element(By.CSS_SELECTOR, "a[href$='/Sign_in']").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/acceptance_test/sign_inpage.png")
        assert setup.current_url == "http://127.0.0.1:5000/Sign_in", \
            self.getLooger().error("Clicking the register button does not open the sign in page")
        self.getLooger().info("Pass,Clicking the register button open the sign in page")