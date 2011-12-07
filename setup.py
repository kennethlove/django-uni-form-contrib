from setuptools import setup, find_packages
import os


setup(
    name="django-uni-form-contrib",
    description="Contributed templates for django-uni-form library",
    long_description=open(os.path.join(os.path.dirname(__file__),
        'README.rst')).read(),
    version="0.0.1",
    author="Kenneth Love",
    install_requires=[
        'uni-form (>0.9.0)',
        ],
    packages=find_packages(),
)

