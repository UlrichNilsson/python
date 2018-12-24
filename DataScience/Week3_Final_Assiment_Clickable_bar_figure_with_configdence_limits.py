
# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

# In[32]:

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

get_ipython().magic('matplotlib notebook')

def update(curr):
    # check if animation is at the last frame, and if so, stop the animation a
    if curr == 100: 
        a.event_source.stop()
    for i in range(len(ax)):
        ax[i].cla()
        ax[i].hist(x[i][:100*curr], bins=20)
        ax[i].set_title(titles[i])
    plt.tight_layout()
    
        
# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax = [ax1, ax2, ax3, ax4]
x = [x1, x2, x3, x4]
titles=['Normal','Gamma','Exponential','Uniform']
            
ani = animation.FuncAnimation(fig, update, interval=20, repeat=False)



# ## 
