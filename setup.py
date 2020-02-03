from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    long_description = file.read()

setup(
    name='gitcd',
    version='0.0.1',
    author='Joseph Lam',
    author_email='mhlamaf@connect.ust.hk',
    description='A terminal tool for easy navigation to local git repository',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Doma1204/gitcd',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
    ],
    keywords='git terminal',
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts':[
            'git-cd=gitcd.cli_interface:cli'
        ],
    },
)