PROJECT:
- Create an S&P stock picker.
- Try to implement DD rules.
- Make it output an Excel sheet with which shares to buy.

NEXT UP:
- Research project paramaters
- Finish this tutorial (currently at 1:38:42 mark) https://www.youtube.com/watch?v=xfzGZB4HhEE
- Finish the 2nd algorithmic trading project now that the script seems to work with my fixes.

LOG:
--- October 8th, 2021 ---
- Found out that several values in the dataframe returned NoneType, likely causing the error.
- Used 'hqm_dataframe = hqm_dataframe.fillna(value=np.nan)' to populate NoneType values with NaN (which is a float???).

--- October 7th, 2021 ---
- Installed scipy
- Started running in to the same Pandas error as I experienced in investment_updater app, where pandas threw a "TypeError: '<' not supported between instances of 'NoneType' and 'float'" error. SOLUTION ATTEMPTED: installed a bunch of earlier versions of libraries used (most importantly pandas 0.25.3).
- Solution didn't work. Error persists regardless of versions, IDE, OS, etc.

--- October 6th, 2021 ---
- Finished the first algorithmic trading project 'Building an Equal-Weight S&P 500 Index Fund'.
- Translated (copy pasted) it in to a regular python script.

--- October 5th, 2021 ---
- Installed Jupyter, requests, xlsxwriter (Numpy + Pandas previously installed) 

--- October 4th, 2021 ---
- Abandoned datacamp course for now because there are too many paid links. Found a Freecodecamp tutorial on youtube that seems suitable and practical.

--- September 26th, 2021 ---
- Initialized project, created .venv etc.
- Found datacamp.com course on algorithmic trading with Python.
- Turns out these courses are paid.
- Installed pandas + pandas-datareader packages