import pandas as pd
import streamlit as st
import plotly.express as px #dynamic picture
df = pd.read_csv('HDDclean.csv')
st.set_page_config(page_title='Housing Dashboard',page_icon=':bar_chart:', layout = 'wide')
st.sidebar.header('Please Filter Here')
town_name = st.sidebar.multiselect(
    "Select Town",
    options = df['town'].unique(),
    default = df['town'].unique() [:5]
)
flat_type=st.sidebar.multiselect(
    "Select Flat Type",
    options = df['flat_type'].unique(),
    default = df['flat_type'].unique() [:5]
)
storey_range=st.sidebar.multiselect(
    "Select Storey Range",
    options = df['storey_range'].unique(),
    default = df['storey_range'].unique() [:5]
)

st.title(":bar_chart: Housing Dashboard")
st.markdown('##')
remaining_lease = df['remaining_lease'].sum()
no_of_town = df['town'].nunique()
left_col, right_col = st.columns(2)
with left_col:
    st.subheader('Total Remaining Lease')
    st.subheader(f"Remaining Lease {remaining_lease}")
with right_col:
    st.subheader('No. of Town')
    st.subheader(f"{no_of_town}")
df_select = df.query("town==@town_name and flat_type==@flat_type and storey_range == @storey_range")
aa = df_select.groupby('town') ['remaining_lease'].sum().sort_values()
fig_remaining_by_town = px.bar(
    aa,
    x=aa.values,
    y=aa.index,
    title= "Remaining Lease by Town"
)
a, b, c = st.columns(3)  
a.plotly_chart(fig_remaining_by_town,use_container_width=True)

fig_remaining_by_flat_type = px.pie(
    df_select,
    values ='remaining_lease',
    names= 'flat_type',
    title= "Remaining Lease by Flat Type"
)
b.plotly_chart(fig_remaining_by_flat_type,use_container_width=True)

bb = df_select.groupby('storey_range') ['remaining_lease'].sum().sort_values()
fig_remaining_by_storey = px.bar(
    bb,
    x=bb.values,
    y=bb.index,
    title= "Remaining Lease by Storey Range"
)
c.plotly_chart(fig_remaining_by_storey,use_container_width=True)

d,e = st.columns(2)
line_fig_remaining_by_storey = px.line(
    bb,
    x=bb.values,
    y=bb.index,
    title= "Remaining Lease by Storey Range"
)
d.plotly_chart(line_fig_remaining_by_storey,use_container_width=True)

scatter_fig_remaining_by_flat_model = px.scatter(
    df_select,
    x='remaining_lease',
    y='flat_model',
    title= "Remaining Lease by Flat Model"
)
e.plotly_chart(scatter_fig_remaining_by_flat_model,use_container_width=True)
