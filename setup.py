from setuptools import setup, find_packages

setup(
    name='xolani',
    version='0.1.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Xolanisilangwe/xolani.git',
    author='Xolani',

    author_email='silangwexolani@gmail.com'
)
