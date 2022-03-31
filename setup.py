import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='yang-compatibility-check',
    version='0.1',
    description=('A plugin to check a YANG file compatibility Schema that according huawei or the third-party rules.'),
    long_description=read('README.md'),
    packages=['compatibilitycheck'],
    author='niubiwocao',
    author_email='niubiwocao@huawei.com',
    license='New-style BSD',
    url='https://github.com/HuaweiDatacomm/yang-compatibility-check',
    install_requires=['pyang'],
    include_package_data=True,
    keywords=['yang', 'compatibility', 'check', 'pyang'],
    classifiers=[],
    
)
