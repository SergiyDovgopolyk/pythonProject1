from setuptools import setup, find_namespace_packages

setup(
    name='clean_programm',
    version='0.0.1',
    description='The programm for scanning and clining folders',
    url='https://github.com/SergiyDovgopolyk/Sorting-programm',
    author='Sergiy Dovgopolyk',
    author_email='dovgopolyks@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
    entry_points={'console_scripts': ['clean-folder = clean_folder.clean:running']}
)