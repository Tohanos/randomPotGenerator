import random

import numpy as np
import matplotlib.pyplot as plt


class RandomPot:
    def __init__(self, initval, maxspeed, mindif):
        self.value = initval
        self.maxSpeed = maxspeed
        self.speed = 0
        self.mindif = mindif

    def calcnextval(self, target):
        dif = target - self.value
        sign = np.sign(dif)
        absdif = np.abs(dif)
        if absdif < self.mindif:
            self.speed = 0
            return target
        if absdif < self.maxSpeed:
            self.speed = absdif / 2
        else:
            self.speed += 1
            if self.speed > self.maxSpeed:
                self.speed = self.maxSpeed
        self.value += self.speed * sign
        return self.value


maxSpeed = 1000
mindif = 2

pot = RandomPot(512, maxSpeed, mindif)

rng = np.arange(1000)
rnd = np.random.randint(0, 1023, size=(1, rng.size))
time = rng
val = []

target = random.randint(0, 1023)
for vals in time:
    print(target)
    nextval = pot.calcnextval(target)
    print(nextval)
    val.append(nextval)
    if nextval == target:
        target = random.randint(0, 1023)

fig, ax = plt.subplots(figsize=(5, 3))
plt.plot(val)
ax.set_title('Pot value with random dispersion')
ax.legend(loc='upper left')
ax.set_ylabel('Value')
ax.set_xlim(xmin=time[0], xmax=time[-1])
fig.tight_layout()

plt.show()
