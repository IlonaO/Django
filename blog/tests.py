import time
from datetime import datetime, timezone

from django.test import TestCase, LiveServerTestCase
from django.test.client import Client
from django.contrib.auth.models import User
from nose.plugins.attrib import attr
from selenium import webdriver

from blog.forms import PostForm, CommentForm
from blog.models import Post, Comment


@attr('db')
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


@attr('db')
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


@attr('db')
class ViewsTestCase(TestCase):
	def setUp(self):
		self.client = Client()
		self.user = User.objects.create_user(username='someuser',
											 email='user@test.com',
											 password='somepassword')
		self.superuser = User.objects.create_superuser(username='superuser',
													   email='superuser@test.com',
													   password='somepassword')
		self.post = Post.objects.create(author=self.user, title='Post title',
										text='Post content',
										created_date=datetime(2017, 8, 2, 8, 7, 53,
															  tzinfo=timezone.utc),
										published_date=datetime(2017, 8, 2, 8, 7, 59,
																tzinfo=timezone.utc))
		self.post2 = Post.objects.create(author=self.user, title='Post title2',
										 text='Post content2',
										 created_date=datetime(2017, 8, 3, 8, 7, 53,
															   tzinfo=timezone.utc))
		self.post3 = Post.objects.create(author=self.user, title='Post title3',
										 text='Post content3')
		self.comment = Comment.objects.create(post=self.post2, author=self.user.username,
											  text='some comment',
											  created_date=datetime(2017, 8, 3, 14, 14, 3,
																	tzinfo=timezone.utc))

	def tearDown(self):
		self.client = None
		self.user = None
		self.superuser = None
		self.post = None
		self.post2 = None
		self.post3 = None
		self.comment = None

	def test_post_list(self):
		response = self.client.get('/')
		self.assertEqual(response.status_code, 200, "status code is not what should be")
		self.assertTemplateUsed(response, 'blog/post_list.html')
		self.assertSequenceEqual(response.context['posts'], [self.post])

	def test_post_detail_published_date(self):
		response = self.client.get('/post/1/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_detail.html')
		self.assertEqual(response.context['post'], self.post)

	def test_post_detail_created_date(self):
		response = self.client.get('/post/2/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_detail.html')
		self.assertEqual(response.context['post'], self.post2)

	def test_post_not_existing(self):
		response = self.client.get('/post/99/')
		self.assertEqual(response.status_code, 404)
		assert '<h1>Not Found</h1><p>The requested URL /post/99/ was' \
			   ' not found on this server.</p>' in response.content.decode('utf-8')

	def test_post_new(self):
		self.client.login(username='someuser', password='somepassword')
		response = self.client.post('/post/new/', {"title": "Lorem", "text": "Ipsum"})
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/post/4/')

	def test_post_new_form_not_valid(self):
		self.client.login(username='someuser', password='somepassword')
		response = self.client.post('/post/new/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_edit.html')

	def test_post_new_get_request(self):
		self.client.login(username='someuser', password='somepassword')
		response = self.client.get('/post/new/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_edit.html')

	def test_post_new_without_user(self):
		response = self.client.get('/post/new/')
		self.assertEqual(response.status_code, 302)

	def test_post_edit(self):
		self.client.login(username='superuser', password='somepassword')
		response = self.client.post('/post/1/edit/', {"title": "Lorem", "text": "Lorem Ipsum"})
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/post/1/')

	def test_post_edit_get_request(self):
		self.client.login(username='superuser', password='somepassword')
		response = self.client.get('/post/1/edit/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_edit.html')

	def test_post_draft_list(self):
		self.client.login(username='superuser', password='somepassword')
		response = self.client.get('/drafts/')
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/post_draft_list.html')
		self.assertSequenceEqual(response.context['posts'], [self.post2, self.post3])

	def test_post_publish(self):
		self.client.login(username='superuser', password='somepassword')
		response = self.client.post('/post/1/publish/')
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/post/1/')

	def test_post_publish_not_found(self):
		self.client.login(username='superuser', password='somepassword')
		response = self.client.post('/post/99/publish/')
		self.assertEqual(response.status_code, 404)

	def test_post_remove(self):
		self.client.login(username='superuser', password='somepassword')
		response = self.client.post('/post/1/remove/')
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/')

	def test_post_remove_not_found(self):
		self.client.login(username='superuser', password='somepassword')
		response = self.client.post('/post/99/remove/')
		self.assertEqual(response.status_code, 404)

	def test_add_comment_to_post(self):
		response = self.client.post('/post/2/comment/',
									{"author": "comment author", "text": "some comment"})
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/post/2/')

	def test_add_comment_to_post_not_found(self):
		response = self.client.post('/post/99/comment/',
									{"author": "comment author", "text": "some comment"})
		self.assertEqual(response.status_code, 404)

	def test_add_comment_to_post_get_request(self):
		response = self.client.get('/post/2/comment/',
									{"author": "comment author", "text": "some comment"})
		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'blog/add_comment_to_post.html')

	def test_comment_approve(self):
		self.client.login(username='superuser', password='somepassword')
		response = self.client.get('/comment/1/approve/')
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/post/2/')

	def test_comment_approve_not_found(self):
		self.client.login(username='superuser', password='somepassword')
		response = self.client.get('/comment/99/approve/')
		self.assertEqual(response.status_code, 404)

	def test_comment_remove(self):
		self.client.login(username='superuser', password='somepassword')
		response = self.client.get('/comment/1/remove/')
		self.assertEqual(response.status_code, 302)
		self.assertRedirects(response, '/post/2/')

	def test_comment_remove_not_found(self):
		self.client.login(username='superuser', password='somepassword')
		response = self.client.get('/comment/99/remove/')
		self.assertEqual(response.status_code, 404)


# @attr('selenium_test')
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
