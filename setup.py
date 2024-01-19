from setuptools import setup, find_packages

setup(
    name="xgboostlss",
    version="0.4.0",
    description="XGBoostLSS - An extension of XGBoost to probabilistic forecasting",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Alexander März",
    author_email="alex.maerz@gmx.net",
    url="https://github.com/StatMixedML/XGBoostLSS",
    license="Apache License 2.0",
    packages=find_packages(exclude=["docs", "tests*"]),
    include_package_data=True,
    package_data={'': ['datasets/*.csv']},
    zip_safe=True,
    python_requires=">=3.9",
    install_requires=[
        "xgboost~=2.0.3",
        "torch~=2.1.2",
        "pyro-ppl~=1.8.6",
        "optuna~=3.5.0",
        "properscoring~=0.1",
        "scikit-learn~=1.4.0",
        "numpy~=1.26.3",
        "pandas~=2.1.4",
        "plotnine~=0.12.4",
        "scipy~=1.11.4",
        "shap~=0.44.0",
        "seaborn~=0.13.1",
        "tqdm~=4.66.1",
        "matplotlib~=3.8.2",
        "ipython~=8.20.0",
    ],
    extras_require={
        "docs": ["mkdocs", "mkdocstrings[python]", "mkdocs-jupyter"]
    },
    test_suite="tests",
    tests_require=["flake8", "pytest"],
)
