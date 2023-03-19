from models.Lift import lift
from utils.errors import NotFound
from utils.db_connect import get_cur
from dao.LiftDAO import *

def NewLiftService(payload):
    Lift = LiftFromJson(payload)
    saveLift(Lift)
    return Lift

def GetLiftService(position):
    sql_result = getLift(position)

    if sql_result == None:
        raise NotFound

    Lift = LiftFromSQL(sql_result)
    return Lift

def GetAllLiftService():
    return AllLiftFromSQL(getAllLift())

def UpdateLiftService(id, payload):
    user = LiftFromJson(payload)
    return updateLift(user, id)

def DeleteLiftService(id):
    deleteLift(id)

    if get_cur.rowcount == 0:
        raise NotFound

def DeleteAllLifts():
    deleteAllLift()

def LiftFromJson(payload):    
    try:
        Exercise = payload['Exercise']
    except:
        return "Missing Exercise field"
    try:
        Set = int(payload['Set'])
    except:
        return "Missing Set field"
    try:
        Rep = int(payload['Rep'])
    except:
        return "Missing Rep field"
    try:
        Weight = payload['Weight']
    except:
        return "Missing Weight field"
    try:
        Metric = payload['Metric']
    except:
        return "Missing Metric field"
    try:
        rpe = payload['RPE']
    except:
        return "Missing RPE field"
    try:
        Tags = payload['Tags']
    except:
        return "Missing Tags field"
    try:
        WorkoutStartTime = payload['WorkoutStartTime']
    except:
        return "Missing Tags field"
    try:
        RestTime = payload['RestTime']
    except:
        return "Missing Tags field"
    try:
        AvgVelocity = float(payload['AvgVelocity'])
    except:
        return "Missing Tags field"
    try:
        RoM = int(payload['RoM'])
    except:
        return "Missing Tags field"
    try:
        PeakVelocity = float(payload['PeakVelocity'])
    except:
        return "Missing Tags field"
    try:
        PeakVelocityLocation = int(payload['PeakVelocityLocation'])
    except:
        return "Missing Tags field"
    try:
        DurationOfRep = float(payload['DurationOfRep'])
    except:
        return "Missing Tags field"
    
    result =lift(Exercise,Weight,Metric,rpe,Tags,WorkoutStartTime,RestTime,AvgVelocity,PeakVelocity, DurationOfRep,PeakVelocityLocation,RoM,Set,Rep)
    return result

def LiftFromSQL(payload):
    try:
        id = payload[0]
    except:
        return "Missing id field"
    try:
        Exercise = payload[1]
    except:
        return "Missing Exercise field"
    try:
        PeakVelocityLocation = payload[2]
    except:
        return "Missing PeakVelocityLocation field"
    try:
        DurationOfRep = payload[3]
    except:
        return "Missing DurationOfRep field"
    try:
        Set = payload[4]
    except:
        return "Missing Set field"
    try:
        Rep = payload[5]
    except:
        return "Missing Rep field"
    try:
        Weight = payload[6]
    except:
        return "Missing Weight field"
    try:
        Metric = payload[7]
    except:
        return "Missing Metric field"
    try:
        rpe = payload[8]
    except:
        return "Missing rpe field"
    try:
        Tags = payload[9]
    except:
        return "Missing Tags field"
    try:
        WorkoutStartTime = payload[10]
    except:
        return "Missing WorkoutStartTime field"
    try:
        PeakVelocity = payload[11]
    except:
        return "Missing PeakVelocity field"
    try:
        RoM = payload[12]
    except:
        return "Missing RoM field"
    try:
        RestTime = payload[13]
    except:
        return "Missing RestTime field"
    try:
        AvgVelocity = payload[14]
    except:
        return "Missing AvgVelocity field"
    
    return lift(Exercise,Set,Rep,Weight,Metric,rpe,Tags,WorkoutStartTime,RestTime ,AvgVelocity,RoM,PeakVelocity,PeakVelocityLocation, DurationOfRep,id)

def AllLiftFromSQL(payload):
    lifts = []
    for lift in payload:
        lifts.append(LiftFromSQL(lift))
    return lifts
