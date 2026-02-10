#!/usr/bin/env python3
"""Wrapper script for sphinx-build to use with Bazel."""

import sys

from sphinx.cmd.build import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
