#!/bin/bash -e

py.test -rsxX -q --cov-config=.coveragerc --cov-report=html --cov-report=term-missing --cov=src ./tests/unit
