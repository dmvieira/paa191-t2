from setuptools import setup, find_packages


with open('./README.md') as fp:
    description = fp.read()

with open('requirements.txt') as reqs:
    requirements = reqs.readlines()

setup(
    name='paa191t2',
    description='Python Library for second poggi homework',
    long_description=description,
    #version='0.0.1',
    author='paa da depressao',
    url='https://github.com/dmvieira/paa191-t2',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=requirements,
    license='Apache 2',
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Education'
    ]
)

