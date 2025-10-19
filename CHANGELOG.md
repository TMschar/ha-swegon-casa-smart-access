# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-19

### Added
- Initial release of Swegon Casa Smart Access Module Home Assistant integration

### Features
- **Climate Entity**: HVAC control with current temperature display
- **Sensor Entities**: 
  - Supply, return, and outdoor temperature sensors
  - Humidity percentage and absolute humidity (g/m³)
  - Fan speed monitoring
  - Boost countdown
- **Select Entities**:
  - Climate mode control
  - Auto humidity control mode
  - Cooling mode selection
  - Fireplace mode toggle
  - Travel mode toggle
- **Number Entities**:
  - Temperature setpoint adjustment
  - Travel mode temperature drop control

### Dependencies
- aiohttp >= 3.8.0
- websockets >= 11.0
- homeassistant >= 2023.12.0
- python-dotenv >= 1.0.0

### Code Quality
- Black code formatting
- isort import sorting
- Ruff linting
- mypy type checking
- Comprehensive test suite

---

For more information, see the [README](README.md).
