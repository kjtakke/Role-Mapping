def arrayFromDelToDF(string, cl, ln, cols):
    import pandas as pd
    import numpy as np
    """
    String: To be turned into an array then converted onto a dataframe
    cl: Column Deliminator
    ln: Line break deliminator
    Cols: An array or column names
    
    Example:
    string = "a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b"
    Output = arrayFromDelToDF(j, "{%,%}", "{%;%}",['Col1','Col2'])
    
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

j = "a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b{%;%}a{%,%}b"
js = arrayFromDelToDF(j, "{%,%}", "{%;%}",['Column 1','Column 2'])
js
