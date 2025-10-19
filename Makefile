# Go testing targets
.PHONY: install test

install:
	uv sync && pnpm install

test:
	@echo "Running all Go tests..."
	@find . -name "*_test.go" | while read file; do \
		dir=$$(dirname "$$file"); \
		echo "Running tests in $$dir"; \
		cd "$$dir" && go test .; \
	done;
	@echo "All JavaScript tests..."
	pnpm test
	@echo "All Python tests..."
	# TODO: Add Python testing to this command