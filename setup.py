from setuptools import setup, find_packages

setup(
    name='table_to_database',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyexcel_ods',
        'ods',
        'pandas',
        'pymysql',
        'mysql-connector-python',
        'sqlalchemy'
    ],
    entry_points={
        'console_scripts': [
            'table_to_database=table_to_database.main:main',
        ],
    },
    author='Danilo Silva',
    description='A package for converting table files to database formats.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/danilocgsilva/table_to_database',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='MIT',
    keywords='database, table, conversion, sqlalchemy, pandas',
)
