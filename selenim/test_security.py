from selenium.webdriver.common.by import By
import pytest
import time

from BaseClass import BaseClass
@pytest.mark.usefixtures("setup")
@pytest.mark.security
class Testsecurity(BaseClass):

#    def test_sign_in(self, setup):
#        setup.get("http://127.0.0.1:5000/")
#        self.getLooger().info("A new user can register to create a account")
#        setup.find_element(By.CSS_SELECTOR, "a[href='/Sign_in']").click()
#        setup.find_element(By.NAME, "Email").send_keys("gog@gmail.com")
#        setup.find_element(By.NAME, "password").send_keys("986")
 #       setup.find_element(By.NAME, "Name").send_keys("gfh")
  #      setup.find_element(By.NAME, "phone_number").send_keys("34567")
 #       setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
  #      setup.find_element(By.NAME, "Email").send_keys("gog@gmail.com")
  #      setup.find_element(By.NAME, "password").send_keys("986")

   #     setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    #    time.sleep(2)
    #    Ur_page = setup.current_url
   #     assert Ur_page == "http://127.0.0.1:5000/Home_page",\
    #        self.getLooger().error("Failed to add an account for the new user")
     #   self.getLooger().info("Pass:succeeded in adding an account for the new user")

    def test_incorrect_details1(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Writing wrong details prevents the browser from entering the site to the home page")
        setup.find_element(By.NAME, "Email").send_keys("marj@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("123456")

        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/security_test/page_incorrect_details1.png")
        assert setup.current_url == "http://127.0.0.1:5000/Log_in",\
            self.getLooger().error("The user entered into the site although the details are incorrect")
        self.getLooger().info("Pass:the user failed to login to the account")

    def test_message_incorrect2(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Writing wrong details shows to the browser a message ")
        setup.find_element(By.NAME, "Email").send_keys("marj@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("123456")
        # button[type='submit']
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/security_test/message_incorrect2.png")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(2)

        assert setup.find_element(By.CSS_SELECTOR, "body center h2").text == "Incorrect Email or password !",\
            self.getLooger().error("The message did not appear when the wrong details were typed")
        self.getLooger().info("Pass,The message incorrect email or password appear when the wrong details were typed")

    def test_admin_account(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info(" Check if the account of admin contains hreh for delete, alter and add movie")
        setup.find_element(By.NAME, "Email").send_keys("Admin@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("Admin")
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)
        assert setup.find_element(By.XPATH, "//a[starts-with(@href,'/add_data')]").is_displayed(),\
            self.getLooger().error("href for add movie does not appear")
        self.getLooger().info("Pass:href for add movie appear")
        setup.find_element(By.XPATH, "//body[1]/a[5]/img[1]").click()
        assert setup.find_element(By.XPATH, "//a[starts-with(@href,'/alter_movie')]").is_displayed(),\
            self.getLooger().error("href for alter movie does not appear")
        self.getLooger().info("Pass:href for alter movie appear")
        assert setup.find_element(By.XPATH, "//a[starts-with(@href,'/delete')]").is_displayed(),\
            self.getLooger().error("href for delete movie does not appear")
        self.getLooger().info("Pass,href for delete movie appear")

    def test_incorrect_email_format3(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Check if the user has entered an email ")
        setup.find_element(By.CSS_SELECTOR, "a[href='/Sign_in']").click()
        setup.find_element(By.NAME, "Email").send_keys("dfgh")
        setup.find_element(By.NAME, "password").send_keys("fhfg")
        setup.find_element(By.NAME, "Name").send_keys("cfgh")
        setup.find_element(By.NAME, "phone_number").send_keys("0545657898")

        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/security_test/incorrect_email_format3.png")
        assert setup.find_element(By.CSS_SELECTOR, "body center h2").text == "Incorrect Email Format !",\
            self.getLooger().error("The message did not appear")
        self.getLooger().info("Pass,the message incorrect email format appear")

    def test_Existing_account4(self, setup):
        setup.get("http://127.0.0.1:5000/")
        self.getLooger().info("Try adding existing account ")
        setup.find_element(By.CSS_SELECTOR, "a[href='/Sign_in']").click()
        setup.find_element(By.NAME, "Email").send_keys("hwr@gmail.com")
        setup.find_element(By.NAME, "password").send_keys("67897899")
        setup.find_element(By.NAME, "Name").send_keys("fgdfg")
        setup.find_element(By.NAME, "phone_number").send_keys("0786456")
        # button[type='submit']
        setup.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        #setup.execute_script("document.body.style.zoom='60%'")
        setup.get_screenshot_as_file("screenshot/security_test/message_exists_email4.png")
        assert setup.find_element(By.CSS_SELECTOR, "body center h2").text == "Email already exists !",\
            self.getLooger().error("The message did not appear")
        self.getLooger().info("Pass:the message email already exists")