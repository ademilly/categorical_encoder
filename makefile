# Simple MAKEFILE for python project

VENV=venv
VENV_PYTHON_BIN=venv/bin/python
VENV_PIP_BIN=venv/bin/pip
VENV_PYTEST_BIN=venv/bin/pytest
PACKAGE=categorical_encoder

default: run

help:
	@echo "Makefile for $(PACKAGE) python project"
	@echo
	@echo "Following commands are available:"
	@echo "    clean"
	@echo "        Remove python artifacts."
	@echo "    test"
	@echo "        Run py.test"
	@echo "    install"
	@echo "        Setup local virtualenv"
	@echo "    install_demo"
	@echo "        Setup local virtualenv for demo"

clean:
	rm -f *.pyc $(PACKAGE)/*.pyc loader/*.pyc tests/*.pyc
	rm -rf $(PACKAGE)/__pycache__ loader/__pycache__ tests/__pycache__

clean_venv: clean
	rm -rf venv

test: clean
	$(VENV_PYTEST_BIN) --verbose --color=yes tests/

demo: install_dev
	$(VENV_PYTHON_BIN) demo.py

install: clean_venv
	virtualenv venv
	$(VENV_PIP_BIN) install -U .

install_dev: clean_venv
	virtualenv venv
	$(VENV_PIP_BIN) install -U scipy
	$(VENV_PIP_BIN) install -U numpy
	$(VENV_PIP_BIN) install -U sklearn
	$(VENV_PIP_BIN) install -U pytest

.PHONY: clean
