try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Indentification Keys Generator',
    'author': 'Gloriana Zamora',
    'url': 'https://github.com/gl0gl0/identification-keys-generator',
    'download_url': 'https://github.com/gl0gl0/identification-keys-generator',
    'author_email': 'glorianazv@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['generator'],
    'scripts': [],
    'name': 'identification-keys-generator'
}

setup(**config)