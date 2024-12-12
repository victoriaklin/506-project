.PHONY: install test run

install:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt


test:
	pytest --maxfail=1 --disable-warnings -q



run:
	. venv/bin/activate && python app.py
