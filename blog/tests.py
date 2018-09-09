import time
from django.test import TestCase, LiveServerTestCase
from selenium import webdriver


# class BasicTestWithSelenium(TestCase):
# 	@classmethod
# 	def setUpClass(cls):
# 		cls.driver = webdriver.Chrome()
# 		super(BasicTestWithSelenium, cls).setUpClass()
#
# 	@classmethod
# 	def tearDownClass(cls):
# 		super(BasicTestWithSelenium, cls).tearDownClass()
# 		cls.driver.quit()
#
# 	def test_if_post_name_is_ok(self):
# 		"""Verifies the name of fifth post in my local project"""
#
# 		self.driver.get('http://127.0.0.1:8000/post/5/')
# 		name = self.driver.find_element_by_class_name('page-header').text
# 		self.assertEqual('Z konsoli', name)
# 		time.sleep(2)
#
# 	def test_if_login_link_is_displayed_when_user_is_not_athenticated(self):
# 		"""Searching if login link is displayed when user isn't logged in"""
#
# 		self.driver.get('http://127.0.0.1:8000')
# 		draft_link = self.driver.find_element_by_partial_link_text('Log in').text
# 		self.assertEqual('Log in', draft_link)
# 		time.sleep(2)
#
#
# class PostsAndCommentsTest(LiveServerTestCase):
# 	def setUp(self):
# 		self.driver = webdriver.Chrome()
#
# 	def tearDown(self):
# 		self.driver.quit()
#
# 	def test_if_authenticated_user_can_add_new_post(self):
# 		pass
