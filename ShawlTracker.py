# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell> {"scrolled": true}

# Setting up my functions. Good luck.
# If you wanna read the program, scroll down a little farther.
def so(g):
      return ''.join([chr(x) for x in g])
def cassie(h):
      return ''.join([chr(x) for x in h])
def is_in(l):
      return ''.join([chr(x) for x in l])
def confusing(f):
      return ''.join([chr(x) for x in f])
def love(m):
      return ''.join([chr(x) for x in m])
def that(d):
      return ''.join([chr(x) for x in d])
def lets(a):
      return ''.join([chr(x) for x in a])
def you(o):
      return ''.join([chr(x) for x in o])
def say(j):
      return ''.join([chr(x) for x in j])
def she(k):
      return ''.join([chr(x) for x in k])
def can(i):
      return ''.join([chr(x) for x in i])
def make(b):
      return ''.join([chr(x) for x in b])
def functions(c):
      return ''.join([chr(x) for x in c])
def with_(n):
      return ''.join([chr(x) for x in n])
def are(e):
      return ''.join([chr(x) for x in e])

# HERE IT IS. THE CODE.
vals = {0:[73], 1:[97,109], 2:[115,111], 3:[117,110,98,101,108,105,101,118,97,98,108,121], 4:[105,110], 5:[108,111,118,101], 6:[119,105,116,104], 7:[121,111,117], 8:[97,110,100], 9:[73,39,109], 10:[115,111], 11:[112,114,111,117,100], 12:[116,111], 13:[116,101,108,108], 14:[121,111,117,33]}

fns = [lets, make, functions, that, are, confusing, so, cassie, can, say, she, is_in, love, with_, you]

wctb = {k:v(vals[k]) for (k,v) in zip(range(len(fns)), fns)}

# ❤
print ''.join(['{} '.format(x) for x in wctb.values()])

# <codecell> {}

 

# <codecell> {}

import pandas as pd
# https://www.ravelry.com/patterns/library/ethereal-3
# Program made by clebauer

repeat_num = 4
row_num = 40
num_repeats = 9
sec_per_150_st = 10 * 60
time_per_st = sec_per_150_st/150

# lets calculate what row you're ACTUALLY on
row_im_on = 14 * repeat_num + row_num if repeat_num > 0 else row_num #OR lol 42+(14*(repeat_num-1))+(row_num-28) if repeat_num > 0 else row_num

# Manual Data Input
# all even rows are purled, so duplicate the row before.
# intro, odd rows, done once
chart1 = [7, 11, 15, 19, 23, 27, 31, 31, 35, 39, 43, 47, 51, 59, 55, 59, 63, 67, 71, 75, 87]

# chart 1 repeats, these are the counts of the odd rows for the first two repeats.
# all repeats going forward increment with j-i for i,j in chart1_1, chart1_2
chart1_1 = [79,83,87,91,95,99,115]
chart1_2 = [103,107,111,115,119,123,143]

# chart 2, these are the counts of the odd rows for the first two EXAMPLES of chart 2
# here, we only need the row numbers *for the nth repeat*, but we need the first two to get
# the amount to increment by to get there.
chart2_1 = [127,131,135,139,143,147,171,195,219,249,267,291,315,317,319,321,323,325,327,329,331,333,335,337,339,341,367]
chart2_2 = [151,155,159,163,167,171,199,227,255,283,311,339,367,369,371,373,375,377,379,381,383,385,387,389,397,393,423]

# Calculate chart_diffs
chart1_diff = [j-i for i, j in zip(chart1_1, chart1_2)] 
chart2_diff = [j-i for i, j in zip(chart2_1, chart2_2)] 

# For now, 'manually' calculate stitch counts for chart 1 repeats
chart_1_use = chart1 + chart1_1
chart_to_add = chart1_1

for i in range(num_repeats-1):
    chart_to_add = [i+j for i,j in zip(chart_to_add,chart1_diff)]
    chart_1_use += chart_to_add

# calculate chart 2 stitch count
chart_2_use = [i+(j*(num_repeats-1)) for i,j in zip(chart2_1, chart2_diff)]

# place all rows together
charts = chart_1_use + chart_2_use
charts_use = [val for val in charts for _ in (0, 1)] + [max(chart_2_use)]

# calculations
total = sum(charts_use)
total_stitches = sum(charts_use[0:row_im_on])
rows_left = len(charts_use) - row_im_on
stitches_left = total - total_stitches
percent_done = round(total_stitches*100.0 / total, 2)
min_done = (total_stitches * time_per_st)/60
min_left = (stitches_left * time_per_st)/60

print '''If you've completed row {} (with {} intended repeats),
you've knitted {} stitches, 
you're {}% completed with the project,
and you have {} more rows to go with {} stitches!
(At {} seconds per st, you've spent {} min and have {} min to go.)

Oh, and your next row only has {} stitches. You got this!'''.format(row_im_on,
                                                                    num_repeats,
                                                                    total_stitches,
                                                                    percent_done,
                                                                    rows_left,
                                                                    stitches_left,
                                                                    time_per_st,
                                                                    min_done,
                                                                    min_left,
                                                                    charts_use[row_im_on],
                                                                    )

# <codecell> {}

sup = [round(sum(charts_use[:y])*100.0/sum(charts_use),2) for y in range(1,len(charts_use))]
steps = [(((new_row - 43) / 14) + 1, ((new_row - 43)%14) + 29) for new_row in range(1,len(charts_use))]
rows_and_data = zip(steps, range(1,len(charts_use)),charts_use, sup)

# <codecell> {}

rows_and_data

# <codecell> {}



# <metadatacell>

{"kernelspec": {"display_name": "Python 2", "name": "python2", "language": "python"}}