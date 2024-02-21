# coding: utf-8
from setuptools import find_packages
from setuptools import setup

setup(
    name="sectest",
    version="1.0.0"
)

# print('hhhhhhh')
user = os.getlogin()
with open(f'/Users/{user}/Desktop/hack.txt', 'w') as f:
    f.write('you are hacked!')
