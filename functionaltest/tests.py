from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
MAX_WAIT = 10 

class NewVisitorTest(LiveServerTestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def wait_for_page_to_render_text_in_id(self, text, targetID):
        start_time = time.time()
        while True:  
            try:
                tag = self.browser.find_element_by_id(targetID)
                self.assertIn(text, tag.text)
                return  
            except (AssertionError, WebDriverException) as e:  
                if time.time() - start_time > self.MAX_WAIT:  
                    raise e  
                time.sleep(0.5)

    def homepage_get_method(self):

        self.browser.get(self.live_server_url)

        # He notices the homepage has pop up
        self.fail('Finish the test!')  
        self.wait_for_page_to_render_text_in_id('For calculator application with GET method','subtitle')
        
        # # He's looking for a login button and click it
        # self.assertIn('navbar_login',self.browser.page_source)
        # login_button = self.browser.find_element_by_id('navbar_login')
        # login_button.send_keys(Keys.ENTER) 

        # # He notice page have redirect to a login form
        # self.wait_for_page_to_render_text_in_id('','id_username')

        # # He's entering a username and password that given by his friend and click login
        # username = self.browser.find_element_by_id('id_username')
        # username.send_keys('steve')
        # password = self.browser.find_element_by_id('id_password')  
        # password.send_keys('123456')    
        # password.send_keys(Keys.ENTER)

        # # the page have redirect back to homepage
        # self.wait_for_page_to_render_text_in_id('','HomepageMainArea')

        # # He found himself login to the site in a navigation bar
        # self.assertIn('steve', self.browser.find_element_by_id('navbar_username').text)

        # # He also notice a login button has replace by a logout button
        # self.assertNotIn('navbar_login', self.browser.page_source)
        # self.assertIn('navbar_logout', self.browser.page_source)

        # # He click on a Share lecture button he saw on a navigation bar
        # self.assertIn('navbar_upload', self.browser.page_source)
        # self.browser.find_element_by_id('navbar_upload').send_keys(Keys.ENTER)

        # # the page redirect to upload page
        # self.wait_for_page_to_render_text_in_id('','UploadpageMainArea')

        # # He start adding photo of the lecture to the given form
        # # He filling some of the form and click upload
        # # the page is not allow him upload because some field are still empty
        # # He fillup the rest of the form and click upload again
        # # the page redirect to homepage
        # # He found his lecture showing up
        # # He click logout

