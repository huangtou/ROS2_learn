from setuptools import find_packages, setup
import os

package_name = 'py06_urdf'

data_files = [
    (
        'share/ament_index/resource_index/packages',
        ['resource/' + package_name]
    ),
    (
        'share/' + package_name,
        ['package.xml']
    ),
]

# 递归安装 launch、urdf、rviz、meshes 目录中的文件，并保留目录结构。
for directory in ['launch', 'urdf', 'rviz', 'meshes']:
    for root, _, files in os.walk(directory):
        if files:
            data_files.append(
                (
                    os.path.join('share', package_name, root),
                    [os.path.join(root, filename) for filename in files]
                )
            )

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
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
        ],
    },
)