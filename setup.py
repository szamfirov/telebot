import os
import sys

from setuptools import find_packages, setup


curr_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(curr_dir, 'README.md')) as f:
    README = f.read()
with open(os.path.join(curr_dir, 'VERSION')) as f:
    build_version = f.read().strip()


requires = [
    'pyramid',
    'telepot',
]


test_requires = requires + [
    'mock',
    'nose',
    'pylint',
]

setup(
    name='telebot',
    version=build_version,
    description="Simple Telegram bot",
    long_description=README + "\n\n",
    classifiers=["Programming Language :: Python"],
    author="Svetlin Zamfirov",
    keywords="Telegram Bot",
    tests_require=test_requires,
    test_suite="nose.collector",
    packages=find_packages(),
    package_data={"telebot": ["telebot"]},
    include_package_data=True,
    zip_safe=True,
    install_requires=requires,
    entry_points={
        "paste.app_factory": [
            "main = telebot:main",
            "lambda = telebot:generate_wsgi_app",
        ],
    },
)
