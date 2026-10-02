# Repository Guidelines

## Project Structure & Module Organization

This repository collects coding challenges, primarily in TypeScript, Python, and Go. Solutions live under `src/`, grouped by source: `leetcode`, `codewars`, `daily-coding-problem`, `exponent`, `hacker-rank`, `interview-cake`, `lambda-school`, and `miscellaneous-code-challenges`. Some groups include difficulty or course-week subdirectories.

Place each challenge in a descriptive kebab-case directory, such as `src/leetcode/easy/climbing-stairs/`, with implementations and tests together. Preserve problem statements and source links; update the relevant Markdown challenge index when adding a solution. There is no central application or shared asset directory.

## Build, Test, and Development Commands

Use Node.js 25, Python 3.14+, Go 1.25.4, Bun, and uv, matching repository configuration.

- `make install` (or `make i`): install Python and TypeScript dependencies.
- `make test-ts`: run all Vitest tests once.
- `bun run test:watch <file>`: watch a TypeScript test file during development.
- `make typecheck`: check TypeScript implementations and tests without emitting files.
- `make test-py`: run Python tests through uv and pytest.
- `make test-go`: run Go tests in challenge directories.
- `bun run format:check`: check configured files with Prettier; `bun run format` applies formatting.

There is no application server or production build step.

## Coding Style & Naming Conventions

Follow neighboring solutions and keep changes focused on the challenge. TypeScript uses strict checking, ES modules, four-space indentation, semicolons, double quotes, and trailing commas through Prettier. Match existing TypeScript filenames, which use both camelCase and kebab-case. Python uses four-space indentation and snake_case filenames and functions; Pylint configuration is in `pyproject.toml`. Format Go changes with `gofmt`.

## Testing Guidelines

Use Vitest with `*.test.ts`, pytest with `test_*.py` (including existing unittest-style tests), and Go's standard `testing` package with `*_test.go`. Cover examples, boundary inputs, and regressions. No numeric coverage threshold is configured.

Run focused tests with `bun run test <file>`, `uv run pytest <path>`, or `go test ./src/<challenge-path>`. Before submitting, run the relevant language suite and TypeScript typechecking when applicable; CI runs all three suites and typechecking.

## Commit & Pull Request Guidelines

Use short, imperative commit subjects consistent with history, such as `Add curry solution + tests` or `Update tests for car fleet`. Keep commits scoped. Pull requests should describe the challenge or fix, explain algorithmic tradeoffs where relevant, list validation commands and results, and link related issues when available.
