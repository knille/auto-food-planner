try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Semi-automatic foodplanning',
    'author': 'Kristian Nordin',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'kristian.nordin@proton.me',
    'version': '0.1',
    'install_requires': [nose],
    'packages': [NAME],
    'scripts': [],
    'name': 'Auto Food Planner'
}

setup(**config)
