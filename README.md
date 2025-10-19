# Swegon Casa Home Assistant Integration

[![GitHub Release](https://img.shields.io/github/release/TMschar/ha-swegon-casa-smart?style=flat-square)](https://github.com/TMschar/ha-swegon-casa-smart/releases)
[![GitHub Downloads](https://img.shields.io/github/downloads/TMschar/ha-swegon-casa-smart/total?style=flat-square)](https://github.com/TMschar/ha-swegon-casa-smart)
[![HACS Badge](https://img.shields.io/badge/HACS-default-41BDF5?style=flat-square)](https://github.com/hacs/integration)

A comprehensive Home Assistant integration for Swegon Casa air handling units. Control your HVAC system, monitor indoor and outdoor air quality, and manage humidity settings directly from Home Assistant.

## Features

**HVAC Control**
- Climate mode selection (Away, Home, Boost, Travel, Off, Fireplace)
- Temperature setpoint adjustment
- Travel mode with temperature drop control
- Fireplace mode toggle

**Monitoring**
- Supply, return, and outdoor temperature sensors
- Humidity percentage and absolute humidity tracking
- Fan speed monitoring (supply and exhaust)
- Boost countdown tracking

**Controls**
- Auto humidity control mode selection
- Summer night cooling mode
- Humidity target adjustment
- Cooling mode control

## Installation

### Via HACS (Recommended)
1. Go to **Settings** → **Devices & Services** → **HACS**
2. Click the **Explore & Download Repositories** button
3. Search for "Swegon Casa Smart Access"
4. Click **Download**
5. Restart Home Assistant

### Manual Installation
1. Download the latest release from [GitHub Releases](https://github.com/TMschar/ha-swegon-casa-smart-access/releases)
2. Extract to `~/.homeassistant/custom_components/swegon_casa`
3. Restart Home Assistant

## Setup

1. Go to **Settings** → **Devices & Services** → **Create Integration**
2. Search for "Swegon Casa Smart Access"
3. Enter your Swegon Casa Smart Access credentials
   You should have these from the package with the Smart Access Module, as a sticker
4. Complete the setup

## Supported Entities

### Climate
- Main HVAC entity with current temperature and mode control

### Sensors
- Supply, return, and outdoor temperatures
- Humidity (% and g/m³)
- Fan speeds and boost countdown

### Selects
- Climate mode
- Auto humidity control
- Cooling mode
- Fireplace mode toggle
- Travel mode toggle

### Numbers
- Temperature setpoint
- Travel mode temperature drop

## Requirements

- Home Assistant 2023.12+
- Python 3.11+
- Swegon Casa Smart Access module with network connectivity

It does not have to be connected to the cloud!

## Troubleshooting

**Integration fails to add:**
- Verify credentials are correct
- Verify the IP is correct (connect to it via web browser)

**Entities not updating:**
- Check Home Assistant logs
- Verify device is still online
- Restart the integration

## Architecture

The integration uses a clean async architecture:
- `client.py`: HTTP/WebSocket client for Swegon API
- `config_flow.py`: Setup wizard and authentication
- `climate.py`: HVAC climate entity
- `sensor.py`: Temperature and humidity sensors
- `select.py`: Mode and control selections
- `number.py`: Numeric controls (temperature setpoints)
- `const.py`: Constants and mappings

## Development

### Setup Development Environment
```bash
uv sync --all-groups
```

### Run Quality Checks
```bash
bash lint.sh
```

### Run Tests
```bash
uv run pytest tests/
```

## License

Apache License

## Support

For issues, feature requests, or questions:
- [GitHub Issues](https://github.com/TMschar/ha-swegon-casa-smart-access/issues)
- Documentation: [Integration Guide](./custom_components/swegon_casa/README.md)

---

*This integration is not affiliated with Swegon or Home Assistant.*
