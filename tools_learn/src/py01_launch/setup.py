from setuptools import find_packages, setup
from glob import glob
package_name = 'py01_launch'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        #这种方法效率太低了 用全局的方法来启动launch文件
        #('share/' + package_name, ['launch/py/py01_helloword_launch.py']),
        ('share/' + package_name, glob(package_name + "/launch/py/*_launch.py")),
        ('share/' + package_name, glob(package_name + "/launch/xml/*_launch.xml")),
        ('share/' + package_name, glob(package_name + "/launch/yaml/*_launch.yaml")),
        ('share/' + package_name + '/config',glob(package_name + "/config/*.yaml")),#安装路径
        
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
            'node_1 = py01_launch.node_1:main'
        ],
    },
)
