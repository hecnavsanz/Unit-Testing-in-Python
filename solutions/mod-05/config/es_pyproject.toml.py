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
bdd_features_base_dir = "tests/features/"
