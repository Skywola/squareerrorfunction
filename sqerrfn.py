import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

# This is the site on Nasa, from which I got the idea for this review
# of the Square Error Function:
# https://www.nasa.gov/sites/default/files/files/YOSS_Act_12.pdf

# WARNING: This is fabricated data, and I am no rocket scientist!
# Suppose we wanted # to land a rover on Mars, but needed to be able to
# predict how many craters were in a given region, so we can to find
# the best place to land in the # regions from which the data was taken
# from.  We have six regions, which are in the area of our trajectory as
# we approach the surface.
#
# Craters on Mars, per km square (1000m sq) in the region we are examining.
#       x   |   y
#       1   |   51.0
#       2   |   55.0
#       3   |   56.0
#       4   |   62.0
#       5   |   65.0
#       6   |   66.0
#       7   |   72.0
#       8   |   74.0

# So this is our data:
x1 = 1.0; x2 = 2.0; x3 = 3.0; x4 = 4.0; x5 = 5.0; x6 = 6.0; x7 = 7.0; x8 = 8.0
y1 = 51.0; y2 = 55.0; y3 = 56.0; y4 = 62.0; y5 = 65.0; y6 = 66.0; y7 = 72.0; y8 = 74.0
# Let's import matplotlib so we can plot this data!  See above ...
x_values = [x1, x2, x3, x4, x5, x6, x7, x8]
y_values = [y1, y2, y3, y4, y5, y6, y7, y8]
m = 8  # m is the number of samples

# Let's plot this data!:        s = size of the points
plt.scatter(x_values, y_values, s=18, color='white')
plt.plot(x_values, y_values, color='lightblue')
plt.xlim(0, 10)
plt.ylim(47, 80)
plt.xlabel('Kilometers Uprange', fontsize=13)
plt.ylabel('Number of Craters', fontsize=13)
plt.title('Craters Per Region Uprange')
ax = plt.gca()
ax.set_facecolor('purple')
plt.show()



'''

# Now that we have the plot of the data, let's investigate what the  squared error function
# can do for us.  In my opinion, I think that calling this function the "cost function"
# confuses a lot of people, because it is not calculating cost,  it is calculating
# squared error values.  I think that it is just plain sloppy to call it a "cost function"!
# That's my rant of the day against the establishment.  The squared error function really
# describes how well current line we are drawing h(x), best fits the data set!
#
#   J(h(x), y) = 1 / 2m Σ(h(x), y)^2
#
# Ok, so now we will define the variables that make up the  cost function:
m = number_of_samples = 8
x = input_variable = kilometers_uprange = 0
y = output_variable = craters_per_km_sqr = 0
# So (x ,y) is a single sample
#
# We can simplify our endeavor to write this equation by peeling off the prefix
# of the function first:
prefix = 1.0 / (2 * m)
# print('Prefix value = ' + str(prefix))

# Now we will need to take the difference between the two values, the hypothesized
# f(x) and the actual y, then square it.  The hypothesized f(x) is a line that we
# think might fit the data.  Let's write a  function to do that:


def sqs(hypothesised_f_x, actual_y):
    sqr = (hypothesised_f_x - actual_y) ** 2
    return sqr

# People often ask why we square it.  The main reason is to get a positive number, and
# no, absolute value does not work as well in this case, because we have the 1/2m prefix,
# which would make the error values extremely small.  Now we just need to put these two
# together, and input some values.

# First, let's re-acquire our berings by seeing our data again:
x1 = 1.0; x2 = 2.0; x3 = 3.0; x4 = 4.0; x5 = 5.0; x6 = 6.0; x7 = 7.0; x8 = 8.0
y1 = 51.0; y2 = 55.0; y3 = 56.0; y4 = 62.0; y5 = 65.0; y6 = 66.0; y7 = 72.0; y8 = 74.0
x_values = [x1, x2, x3, x4, x5, x6, x7, x8]
y_values = [y1, y2, y3, y4, y5, y6, y7, y8]

# Let's  define our hypothesized function (that is, a line that will predict the values
# in any given area), with optional inputs for the slope and b values that allow us to
# change it as we please.


def hypothesized_function(xin, slope=0, b=48):
    return slope * xin + b

# Now let's plot the fit line.  WARNING . . . the parameters for this line are
# ([x-start, x-end], [y-start, y-end] NOT [x-start, y-start], [x-end, y-end]
plt.plot([0, 10], [hypothesized_function(0), hypothesized_function(10)], color='red', linestyle='-', linewidth=1)

n = 0
errors = []
for xval in x_values:
    squared_error_fn_result = prefix * ((hypothesized_function(xval) - y_values[n])**2)
    errors.append(squared_error_fn_result)
    n += 1
    continue

# Let's look at the errors:
n = 0
for e in errors:
    print('point ' + str(n) + ' error = ' + str(e))
    n += 1

plt.show()



def sqs():
    result = 0
    for item in data:
        sq = (item[1] - item[0]) ** 2
        result += sq
        continue
    return result


Other crap
# ax.set_axis_bgcolor((0, 1, 0))
# print(help(plt.plot))


'''
