"""Setup.py file for Atemon.SMS package."""
from distutils.core import setup

setup(
    name='Atemon-SMSAPI',
    version='0.1.0.0',
    packages=['Atemon', 'Atemon.SMS', 'Atemon.SMS.GAG'],
    long_description="Connect to SMS API with Python",
    author="Varghese Chacko",
    author_email="varghese@atemon.com",
    maintainer="Priya Mary Philip",
    maintainer_email="priya@atemon.com",
    url="https://github.com/atemon/python-sms-api",
    install_requires=["requests>=2.12.3"],
    provides=["SMS"],
    license="MIT License (modified)",
)
