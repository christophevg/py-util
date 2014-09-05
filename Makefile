APP=py-util

PYTHON=PYTHONPATH=src/:. python
COVERAGE=/usr/local/bin/coverage

all: test

test:
	@echo "*** performing $(APP) tests"
	@$(PYTHON) $(COVERAGE) run test/all.py

.PHONY: test
