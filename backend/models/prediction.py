class Prediction:
    def __init__(self, prediction_id, robot_id, prediction, confidence, recommendation):
        self.prediction_id = prediction_id
        self.robot_id = robot_id
        self.prediction = prediction
        self.confidence = confidence
        self.recommendation = recommendation
