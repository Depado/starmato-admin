import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='starmato-admin',
    version='0.2.1',
    packages=find_packages(),
    package_data={
        'starmato.admin': [
            'templates/admin/*.*',
            'templates/admin/edit_inline/*.*',
            'templates/admin/includes/*.*',
            'media/admin/js/*.*',
            'media/admin/css/*.*',
            'media/admin/images/*.*',
            'locale/fr_FR/LC_MESSAGES/*.*'
        ],
    },
    license='MIT',
    description='A Django app to upgrade django admin.',
    url='http://www.go-tsunami.com/',
    author='GoTsunami',
    author_email='ab@go-tsunami.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
