try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Automate your weekly dinnerplanning',
    'author': 'Kristian Nordin',
    'url': 'https://www.github.com/knille/auto-food-planner',
    'download_url': 'Where to download it.',
    'author_email': 'kristian.nordin@proton.me',
    'version': '0.1',
    'install_requires': [nose],
    'packages': [NAME],
    'scripts': [],
    'name': 'Auto Food Planner'
}

setup(**config)
