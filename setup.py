from setuptools import setup

setup(
    name='my_chatgpt_package',
    version='0.1.0',
    description='A package for connecting to ChatGPT via Alexa',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/my_chatgpt_package',
    packages=['my_chatgpt_package'],
    install_requires=[
        'requests',
    ],
)