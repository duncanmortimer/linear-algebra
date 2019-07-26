#!/bin/sh

jupyter notebook \
  --ip=0.0.0.0\
  --allow-root\
  --no-browser\
  --config=/workspaces/linear-algebra/config/jupyter_notebook_config.py
