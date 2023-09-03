PACKAGE?="requests"
VERSION?=3.0.0

.PHONY: install install-version install-all upgrade uninstall list show check

install:
	pip install $(PACKAGE)

install-version:
	pip install $(PACKAGE)==$(VERSION)

install-all:
	pip install -r requirements.txt

upgrade:
	pip install --upgrade $(PACKAGE)

uninstall:
	pip uninstall $(PACKAGE)

list:
	pip list

show:
	pip show $(PACKAGE)

check:
	pip check
