from distutils.core import setup

setup(
    name = 'py-football',
    version = '1.0.3',
    description = 'Football Wrapper',
    long_description = 'Football Wrapper',

    author = 'Prabhu Rajendran',
    author_email = 'prabhu@fantain.com',
    url = 'https://github.com/prabhufantain/pyfootball',
    package_dir={'': 'src'},
    packages=[''],
    install_requires=['certifi==2022.12.7', 'chardet==3.0.4', 'idna==2.5',
                      'requests>=2.18.1', 'urllib3>=1.24.2'],
    entry_points='''
        [console_scripts]
        pyfootball=src.pyfootball:RcaApp
    '''
)
