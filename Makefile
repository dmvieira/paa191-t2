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

jupyter:
	@rm -fr dist/*
	@python setup.py sdist
	@cp -f dist/paa191t2-0.0.0.tar.gz /Users/arnour.sabino/DockerVolumes/jupyter/paa191t2-0.0.0.tar.gz
	@cp -fR paa191t2/resources/nl*.txt /Users/arnour.sabino/DockerVolumes/jupyter/np/