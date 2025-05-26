from setuptools import setup, find_packages

setup(
    name='QuantumPortfolioPIMC',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A project for Path Integral Monte Carlo simulations and portfolio optimization.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'matplotlib>=3.4.0',
        'scipy>=1.7.0',
        'seaborn>=0.11.0',
        'scikit-learn>=1.0.0',
        'pytest>=6.0.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)