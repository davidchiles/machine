from setuptools import setup
from os.path import join, dirname
import sys

with open(join(dirname(__file__), 'openaddr', 'VERSION')) as file:
    version = file.read().strip()

conditional_requirements = list()

if sys.version_info[0] == 2:
    conditional_requirements += [
        # http://python-future.org
        'future >= 0.14.3',
        
        # https://github.com/jdunck/python-unicodecsv
        'unicodecsv >= 0.11.2',
        
        # https://code.google.com/p/python-subprocess32/
        'subprocess32 == 3.2.6',

        # https://pypi.python.org/pypi/python-memcached
        'python-memcached == 1.57',

        # https://github.com/kennethreitz/requests/issues/2022#issuecomment-143348232
        'ndg-httpsclient == 0.4.0',
        'pyOpenSSL == 16.0.0',
        'pyasn1 == 0.1.9',
    ]
else:
    conditional_requirements += [
        # https://pypi.python.org/pypi/python-memcached
        'python3-memcached == 1.51',
    ]

setup(
    name = 'OpenAddresses-Machine',
    version = version,
    url = 'https://github.com/openaddresses/machine',
    author = 'Michal Migurski',
    author_email = 'mike-pypi@teczno.com',
    description = 'In-progress scripts for running OpenAddresses on a complete data set and publishing the results.',
    packages = ['openaddr', 'openaddr.util', 'openaddr.ci', 'openaddr.tests', 'openaddr.parcels'],
    entry_points = dict(
        console_scripts = [
            'openaddr-render-us = openaddr.render:main',
            'openaddr-preview-source = openaddr.preview:main',
            'openaddr-process-one = openaddr.process_one:main',
            'openaddr-ci-recreate-db = openaddr.ci.recreate_db:main',
            'openaddr-ci-run-dequeue = openaddr.ci.run_dequeue:main',
            'openaddr-ci-worker = openaddr.ci.worker:main',
            'openaddr-enqueue-sources = openaddr.ci.enqueue:main',
            'openaddr-collect-extracts = openaddr.ci.collect:main',
            'openaddr-index-tiles = openaddr.ci.tileindex:main',
            'openaddr-run-ec2-command = openaddr.run_ec2_ami:main',
            'openaddr-update-dotmap = openaddr.dotmap:main',
        ]
    ),
    package_data = {
        'openaddr': [
            'geodata/*.shp', 'geodata/*.shx', 'geodata/*.prj', 'geodata/*.dbf',
            'geodata/*.cpg', 'VERSION',
        ],
        'openaddr.ci': [
            'schema.pgsql', 'templates/*.*', 'static/*.*'
        ],
        'openaddr.tests': [
            'data/*.*', 'outputs/*.*', 'sources/*.*', 'sources/fr/*.*',
            'sources/us/*/*.*', 'sources/de/*.*', 'sources/nl/*.*',
            'conforms/lake-man-gdb.gdb/*',
            'conforms/*.csv', 'conforms/*.dbf', 'conforms/*.zip', 'conforms/*.gfs',
            'conforms/*.gml', 'conforms/*.json', 'conforms/*.prj', 'conforms/*.shp',
            'conforms/*.shx', 'conforms/*.vrt',
            'parcels/sources/us/ca/*.*', 'parcels/sources/us/id/*.*',
            'parcels/data/*.*', 'parcels/data/us/ca/*.*',
            'parcels/data/us/ca/berkeley/*.*'
        ],
        'openaddr.parcels': [
            'README.md'
        ],
        'openaddr.util': [
            'templates/*.*'
        ]
    },
    test_suite = 'openaddr.tests',
    install_requires = [
        'boto == 2.43.0', 'dateutils == 0.6.6', 'ijson == 2.3',
        
        # Honcho (imported for worker) requires Jinja2 < 2.8.
        'Jinja2 == 2.7.3',

        # http://flask.pocoo.org
        'Flask == 0.11.1',
        
        # http://flask-cors.corydolphin.com
        'Flask-Cors == 3.0.2',
        
        # https://www.palletsproject.com/projects/werkzeug/
        'Werkzeug == 0.11.11',
        
        # http://gunicorn.org
        'gunicorn == 19.6.0',

        # http://www.voidspace.org.uk/python/mock/
        'mock == 2.0.0',

        # https://github.com/uri-templates/uritemplate-py/
        'uritemplate == 0.6',
        
        # https://github.com/malthe/pq/
        'pq == 1.4',
        
        # http://initd.org/psycopg/
        'psycopg2 == 2.6.2',
        
        # http://docs.python-requests.org/en/master/
        'requests == 2.11.1',

        # https://github.com/patrys/httmock
        'httmock == 1.2.5',
        
        # https://boto3.readthedocs.org
        'boto3 == 1.4.1',

        # https://github.com/openaddresses/pyesridump
        'esridump == 1.4.1',

        # Used in openaddr.parcels
        'Shapely == 1.5.17',
        #'Fiona == 1.7.0.post2',

        # http://pythonhosted.org/itsdangerous/
        'itsdangerous == 0.24',
        
        # https://aws.amazon.com/cli/
        'awscli == 1.11.22',
        'botocore == 1.4.79',

        ] + conditional_requirements
)
