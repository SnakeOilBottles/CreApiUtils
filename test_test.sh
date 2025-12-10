#!/bin/sh
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple CreApiUtils
python -m unittest
pip3 uninstall -y CreApiUtils
pip3 install CreApiUtils
