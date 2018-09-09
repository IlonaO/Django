import time
from datetime import datetime, timezone

from django.test import TestCase, LiveServerTestCase
from django.contrib.auth.models import User
from selenium import webdriver

from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment


class PostTestCase(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='someuser',
											 email='user@test.com',
											 password='somepassword')
		self.post = Post.objects.create(author=self.user, title='Post title',
										text='Post content',
										created_date=datetime(2017, 8, 2, 8, 7, 53,
															  tzinfo=timezone.utc))
		self.post2 = Post.objects.create(author=self.user, title='Post title2',
										 text='Post content2',
										 created_date=datetime(2017, 8, 3, 8, 7, 53,
															   tzinfo=timezone.utc))
		self.comment = Comment.objects.create(post=self.post2, author=self.user.username,
											  text='some comment', approved_comment=True,
											  created_date=datetime(2017, 8, 3, 14, 14, 3,
																	tzinfo=timezone.utc))

	def tearDown(self):
		self.user = None
		self.post = None
		self.post2 = None
		self.comment = None

	def test_publish(self):
		self.assertEqual(self.post.published_date, None)
		self.post.publish()
		self.assertNotEqual(self.post.published_date, None)

	def test_approved_comments_without_comments(self):
		self.assertSequenceEqual(self.post.approved_comments(), [])

	def test_approved_comments_with_comments(self):
		self.assertSequenceEqual(self.post2.approved_comments(), [self.comment])

	def test_str(self):
		self.assertEqual(str(self.post), "Post title")
		self.assertEqual(str(self.post2), "Post title2")


class CommentTestCase(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='someuser',
											 email='user@test.com',
											 password='somepassword')
		self.post = Post.objects.create(author=self.user, title='Post title',
										text='Post content',
										created_date=datetime(2017, 8, 2, 8, 7, 53,
															  tzinfo=timezone.utc))
		self.comment = Comment.objects.create(post=self.post, author=self.user.username,
											  text='some comment',
											  created_date=datetime(2017, 8, 3, 14, 14, 3,
																	tzinfo=timezone.utc))

	def tearDown(self):
		self.user = None
		self.post = None
		self.comment = None

	def test_approve(self):
		self.assertFalse(self.comment.approved_comment)
		self.comment.approve()
		self.assertTrue(self.comment.approved_comment)

	def test_str(self):
		self.assertEqual(str(self.comment), "some comment")


class FormsTestCase(TestCase):
	def test_post_form(self):
		form_data = {'title': 'sometitle', 'text': 'sometext'}
		form = PostForm(data=form_data)
		self.assertTrue(form.is_valid())

	def test_comment_form(self):
		form_data = {'author': 'someuser', 'text': 'sometext'}
		form = CommentForm(data=form_data)
		self.assertTrue(form.is_valid())


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
