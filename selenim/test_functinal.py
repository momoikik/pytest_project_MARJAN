from selenium.webdriver.common.by import By
import pytest
import time
from BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
@pytest.mark.functinal
class Testfunctinal(BaseClass):
    def test_delete_movie(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Check if the admin can add and delete a movie")
        setup.find_element(By.NAME, "Email").send_keys("Admin@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("Admin")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        len_images_first = len(setup.find_elements(By.XPATH, "//a[starts-with(@href,'/movie_info')]"))
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
        setup.find_element(By.NAME, "filename").send_keys("C:\Mean Girls.jpg ")
        setup.find_element(By.NAME, "movie_title").send_keys("hanny")
        setup.find_element(By.NAME, 'description').send_keys("that so cute")
        setup.find_element(By.NAME, 'director').send_keys("Marjan")
        setup.find_element(By.NAME, 'release_year').send_keys("1998")
        setup.find_element(By.NAME, 'actors').send_keys("Marjan,Noor,Ahmad,Samer")
        time.sleep(2)
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        len_images_second = len(setup.find_elements(By.XPATH, "//a[starts-with(@href,'/movie_info')]"))
        assert len_images_first + 1 == len_images_second,\
                self.getLooger().error("is not add the movie")
        self.getLooger().info("Pass:the movie has been adding ")
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/functinal_test/movie_homepage_before_delete1.png")
        len_images_first = len(setup.find_elements(By.XPATH, "//a[starts-with(@href,'/movie_info_admin')]"))

        setup.find_element(By.XPATH, f"//body/a[{len_images_first + 1}]/img[1]").click()
        setup.find_element(By.XPATH, "//a[starts-with(@href,'/delete')]").click()
        len_images_second = len(setup.find_elements(By.XPATH, "//a[starts-with(@href,'/movie_info')]"))
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/functinal_test/movie_homepage_after_delete2.png")
        assert len_images_first - 1 == len_images_second,\
                self.getLooger().error("the movie has not been deleted")
        self.getLooger().info("Pass:the movie has been deleted")

    def test_add_movie(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Check if the admin can add  a new movie")
        setup.find_element(By.NAME, "Email").send_keys("Admin@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("Admin")


        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        setup.get_screenshot_as_file("screenshot/functinal_test/movie_homepage_before_add.png")
        len_images_first = len(setup.find_elements(By.XPATH, "//a[starts-with(@href,'/movie_info')]"))
        setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
        setup.find_element(By.NAME, "filename").send_keys("C:\Mean Girls.jpg ")
        setup.find_element(By.NAME, "movie_title").send_keys("hanny")
        setup.find_element(By.NAME, 'description').send_keys("that so cute")
        setup.find_element(By.NAME, 'director').send_keys("Marjan")
        setup.find_element(By.NAME, 'release_year').send_keys("1998")
        setup.find_element(By.NAME, 'actors').send_keys("Marjan,Noor,Ahmad,Samer")
        time.sleep(2)
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        setup.get_screenshot_as_file("screenshot/functinal_test/new movie.png")
        len_images_second = len(setup.find_elements(By.XPATH, "//a[starts-with(@href,'/movie_info')]"))
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/functinal_test/movie_homepage_after_delete3.png")
        assert len_images_first + 1 == len_images_second,\
                self.getLooger().error(" The new movie has not been added")
        self.getLooger().info("Pass:the movie has been adding")

    def test_alter_title_description(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Admin check if the movie title and description have changed "
                              "after he put the information in the alter page")
        setup.find_element(By.NAME, "Email").send_keys("Admin@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("Admin")
        # button[type='submit']
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        # alter
        # chaing the description and movie title(test case 1)
        setup.find_element(By.XPATH, "//body[1]/a[6]/img[1]").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/functinal_test/movie_before_alter_title.png")
        setup.find_element(By.XPATH, "//a[starts-with(@href,'/alter_movie')]").click()
        time.sleep(2)
        setup.find_element(By.NAME, "movie_title").send_keys("goood")
        setup.find_element(By.NAME, 'description').send_keys("that so cute")

        time.sleep(2)
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/functinal_test/movie_after_alter_title.png")
        assert setup.find_element(By.TAG_NAME, "h1").text == "goood",\
                self.getLooger().error("The movie title has not changed")

        self.getLooger().info("Pass:The movie title has changed")
        assert setup.find_element(By.CSS_SELECTOR, "body ul li:nth-child(2)").text == "that so cute",\
                self.getLooger().error("The movie description has not changed")
        self.getLooger().info("Pass:The movie description has  changed")

    def test_alter_director_year_actors(self, setup):
        # chaing the actors and director and release_year(test case 2)
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Admin check if the movie director and year and actors have changed "
                              "after he put the information in the alter page")
        setup.find_element(By.NAME, "Email").send_keys("Admin@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("Admin")
        # button[type='submit']
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        # alter
        # chaing the description and movie title(test case 1)
        setup.find_element(By.XPATH, "//body[1]/a[6]/img[1]").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/functinal_test/movie_before_alter_director.png")
        setup.find_element(By.XPATH, "//a[starts-with(@href,'/alter_movie')]").click()

        time.sleep(2)

        setup.find_element(By.NAME, 'director').send_keys("Marjan")
        setup.find_element(By.NAME, 'release_year').send_keys("1998")
        setup.find_element(By.NAME, 'actors').send_keys("Marjan,Noor,Ahmad,Samer")
        time.sleep(2)
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        setup.get_screenshot_as_file("screenshot/functinal_test/movie_after_alter_director.png")
        assert setup.find_element(By.CSS_SELECTOR, "body ul li:nth-child(4)").text == "Marjan",\
                self.getLooger().error("The movie director has not changed")
        self.getLooger().info("Pass:The movie director has changed")
        assert setup.find_element(By.CSS_SELECTOR, "body ul li:nth-child(6)").text == "1998",\
                self.getLooger().error("The movie release year has not changed")
        self.getLooger().info("Pass:The movie release year has changed")
        assert setup.find_element(By.CSS_SELECTOR, "body ul li:nth-child(8)").text == "Marjan,Noor,Ahmad,Samer",\
                self.getLooger().error("The movie actors has not changed")
        self.getLooger().info("Pass:The movie actors has  changed")

    def test_add_review_name(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Check if the user can write his name and review ")
        setup.find_element(By.NAME, "Email").send_keys("marjanik@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("123456")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        # check if the review and name is written(test case3)

        setup.find_element(By.XPATH, "//body/a[5]/img[1]").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/functinal_test/review_before_add_name.png")
        setup.find_element(By.NAME, 'name').send_keys("hnan")
        setup.find_element(By.NAME, 'review_text').send_keys("so gooood")

        time.sleep(2)
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/functinal_test/review_after_add_name.png")
        elements = setup.find_elements(By.CLASS_NAME, "movie_review")
        for x in elements:
            if x.find_element(By.CLASS_NAME, "movie_review_name").text == "hnan" and \
                    x.find_element(By.CLASS_NAME, "movie_review_text").text == "so gooood":
                name_review = "name and review is written"

        assert name_review == "name and review is written",\
                self.getLooger().error("review and name is not written")
        self.getLooger().info("Pass:review and name is written")

    def test_add_name_rating(self, setup):
        # check if the rating and name written(test case 4)

        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Check if the user can write his name and rating")
        setup.find_element(By.NAME, "Email").send_keys("marjanik@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("123456")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.find_element(By.XPATH, "//body/a[6]/img[1]").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/functinal_test/review_before_add_rating.png")
        setup.find_element(By.NAME, 'name').send_keys("noor")
        setup.find_element(By.NAME, "rating").send_keys("7")
        time.sleep(2)
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/functinal_test/review_after_add_rating.png")
        elements = setup.find_elements(By.CLASS_NAME, "movie_review")
        for z in elements:
            if z.find_element(By.CLASS_NAME, "movie_review_rating").text == "7" \
                    and z.find_element(By.CLASS_NAME, "movie_review_name").text == "noor":
                name_rating = " written"
        assert name_rating == " written",\
                self.getLooger().error("rating and name is not written")
        self.getLooger().info("Pass:rating and name is written")





