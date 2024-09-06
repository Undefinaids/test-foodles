from pathlib import Path

from setuptools import find_packages, setup

version = Path(__file__).resolve().parents[0].joinpath("version").read_text().strip()

setup(
    name="foodles",
    version=version,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    author="Nicolas LEMAIRE",
    author_email="nicolas.lemaire@epitech.eu",
    description="Foodles technical test",
    python_requires=">=3.8",
    install_requires=[],
    entry_points={
        "console_scripts": [
            "foodles = foodles.cli:run",
        ]
    },
)
