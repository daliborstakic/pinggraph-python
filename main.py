from pythonping import ping
from itertools import count
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

hostname = '192.168.1.1'

x_values = []
y_values = []

index = count()


def ping_host():
    response_list = ping(hostname)
