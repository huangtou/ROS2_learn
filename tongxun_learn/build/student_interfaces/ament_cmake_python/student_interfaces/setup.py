from setuptools import find_packages
from setuptools import setup

setup(
    name='student_interfaces',
    version='0.0.0',
    packages=find_packages(
        include=('student_interfaces', 'student_interfaces.*')),
)
