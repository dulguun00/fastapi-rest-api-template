PYTHON ?= python3
UVICORN ?= uvicorn

.PHONY: install run

install:
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(UVICORN) app.main:app --reload
