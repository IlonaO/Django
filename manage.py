#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings.local")
	try:
		from django.core.management import execute_from_command_line
	except ImportError:
		try:
			import django  # noqa: F401
		except ImportError:
			raise ImportError("Couldn't import Django")
		raise

	is_testing = 'test' in sys.argv

	if is_testing:
		import coverage

		cov = coverage.coverage()
		cov.erase()
		cov.start()

	execute_from_command_line(sys.argv)

	if is_testing:
		cov.stop()
		cov.save()
		cov.html_report()
