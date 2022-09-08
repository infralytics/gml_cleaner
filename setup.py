from setuptools import setup, find_packages


with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='gml-cleaner',
    license='MIT',
    license_files='LICENSE.txt',
    description='Gml cleaner is a python library for manupulating data and meta data.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='1.0',
    url='https://github.com/infralytics/gml_cleaner',
    author='Wouter van Riel',
    author_email='wouter.van.riel@infralytics.org',
    packages=find_packages(
        include=['gml_cleaner']),
    install_requires=['setuptools'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Text Processing :: Markup :: XML'
        ]
    )
