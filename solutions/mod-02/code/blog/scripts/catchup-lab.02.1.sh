#!/usr/bin/env bash

# create blog project directories
rm -Rf "$HOME"/blog
mkdir -p "$HOME"/blog
mkdir -p "$HOME"/blog/blog-tests
mkdir -p "$HOME"/blog/blog-tests/all
mkdir -p "$HOME"/blog/blog-tests/by-function
mkdir -p "$HOME"/blog/check
mkdir -p "$HOME"/blog/check/no-check
cd "$HOME"/blog || exit
pwd
ls -l ./*

# 1. Configure non-default naming conventions for Pytest directories and files

cp /solutions/mod-02/code/blog/__init__.py "$HOME"/blog/__init__.py
cp /solutions/mod-02/code/blog/lab_02.1_1.a_main.py "$HOME"/blog/main.py
cp /solutions/mod-02/code/blog/lab_02.1_1.a_blog.py "$HOME"/blog/blog.py
bat --pager=never "$HOME"/blog/blog.py
bat --pager=never "$HOME"/blog/main.py

python main.py

cp /solutions/mod-02/code/blog/blog-tests/all/lab_02.1_1.d_blog-test-case-all.py \
    "$HOME"/blog/blog-tests/all/blog-test-case-all.py
cp /solutions/mod-02/code/blog/blog-tests/by-function/lab_02.1_1.d_blog-test-case-by-function.py \
    "$HOME"/blog/blog-tests/by-function/blog-test-case-by-function.py
bat --pager=never "$HOME"/blog/blog-tests/all/blog-test-case-all.py
bat --pager=never "$HOME"/blog/blog-tests/by-function/blog-test-case-by-function.py

pytest

cp /solutions/mod-02/code/blog/config/lab_02.1_1.f_pytest.ini "$HOME"/blog/pytest.ini
bat --pager=never "$HOME"/blog/pytest.ini

pytest

rm -Rf "$HOME"/blog/pytest.ini
cp /solutions/mod-02/code/blog/config/lab_02.1_1.h_pyproject.toml "$HOME"/blog/pyproject.toml
bat --pager=never "$HOME"/blog/pyproject.toml

pytest

# 2. Configure to not scan some directories when running Pytest

cp /solutions/mod-02/code/blog/config/lab_02.1_2.a_pyproject.toml "$HOME"/blog/pyproject.toml
bat --pager=never "$HOME"/blog/pyproject.toml

pytest

# 3. Configure non-default naming conventions for Pytest classes and functions

cp /solutions/mod-02/code/blog/config/lab_02.1_3.a_pyproject.toml "$HOME"/blog/pyproject.toml
cp /solutions/mod-02/code/blog/check/lab_02.1_3.a_blog-check-class-function.py \
    "$HOME"/blog/check/blog-check-class-function.py
bat --pager=never "$HOME"/blog/pyproject.toml
bat --pager=never "$HOME"/blog/check/blog-check-class-function.py

pytest

# 4. Configure to display the Pytest output with different verbosity levels

cp /solutions/mod-02/code/blog/config/lab_02.1_4.a_pyproject.toml "$HOME"/blog/pyproject.toml
cp /solutions/mod-02/code/blog/check/lab_02.1_4.a_utils-check-verbosity.py \
    "$HOME"/blog/check/utils-check-verbosity.py
cp /solutions/mod-02/code/blog/lab_02.1_4.a_utils.py "$HOME"/blog/utils.py
bat --pager=never "$HOME"/blog/pyproject.toml
bat --pager=never "$HOME"/blog/check/utils-check-verbosity.py
bat --pager=never "$HOME"/blog/utils.py

pytest

cp /solutions/mod-02/code/blog/config/lab_02.1_4.c_pyproject.toml "$HOME"/blog/pyproject.toml
bat --pager=never "$HOME"/blog/pyproject.toml

pytest

cp /solutions/mod-02/code/blog/config/lab_02.1_4.e_pyproject.toml "$HOME"/blog/pyproject.toml
bat --pager=never "$HOME"/blog/pyproject.toml

pytest

# 5. Configure to ignore some test files

cp /solutions/mod-02/code/blog/config/lab_02.1_5.a_pyproject.toml "$HOME"/blog/pyproject.toml
cp /solutions/mod-02/code/blog/check/lab_02.1_5.a_utils-check-ignore.py \
    "$HOME"/blog/check/utils-check-ignore.py
bat --pager=never "$HOME"/blog/pyproject.toml
bat --pager=never "$HOME"/blog/check/utils-check-ignore.py

ls -l check

pytest

# 6. Use of environment variables in Pytest

pip install -r /solutions/mod-02/requirements/pygments.txt

cp /solutions/mod-02/code/blog/config/lab_02.1_4.a_pyproject.toml "$HOME"/blog/pyproject.toml
cp /solutions/mod-02/code/blog/check/lab_02.1_4.a_utils-check-verbosity.py \
    "$HOME"/blog/check/utils-check-verbosity.py
bat --pager=never "$HOME"/blog/pyproject.toml
bat --pager=never "$HOME"/blog/check/utils-check-verbosity.py

pytest

PY_COLORS=0 pytest

# 7. Use command-line options in Pytest

cp /solutions/mod-02/code/blog/config/lab_02.1_7.a_pyproject.toml "$HOME"/blog/pyproject.toml
bat --pager=never "$HOME"/blog/pyproject.toml

mv check my-tests
ls -l my-tests
mv pyproject.toml my-pyproject.toml
ls -l

PYTHONPATH=. pytest \
--config-file=my-pyproject.toml --rootdir=my-tests -k "not url" --ignore-glob=*-ignore.py --color=yes --verbosity=2

# 8. The Pytest cache

echo 'cache_dir = "/tmp/blog-cache-dir"' >> my-pyproject.toml
bat --pager=never "$HOME"/blog/my-pyproject.toml

PYTHONPATH=. pytest \
--config-file=my-pyproject.toml --rootdir=my-tests -k "not url" \
--ignore-glob=*-ignore.py --color=yes --verbosity=2

pytest --config-file=my-pyproject.toml --cache-show

PYTHONPATH=. pytest \
--config-file=my-pyproject.toml --rootdir=my-tests \
--ignore-glob=*-ignore.py --color=yes --verbosity=2

PYTHONPATH=. pytest \
--config-file=my-pyproject.toml --rootdir=my-tests \
--ignore-glob=*-ignore.py --color=yes --verbosity=2 --last-failed

# 9. Targeting tests in Pytest

PYTHONPATH=. pytest \
--config-file=my-pyproject.toml \
my-tests/blog-check-class-function.py::CheckBlog::add_blog_entry_check -vv

cd "$HOME" || exit
