class Telemetry:
    def __init__(
        self,
        telemetry_id,
        robot_id,
        temperature,
        vibration,
        current,
        voltage,
        power,
        rpm,
        timestamp,
    ):
        self.telemetry_id = telemetry_id
        self.robot_id = robot_id
        self.temperature = temperature
        self.vibration = vibration
        self.current = current
        self.voltage = voltage
        self.power = power
        self.rpm = rpm
        self.timestamp = timestamp
