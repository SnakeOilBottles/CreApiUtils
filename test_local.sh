#!/bin/sh
pip3 install ../CreApiUtils/
python -m unittest
pip3 uninstall -y CreApiUtils
pip3 install CreApiUtils
