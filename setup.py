from setuptools import setup
from pip.req import parse_requirements

def requirements():
    install_requirements = parse_requirements('requirements.txt')
    requirements = [str(ir.req) for ir in install_requirements]
    return requirements
setup(
    name='SensorInterfaces',
    version='0.0.0',    
    description='Sensors and Camera interface for PI',
    url='https://github.com/Tyler-42690/SensorInterfaces',
    author='Tyler Casas',
    author_email='sharknado8575@gmail.com',
    license='',
    packages=['SensorInterfaces'],
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