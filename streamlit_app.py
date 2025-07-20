import streamlit as st
import pandas as pd
import math 

st.title("Excel-like High-Low Calculator Web App")

# Sample data structure for multiple rows (you can expand this)
data = [
    {"Label": "NIFTY", "High": 0, "Low": 0},
    # {"Label": "BANKNIFTY", "High": 0, "Low": 0},
    # {"Label": "RELIANCE", "High": 0, "Low": 0},
]

# Allow user to input High/Low for each row
for row in data:
    st.subheader(row["Label"])
    row["High"] = st.number_input(f"{row['Label']} High", value=row["High"], key=f"{row['Label']}_high")
    row["Low"] = st.number_input(f"{row['Label']} Low", value=row["Low"], key=f"{row['Label']}_low")

# Calculate dependent columns
for row in data:
    diff = row["High"] - row["Low"]
    row["Diff"] = diff
    row["0.146x"] = diff * 0.146
    row["0.236x"] = diff * 0.236
    row["onm"] = row["High"] + row["0.146x"]
    row["decider"]= row["High"] + row["0.236x"]
    row["Target 1"]= round(row["onm"] + (row["0.146x"] * 5))
    row["Target 2"]= round(row["onm"] + (row["0.146x"] * 9))
    row["Target 3"]= round(row["decider"] + (row["0.236x"] * 5))
    row["Target 4"]= round(row["decider"] + (row["0.236x"] * 9))

# Display as DataFrame
df = pd.DataFrame(data)
st.write("Calculated Table:")
st.dataframe(df)