# Go testing targets
.PHONY: install test

install:
	uv sync && pnpm install

test-go:
	@echo "Running all Go tests..."
	@find . -name "*_test.go" | while read file; do \
		dir=$$(dirname "$$file"); \
		echo "Running tests in $$dir"; \
		go test "$$dir"; \
	done;

test-js:
	@echo "All JavaScript tests..."
	pnpm test
	@echo "All Python tests..."

test-py:
    # NOTE: This isn't a standard way to run Python tests, but I didn't each directory with an __init__.py file so here we are.
	@echo "Running all Python tests..."
	find src -name "test_*.py" -type f | while read file; do \
		echo "\n==============================================\n\nRunning $$file"; \
		python "$$file"; \
	done;