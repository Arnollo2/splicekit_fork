# splicekit

from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_desc = fh.read()
    long_desc = "\n".join(long_desc.split("\n")[1:])

setup(
    name='splicekit',
    version = open("splicekit/version", "rt").readlines()[0].replace("\n", "").replace("\r", ""),
    packages=find_packages(),
    description='splicekit: comprehensive toolkit for splicing analysis from short-read RNA-seq',
    long_description = long_desc,
    long_description_content_type = "text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    zip_safe=False,
    author='Roche, PMDA Spliceosome team',
    scripts=["splicekit/splicekit", "splicekit/splicecompare"],
    author_email='gregor.rot@gmail.com',
    url='https://github.com/bedapub/splicekit',
    keywords=['splicekit', 'splicing', 'transcriptomics', 'bioinformatics'],
    include_package_data=True,
    package_data={
        'splicekit': ['splicekit.config.template', 'version'],
    },
    install_requires=["pybio", "scanRBP", "pysam", "numpy", "psutil", "bs4", "requests", "rangehttpserver"],
)
