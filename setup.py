#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for bulk-management"""

import os
from urllib.parse import urlparse, parse_qs
from setuptools import find_packages, setup

version = "0.1.0"
here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md"), "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

with open(os.path.join(here, "CHANGELOG.md"), "r", encoding="utf-8") as changelog_file:
    changelog = changelog_file.read()


def parse_requirements(file):
    required = []
    with open(file) as f:
        for req in f:
            req = req.strip()
            if req.startswith("#"):
                continue
            if "egg" in req:
                if req.startswith("-e"):
                    vcs_pkg = urlparse(req.split(" ")[1])
                else:
                    vcs_pkg = urlparse(req)
                req = parse_qs(vcs_pkg.fragment)["egg"][0]
            required.append(req)
    return required


requirements = parse_requirements("requirements.txt")
test_requirements = parse_requirements("requirements.test.txt")

setup(
    name="Bulk management API Gateway",
    version=version,
    description="The API gateway takes all GraphQL API requests from a client "
    "(frontend: mobile app, browser app...), determines "
    "which services are needed (Warehouse Management System (WMS), "
    "Product Information Management (PIM), ...), "
    "and combines them into a synchronous experience for the user.",
    long_description=readme + "\n\n" + changelog,
    long_description_content_type="text/markdown",
    author="Pierre Verkest",
    author_email="pierreverkest84@gmail.com",
    url="https://github.com/avracadabra/api-gateway",
    packages=find_packages(),
    entry_points="""""",
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords="bulk,wms",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    test_suite="tests",
    tests_require=test_requirements,
)
