# Email: 24f3003270@ds.study.iitm.ac.in
# This Marimo notebook demonstrates variable dependencies and interactivity.

import marimo as mo

# Cell 1: Data and base variables
@mo.cell
def _(mo):
    # Initial dataset
    x = [1, 2, 3, 4, 5]
    y = [i * 2 for i in x]  # Dependent variable
    
    # Comment about data flow:
    # y depends directly on x through a linear transformation (y = 2x)
    return x, y

# Cell 2: Interactive Slider
@mo.cell
def _(mo):
    # Slider to scale the output
    scale = mo.ui.slider(start=1, stop=10, value=2, step=1)
    mo.md(f"### Scale Factor: {scale.value}")
    return scale

# Cell 3: Variable dependency using slider
@mo.cell
def _(x, y, scale):
    # New dependent variable influenced by slider
    scaled_y = [i * scale.value for i in y]

    # Data flow:
    # scaled_y depends on both y (Cell 1) and scale (Cell 2)

    return scaled_y

# Cell 4: Dynamic Markdown Output
@mo.cell
def _(mo, scaled_y, scale):
    mo.md(f"""
    ## Interactive Data Output

    The current **scale factor** is: `{scale.value}`  

    Original relationship: `y = 2x`  
    Updated relationship: `y = 2x × {scale.value}`  

    ### Scaled Output Values:
    {scaled_y}
    """)

    return
