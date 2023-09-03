VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python
PIP=${VENV_NAME}/bin/pip
PACKAGE?="requests"
VERSION?=3.0.0

.PHONY: venv install install-version install-all upgrade uninstall list show check activate

venv:
	@test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)

install: venv
	$(PIP) install $(PACKAGE)

install-version: venv
	$(PIP) install $(PACKAGE)==$(VERSION)

install-all: venv
	$(PIP) install -r requirements.txt

upgrade: venv
	$(PIP) install --upgrade $(PACKAGE)

uninstall: venv
	$(PIP) uninstall $(PACKAGE)

list: venv
	$(PIP) list

show: venv
	$(PIP) show $(PACKAGE)

check: venv
	$(PIP) check

activate:
	@echo "To activate the virtual environment, run:"
	@echo "source $(VENV_NAME)/bin/activate"
