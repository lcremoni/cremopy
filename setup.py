from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='Cremopy',
    url='https://github.com/lcremoni/cremopy',
    author='Luca Cremonini',
    author_email='l.cremonini@myemail.com',
    # Needed to actually package something
    packages=['cremopy'],
    # Needed for dependencies
    #install_requires=['numpy'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='My python package',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
