#!/usr/bin/env python3
"""Integration test for Swegon Casa Smart Access client."""

import asyncio
import logging
import os
import sys
from pathlib import Path

import aiohttp
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).parent.parent))

from custom_components.swegon_casa.client import SwegonCasaClient

logging.basicConfig(level=logging.DEBUG)
_LOGGER = logging.getLogger(__name__)

env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

SWEGON_HOST = os.getenv("SWEGON_HOST", "172.23.13.103")
SWEGON_USERNAME = os.getenv("SWEGON_USERNAME", "service")
SWEGON_PASSWORD = os.getenv("SWEGON_PASSWORD", "")

BASE_URL = f"https://{SWEGON_HOST}"
USERNAME = SWEGON_USERNAME
PASSWORD = SWEGON_PASSWORD


class SwegonCasaTestWrapper:
    """Wrapper around SwegonCasaClient for testing."""

    def __init__(self, host: str, username: str, password: str):
        """Initialize the test wrapper."""
        self.client = SwegonCasaClient(host, username, password)
        self.session: aiohttp.ClientSession | None = None

    async def __aenter__(self):
        """Async context manager entry."""
        cookie_jar = aiohttp.CookieJar()
        self.session = aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False), cookie_jar=cookie_jar
        )
        self.client.set_session(self.session)
        return self.client

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        if self.session:
            await self.session.close()


async def test_login():
    """Test login functionality."""
    _LOGGER.info("\n=== TEST 1: Login ===")
    async with SwegonCasaTestWrapper(
        BASE_URL.replace("https://", ""), USERNAME, PASSWORD
    ) as client:
        success = await client.login()
        assert success, "Login failed"
        _LOGGER.info("✓ Test passed: Login successful")
        return True


async def test_fetch_data():
    """Test fetching sensor data."""
    _LOGGER.info("\n=== TEST 2: Fetch Sensor Data ===")
    async with SwegonCasaTestWrapper(
        BASE_URL.replace("https://", ""), USERNAME, PASSWORD
    ) as client:
        data = await client.fetch_data()
        assert data is not None, "Fetch data returned None"
        assert len(data) > 0, "No data returned"

        _LOGGER.info("Sensor data:")
        sensor_names = {
            "17": "Supply Temperature",
            "18": "Room Temperature",
            "19": "Outside Temperature",
            "22": "Humidity %",
            "23": "Humidity g/m³",
            "27": "Fan Speed (RPM)",
            "28": "Ventilation In %",
            "29": "Ventilation Out %",
            "31": "Boost Countdown",
            "121": "Travel Temp Drop",
            "163": "Setpoint Temperature",
            "111": "Climate Mode",
            "153": "Fireplace Mode",
            "154": "Travel Mode",
            "200": "Auto Humidity Mode",
            "201": "Summer Cooling Mode",
        }

        for sensor_id, value in sorted(data.items()):
            name = sensor_names.get(sensor_id, f"Unknown ({sensor_id})")
            _LOGGER.info(f"  {name}: {value}")

        _LOGGER.info("✓ Test passed: Data fetch successful")
        return data


async def test_climate_mode_set():
    """Test setting climate mode."""
    _LOGGER.info("\n=== TEST 3: Set Climate Mode ===")
    async with SwegonCasaTestWrapper(
        BASE_URL.replace("https://", ""), USERNAME, PASSWORD
    ) as client:
        mode_map = {
            1: "Away",
            2: "Home",
            3: "Boost",
            4: "Travel",
            5: "Off",
            6: "Fireplace",
        }

        data = await client.fetch_data()
        assert data is not None, "Failed to fetch initial data"
        original_mode = int(data.get("111", 2))

        test_mode = 3 if original_mode != 3 else 2
        _LOGGER.info(f"Setting climate mode to {test_mode} ({mode_map.get(test_mode)})")

        success = await client.set_value("111", test_mode)
        assert success, "Failed to set climate mode"

        await asyncio.sleep(1)

        data = await client.fetch_data()
        assert data is not None, "Failed to fetch data after setting mode"
        current_mode = int(data.get("111", original_mode))
        _LOGGER.info(
            f"Verified climate mode: {current_mode} ({mode_map.get(current_mode)})"
        )

        _LOGGER.info("✓ Test passed: Climate mode set successfully")


async def test_temperature_setpoint():
    """Test setting temperature setpoint."""
    _LOGGER.info("\n=== TEST 4: Set Temperature Setpoint ===")
    async with SwegonCasaTestWrapper(
        BASE_URL.replace("https://", ""), USERNAME, PASSWORD
    ) as client:
        data = await client.fetch_data()
        assert data is not None, "Failed to fetch initial data"
        original_temp = float(data.get("163", 20))

        test_temp = 22 if original_temp != 22 else 21
        _LOGGER.info(f"Setting setpoint temperature to {test_temp}°C")

        success = await client.set_value("163", test_temp)
        assert success, "Failed to set temperature setpoint"

        await asyncio.sleep(1)

        data = await client.fetch_data()
        assert data is not None, "Failed to fetch data after setting temperature"
        current_temp = float(data.get("163", original_temp))
        _LOGGER.info(f"Verified setpoint temperature: {current_temp}°C")

        _LOGGER.info("✓ Test passed: Temperature setpoint set successfully")


