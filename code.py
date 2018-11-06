
def do_something():
    
    import matplotlib.pyplot as plt
    
    
    circle1 = plt.Circle((0, 0), 2, color='r')
    # now make a circle with no fill, which is good for hi-lighting key results
    circle2 = plt.Circle((5, 5), 0.5, color='b', fill=False)
    circle3 = plt.Circle((10, 10), 2, color='g', clip_on=False)
    
    ax = plt.gca()
    ax.cla() # clear things for fresh plot
    
    # change default range so that new circles will work
    ax.set_xlim((0, 10))
    ax.set_ylim((0, 10))
    # some data
    ax.plot(range(11), 'o', color='black')
    # key data point that we are encircling
    ax.plot((5), (5), 'o', color='y')
    
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(circle3)
    
    print("plot some fun circles")# this will make it much easier in future problems to see that something is actually happening
