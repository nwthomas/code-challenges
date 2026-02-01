# Code Challenges

## Purpose

This repository is a collection of completed code challenges from a variety of places.

## Table of Contents

-   [Codewars](src/codewars/)
-   [Daily Coding Problem](src/daily-coding-problem)
-   [HackerRank](src/hacker-rank/)
-   [Interview Cake](src/interview-cake/)
-   [Lambda School](src/lambda-school/)
-   [LeetCode](src/leetcode/leetcode.md)
-   [Miscellaneous Code Challenges](src/miscellaneous-code-challenges/misc-code-challenges.md)
-   [Exponent Interviews](src/exponent/exponent.md)

## Built With

-   Aside from a few one-off solutions, the code challenges in this repository use [Golang](https://go.dev), [JavaScript](https://www.ecma-international.org/ecma-262/6.0/), and [Python](https://www.python.org/)
-   The JavaScript tests are written with Facebook's [Jest](https://jestjs.io/en/) for unit testing, while Python uses [pytest](https://docs.pytest.org/en/stable/index.html). Go tests are written using the standard library [testing](https://pkg.go.dev/testing) package.

## Getting Started

1. Fork or clone this repository to your local machine

2. Install the languages and package/dependency management software for all languages:

    - Install [Go](https://go.dev), [JavaScript](https://nodejs.org), and [Python](https://www.python.org) - see each languages setup files in this repository for required versions
    - Ensure installation of [bun](https://bun.com) for JavaScript and [uv](https://docs.astral.sh/uv) for Python before doing dependency installation

3. Run `make i` or `make install` to install all required dependencies for all languages

4. For Go challenges:

    - Run the command `make test-go` to run all Go tests

5. For JavaScript challenges:

    - Run `make test-js`, `bun test <file name>`, or `bun test <file name> --watch` to run JS tests

6. For Python challenges:

    - Run `make test-py` to run all Python tests in the repository
