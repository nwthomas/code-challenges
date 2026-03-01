# Go testing targets
.PHONY: install i test

install i:
	uv sync && bun install

test-go:
	@echo "Running all Go tests..."
	@find . -name "*_test.go" | while read file; do \
		dir=$$(dirname "$$file"); \
		echo "Running tests in $$dir"; \
		go test "$$dir"; \
	done;

test-js:
	@echo "All JavaScript tests..."
	bun run test

test-py:
	@echo "Running all Python tests..."
	# -s: Allows for print statements to be displayed
	# -v: Increases verbosity of test output
	# -vv: Does not truncate test output
	uv run pytest -s -vv