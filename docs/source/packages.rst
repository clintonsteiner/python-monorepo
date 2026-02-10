Packages
========

The Hildie monorepo contains several packages, each serving a specific purpose.

archive-git-forks
-----------------

Tools for archiving and managing Git fork repositories.

**Purpose:** Helps manage and archive Git forks when you need to preserve copies of
forked repositories.

**Location:** ``packages/archive-git-forks``

my-app
------

Application utilities and helpers.

**Purpose:** Common utilities for building Python applications.

**Location:** ``packages/my-app``

my-cli
------

Command-line interface tools and utilities.

**Purpose:** Tools for building CLI applications with Python.

**Location:** ``packages/my-cli``

my-library
----------

Core library functions and utilities.

**Purpose:** General-purpose utilities and helper functions used across the monorepo.

**Location:** ``packages/my-library``

Package Structure
-----------------

Each package follows a consistent structure:

.. code-block:: text

   packages/<package-name>/
   ├── BUILD.bazel          # Bazel build configuration
   ├── pyproject.toml       # Package metadata
   ├── src/                 # Source code
   │   └── <package>/
   │       └── __init__.py
   └── tests/               # Tests
       └── test_*.py

Building Packages
-----------------

Using Bazel:

.. code-block:: bash

   # Build all packages
   bazel build //...

   # Build a specific package
   bazel build //packages/my-library:my-library

   # Run tests
   bazel test //...

Using standard Python tools:

.. code-block:: bash

   # From a package directory
   cd packages/my-library
   uv pip install -e .
