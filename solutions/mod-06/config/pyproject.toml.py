# pyproject.toml config file
[tool.pytest.ini_options]
minversion = "8.0"
addopts = ["--capture=no"]
python_files = ["test_*.py"]
python_classes = ["Test"]
python_functions = ["test"]
pythonpath = ["."]
testpaths = ["tests"]
verbosity_assertions = 1
verbosity_test_cases = 1
# pytest-env
[tool.pytest_env]
DB_PORT = 3306
DB_USERNAME = "root"
DB_PASSWORD = "Pytest-TDD.Labs_4ALL"
DB_ROOT_PASSWORD = "Pytest-TDD.Labs_4ALL"
DB_NAME = "crmdb"
DB_SEED = "tests/data"
# pytest-bdd
# bdd_features_base_dir = "tests/features/"
