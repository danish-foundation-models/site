from setuptools import setup
from setuptools import find_packages


def setup_package():
    setup(
        packages=find_packages(
            "src",
            exclude=[
                "application",
                "application/*",
            ],
        ),
        package_dir={"": "src"},
    )


if __name__ == "__main__":
    setup_package()
