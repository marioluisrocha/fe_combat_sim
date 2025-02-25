from setuptools import setup, find_packages

setup(
    name="fe_combat_sim",
    version="0.1.0",
    packages=find_packages(),
    description="A Python package for simulating Fire Emblem-style combats",
    author="Your Name",
    author_email="your.email@example.com",
    keywords="game, simulation, rpg, fire emblem",
    install_requires=[
        "streamlit>=1.22.0",
        "pandas>=1.5.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
)
