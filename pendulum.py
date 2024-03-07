from matplotlib import pyplot as plt
from math import sin,pi
def pendulum_graph(startingPos,startingVel,gravity,length,airResistance,expTime,timeStep,yGraph1="position",yGraph2=False,yGraph3=False,xGraph="time"):
    step = timeStep
    pos = startingPos
    vel = startingVel
    g = gravity
    # length of the pendulum is .75 m , g / l =....
    c = g/length
    velList=[]
    posList = []
    timeList = []
    accelList = []
    airRes = airResistance
    time = expTime

    for i in range(0,int(time/step)):
        accel = -c * sin(pos) - airRes * vel
        accelList.append(accel)
        vel += accel * step
        velList.append(vel)
        pos += vel * step
        posList.append(pos)
        timeList.append(i*step)
    valList = {"position":posList,"velocity":velList,"acceleration":accelList,"time":timeList}
    plt.plot(valList[xGraph.lower()],valList[yGraph1.lower()])
    if yGraph2:
        plt.plot(valList[xGraph.lower()], valList[yGraph2.lower()])
    if yGraph3:
        plt.plot(valList[xGraph.lower()], valList[yGraph3.lower()])
    plt.show()
pendulum_graph(pi/1.5,1.5,9.8,.5,0.01,15,0.001,"position","velocity","acceleration")