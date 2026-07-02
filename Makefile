.PHONY: install quality test demo

install:
	pip install -e .
	pre-commit install

quality:
	pre-commit run --all-files

test:
	pytest

demo:
	python demos/demo_header_parser.py
	