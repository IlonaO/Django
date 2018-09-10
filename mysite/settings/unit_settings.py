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
    '--attr=!selenium_test,!db,!rpc,!todo',
    # '--with-coverage',
    '--with-doctest',
]
SELENIUM_DIR = os.path.join(BASE_DIR, 'selenium')
if os.path.exists(SELENIUM_DIR):
    NOSE_ARGS.append('--exclude-dir=%s' % SELENIUM_DIR)

TEST_OUTPUT_FILE = os.path.join(TESTS_OUTPUT_PATH, 'test-output.html')

