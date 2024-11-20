#!/usr/bin/env bash

CWD=$(pwd)

cd solutions/mod-08/code/events-app-selenium

python -m pytest -vv tests/test_simpletest.py

cd $CWD

# =============================================== test session starts ================================================
# platform win32 -- Python 3.13.0, pytest-8.3.3, pluggy-1.5.0 -- C:\Users\hnavarro\selenium-venv\Scripts\python.exe
# cachedir: .pytest_cache
# rootdir: C:\Users\hnavarro\Documents\test-projects\solutions\mod-08\code\events-app-selenium
# collected 1 item

# tests/test_simpletest.py::TestSimpletest::test_simpletest
# DevTools listening on ws://127.0.0.1:57551/devtools/browser/8710d66b-70a5-41c4-a05e-940bf6a8ce68
# Created TensorFlow Lite XNNPACK delegate for CPU.
# PASSED                                              [100%]

# ================================================ 1 passed in 16.41s ================================================
