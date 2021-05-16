import matplotlib.pyplot as plt


plt.ion()
def plot_bar(nums, ind):
    n = len(nums)
    color = ['blue'] * n
    color[ind] = 'green'
    index = range(n)
    plt.bar(index, nums, color=color)
    plt.draw()
    plt.pause(1e-6)
    plt.clf()
