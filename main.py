from pythonping import ping
from itertools import count
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

hostname = '192.168.1.1'

plt.style.use('dark_background')

x_values = []
y_values = []

index = count()

fig = plt.gcf()
fig.canvas.set_window_title('Ping Tester')


def ping_host():
    response_list = ping(hostname)
    return float(response_list.rtt_avg_ms)


def animate(i):
    x_values.append(next(index))
    y_values.append(ping_host())

    plt.cla()
    plt.plot(x_values, y_values, 'g', label='Ping (ms)')

    plt.xlabel('Time (s)')
    plt.ylabel('Ping (ms)')

    plt.legend()


ani = FuncAnimation(fig, animate, interval=ping_host())

plt.tight_layout()
plt.show()
