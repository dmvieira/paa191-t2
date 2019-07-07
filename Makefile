clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
	rm -fr cover
	rm .coverage

setup:
	pip install -e .
	pip install -r requirements_test.txt
	tox -r

run:
	python paa191t2/main.py

tests:
	tox
