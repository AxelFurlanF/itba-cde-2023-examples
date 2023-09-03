PYTHON_VERSION?=3.9.0

.PHONY: install-python list-versions set-global-python set-local-python uninstall-python

install-python:
	pyenv install ${PYTHON_VERSION}
	pyenv rehash

list-versions:
	pyenv versions
	pyenv install --list

set-global-python:
	pyenv global ${PYTHON_VERSION}

set-local-python:
	pyenv local ${PYTHON_VERSION}

uninstall-python:
	pyenv uninstall ${PYTHON_VERSION}
