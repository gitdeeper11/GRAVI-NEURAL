install:
	pip install -e .[dev]

test:
	pytest tests/ -v

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache

build:
	python -m build

run:
	python bin/compute_metric.py --verbose
