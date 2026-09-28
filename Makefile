# Development commands
.PHONY: install i test-go test-ts typecheck test-py

install i:
	uv sync && bun install

test-go:
	@echo "Running all Go tests..."
	@find . -name "*_test.go" | while read file; do \
		dir=$$(dirname "$$file"); \
		echo "Running tests in $$dir"; \
		go test "$$dir"; \
	done;

test-ts:
	@echo "Running all TypeScript tests..."
	bun run test

typecheck:
	bun run typecheck

test-py:
	@echo "Running all Python tests..."
	# -s: Allows for print statements to be displayed
	# -v: Increases verbosity of test output
	# -vv: Does not truncate test output
	uv run pytest -s -vv
