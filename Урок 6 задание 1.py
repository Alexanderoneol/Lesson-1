from time import sleep


class Trafficlight:
    __color = "Черный"


    def running(self):
       while True:
           print("Trafficlight is red now")
           sleep(7)
           print("Trafficlight is yellow now")
           sleep(2)
           print("Trafficlight is green now")
           sleep(7)
           print("Trafficlight is yellow now")
           sleep(2)

trafficlight = Trafficlight()
trafficlight.running()