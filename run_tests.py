import os
import sys
import pytest

# Ensure the src directory is in the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Run the tests and generate a coverage report
exit_code = pytest.main([
    '--cov=src',        # Measure coverage for the src directory
    '--cov-report=term-missing',  # Show missing lines in the terminal
    '--cov-fail-under=85',  # Fail if coverage is under 85%
    '--cov-report=html',  # Generate an HTML report
    'tests'  # Directory containing the test files
])

sys.exit(exit_code)

