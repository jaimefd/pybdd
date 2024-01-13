from setuptools import setup, Extension

# Define the CUDD source files
cudd_sources = [
    'PyBDD/src/cudd-3.0.0/cudd/cuddAddAbs.c',
    # Add more source files as needed
]

# Define the extension module
cudd_extension = Extension(
    'pybdd',  # Extension name
    sources=cudd_sources,
    include_dirs=['PyBDD/src/cudd-3.0.0'],  # Include directory for CUDD header files
    # Add other compiler/linker flags if necessary
)

# Define the setup configuration
setup(
    name='pybdd',
    version='0.1',
    packages=['pybdd'],
    ext_modules=[cudd_extension],  # Include the CUDD extension module
    install_requires=[
        # List your other dependencies here
    ],
)