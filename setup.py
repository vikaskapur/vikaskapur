"""This module sets up the package for the *** vikaskapur ***"""

from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(    
    name="vikaskapur",
    author="Vikas Kapur",
    author_email="vikaskapur04@gmail.com",
    maintainer="Vikas Kapur",
    maintainer_email="vikaskapur04@gmail.com",
    version="1.0.0",
    url="https://github.com/vikaskapur/vikaskapur.git",
    download_url='https://github.com/vikaskapur/vikaskapur.git',
    keywords=['Vikas Kapur', 'vikaskapur', 'profile', 'terminal'],
    license="MIT",
    description="A simple package to display profile in terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/vikaskapur/vikaskapur/issues",
    },
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'climage',
        'pyfiglet',
        'setuptools',
        'pytest',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3'],
    entry_points={
        'console_scripts': [
            'profile = vikaskapur.__main__:main',
            'name = vikaskapur.__main__:name',
            'photo = vikaskapur.__main__:image'
        ]},
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)