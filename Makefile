all: package

package:
	python3 setup.py sdist bdist_wheel

upload: package
	twine upload dist/*

clean:
	rm -rf build dist *.egg-info
	sed -i "s/__version__ = .*/__version__ = 'GIT_TAG'/g" drawio/__init__.py
