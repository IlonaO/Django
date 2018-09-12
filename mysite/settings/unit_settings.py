from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}


TESTS = True
TESTS_OUTPUT_PATH = '/tests'

TEST_RUNNER = 'myvenv.lib.testrunner.NoseTestRunner'

NOSE_ARGS = [
    '--attr=!selenium_test,!db,!todo',
    '--with-doctest',
	'--exe',
]

TEST_OUTPUT_FILE = os.path.join(TESTS_OUTPUT_PATH, 'test-output.html')

