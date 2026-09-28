# Code Challenges

## Purpose

This repository is a collection of completed code challenges from a variety of places.

## Table of Contents

- [Codewars](src/codewars/)
- [Daily Coding Problem](src/daily-coding-problem)
- [HackerRank](src/hacker-rank/)
- [Interview Cake](src/interview-cake/)
- [Lambda School](src/lambda-school/)
- [LeetCode](src/leetcode/leetcode.md)
- [Miscellaneous Code Challenges](src/miscellaneous-code-challenges/misc-code-challenges.md)
- [Exponent Interviews](src/exponent/exponent.md)

## Built With

- Aside from a few one-off solutions, the code challenges in this repository use [Golang](https://go.dev), [TypeScript](https://www.typescriptlang.org/), and [Python](https://www.python.org/)
- The TypeScript tests use [Vitest](https://vitest.dev/) for unit testing, while Python uses [pytest](https://docs.pytest.org/en/stable/index.html). Go tests are written using the standard library [testing](https://pkg.go.dev/testing) package.

## Getting Started

1. Fork or clone this repository to your local machine

2. Install the languages and package/dependency management software for all languages:

    - Install [Go](https://go.dev), [Node.js](https://nodejs.org), and [Python](https://www.python.org) - see each languages setup files in this repository for required versions
    - Ensure installation of [bun](https://bun.com) for TypeScript dependencies and [uv](https://docs.astral.sh/uv) for Python before doing dependency installation

3. Run `make i` or `make install` to install all required dependencies for all languages

4. For Go challenges:

    - Run the command `make test-go` to run all Go tests

5. For TypeScript challenges:

    - Run `make test-ts` or `bun run test` to run all tests once
    - Run `bun run test <file name>` to run a single test file
    - Run `bun run test:watch <file name>` for watch mode
    - Run `make typecheck` or `bun run typecheck` to check implementations and tests with strict TypeScript settings

6. For Python challenges:

    - Run `make test-py` to run all Python tests in the repository

## TypeScript conventions

The TypeScript challenges use ESM (`import` / `export`) and explicit `.ts` extensions for relative imports. Keep each solution and its `.test.ts` file together. Import test helpers such as `describe`, `test`, and `expect` from `vitest`.

Vitest runs TypeScript directly; no build output is needed. Type checking is a separate step, and CI runs both checks. Use `bun run test`, since `bun test` starts Bun's own test runner instead of Vitest.

Tests that intentionally pass invalid inputs retain their runtime assertions and use a documented `@ts-expect-error` on the invalid call. Avoid suppressing errors in solution code. Unfinished challenge directories already listed in `.gitignore` are also excluded from `tsconfig.json`; remove that exclusion when completing a challenge.
