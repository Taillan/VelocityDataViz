from utils.db_connect import db_connection,get_cur
import sys

def saveLift(Lift):
    instruction = f'insert into Lift (exercise,set_number,rep,weight,metric,RPE,Tags,start_time,rest_time,avg_velocity,RoM,peak_velocity,peak_velocity_location,duration_of_rep) values ("{Lift.Exercise}","{Lift.Set}","{Lift.Rep}","{Lift.Weight}","{Lift.Metric}","{Lift.RPE}","{Lift.Tags}","{Lift.WorkoutStartTime}","{Lift.RestTime}","{Lift.AvgVelocity}","{Lift.RoM}","{Lift.PeakVelocity}","{Lift.PeakVelocityLocation}","{Lift.DurationOfRep}")'
    db_connection(instruction)
    return get_cur().lastrowid

def updateLift(Lift, id):
    instruction =   f'update Lift set Exercise="{Lift.Exercise}", Set="{Lift.Set}", Rep="{Lift.Rep}, Weight="{Lift.Weight}, Metric="{Lift.Metric}, RPE="{Lift.RPE}, Tags="{Lift.Tags}, WorkoutStartTime="{Lift.WorkoutStartTime}, RestTime="{Lift.RestTime}, AvgVelocity="{Lift.AvgVelocity}, RoM="{Lift.RoM}, PeakVelocity="{Lift.PeakVelocity}, PeakVelocityLocation="{Lift.PeakVelocityLocation}, DurationOfRep="{Lift.DurationOfRep}" where id={id}'
    return db_connection(instruction)
    
def getLift(id):    
    instruction = f'select * from Lift where id={id}'
    return db_connection(instruction).fetchone()

def getAllLift():
    instruction = f'select * from Lift;'
    return db_connection(instruction)

def deleteLift(id):
    instruction = f'delete from Lift where id={id}'
    return db_connection(instruction)

def deleteAllLift():
    instruction = f'delete from Lift'
    return db_connection(instruction)