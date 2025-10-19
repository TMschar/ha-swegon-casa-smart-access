"""Swegon Casa library constants and types."""

from enum import StrEnum


class MeasurementType(StrEnum):
    """Measurement types."""

    SUPPLY_TEMPERATURE = "supply_temperature"
    ROOM_TEMPERATURE = "room_temperature"
    OUTSIDE_TEMPERATURE = "outside_temperature"
    HUMIDITY_PERCENTAGE = "humidity_percentage"
    HUMIDITY_ABSOLUTE = "humidity_absolute"
    CURRENT_FAN_SPEED = "fan_speed"
    VENTILATION_LEVEL_IN = "ventilation_level_in"
    VENTILATION_LEVEL_OUT = "ventilation_level_out"
    BOOST_COUNTDOWN = "boost_countdown"
    TRAVEL_TEMP_DROP = "travel_temp_drop"
    SUPPLY_TEMP_SETPOINT = "supply_temp_setpoint"
    CURRENT_MODE = "current_mode"


class ModeType(StrEnum):
    """Mode types."""

    CLIMATE_MODE = "climate_mode"
    AUTO_HUMIDITY_CONTROL_MODE = "auto_humidity_control_mode"
    SUMMER_NIGHT_COOLING_MODE = "summer_night_cooling_mode"


class SettingType(StrEnum):
    """Setting types."""

    SUPPLY_TEMP_SETPOINT = "supply_temp_setpoint"
    TRAVEL_TEMP_DROP = "travel_temp_drop"


class ClimateModes(StrEnum):
    """Climate mode options."""

    AWAY = "Away"
    HOME = "Home"
    BOOST = "Boost"
    TRAVEL = "Travel"
    OFF = "Off"
    FIREPLACE = "Fireplace"


class AutoHumidityControlModes(StrEnum):
    """Auto humidity control mode options."""

    OFF = "Off"
    USER = "User"
    LOW = "Low"
    NORMAL = "Normal"
    HIGH = "High"
    FULL = "Full"


class SummerNightCoolingModes(StrEnum):
    """Summer night cooling mode options."""

    OFF = "Off"
    LOW = "Low"
    NORMAL = "Normal"
    HIGH = "High"
    FULL = "Full"
    USER = "User"


class FireplaceModes(StrEnum):
    """Fireplace mode options."""

    OFF = "Off"
    ON = "On"


class TravelModes(StrEnum):
    """Travel mode options."""

    OFF = "Off"
    ON = "On"


class SwegonObjectId(StrEnum):
    """Swegon Casa object IDs."""

    TEMPERATURE_SUPPLY = "17"
    TEMPERATURE_ROOM = "18"
    TEMPERATURE_OUTSIDE = "19"
    HUMIDITY_PERCENTAGE = "22"
    HUMIDITY_ABSOLUTE = "23"
    CURRENT_FAN_SPEED = "27"
    VENTILATION_LEVEL_IN = "28"
    VENTILATION_LEVEL_OUT = "29"
    BOOST_COUNTDOWN = "31"
    SETPOINT_SUPPLY_TEMPERATURE = "163"
    CLIMATE_MODE = "111"
    TRAVEL_MODE_TEMPERATURE_DROP = "121"
    AUTO_HUMIDITY_CONTROL_MODE = "200"
    SUMMER_NIGHT_COOLING_MODE = "201"
    FIREPLACE_MODE = "153"
    TRAVEL_MODE = "154"
