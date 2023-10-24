from setuptools import setup, find_packages

setup(
    name='zebra_day',
    version='0.0.25',
    description='A Python library to manage a zebra printer fleet and an api for ZPL print requests.',
    author='John Major',
    author_email='john@daylilyinformatics.com',
    url='https://github.com/Daylily-Informatics/zebra_day',
    packages=find_packages(),
    install_requires=[
        'yaml_config_day',
        'requests',
        'pytz',
        'cherrypy',
        'ipython'
    ],
    include_package_data=True,
    package_data={'zebra_day':['bin/*','etc/*']},
    entry_points={
        'console_scripts': [
            'zday_quickstart = zebra_day.print_mgr:main',
        ],
    },
)