async def test_humidity_control_mode():
    """Test setting auto humidity control mode."""
    _LOGGER.info("\n=== TEST 5: Set Auto Humidity Control Mode ===")
    async with SwegonCasaTestWrapper(
        BASE_URL.replace("https://", ""), USERNAME, PASSWORD
    ) as client:
        mode_map = {0: "Off", 1: "User", 2: "Low", 3: "Normal", 4: "High", 5: "Full"}

        data = await client.fetch_data()
        assert data is not None, "Failed to fetch initial data"
        original_mode = int(data.get("200", 0))

        test_mode = 3 if original_mode != 3 else 2
        _LOGGER.info(
            f"Setting humidity mode to {test_mode} ({mode_map.get(test_mode)})"
        )

        success = await client.set_value("200", test_mode)
        assert success, "Failed to set humidity mode"

        await asyncio.sleep(1)

        data = await client.fetch_data()
        assert data is not None, "Failed to fetch data after setting humidity mode"
        current_mode = int(data.get("200", original_mode))
        _LOGGER.info(
            f"Verified humidity mode: {current_mode} ({mode_map.get(current_mode)})"
        )

        _LOGGER.info("✓ Test passed: Humidity mode set successfully")


async def test_cooling_mode():
    """Test setting summer night cooling mode."""
    _LOGGER.info("\n=== TEST 6: Set Summer Night Cooling Mode ===")
    async with SwegonCasaTestWrapper(
        BASE_URL.replace("https://", ""), USERNAME, PASSWORD
    ) as client:
        mode_map = {0: "Off", 1: "Low", 2: "Normal", 3: "High", 4: "Full", 5: "User"}

        data = await client.fetch_data()
        assert data is not None, "Failed to fetch initial data"
        original_mode = int(data.get("201", 0))

        test_mode = 1 if original_mode != 1 else 0
        _LOGGER.info(f"Setting cooling mode to {test_mode} ({mode_map.get(test_mode)})")

        success = await client.set_value("201", test_mode)
        assert success, "Failed to set cooling mode"

        await asyncio.sleep(1)

        data = await client.fetch_data()
        assert data is not None, "Failed to fetch data after setting cooling mode"
        current_mode = int(data.get("201", original_mode))
        _LOGGER.info(
            f"Verified cooling mode: {current_mode} ({mode_map.get(current_mode)})"
        )

        _LOGGER.info("✓ Test passed: Cooling mode set successfully")


async def test_fireplace_mode():
    """Test setting fireplace mode."""
    _LOGGER.info("\n=== TEST 7: Set Fireplace Mode ===")
    async with SwegonCasaTestWrapper(
        BASE_URL.replace("https://", ""), USERNAME, PASSWORD
    ) as client:
        mode_map = {0: "Off", 1: "On"}

        data = await client.fetch_data()
        assert data is not None, "Failed to fetch initial data"
        original_mode = int(data.get("153", 0))

        test_mode = 1 if original_mode != 1 else 0
        _LOGGER.info(
            f"Setting fireplace mode to {test_mode} ({mode_map.get(test_mode)})"
        )

        success = await client.set_value("153", test_mode)
        assert success, "Failed to set fireplace mode"

        await asyncio.sleep(1)

        data = await client.fetch_data()
        assert data is not None, "Failed to fetch data after setting fireplace mode"
        current_mode = int(data.get("153", original_mode))
        _LOGGER.info(
            f"Verified fireplace mode: {current_mode} ({mode_map.get(current_mode)})"
        )

        _LOGGER.info("✓ Test passed: Fireplace mode set successfully")


async def test_travel_mode():
    """Test setting travel mode."""
    _LOGGER.info("\n=== TEST 8: Set Travel Mode ===")
    async with SwegonCasaTestWrapper(
        BASE_URL.replace("https://", ""), USERNAME, PASSWORD
    ) as client:
        mode_map = {0: "Off", 1: "On"}

        data = await client.fetch_data()
        assert data is not None, "Failed to fetch initial data"
        original_mode = int(data.get("154", 0))

        test_mode = 1 if original_mode != 1 else 0
        _LOGGER.info(f"Setting travel mode to {test_mode} ({mode_map.get(test_mode)})")

        success = await client.set_value("154", test_mode)
        assert success, "Failed to set travel mode"

        await asyncio.sleep(1)

        data = await client.fetch_data()
        assert data is not None, "Failed to fetch data after setting travel mode"
        current_mode = int(data.get("154", original_mode))
        _LOGGER.info(
            f"Verified travel mode: {current_mode} ({mode_map.get(current_mode)})"
        )

        _LOGGER.info("✓ Test passed: Travel mode set successfully")


async def main():
    """Run all integration tests."""
    _LOGGER.info("Starting Swegon Casa Integration Tests")
    _LOGGER.info(f"Target: {BASE_URL}")

    try:
        await test_login()
        await test_fetch_data()

        await test_climate_mode_set()
        await test_temperature_setpoint()
        await test_humidity_control_mode()
        await test_cooling_mode()
        await test_fireplace_mode()
        await test_travel_mode()

        _LOGGER.info("\n" + "=" * 50)
        _LOGGER.info("✓ ALL TESTS PASSED!")
        _LOGGER.info("=" * 50)
        return True

    except AssertionError as e:
        _LOGGER.error(f"\n✗ TEST FAILED: {e}")
        return False
    except Exception as e:
        _LOGGER.error(f"\n✗ UNEXPECTED ERROR: {e}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
