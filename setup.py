import subprocess
import os
from setuptools import setup

LONG_DESCRIPTION = """
Library to plot networkx graphs with diagrams.net

Formerly known as draw.io, diagrams.net offers an opensource interface to
plot graphs. It also happens to offer a convenient way to describe graphs
in csv files. This library offers a way to create such csv files in a
programmatic fashion.
"""

DESCRIPTION         = 'drawio: plot networkx graphs with diagrams.net'
NAME                = 'drawio'
PACKAGES            = ['drawio']
AUTHOR              = 'Christophe-Marie Duquesne'
AUTHOR_EMAIL        = 'chmd@chmd.fr'
URL                 = 'https://github.com/chmduquesne/python-drawio'
DOWNLOAD_URL        = 'https://github.com/chmduquesne/python-drawio'
LICENSE             = 'MIT'
INSTALL_REQUIRES    = ['networkx']


def git_tag():
    tag = os.getenv('TRAVIS_TAG')
    if not tag:
        tag = subprocess.check_output(
                'git describe --abbrev=0'.split(' ')
                ).strip().decode('utf-8')
    return tag


def pkg_version():
    with open('drawio/__init__.py') as f:
        for line in f:
            if line.startswith("__version__ = "):
                return line[len("__version__ = '"):-2]


if pkg_version() != 'GIT_TAG':
    VERSION = pkg_version()
else:
    # update __version__ in __init__.py
    with open('drawio/__init__.py') as f:
        init_py = f.read()
    init_py = init_py.replace('GIT_TAG', git_tag())
    with open('drawio/__init__.py', 'w') as f:
        f.write(init_py)
    VERSION = pkg_version()


setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=DOWNLOAD_URL,
      license=LICENSE,
      packages=PACKAGES,
      # package_data=PACKAGE_DATA,
      install_requires=INSTALL_REQUIRES,
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8'],
     )
