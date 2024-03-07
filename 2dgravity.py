import numpy
from matplotlib import pyplot as plt
class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.magnitude = self.findMagnitude()
    def findMagnitude(self):
        return (self.x**2 + self.y**2)**0.5
    def findUnitVector(self):
        return Vector2D(self.x/self.magnitude,self.y/self.magnitude)
    def __add__(self, other):
        return Vector2D(self.x+other.x,self.y+other.y)
    def __sub__(self, other):
        return Vector2D(self.x-other.x,self.y-other.y)
    def __mul__(self, other):
        return Vector2D(self.x*other,self.y*other)
    def __neg__(self):
        return Vector2D(-self.x,-self.y)


G = 6.67 * 10**-11
class Planet:
    def __init__(self,mass,velocity,position):
        self.mass = mass
        self.velocity = velocity
        self.position = position
    def setAcceleration(self,planet2):
        differenceVector = self.position - planet2.position
        self.acceleration =differenceVector.findUnitVector() * (-(planet2.mass * G)/(differenceVector.findMagnitude()**2))


# helpful data for testing:
# 1 year is 3 x 10^7 seconds
# the earth and moon are 4 x 10^8 meters apart
# the earth's orbital speed is 3 x 10^4 meters per second
# the mass of the earth is 6 x 10^24 kilograms
# the distance between the earth and sun is 1.5 x 10^11 meters
# the mass of the sun is 2 x 10^30 kg
time = 700000000
step = 1000
planet1 = Planet(2*10**30,Vector2D(0,0),Vector2D(0,0))
planet2 = Planet(5*10**28,Vector2D(0,4*10**4),Vector2D(1.5*10**11,0))
planet1Data = {"position":[[],[]],"velocity":[[],[]],"acceleration":[[],[]]}
planet2Data = {"position":[[],[]],"velocity":[[],[]],"acceleration":[[],[]]}
timeData = []


for i in range(int(time/step)):
    planet1.setAcceleration(planet2)
    planet2.setAcceleration(planet1)
    planet1.velocity = planet1.velocity + (planet1.acceleration * step)
    planet2.velocity = planet2.velocity + (planet2.acceleration * step)
    planet1.position = planet1.position + (planet1.velocity * step)
    planet2.position = planet2.position + (planet2.velocity * step)

    planet1Data["position"][0].append(round(planet1.position.x))
    planet1Data["position"][1].append(round(planet1.position.y))
    planet1Data["velocity"][0].append(round(planet1.velocity.x))
    planet1Data["velocity"][1].append(round(planet1.velocity.y))
    planet1Data["acceleration"][0].append(round(planet1.acceleration.x))
    planet1Data["acceleration"][1].append(round(planet1.acceleration.y))

    planet2Data["position"][0].append(round(planet2.position.x))
    planet2Data["position"][1].append(round(planet2.position.y))
    planet2Data["velocity"][0].append(round(planet2.velocity.x))
    planet2Data["velocity"][1].append(round(planet2.velocity.y))
    planet2Data["acceleration"][0].append(round(planet2.acceleration.x))
    planet2Data["acceleration"][1].append(round(planet2.acceleration.y))
    timeData.append(i*step)
    print(i*step*100/time)


plt.plot(planet1Data["position"][0],planet1Data["position"][1])
plt.plot(planet2Data["position"][0],planet2Data["position"][1])
plt.show()