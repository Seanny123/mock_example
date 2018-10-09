from setuptools import setup

setup(
    name='ChuChu',
    packages=['chuchu'],
    extras_require={
        "tests": [
            "pytest",
            "pytest-mock"
        ]
    }
)