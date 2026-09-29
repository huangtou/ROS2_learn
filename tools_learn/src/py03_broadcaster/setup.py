from setuptools import find_packages, setup

package_name = 'py03_broadcaster'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
            'demo01_tf_static_broadcaster_py = py03_broadcaster.demo01_tf_static_broadcaster_py:main',
            'demo02_dongtai_broadcaster_py = py03_broadcaster.demo02_dongtai_broadcaster_py:main',
            'demo03_pub_point_py = py03_broadcaster.demo03_pub_point_py:main',
                        


        ],
    },
)
