def maintenance_status(prediction):
    if prediction == "Maintenance Required":
        return "Schedule Maintenance"
    return "No Maintenance Required"
