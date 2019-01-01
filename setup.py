import setuptools

with open('README.md', 'r') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name='google-reminder-api-wrapper',
    version='0.0.1',
    author='Marcus Windmark',
    author_email='marcus.windmark@gmail.com',
    description='An unofficial API wrapper for the Google Reminder',
    long_description=readme,
    license=license,
    url='https://github.com/windmark/google-reminder-api-wrapper',
    packages=setuptools.find_packages(exclude=('tests', 'docs')),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'requests==2.21.0',
        'python-dateutil==2.7.5'
    ]
)