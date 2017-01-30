"""
Japronto
"""
import codecs
import os
import re
from setuptools import setup, find_packages


with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'src', 'japronto', '__init__.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


setup(
    name='japronto',
    version=version,
    url='http://github.com/squeaky-pl/japronto/',
    license='MIT',
    author='Paweł Piotr Przeradowski',
    author_email='przeradowski@gmail.com',
    description='A micro-framework bundled with server' +
                'based on uvloop and picohttpparser',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    keywords=['web asyncio'],
    platforms='linux',
    install_requires=[
        'uvloop>=0.7.2',
    ],
    entry_points="""
         [console_scripts]
         japronto = japronto.__main__:main
    """,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP'
    ],
)
