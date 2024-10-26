print('Lesson2, Python OOP')


class Marker:
    def __init__(self, color, thikness, isAvailable = True ):
        self.color = 'black'
        self.isAvailable = True
        self.thikness = 5


    def getInfo(self):
            print('genaral info:')
            if self.isAvailable:
             print(f'color-{self.color} | thk - {self.thikness}')
            else:
                print('\tthis marker is absent in storage')

markerRed = Marker('red', 2)
markerRed.getInfo()
markerRed.color = 'black'
markerRed.getInfo()
