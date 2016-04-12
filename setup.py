from setuptools import setup, find_packages

version = '1.0'

REQUIREMENTS = [
    'beautifulsoup',
    'requests'
]

setup(
    name='incapsula-cracker',
    version=version,
    packages=find_packages(),
    url='https://github.com/ziplokk1/incapsula-cracker',
    license='LICENSE.txt',
    author='Mark Sanders',
    author_email='sdscdeveloper@gmail.com',
    install_requires=REQUIREMENTS,
    description='A way to bypass incapsula robot checks using the python requests library.'
)
