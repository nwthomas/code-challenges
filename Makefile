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

test-python:
	@echo "All Python tests..."
	# TODO: Add Python testing to this command