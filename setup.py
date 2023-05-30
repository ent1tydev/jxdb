from setuptools import setup

with open('LICENSE', 'r', encoding='utf-8') as file:
    license_text = file.read()

with open('README.md', 'r', encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='jxdb',
    version='0.0.3',
    description='Secured Python Json Database',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='xinyc',
    author_email='csecinside@proton.me',
    url='https://github.com/ent1tydev/jxdb',
    license=license_text,
    packages=['jxdb'],
    classifiers=[
        'License :: OSI Approved',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'pycryptodome'
    ]
)
