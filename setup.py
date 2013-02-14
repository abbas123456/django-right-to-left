import os
from setuptools import setup


PROJECT_DIR = os.path.dirname(__file__)

setup(
    name = 'django-right-to-left',
    packages = ['rtl'],
    version = '0.1',
    license = 'BSD',
    keywords = 'Django, translation, internationalization, righ to left, bidi',
    description = 'A django template loader that looks for a right to left version of a template if the activated language is a right to left language (e.g Arabic, Hebrew)',
    long_description=open(os.path.join(PROJECT_DIR, 'README.rst')).read(),
    author='Mohammad Abbas',
    author_email='mohammad.abbas86@gmail.com',
    url='https://github.com/abbas123456/django-right-to-left',
    classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internationalization'],
)