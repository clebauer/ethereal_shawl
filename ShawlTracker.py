# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell> {}

# https://www.ravelry.com/patterns/library/ethereal-3
# Program made by clebauer

repeat_num = 4
row_num = 29
num_repeats = 9

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

print '''If you've completed row {} (with {} intended repeats),
you've knitted {} stitches, 
you're {}% completed with the project,
and you have {} more rows to go with {} stitches!

Oh, and your next row only has {} stitches. You got this!'''.format(row_im_on,
                                                                    num_repeats,
                                                                    total_stitches,
                                                                    percent_done,
                                                                    rows_left,
                                                                    stitches_left,
                                                                    charts_use[row_im_on])

# <codecell> {}

sup = [round(sum(charts_use[:y])*100.0/sum(charts_use),2) for y in range(1,len(charts_use))]
steps = [(((new_row - 43) / 14) + 1, ((new_row - 43)%14) + 29) for new_row in range(1,len(charts_use))]
rows_and_data = zip(steps, range(1,len(charts_use)),charts_use, sup)

# <codecell> {}

rows_and_data

# <codecell> {}



# <metadatacell>

{"kernelspec": {"display_name": "Python 2", "name": "python2", "language": "python"}}