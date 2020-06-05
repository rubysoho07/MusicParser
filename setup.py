from setuptools import setup, find_packages

setup(
    name='MusicParser',
    version='1.0.1',
    url='https://github.com/rubysoho07/MusicParser',
    author='Yungon Park',
    author_email='hahafree12@gmail.com',
    description='Parsing music album from music information sites.',
    install_requires=[
        "requests == 2.20.0",
        "beautifulsoup4 == 4.6.0"
    ],
    packages=find_packages()
)
