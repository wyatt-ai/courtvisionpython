# -*- coding: utf-8 -*-
import versioneer
from setuptools import setup

setup(
    name="courtvisionpython",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Wyatt AI",
    author_email="jwsmith@wyattai.com",
    packages=["courtvisionpython"],
    license="MIT",
    install_requires=[
        "pandas==1.1.5",
        "requests==2.26.0",
        "pytest==6.2.4"
    ],
    include_package_data=True,
    test_suite="tests",
    zip_safe=False,
)
