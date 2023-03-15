from selenium.webdriver.common.by import By
import pytest
import time
from BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
@pytest.mark.Smoke
class TestSmoke(BaseClass):
        def test_admin_homepage1(self, setup):
                setup.get("http://127.0.0.1:5000/")
                self.getLooger().info("Writing the admin details opens the admin account (home_page_admin)")
                setup.find_element(By.NAME, "Email").send_keys("Admin@gmail.com")
                setup.find_element(By.NAME, "password").send_keys("Admin")
                setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
                time.sleep(2)
                #setup.execute_script("document.body.style.zoom='60%'")
                setup.get_screenshot_as_file("screenshot/smoke_test/admin_account1.png")
                assert setup.current_url == "http://127.0.0.1:5000/Home_page_Admin",\
                self.getLooger().error("The admin home page has not been opened")
                self.getLooger().info("Pass:The admin home page has been opened")
        def test_Add_page_open2(self, setup):
                setup.get("http://127.0.0.1:5000/")
                self.getLooger().info("Check if the alter page in the admin account exists")
                setup.find_element(By.NAME, "Email").send_keys("Admin@gmail.com")
                setup.find_element(By.NAME, "password").send_keys("Admin")
                setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
                time.sleep(2)
                setup.find_element(By.CSS_SELECTOR, "a[href='/add_data']").click()
                time.sleep(2)
                setup.get_screenshot_as_file("screenshot/smoke_test/add_page2.png")
                assert setup.current_url == "http://127.0.0.1:5000/add_data",\
                self.getLooger().error("The alter page in the admin account does not exist")
                self.getLooger().info("Pass,The alter page in the admin account opened")


        def test_Log_in_User3(self, setup):
                setup.get("http://127.0.0.1:5000/")
                self.getLooger().info("Writing the user details opens the admin account (home_page")
                setup.find_element(By.NAME, "Email").send_keys("marjanik@gmail.com")
                setup.find_element(By.NAME, "password").send_keys("123456")
                setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
                time.sleep(2)
                #setup.execute_script("document.body.style.zoom='60%'")
                setup.get_screenshot_as_file("screenshot/smoke_test/user_homepage3.png")
                assert setup.current_url == "http://127.0.0.1:5000/Home_page",\
                self.getLooger().error("The user account has not been opened")
                self.getLooger().info("Pass:The user account has been opened")

        def test_movie_info_pageuser_open4(self, setup):
                setup.get("http://127.0.0.1:5000/")
                self.getLooger().info("Check if clicking on a specific image opens the movie page for "
                                      "the user, the URL of the specified movie")
                setup.find_element(By.NAME, "Email").send_keys("marjanik@gmail.com")
                setup.find_element(By.NAME, "password").send_keys("123456")
                setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
                time.sleep(2)
                url_movie_info = setup.find_element(By.XPATH, "//a[starts-with(@href,'/movie_info/1')]").get_attribute(
                        "href")
                setup.find_element(By.XPATH, "//a[starts-with(@href,'/movie_info/1')]").click()
                #setup.execute_script("document.body.style.zoom='60%'")
                setup.get_screenshot_as_file("screenshot/smoke_test/movie_info_page4.png")
                assert setup.current_url == url_movie_info,\
                self.getLooger().error("The movie page is not shown to the user")
                self.getLooger().info("Pass:The movie page is not shown to the user")

        def test_movie_info_pageuser_open5(self, setup):
                setup.get("http://127.0.0.1:5000/")
                self.getLooger().info("Check if clicking on a specific image opens the movie page for "
                                      "the user, the URL of the specified movie")
                setup.find_element(By.NAME, "Email").send_keys("marjanik@gmail.com")
                setup.find_element(By.NAME, "password").send_keys("123456")
                setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
                time.sleep(2)
                url_movie_info = setup.find_element(By.XPATH, "//a[starts-with(@href,'/movie_info/1')]").get_attribute(
                        "href")
                setup.find_element(By.XPATH, "//a[starts-with(@href,'/movie_info/1')]").click()
                #setup.execute_script("document.body.style.zoom='60%'")
                setup.get_screenshot_as_file("screenshot/smoke_test/movie_info_page5.png")
                assert setup.current_url == url_movie_info,\
                self.getLooger().error("The movie page is not shown to the user")
                self.getLooger().info("Pass:The movie page is not shown to the user")

        def test_movie_info_pageadmin_open6(self, setup):
                setup.get("http://127.0.0.1:5000/")
                self.getLooger().info("Check if clicking on a specific image opens the movie page for "
                                      "the admin, the URL of the specified movie")
                self.getLooger().info("Check if the alter page in the admin account exists")
                setup.find_element(By.NAME, "Email").send_keys("Admin@gmail.com")
                setup.find_element(By.NAME, "password").send_keys("Admin")
                setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
                time.sleep(1)
                url_movie_info = setup.find_element(By.XPATH, "//a[starts-with(@href,'/movie_info_admin/2')]").get_attribute(
                        "href")
                setup.find_element(By.XPATH, "//a[starts-with(@href,'/movie_info_admin/2')]").click()
                #setup.execute_script("document.body.style.zoom='60%'")
                setup.get_screenshot_as_file("screenshot/smoke_test/movie_info_pageAdmin6.png")
                assert setup.current_url == url_movie_info, \
                        self.getLooger().error("The movie page is not shown to the admin")
                self.getLooger().info("Pass:The movie page is not shown to the admin")
