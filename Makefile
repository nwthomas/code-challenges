# Development commands
.PHONY: install i
install i:
	uv sync && bun install

.PHONY: test-go
test-go:
	@echo "Running all Go tests..."
	@go test -count=1 ./...

.PHONY: test-ts
test-ts:
	@echo "Running all TypeScript tests..."
	bun run test

.PHONY: typecheck
typecheck:
	bun run typecheck

.PHONY: test-py
test-py:
	@echo "Running all Python tests..."
	# -s: Allows for print statements to be displayed
	# -v: Increases verbosity of test output
	# -vv: Does not truncate test output
	uv run pytest -s -vv
