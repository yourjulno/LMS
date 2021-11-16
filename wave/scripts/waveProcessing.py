import waveFunctions as wave
import numpy as np
import matplotlib.pyplot as plt

path = '! wave-starter-kit/data example/'

data20, duration, count = wave.readWaveData(path + '20 mm.txt')
data40, duration, count = wave.readWaveData(path + '40 mm.txt')
data60, duration, count = wave.readWaveData(path + '60 mm.txt')
data80, duration, count = wave.readWaveData(path + '80 mm.txt')
data100, duration, count = wave.readWaveData(path + '100 mm.txt')
data120, duration, count = wave.readWaveData(path + '120 mm.txt')

heights = [40, 60, 80, 100, 120]
adc = [np.mean(data20), np.mean(data40), np.mean(data60), np.mean(data80), np.mean(data100), np.mean(data120)]

plt.plot(adc, heights)
plt.title('Калибровочный график')
plt.ylabel(u'h, mm')
plt.xlabel(u'adc')
plt.minorticks_on()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)

plt.show()

p = np.polyfit(adc, heights, 3)


waveData, duration, count = wave.readWaveData(path + 'wave.txt')

t = np.linspace(0, duration, count)

plt.plot(t, np.polyval(p, waveData))
plt.title('Зависимость уровня воды от времени')
plt.ylabel(u'h, mm')
plt.xlabel(u't, с')
plt.minorticks_on()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linestyle = '--', linewidth = 0.5)
plt.show()
