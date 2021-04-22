from setuptools import setup

setup(
    name='site_check',
    version='0.0.1',
    packages=['tests'],
    url='https://github.com/kindermax/site-check',
    license='BSD-3-Clause',
    author='Kindritskiy Max',
    author_email='kindritskiy.m@gmail.com',
    description='Simple site checker',

    python_requires='>=3.8',
    install_requires=[
        'pytest',
        'validators'
    ]
)
