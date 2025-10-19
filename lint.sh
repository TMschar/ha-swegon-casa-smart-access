#!/bin/bash

set -e

echo "Running code quality checks..."

venv_bin=".venv/bin"

echo "Running black..."
$venv_bin/black custom_components/swegon_casa

echo "Running isort..."
$venv_bin/isort custom_components/swegon_casa

echo "Running ruff..."
$venv_bin/ruff check --fix custom_components/swegon_casa

echo "Running mypy..."
$venv_bin/mypy custom_components/swegon_casa

echo "All checks passed!"
