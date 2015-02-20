from setuptools import setup
from urllib import urlretrieve
from os import mkdir, path, remove
from shutil import rmtree
from zipfile import ZipFile


def download_and_extract_static():  # Guessing that having this function in "setup.py" is frowned upon?
    filename = 'web_frontend.zip'
    folder_name = 'static'

    if path.exists(filename):
        remove(filename)

    print 'Downloading static files from GitHub...'
    urlretrieve('https://github.com/bettertutors/web-frontend/archive/master.zip', filename)
    if not path.isfile(filename):
        raise IOError('Failed to retrieve static files from GitHub')

    if path.isdir(folder_name):
        rmtree(folder_name)
    mkdir(folder_name)

    print 'Extracting zip file...'
    with ZipFile(filename) as zip_f:
        zip_f.extractall(folder_name)


if __name__ == '__main__':
    package_name = 'bettertutors_static_api'

    download_and_extract_static()

    setup(
        name=package_name,
        version='0.1.0',
        author='Samuel Marks',
        py_modules=[package_name],
        install_requires=['bottle', 'webtest'],
        test_suite='tests'
    )
