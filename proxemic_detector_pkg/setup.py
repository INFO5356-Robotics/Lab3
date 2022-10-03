from setuptools import setup
import os
from glob import glob

package_name = 'proxemic_detector_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('sahre', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sam Ken Soul',
    maintainer_email='soulatwork001@gmail.com',
    description='A pakage to detect proximity, read depth and rgb, and aleart with sound',
    license='No License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'turtlebot_proxemic_detector_node = proxemic_detector_pkg.turtlebot_proxemic_detector_node:main',
            'rgb_image_publisher_node  = proxemic_detector_pkg.rgb_image_publisher_node:main',
            'depth_image_publisher_node = proxemic_detector_pkg.depth_image_publisher_node:main'
        ],
    },
)
