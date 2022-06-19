import numpy as np
import matplotlib.pyplot as plt
import random

# N is +X, S is -X
# E is +Y, W is -Y
class Walk():

    def __init__(self):
        # All individuals start at 0, 0
        # remove step_number?
        self.step_number = 0
        self.pa_step = [0, 0]
        self.mima_step = [0, 0]
        self.reggie_step = [0, 0]
        self.pa_old_step = [0, 0]
        self.ma_old_step = [0, 0]
        self.reggie_old_step = [0, 0]


    def pa(self):
        """
        Pa:
        Wanders at n+1 steps
        Every even step is a random direction
        Every third step follows:
            If the even step is N or S, the third step is W
            If the even step is W, the third step is E
            if the even step is E, the third step is 25% goes W, 75% goes NSE
        """
        self.step_number += 1
        self.pa_old_step = self.pa_step
        old_stepX = self.pa_old_step[0]
        old_stepY = self.pa_old_step[1]
        stepX = self.pa_step[0]
        stepY = self.pa_step[1]
        new_direction = random.randint(0, 3)
        # 0 == W; 1 == E; 2 == N; 3 == S
        # goes E or W
        if self.step_number // 2 == 0:
            # cleaner than if-else statements
            match new_direction:
                case 0: stepX -= 1
                case 1: stepX += 1
                case 2: stepY += 1
                case 3: stepY -= 2

        if self.step_number % 3 == 0:
            if stepX == old_stepX:
                stepX -= 1

            if stepX > old_stepX:
                stepX = stepX+1

            if stepX < old_stepX:
                match new_direction:
                    case 0: stepX = stepX - 1
                    case 1: stepX = stepX + 1
                    case 2: pass
                    case 3: pass

        new_step_coor = [stepX, stepY]
        return new_step_coor
            

    def mi_ma(self):
        """
        Ma & Mule:
        Goes S twice as often -> Sx2
        """
        self.ma_old_step = self.mima_step
        old_stepX = self.ma_old_step[0]
        old_stepY = self.ma_old_step[1]
        stepX = self.mima_step[0]
        stepY = self.mima_step[1]
        new_direction = random.randint(0, 4)
        # 0 == W; 1 == E; 2 == N; 3 == S
        # goes E or W
        if self.step_number:
            match new_direction:
                case 0: stepX -= 1
                case 1: stepX += 1
                case 2: stepY += 1
                case 3: stepY -= 1
                case 4: stepY -= 1

        new_step_coor = [stepX, stepY]
        return new_step_coor


    def reggie(self):
        # Reg only goes E or W
        self.reg_old_step = self.reggie_step
        stepX = self.reggie_step[0]
        new_direction = random.randint(0, 1)
        # W == 0, E == 1
        match new_direction:
            case 0: stepX = stepX - 1
            case 1: stepX = stepX + 1

        self.reggie_step[0] = stepX
        return [self.reggie_step]



pa_step = [[0,0],]
ma_step = [[0,0],]
reg_step = [[0,0],]


for step in range(100):
    pa_old = pa_step[-1]
    mima_old = ma_step[-1]
    reggie_old = reg_step[-1]

    pa_new_step = Walk().pa()
    ma_new_step = Walk().mi_ma()
    reggie_step = Walk().reggie()

    pa_new_step = np.add(np.array(pa_new_step), np.array(pa_old))
                   
    ma_new_step = np.add(np.array(ma_new_step), np.array(mima_old))

    reggie_step = np.add(np.array(reggie_step), np.array(reggie_old))

    pa_step.append(pa_new_step.tolist())
    ma_step.append(ma_new_step.tolist())
    reg_step.append(reggie_step.tolist())

pa_X = [pa_step[x][0] for x in range(len(pa_step))]
pa_Y = [pa_step[y][1] for y in range(len(pa_step))]


plt.style.use('_mpl-gallery')

plt.plot(pa_X, pa_Y)
plt.show()
