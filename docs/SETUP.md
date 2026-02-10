# Documentation Setup Instructions

## Add Hildie's Photo

To complete the documentation setup, add Hildie's photo to the static directory:

```bash
# Copy hildie.jpeg (or hildie_dog.jpeg) to the docs static directory
cp hildie.jpeg docs/source/_static/hildie.jpeg
```

Or if the file is named differently:

```bash
cp path/to/hildie_dog.jpeg docs/source/_static/hildie.jpeg
```

The documentation is configured to display this image on:
- The main index page
- The "About Hildie" page
- As the site logo (in the sidebar)
- As the favicon

## Build and View

Once the image is in place:

```bash
# Install dependencies
uv pip install -e ".[docs]"

# Build the docs
cd docs
make html

# Open in browser
open build/html/index.html
```

## What's Included

The documentation includes:

- **About page**: Tells the story of why the package is named after Hildie
- **Installation guide**: How to install the package
- **Packages overview**: Description of each package in the monorepo
- **API reference**: Auto-generated API documentation

The "About" page specifically highlights that all the good package names were taken,
so the project is named after Hildie, the best dog!
