from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='This code is a Python script that organizes files in a specified folder.'
                  'It normalizes file names, moves them to respective categories (images, videos, documents, audio, archives), and removes empty folders.'
                  'Unknown files are moved to a separate folder.',
      url='https://github.com/DenK0-UA/Python_Core_Hw07/tree/master/clean_folder/',
      author='Denis Yevtushenko',
      author_email='denidinamo@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['cleanfolder = clean_folder.clean:main']}
      )
