# CODE CHALLENGES 👨🏻‍💻

## PURPOSE

This repository is a collection of completed code challenges, katas, whiteboarding question practice, and other assorted problems from a variety of places.

A good general place to start is this [list of 14 techniques that are good to know for interviews](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed).

## TABLE OF CONTENTS

-   [Codewars](src/codewars/)
-   [Daily Coding Problem](src/daily-coding-problem)
-   [HackerRank](src/hacker-rank/)
-   [Interview Cake](src/interview-cake/)
-   [Lambda School](src/lambda-school/)
-   [LeetCode](src/leetcode/leetcode.md)
-   [Miscellaneous Code Challenges](src/miscellaneous-code-challenges/misc-code-challenges.md)
-   [Exponent Interviews](src/exponent/exponent.md)

## BUILT WITH

-   Aside from a few one-off solutions, the code challenges in this repository use [Golang](https://go.dev), [JavaScript](https://www.ecma-international.org/ecma-262/6.0/), and [Python](https://www.python.org/)
-   The JavaScript tests are written with Facebook's [Jest](https://jestjs.io/en/) for unit testing, while Python uses its built-in [unittest](https://docs.python.org/3.7/library/unittest.html#assert-methods). Go tests are written using the standard library [testing](https://pkg.go.dev/testing) package.

## GETTING STARTED

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

## ACKNOWLEDGEMENTS

-   Thanks to [Frank Faustino](https://github.com/frankfaustino) for inspiring me to create my own completed code challenges repository.
