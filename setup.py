from setuptools import setup, find_packages

setup(
    name='spinnaker_vision',
    version='0.0.1',
    packages=find_packages(),
    license='',
    author='Petrut Antoniu Bogdan',
    author_email='pab@cs.man.ac.uk',
    description='Spiking neural network vision system using a silicon sensor retina running on SpiNNaker',
    # Requirements
    dependency_links = ['https://github.com/nengo/nengo/tarball/23107fe#egg=nengo-2.1.0.dev0',
                        'https://github.com/pabogdan/nengo_spinnaker/tarball/master#egg=nengo-spinnaker-0.2.4'],

    install_requires=["nengo==2.1.0.dev0", "rig>=0.5.3, <1.0.0",
                      "bitarray>=0.8.1, <1.0.0", "nengo-spinnaker==0.2.4"],
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",

        "Programming Language :: Python :: 2.7"
    ]
)