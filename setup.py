#!/usr/bin/env python

from setuptools import setup, find_packages
import argparse
import sys


def newest_version():
    setup(
        name='spinnaker_vision',
        version='0.0.1',
        packages=find_packages(),
        license='',
        author='Petrut Antoniu Bogdan',
        author_email='pab@cs.man.ac.uk',
        description='Spiking neural network vision system using a silicon sensor retina running on SpiNNaker',
        # Requirements
        dependency_links=['https://github.com/nengo/nengo/tarball/master#egg=nengo-2.1.0.dev0',
                          'https://github.com/project-rig/nengo_spinnaker/tarball/master#egg=nengo-spinnaker',
                          'https://github.com/nengo/nengo_gui/tarball/master',
                          'https://github.com/ctn-waterloo/nengo_pushbot/tarball/master#egg=nengo-pushbot-0.0.1.dev0'],

        install_requires=["nengo==2.1.0.dev0", "rig>=0.5.3, <1.0.0",
                          "bitarray>=0.8.1, <1.0.0", "nengo-spinnaker>=0.2.5", "nengo_gui>=0.1.4",
                          "nengo-pushbot==0.0.1.dev0"],
        classifiers=[
            "Operating System :: POSIX :: Linux",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: MacOS",

            "Programming Language :: Python :: 2.7"
        ]
    )


def compatibility_version():
    setup(
        name='spinnaker_vision',
        version='0.0.1',
        packages=find_packages(),
        license='',
        author='Petrut Antoniu Bogdan',
        author_email='pab@cs.man.ac.uk',
        description='Spiking neural network vision system using a silicon sensor retina running on SpiNNaker',
        # Requirements
        dependency_links=['https://github.com/nengo/nengo/tarball/23107fe#egg=nengo-2.1.0.dev0',
                          'https://github.com/pabogdan/nengo_spinnaker/tarball/master#egg=nengo-spinnaker-0.2.4',
                          'https://github.com/nengo/nengo_gui/tarball/master',
                          'https://github.com/ctn-waterloo/nengo_pushbot/tarball/master#egg=nengo-pushbot-0.0.1.dev0'],

        install_requires=["nengo==2.1.0.dev0", "rig>=0.5.3, <1.0.0",
                          "bitarray>=0.8.1, <1.0.0", "nengo-spinnaker==0.2.4",
                          "nengo-pushbot==0.0.1.dev0", "nengo_gui>=0.1.4"],
        classifiers=[
            "Operating System :: POSIX :: Linux",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: MacOS",

            "Programming Language :: Python :: 2.7"
        ]
    )

parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument('--newest', dest='version', action='store_true')
parser.add_argument('--compatibility', dest='version', action='store_false')
parser.set_defaults(version=True)
args, extra = parser.parse_known_args()

if "--newest" in sys.argv:
    sys.argv.remove("--newest")
if "--compatibility" in sys.argv:
    sys.argv.remove("--compatibility")

if args.version:
    newest_version()
else:
    compatibility_version()
