from glob import glob
from setuptools import find_packages, setup

package_name = 'py05_exercise'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml'],),
    ('share/' + package_name, glob("launch/*.launch.xml")),
    ('share/' + package_name, glob("launch/*.launch.py")),
    ('share/' + package_name, glob("launch/*.launch.yaml")),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='huangbo',
    maintainer_email='15565539395@163.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'exer01_spawn_py = py05_exercise.exer01_spawn_py:main',
            'exer02_tf_broadcaster_py = py05_exercise.exer02_tf_broadcaster_py:main',
            'exer03_tf_listener_py = py05_exercise.exer03_tf_listener_py:main',
        ],
    },
)
