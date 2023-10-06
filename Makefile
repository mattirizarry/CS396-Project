# This Makefile is used to install Python dependencies with pip.

# Define the Python interpreter to use. You can change this if needed.
PYTHON := python3

# List your project's dependencies here.
DEPENDENCIES := \
    package1 \
    package2 \
    package3

# Default target: Install dependencies
install:
	@echo "Installing Python dependencies..."
	$(PYTHON) -m pip install -U -r requirements.txt

# Clean target: Remove installed dependencies
clean:
	@echo "Removing Python dependencies..."
	$(PYTHON) -m pip uninstall -y -r requirements.txt

.PHONY: install clean help
