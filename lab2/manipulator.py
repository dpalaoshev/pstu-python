class Segment:
    def __init__(self, length, angle=0):
        self._length = length
        self._angle = angle

    def length(self):
        return self._length

    def angle(self):
        return self._angle

    def __str__(self):
        return f"Segment(length={self.length}, angle={self.angle} degrees)"

    def rotate(self, angle):
        self._angle += angle

    def move(self, distance):
        self._length += distance


class Manipulator:
    def __init__(self, num_segments):
        self.segments = [Segment(1.0) for _ in range(num_segments)]

    def __str__(self):
        return f"Manipulator with {len(self.segments)} segments"

    def __getitem__(self, index):
        return self.segments[index]

    def __setitem__(self, key, value):
        self.segments[key] = value

    def move(self, distances):
        if len(distances) == len(self.segments):
            for i in range(len(distances)):
                self.segments[i].move(distances[i])

manipulator = Manipulator(4)

print(manipulator)

manipulator[0].rotate(45)
manipulator[1].rotate(10)

print(manipulator[0])
print(manipulator[1])
print(manipulator[2])

manipulator.move([0.1, 0.5, 0.8, 0.1])
print(manipulator[1])
print(manipulator[2])