#!/usr/bin/env python3
import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='mqtt_alarm_server',
    version='2018061301',
    url='https://github.com/fliphess/mqtt_alarm_server.git',
    license='copyleft',
    author='Flip Hess',
    author_email='flip@fliphess.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: CopyLeft',
        'Intended Audience :: Homeautomation Adepts',
        'Topic :: MQTT',
        'Topic :: Security',
        'Topic :: Internet Of Things',
        'Programming Language :: Python :: 3.6',
    ],
    description='mqtt_alarm_server',
    install_requires=[
        'pid',
        'PyYAML',
        'paho-mqtt',
    ],
    packages=[
        'mqtt_listener',
    ],
    entry_points=dict(console_scripts=[
        'mqtt-alarm-server = mqtt_listener.main:main',
    ]),
)
