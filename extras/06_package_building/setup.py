from setuptools import setup, find_packages

setup(
    name='python_mini_course',
    version='0.1.0',
    packages=find_packages(include=["*"]),
    install_requires=[
        'numpy',
        'pandas',
        'requests',
        'pytest'
    ],
    author='Thamarai Kannan',
    author_email='shreethamarai@email.com',
    description='A hands-on Python mini-course from basics to systems',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/shreethamarai/python-mini-course',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.8',
)

