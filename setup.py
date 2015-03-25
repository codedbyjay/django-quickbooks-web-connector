import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-quickbooks-web-connector',
    version='0.1',
    packages=['quickbooks_web_connector'],
    include_package_data=True,
    license='GPL v2 License',  
    description='A simple quickbooks-web-connector Django library',
    long_description=README,
    url='',
    author='Jean-Mark Wright',
    author_email='jeanmark.wright@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL v2 License', 
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires = [line for line in open("requirements.txt").read().splitlines() if not line.startswith("#")]

)