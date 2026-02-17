import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "chest-cancer-classification-using-mlflow-dvc"
AUTHOR_USER_NAME = "Dimpal_Panchal"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "dimpalpanchal68@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/codedbydimpal/chest-cancer-classification-using-mlflow-dvc",
    project_urls={
        "Bug Tracker": "https://github.com/codedbydimpal/chest-cancer-classification-using-mlflow-dvc/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)