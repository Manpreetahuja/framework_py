from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(

name='python-taf',
version='1.0.0',
packages=find_packages(where='src'),
python_requires='>=3.6',
install_requires=[
   'pandas',
   'numpy'
],
data_files=[('config', ['cfg/data.cfg']),('testData',['resources/testData.yml'])],
entry_points={  
        'console_scripts': [
            'runner=src.runner.TestRunner:main',
        ],
    },

)