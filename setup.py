from setuptools import setup, find_packages
from codecs import open
from os import path
import remote-joystick

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='remote-joystick',

    version=remote-joystick.__version__,

    description='Remote joysticks can be used as locals ones.',

    long_description=long_description,

    url='https://github.com/littlecodersh/remote-joystick',

    author='LittleCoder',
    author_email='i7meavnktqegm1b@qq.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
    ],

    keywords='joystick remote socket',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    install_requires=['pygame'],

    # List additional groups of dependencies here
    extras_require={},

    entry_points={
        'console_scripts':[
            'remote-joystick = remote-joystick.main:main'
        ]
    },
)
