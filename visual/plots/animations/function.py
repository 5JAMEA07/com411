import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()


def animate(frame):
    print(frame)


def run():
    global fig
    # your code here (use fig with animation function)
    ant = animation.FuncAnimation(fig, animate, frames=10, interval=1000)
    plt.show()


run()