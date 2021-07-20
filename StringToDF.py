def arrayFromDelToDF(string, cl, ln, cols):
    import pandas as pd
    import numpy as np
    """
    string: To be turned into an array then converted onto a dataframe
    cl: Column Deliminator
    ln: Line break deliminator
    cols: An array or column names
    
    Example:
    string = "a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b"
    Input = arrayFromDelToDF(string, "{%,%}", "{%;%}",['Col1','Col2'])
    Output:
      Col1 Col2
    0	a	b
    1	a	b
    2	a	b
    3	a	b
    4	a	b
    """
    js = string.split(ln)
    lg = []
    for i in js:
        sp = i.split(cl)
        lg.append(sp)
        
    return pd.DataFrame(lg, columns=cols)

#Table 1
j = "a{%,%}b{%;%}c{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}d{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b"
js = arrayFromDelToDF(j, "{%,%}", "{%;%}",['Column 1','Column 2'])

#Table 2
l = "a{%,%}b{%,%}c{%,%}d{%;%}c{%,%}b{%,%}c{%,%}d"
ls = arrayFromDelToDF(l, "{%,%}", "{%;%}",['Column 3','Column 4','Column 5','Column 6'])

#Join
df = pd.merge(js, ls, left_on=['Column 1','Column 2'], right_on=['Column 3','Column 4'], how='left')

#Drop Columns
df = df.drop(['Column 3','Column 4'], 1)
df.head()
