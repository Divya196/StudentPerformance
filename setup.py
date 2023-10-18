from setuptools import find_packages,setup
from typing import List

def get_requirements(filepath:str)->List[str]:
    '''
    this function returns a list of requirements
    '''
    HYPEN_E_DOT = '-e .'
    requirements=[]
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace('\n','') for i in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

setup(
name='Student Performance',
version='0.1',
author='divya',
author_email='divyaramesh196@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)