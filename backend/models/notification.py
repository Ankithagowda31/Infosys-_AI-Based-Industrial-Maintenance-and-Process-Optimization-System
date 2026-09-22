class Notification:
    def __init__(self, notification_id, robot_id, alert_type, message, priority):
        self.notification_id = notification_id
        self.robot_id = robot_id
        self.alert_type = alert_type
        self.message = message
        self.priority = priority
