
clean:
	rm -rf build dist *egg-info*

build:
	python3 setup.py sdist bdist_wheel

prelease:
	make clean
	make build
	twine check dist/*

release:
	make prelease
	twine upload dist/*