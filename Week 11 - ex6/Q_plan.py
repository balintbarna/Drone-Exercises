##############################################################
#Call this function with the filename string to generate the 
#JSON file for QGround Control
##############################################################

import json



def Qplan(file):
    ####Reading the file contents as lat,lon and alt
    myfile = open(file,'r')
    lat=[]
    lon=[]
    alt=[]

    while True:
        line = myfile.readline().split("\n")[0].split("\t")
        if '' == line[0]:
            break
        lat.append(line[1])
        lon.append(line[2])
        alt.append(line[3])

    ######## Starting the JSON part from here
    plan = {}
    geoFence = {}
    plan['fileType'] = 'Plan'

    geoFence['polygon'] = [] 
    geoFence['version'] = 1 
    plan['geoFence'] = geoFence

    plan['groundStation'] = 'QGroundControl'

    items = []
    for i in range(len(lat)):
        if (i*20) >= len(lat):
            break
        item = {}
        item['autoContinue'] = True
        if i is 0:
            item['command'] = 22
        else:
            item['command'] = 16
        item['doJumpId'] = i+1
        item['frame'] = 3
        item['params'] = [0,0,0,0,float(lat[i*20]),float(lon[i*20]),float(alt[i*20])]
        item['type'] = 'SimpleItem'
        items.append (item)


    mission = {}
    mission['cruiseSpeed'] = 15
    mission['firmwareType'] = 3
    mission['hoverSpeed'] = 5
    mission['items'] = items
    mission['plannedHomePosition'] = [float(lat[0]), float(lon[0]), float(alt[0])]
    mission['vehicleType'] = 2
    mission['version'] = 2
    plan['mission'] = mission

    rallyPoints = {}
    rallyPoints['points'] = [] 
    rallyPoints['version'] = 1 
    plan['rallyPoints'] = rallyPoints

    plan['version'] = 1

    plan_json = json.dumps(plan, indent=4, sort_keys=True)

    file = open('mission_test.plan','w') 
    file.write (plan_json)
    file.close()

