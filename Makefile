
clean:
	rm -rf build dist *egg-info*

build:
	python3 setup.py sdist bdist_wheel

prelease:
	twine check dist/*

release:
	make build
	make prelease
	twine upload dist/*