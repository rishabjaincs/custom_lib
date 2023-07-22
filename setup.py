from setuptools import setup, find_packages
with open('requirements.txt') as f:
    install_requires = f.read().splitlines()
setup(
    name='custom_library',
    version='0.1.0',
    description='This is a custom library created for learning purpose',
    packages=find_packages(),
    install_requires=install_requires,
)
