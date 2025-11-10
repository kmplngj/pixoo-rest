# Pixoo REST

> A modern, async RESTful API built with FastAPI to easily interact with Wi-Fi enabled [Divoom Pixoo](https://www.divoom.com/de/products/pixoo-64) devices.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

:sparkles: **NEW IN v2.0.0**  

Complete rewrite using **FastAPI** with modern async architecture!

* :zap: **Async/await** support for better performance
* :white_check_mark: **Pydantic v2** validation with automatic request validation
* :robot: **Automatic OpenAPI** documentation (Swagger UI + ReDoc)
* :package: **Modern Python packaging** with pyproject.toml and uv
* :shield: **Type hints** throughout for better IDE support
* :rocket: **Faster** response times with async HTTP calls

---

:information_source: **INFORMATION**  

This project was created back in February 2022; aiming to provide a REST-like interface for the [pixoo library](https://github.com/SomethingWithComputers/pixoo).  
With an [update from August 2024](https://github.com/SomethingWithComputers/pixoo/commit/9984e4dfea1cf60ae0ec2cd05a6d39fb40bd8644), the library's creator decided to implement/integrate a dedicated REST-interface himself.

However, `pixoo-rest` still offers unique features like ...

* :sparkles: Modern **FastAPI** architecture with automatic OpenAPI documentation
* :zap: **Async/await** support for concurrent operations
* :white_check_mark: **Pydantic validation** for request/response handling
* :package: **Modern Python tooling** with uv and pyproject.toml
* :framed_picture: **Image/GIF upload** support with file handling
* :globe_with_meridians: **URL downloads** for images and GIFs
* :arrow_forward: Built-in **Swagger UI** and ReDoc
* :whale: Pre-built **container images**

So... I'll keep maintaining the project as long as there's enough interest.

---

## Table of Contents

* [Introduction](#introduction)
* [Disclaimer](#disclaimer)
* [Changelog](#changelog)
* [Getting started](#getting-started)
   * [Clone](#clone)
   * [Init](#init)
   * [Configure](#configure)
* [Running](#running)
   * [Direct](#direct)
   * [Containerized](#containerized)
* [Usage](#usage)
   * [Examples](#examples)
* [License](#license)

## Introduction

**Pixoo REST v2.0** is a complete rewrite using **FastAPI**, providing a modern, async RESTful API with automatic documentation to interact with your Pixoo device.

### Features

* :pencil2: **Draw** - pixels, lines, rectangles, text, and characters
* :framed_picture: **Images** - upload files or provide URLs for images
* :film_strip: **GIFs** - animated GIF support with speed control
* :gear: **Settings** - brightness, channel, clock faces, visualizers
* :arrow_down: **Downloads** - automatically fetch and display images/GIFs from URLs
* :globe_with_meridians: **Divoom API** - device discovery and dial/clock browsing
* :zap: **Async** - non-blocking operations for better performance
* :white_check_mark: **Validation** - automatic request/response validation with Pydantic
* :robot: **Documentation** - interactive API docs at `/docs` and `/redoc`

**Pixoo REST** makes use of the great [Pixoo Python library](https://github.com/SomethingWithComputers/pixoo) by [SomethingWithComputers](https://github.com/SomethingWithComputers); which offers various helpful features like automatic image conversion. :thumbsup: 

## Disclaimer

This REST API is by no means a by-the-books reference on how proper REST APIs should be implemented; but simply a "convenience wrapper" for the aforementioned Pixoo library.

The actual HTTP API of the Pixoo device leaves a lot to be desired.  
First and foremost proper/official documentation. :wink:  
Most of the **pass-through** payload objects got discovered via *reverse engineering*, try-and-error, or this website: [doc.divoom-gz.com](http://doc.divoom-gz.com/web/#/12?page_id=143).

:warning: Use at your own risk.

## Changelog

A (more or less) detailed changelog can be found here: [:open_book:](CHANGELOG.md)

## Getting started

### Clone

Clone this repo ...
```bash
git clone https://github.com/4ch1m/pixoo-rest.git
```
... and change directory:
```bash
cd pixoo-rest
```

### Configure

Create an `.env`-file alongside the [compose.yml](compose.yml)-file and put your individual settings in it; like so:

```bash
# MANDATORY: the hostname or IP address of your Pixoo device
# Examples: "Pixoo64", "192.168.1.100"
PIXOO_HOST=192.168.178.11

# OPTIONAL: enable debug mode for the Pixoo library; defaults to "false"
PIXOO_DEBUG=false

# OPTIONAL: the screen size of your Pixoo device; defaults to "64"
# Valid values: 16, 32, 64
PIXOO_SCREEN_SIZE=64

# OPTIONAL: the hostname to listen on; defaults to "127.0.0.1"
PIXOO_REST_HOST=0.0.0.0

# OPTIONAL: the port being used; defaults to "5000"
PIXOO_REST_PORT=5000

# OPTIONAL: number of connection retries when starting; defaults to 3
PIXOO_TEST_CONNECTION_RETRIES=3
```

**Note:** All settings can also be passed as environment variables directly.

## Running

The app can now be run ...
* :snake: directly; using your existing (venv-)Python installation

or

* :package: fully packaged inside a dedicated (Docker-)container

### Direct

#### Using uv (Recommended)

This project uses [uv](https://docs.astral.sh/uv/) for fast and modern Python dependency management.

Install uv if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Sync dependencies and create virtual environment:
```bash
uv sync
```

Run the app with uv:
```bash
# Using the command-line entry point
uv run pixoo-rest

# Or run the module directly
uv run python -m pixoo_rest.app
```

Or activate the virtual environment and run directly:
```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pixoo-rest
```

#### Using pip (Traditional)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install from pyproject.toml
pip install -e .

# Run the app
pixoo-rest
```

### Containerized

Simply execute ...
```bash
docker compose up
```
... to automatically build the container and run it.

#### NEW :star:

If you don't want to build the container image yourself, you now can use the pre-built image from [hub.docker.com](https://hub.docker.com/r/4ch1m/pixoo-rest).

Simply uncomment the `image`-attribute in [compose.yml](compose.yml), and comment out the `build`-attribute:

```yaml
  app:
    image: 4ch1m/pixoo-rest:latest
    #build: .
```

## Usage

Once the server is running, you can access:

* **Interactive API docs (Swagger UI):** [http://localhost:5000/docs](http://localhost:5000/docs)
* **Alternative API docs (ReDoc):** [http://localhost:5000/redoc](http://localhost:5000/redoc)
* **OpenAPI schema:** [http://localhost:5000/openapi.json](http://localhost:5000/openapi.json)
* **Health check:** [http://localhost:5000/health](http://localhost:5000/health)

### Quick Examples

#### Draw a red pixel
```bash
curl -X POST "http://localhost:5000/draw/pixel" \
  -H "Content-Type: application/json" \
  -d '{"x": 10, "y": 10, "r": 255, "g": 0, "b": 0, "push_immediately": true}'
```

#### Fill screen with color
```bash
curl -X POST "http://localhost:5000/draw/fill" \
  -H "Content-Type: application/json" \
  -d '{"r": 0, "g": 100, "b": 255, "push_immediately": true}'
```

#### Set brightness
```bash
curl -X PUT "http://localhost:5000/set/brightness/80"
```

#### Send scrolling text
```bash
curl -X POST "http://localhost:5000/send/text" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Hello World!",
    "x": 0, "y": 24,
    "r": 255, "g": 255, "b": 0,
    "scroll_speed": 50
  }'
```

#### Display image from URL
```bash
curl -X POST "http://localhost:5000/download/image" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/image.png", "x": 0, "y": 0}'
```

#### Upload and display a GIF
```bash
curl -X POST "http://localhost:5000/sendGif" \
  -F "gif=@animation.gif" \
  -F "speed=100" \
  -F "skip_first_frame=false"
```

### API Endpoints

The API provides the following endpoint groups:

* **`/draw/*`** - Drawing operations (pixel, line, rectangle, text, etc.)
* **`/send/*`** - Send text with scrolling/animation
* **`/set/*`** - Device settings (brightness, channel, screen on/off)
* **`/image`** - Upload or display images from URLs (supports GIFs)
* **`/sendGif`** - Upload and display animated GIFs
* **`/download/*`** - Download and display images/GIFs/text from URLs
* **`/divoom/*`** - Divoom cloud API access (device discovery, clock faces)

For detailed documentation of all endpoints, parameters, and response schemas, visit the **Swagger UI** at `/docs` after starting the server.

### Shell Script Examples

A few example (shell-)scripts can be found here: [:toolbox:](examples)

## Credits

Example animation file ([duck.gif](swag/duck.gif)) by `kotnaszynce` / [OpenGameArt](https://opengameart.org/content/cute-duck-animated-set).

## License

Please read the [LICENSE](LICENSE) file.
