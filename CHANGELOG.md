# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.7.0] - 2025-11-09

### Added
- Modern `pyproject.toml` with PEP 621 compliant metadata
- Support for `uv` package manager for faster dependency resolution
- `agents.md` documentation for AI-assisted development workflow
- Development dependencies group (pytest, black, ruff, mypy)
- Proper project classifiers and URLs in package metadata
- Enhanced `/image` endpoint that accepts both file uploads and image URLs

### Changed
- Migrated from `requirements.txt` to `pyproject.toml` for dependency management
- Adopted Semantic Versioning 2.0.0
- **BREAKING**: Updated minimum Python version requirement to `>=3.10` (required by pixoo dependency)
- Improved project structure following modern Python standards
- Updated CHANGELOG format to follow Keep a Changelog standard
- Modernized Dockerfile to use Python 3.12 and uv package manager

### Deprecated
- `requirements.txt` (use `pyproject.toml` instead)
- `version.txt` (version now managed in `pyproject.toml`)

### Removed
- Legacy `requirements.txt` workflow in favor of `pyproject.toml`
- Helm chart directory (no longer supported)
- Renamed `docker-compose.yml` to `compose.yml` (modern Docker Compose naming)

## [1.6.0] - 2024-08-28

* removed `pixoo` as git-submodule; now added via PyPi package
* other dependencies updated

## 1.5.1 (2024-05-09)

* improved configuration options when running behind a reverse proxy:  
  the `SCRIPT_NAME` environment variable (see [WSGI docs](https://wsgi.readthedocs.io/en/latest/definitions.html#envvar-SCRIPT_NAME)) is now taken into consideration; making it possible to set a custom base-path

## 1.5.0 (2024-05-06)

* new: (passthrough-)endpoint `sendHttpItemList`, which is available with the latest firmware update and offers drawing of multiple text-elements at once
* new: custom `download/text` endpoint
* new: Helm charts / K8s
* improved handling for GIF file upload (automatically limit to 59 frames; following the restriction of the device/API)
* updated dependencies
* other minor improvements

## 1.4.2 (2024-02-10)

* updated dependencies
* minor improvements (Dockerfile, docker-compose, log output, etc.)

## 1.4.1 (2023-10-16)

* updated dependencies
* minor improvements

## 1.4.0 (2023-07-23)

* new "download" endpoints (automatically download and send images to your Pixoo)

## 1.3.4 (2023-06-26)

* dependency updates

## 1.3.3 (2023-05-06)

* dependency updates

## 1.3.2 (2023-03-21)

* fix dependency conflict (_flasgger_ requires _Pillow_ 9.2.0)

## 1.3.1 (2023-03-21)

* dependency updates
* "restart" directive removed from [docker-compose.yml](docker-compose.yml) 

## 1.3.0 (2023-01-06)

* new: 'divoom' section (query official [API](https://app.divoom-gz.com))
* dependency updates
* other minor improvements

## 1.2.0 (2022-10-29)

* new environment settings `PIXOO_REST_HOST` and `PIXOO_REST_DEBUG` (see [README](README.md))
* new passthrough-commands:
  * GetDeviceTime
  * SetDisTempMode
  * SetTime24Flag
  * setHighLightMode
  * SetWhiteBalance
  * GetWeatherInfo
  * PlayBuzzer
* other minor improvements

## 1.1.0 (2022-10-05)

* improved [Dockerfile](Dockerfile) (checkout of the pixoo-library's explicit commit-hash; which should correlate with the git-submodule and pin the actual dependencies)
* new `screen/on/{true|false}` endpoint
* new passthrough-commands:
  * SetScreenRotationAngle
  * SetMirrorMode
* other minor improvements

## 1.0.0 (2022-03-05)

* initial release