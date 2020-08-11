from pythonping import ping
from itertools import count
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

hostname = '192.168.1.1'

x_values = []
y_values = []

index = count()


def ping_host():
    response_list = ping(hostname)
    return float(response_list.rtt_avg_ms)


def animate(i):
    x_values.append(next(index))
    y_values.append(ping_host())

    plt.cla()
    plt.plot(x_values, y_values)


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()

plt.xlabel('Time (s)')
plt.ylabel('Ping (ms)')

plt.show()
