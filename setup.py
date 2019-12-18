from setuptools import setup, Extension, find_packages


requirements = [
    'setuptools>=18.0',
    'opencv-python==3.4.2.17',
    'opencv-contrib-python==3.4.2.17',
    'pandas',
    'sklearn',
    'numpy',
]


setup(
    name='mmt',
    version=__version__,
    install_requires=requirements,
    packages=['mmt'],
    description='Stereo feature-based motion tracker.',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    python_requires='>=3.4, <3.8'
)