from setuptools import setup, find_packages

setup(
    name='eda_library',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib',
        'seaborn'
    ],
    author='Manikanteswar Gampala',
    author_email='mani.eswar45@example.com',
    description='A library for automated EDA',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/manieswar45/eda_library',  # Update this with your GitHub repo
)
