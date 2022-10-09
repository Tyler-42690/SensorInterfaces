from setuptools import setup
import os

def requirements():
    with open('requirements.txt') as file:
        required = file.read().splitlines()
        return required
setup(
    name='SensorInterfaces',
    version='0.0.0',    
    description='Sensors and Camera interface for PI',
    url='https://github.com/Tyler-42690/SensorInterfaces',
    author='Tyler Casas',
    author_email='sharknado8575@gmail.com',
    license='',
    packages=['Sensors'],
    install_requires=requirements(),

    classifiers=[
        'Development Status :: In the Works',
        'Intended Audience :: Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)