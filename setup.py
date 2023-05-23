from setuptools import setup, find_packages

setup(
    name='MusicParser',
    version='1.0.2',
    url='https://github.com/rubysoho07/MusicParser',
    author='Yungon Park',
    author_email='hahafree12@gmail.com',
    description='Parsing music album from music information sites.',
    install_requires=[
        "requests==2.31.0",
        "beautifulsoup4==4.11.1"
    ],
    packages=find_packages()
)
