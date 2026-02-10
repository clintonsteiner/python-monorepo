# Adding a New Package with Separate Dependencies

This guide shows how to add a new package "hildie-web" that depends on the hildie library but has its own dependencies (Flask).

## Option 1: Share the Main Requirements File (Recommended for Simple Cases)

### 1. Add dependencies to `lock_requirements.txt`
```txt
# Add your new dependencies
flask==3.0.0
```

### 2. Create source code structure
```bash
mkdir -p src/hildie/hildie_web
```

Create `src/hildie/hildie_web/__init__.py`:
```python
"""Hildie web package."""
from .app import create_app

__all__ = ["create_app"]
```

Create `src/hildie/hildie_web/app.py`:
```python
"""Flask web application."""
from flask import Flask
from hildie.hildie_library import add, multiply

def create_app():
    app = Flask(__name__)

    @app.route("/add/<int:a>/<int:b>")
    def add_numbers(a, b):
        return {"result": add(a, b)}

    @app.route("/multiply/<int:a>/<int:b>")
    def multiply_numbers(a, b):
        return {"result": multiply(a, b)}

    return app
```

Create `src/hildie/hildie_web/main.py`:
```python
"""CLI entrypoint for web server."""
import click
from .app import create_app

@click.command()
@click.option("--port", default=5000, help="Port to run on")
def cli(port):
    """Run the Hildie web server."""
    app = create_app()
    app.run(port=port)

if __name__ == "__main__":
    cli()
```

### 3. Create test structure
```bash
mkdir -p packages/web/tests
```

Create `packages/web/tests/test_web.py`:
```python
"""Tests for hildie-web package."""
from hildie.hildie_web import create_app

def test_create_app():
    """Test app creation."""
    app = create_app()
    assert app is not None

def test_add_endpoint():
    """Test add endpoint."""
    app = create_app()
    client = app.test_client()
    response = client.get("/add/2/3")
    assert response.json == {"result": 5}
```

### 4. Create `packages/web/BUILD.bazel`
```python
"""BUILD file for hildie-web tests."""

load("//tools:pytest.bzl", "package_tests")

package_tests(deps = ["@pip//flask"])
```

### 5. Add CLI binary to root `BUILD.bazel`
```python
hildie_cli(
    name = "hildie-web",
    module = "hildie_web",
)
```

### 6. Add to test suite in root `BUILD.bazel`
```python
all_package_tests(
    name = "all_tests",
    packages = [
        "archive-git-forks",
        "my-app",
        "my-cli",
        "my-library",
        "web",  # Add this
    ],
)
```

### 7. Update lock file and build
```bash
bazel run @pip//:requirements.update
bazel build //packages/web:tests
bazel test //packages/web:tests
bazel run //:hildie-web -- --port 8080
```

---

## Option 2: Separate Requirements File (Recommended for Complex Dependencies)

### 1. Create separate requirements file

Create `packages/web/requirements.txt`:
```txt
flask==3.0.0
werkzeug==3.0.0
```

Create `packages/web/lock_requirements.txt` (run `pip-compile` or manually):
```txt
flask==3.0.0
werkzeug==3.0.0
blinker==1.7.0
click==8.1.7
itsdangerous==2.1.2
jinja2==3.1.2
markupsafe==2.1.3
```

### 2. Update `MODULE.bazel` to add new pip hub
```python
pip = use_extension("@rules_python//python/extensions:pip.bzl", "pip")
pip.parse(
    hub_name = "pip",
    python_version = "3.12",
    requirements_lock = "//:lock_requirements.txt",
)
pip.parse(
    hub_name = "pip_docs",
    python_version = "3.12",
    requirements_lock = "//docs:lock_requirements.txt",
)
# Add new pip hub for web package
pip.parse(
    hub_name = "pip_web",
    python_version = "3.12",
    requirements_lock = "//packages/web:lock_requirements.txt",
)
use_repo(pip, "pip", "pip_docs", "pip_web")
```

### 3. Update `packages/web/BUILD.bazel` to use new hub
```python
"""BUILD file for hildie-web tests."""

load("//tools:pytest.bzl", "package_tests")

# Note: Using pip_web hub instead of pip
package_tests(deps = ["@pip_web//flask"])
```

### 4. Create CLI binary with web dependencies

In root `BUILD.bazel`, you'll need a custom binary (not using the macro):
```python
py_binary(
    name = "hildie-web",
    srcs = ["src/hildie/hildie_web/main.py"],
    main = "src/hildie/hildie_web/main.py",
    deps = [
        ":hildie",
        "@pip_web//flask",
    ],
)
```

---

## Quick Reference

### File Structure
```
├── src/hildie/
│   └── hildie_web/          # Source code
│       ├── __init__.py
│       ├── app.py
│       └── main.py
├── packages/
│   └── web/                 # Tests
│       ├── BUILD.bazel
│       ├── requirements.txt (Option 2 only)
│       ├── lock_requirements.txt (Option 2 only)
│       └── tests/
│           └── test_web.py
├── BUILD.bazel              # Add binary + test suite
└── MODULE.bazel             # Add pip hub (Option 2 only)
```

### Common Commands
```bash
# Build tests
bazel build //packages/web:tests

# Run tests
bazel test //packages/web:tests

# Run all tests including new package
bazel test //:all_tests

# Run the CLI
bazel run //:hildie-web

# Update dependencies (Option 1)
bazel run @pip//:requirements.update

# Update dependencies (Option 2)
bazel run @pip_web//:requirements.update
```

### When to Use Which Option?

**Option 1 (Shared requirements):**
- ✅ Simple, fewer files
- ✅ Good for packages with overlapping dependencies
- ✅ Easier to manage
- ❌ All packages share same dependency versions

**Option 2 (Separate requirements):**
- ✅ Isolated dependency versions per package
- ✅ Better for conflicting dependency requirements
- ✅ Clearer dependency boundaries
- ❌ More configuration overhead
- ❌ More lock files to maintain
