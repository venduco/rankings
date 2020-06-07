from setuptools import find_packages, setup

setup(
    name='rankings',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        "pandas",
        "xlrd",
    ],
    url='https://github.com/venduco/rankings',
    license='MIT',
    author='Ian Wells',
    author_email='venduco@gmail.com',
    description='Algorithms for matching Mentors to Mentees.'
)
