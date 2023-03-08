class lift():
    def __init__(self,Exercise: str,  Weight: str, Metric: str, RPE: int, Tags: str, WorkoutStartTime: str, RestTime: str, AvgVelocity: float,  PeakVelocity: float, DurationOfRep: float,PeakVelocityLocation:int=0, RoM: int=0,  Set: int=0, Rep: int=0,id: int=None):
        self.id = id,
        self.Exercise =Exercise,
        self.Set = Set,
        self.Rep = Rep,
        self.Weight = Weight,
        self.Metric = Metric,
        self.RPE = RPE,
        self.Tags = Tags,
        self.WorkoutStartTime = WorkoutStartTime,
        self.RestTime = RestTime,
        self.AvgVelocity = AvgVelocity,
        self.RoM = RoM,
        self.PeakVelocity = PeakVelocity,
        self.PeakVelocityLocation = PeakVelocityLocation,
        self.DurationOfRep = DurationOfRep
    
    def toJSON(self):
        return {"Exercise": self.Exercise, "Set": self.Set, "Rep":self.Rep, "Weight": self.Weight, "Metric":self.Metric, "RPE": self.RPE, "Tags":self.Tags, "WorkoutStartTime": self.WorkoutStartTime, "RestTime":self.RestTime, "AvgVelocity": self.AvgVelocity, "RoM":self.RoM, "PeakVelocity": self.PeakVelocityLocation, "email":self.PeakVelocityLocation, "DurationOfRep": self.DurationOfRep}