from commodutil import dates
default_line_col = 'khaki'

# try to put deeper colours for recent years, lighter colours for older years
year_col_map = {
    -10: 'wheat',
    -9: 'burlywood',
    -8: 'steelblue',
    -7: 'aquamarine',
    -6: 'coral',
    -5: 'yellow',
    -4: 'saddlebrown',
    -3: 'mediumblue',
    -2: 'darkgreen',
    -1: 'orangered',
    0: 'black',
    1: 'red',
    2: 'firebrick',
    3: 'darkred',
    4: 'crimson',
}

"""
Given a year, calculate a consistent line colour across charts
"""
def get_year_line_col(year):
    if isinstance(year, str):
        year = int(year)

    delta = year - dates.curyear

    return year_col_map.get(delta, default_line_col)


"""
Given a timeseries, produce a string which shows the latest change
For example if T-1 value is 50 and T-2 is 45, return 50.00  △: +5
"""
def delta_summary_str(df):
    val1 = df.tail(1).iloc[0, 0]
    val2 = df.tail(2).head(1).iloc[0, 0 ]
    delta = (val1-val2).round(2)
    symb = '+' if delta > 0.0 else ''

    s = '{}   △: {}{}'.format(val1.round(2), symb,delta)
    return s