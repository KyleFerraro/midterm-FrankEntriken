# Midterm Grading

0. Code Structure [24/25]
    - README signature [5/5]
    - Travis-ci automation [5/5]
    - `midterm.py` exists and well-formatted [4/5]
        - Forgot module docstring
    - `Midterm.ipynb` exists and well-formatted [5/5]
    - Report professional [5/5]
1. Sequence Implementation [30/30]
    - `MysterySequence` implemented [5/5]
    - `__init__` correct [5/5]
    - `self.xs` initialized [5/5]
    - `evaluate` method implemented correctly [10/10]
    - `__call__` method implemented correctly [5/5]
1. Plotting Implementation [12/12]
    - `SequencePlotter` implemented [4/4]
    - `plot` method implemented correctly [8/8]
        - Axes labeled [2/2]
        - Title correct [2/2]
        - Range, lines, markers [2/2]
        - Style correct [2/2]
1. Scatterplot Implementation [11/13]
    - Sequences computed and truncated [5/5]
    - Iterated scatter plots [2/2]
    - Black dots only [0/2]
        - Plotted in red instead of black.
    - Domain and Range correct [2/2]
    - Correct plot specification [2/2]
1. Notebook Sequence Investigation [10/10]
    - r = 2.5, 3.2, 3.5 [3/3]
    - r = 3.5441, 3.5699, 3.57 [3/3]
    - Qualitative behavior discussed [2/2]
    - Conclusions discussed [2/2]
1. Notebook Scatterplot and Conclusions [9/10]
    - Plot shown [2/2]
    - Plot conclusions discussed [2/2]
    - Discussion of features [2/2]
    - Quantitative analysis [1/2]
        - Much more could be done here to support your qualitative analysis, such as investigating the sequence behavior at 3.6 or 3.85.
    - Discussion of future work [2/2]

**Overall grade: [96/100]**

Other Comments:
- `midterm.py`, lines 44: no need for parentheses here
- `midterm.py`, line 80: no need to use `del`, can just slice `temp_ys[151:]`
