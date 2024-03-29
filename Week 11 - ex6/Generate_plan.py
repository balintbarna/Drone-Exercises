import json
from math import atan2, degrees

class plan_generator():
    def __init__(self, alleVal,allnVal):
        self.alleVal = alleVal
        self.allnVal = allnVal

        self.plan = {}
        self.items = []
        self.plan['fileType'] = 'Plan'

        self.plan['version'] = 1
        self.plan['groundStation'] = 'QGroundControl'
        geoFence = {}
        geoFence['polygon'] = [] 
        geoFence['version'] = 1 
        self.plan['geoFence'] = geoFence
        rallyPoints = {}
        rallyPoints['points'] = [] 
        rallyPoints['version'] = 1 
        self.plan['rallyPoints'] = rallyPoints

    def getAngle(self,posS,posT):
        return degrees(atan2(posT[1]-posS[1],posT[0]-posS[0]))

    def minimizeDisErr(self):

        print("Plz make this")

    def minimizeAngErr(self):
        print("Plz make this")

    def addItem(self,command,doJumpId,frame,lat,lon):
        item = {}
        item['autoContinue'] = True
        item['command'] = command
        item['doJumpId'] = doJumpId
        item['frame'] = frame
        item['params'] = [0,0,0,0,lat,lon,50]
        item['type'] = 'SimpleItem'
        self.items.append (item)
    
    def setMission(self,home,cruise=15,hover=5):
        mission = {}
        mission['cruiseSpeed'] = cruise
        mission['firmwareType'] = 3
        mission['hoverSpeed'] = hover
        mission['items'] = self.items
        mission['plannedHomePosition'] = [home[0], home[1], home[3]]
        mission['vehicleType'] = 2
        mission['version'] = 2
        self.plan['mission'] = mission

    def make(self):
        plan_json = json.dumps(self.plan, indent=4, sort_keys=True)
        file = open('mission.plan','w') 
        file.write (plan_json)
        file.close()