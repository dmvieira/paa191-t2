clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
	rm -fr cover
	rm .coverage

setup:
	pip install -r requirements.txt
	pip install -r requirements_test.txt
	tox -r

tests:
	tox
