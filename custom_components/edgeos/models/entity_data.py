from __future__ import annotations

import datetime
from datetime import date
from typing import Optional

from homeassistant.helpers.typing import StateType

from ..helpers.const import *


class EntityData:
    unique_id: str
    name: str
    state: StateType | date | datetime
    attributes: dict
    icon: str
    device_name: str
    status: str
    disabled: bool
    binary_sensor_device_class: BinarySensorDeviceClass | None
    sensor_device_class: SensorDeviceClass | None
    sensor_state_class: SensorStateClass | None

    def __init__(self):
        self.unique_id = ""
        self.name = ""
        self.state = 0
        self.attributes = {}
        self.icon = ""
        self.device_name = ""
        self.status = ENTITY_STATUS_CREATED
        self.disabled = False
        self.binary_sensor_device_class = None
        self.sensor_device_class = None
        self.sensor_state_class = None

    def __repr__(self):
        obj = {
            ENTITY_NAME: self.name,
            ENTITY_STATE: self.state,
            ENTITY_ATTRIBUTES: self.attributes,
            ENTITY_ICON: self.icon,
            ENTITY_DEVICE_NAME: self.device_name,
            ENTITY_STATUS: self.status,
            ENTITY_UNIQUE_ID: self.unique_id,
            ENTITY_DISABLED: self.disabled,
            ENTITY_BINARY_SENSOR_DEVICE_CLASS: self.binary_sensor_device_class,
            ENTITY_SENSOR_DEVICE_CLASS: self.sensor_device_class,
            ENTITY_SENSOR_STATE_CLASS: self.sensor_state_class
        }

        to_string = f"{obj}"

        return to_string
