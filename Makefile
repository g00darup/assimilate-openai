install:
	curl https://bootstrap.pypa.io/get-pip.py --ssl-no-revoke -o get-pip.py && python get-pip.py &&	pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m pytest -vv test_hello.py

format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint test