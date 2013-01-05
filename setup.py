try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A Tic Tac Toe Game',
    'author': 'Michael Marshall',
    'url': 'URL to get it at.',
    'download_url': 'https://github.com/mtmarsh2',
    'author_email': 'mtmarsh2@illinois.edu',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['Tic Tac Toe'],
    'scripts': [],
    'name': 'Tic Tac Toe '
}

setup(**config)