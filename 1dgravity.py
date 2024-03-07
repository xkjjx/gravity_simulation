from matplotlib import pyplot as plt
G = 6.67 * 10**-11
class Planet:
    def __init__(self,mass,velocity,position):
        self.mass = mass
        self.velocity = velocity
        self.position = position
    def setAcceleration(self,planet2):
        self.acceleration = ((planet2.mass * G)/((abs(self.position - planet2.position))**2)) * ((planet2.position - self.position)/(abs(self.position - planet2.position)))


planets = [Planet(8 * 10**24, 0,4*10**9),Planet(10**25,0,10**8)]
planetData = {planets[0]:{"position":[],"velocity":[],"acceleration":[]},planets[1]:{"position":[],"velocity":[],"acceleration":[]}}
timeData = []
step = 100
time = 100000000

for i in range(0,int(time/step)):
    planets[0].setAcceleration(planets[1])
    planets[1].setAcceleration(planets[0])
    for planet in planets:
        planet.velocity += planet.acceleration*step
        planet.position += planet.velocity*step
        planetData[planet]["position"].append(planet.position)
        planetData[planet]["velocity"].append(planet.velocity)
        planetData[planet]["acceleration"].append(planet.acceleration)
        print(i*step*100/time)
    timeData.append(i*step)
plt.plot(timeData,planetData[planets[0]]["position"])
plt.plot(timeData,planetData[planets[1]]["position"])
print(planetData[planets[0]]["velocity"][-2:])
print(planetData[planets[1]]["velocity"][-2:])
plt.show()
