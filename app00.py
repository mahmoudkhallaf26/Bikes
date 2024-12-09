import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
df = pd.read_csv("Bikes.csv")
df["time"] = df["datetime"].apply(lambda x: x.split(" ")[1])
df["date"] = df["datetime"].apply(lambda x: x.split(" ")[0])
df["date"] = pd.to_datetime(df["date"])
df.drop(['datetime'] , axis = 1 , inplace = True)
tab1 , tab2 , tab3 = st.tabs(['Seasonal and timing analysis' , 'Weather and environmental factors' , 'Profit'])
season=st.sidebar.multiselect("select the season for tab Profit",df["season"].unique(),default=df["season"].unique())
mask1 = df["season"].isin(season)
df_filter = df[mask1]
with tab1:
    fig1=px.pie(data_frame=df,names="season",values="rented_bikes_count",facet_col=df["date"].dt.year,title="Season effect on rented bikes count")
    st.plotly_chart(fig1)
    fig2=px.histogram(data_frame=df,x="time",y="rented_bikes_count",title="The time of day when the rented_bikes_count is highest")
    st.plotly_chart(fig2)
    

with tab2:
    fig3=px.histogram(data_frame=df,x="weather",y="rented_bikes_count",facet_col=df["date"].dt.year,histfunc="count",title="Relationship between weather and Rented Bikes")
    st.plotly_chart(fig3)
    fig4 = px.scatter(data_frame=df,x="temp",y="rented_bikes_count",title="Relationship between Temperature and Rented Bikes",trendline="ols")
    st.plotly_chart(fig4)
    fig5 =px.scatter(data_frame=df,x="windspeed",y="rented_bikes_count",color="weather",title="Windspeed effect on rental")
    st.plotly_chart(fig5)
    

with tab3:
    fig6=px.scatter(data_frame=df_filter,x="rented_bikes_count",y="Profit",marginal_x="box",marginal_y="box" ,hover_data="date",title="Relationship between Profit and Rented Bikes")
    st.plotly_chart(fig6)
    fig9=px.histogram(data_frame=df_filter,x="weather",y="Profit",hover_data="date",title="Relationship between Profit and weather")
    st.plotly_chart(fig9)
    fig8=px.pie(data_frame=df,names="season",values="Profit",facet_col=df["date"].dt.year,title= "profit for each season")
    st.plotly_chart(fig8)
    fig7 = go.Figure()
    fig7.add_trace(go.Scatter(x=df_filter["date"],y=df["registered"],mode='lines', name='Registered Users',line=dict(color='green')))
    fig7.add_trace(go.Scatter(x=df_filter["date"],y=df["casual"],mode='lines',name='Casual Users',line=dict(color='blue')))
    fig7.update_layout(title="Comparison of Registered and Casual Users Over Time")
    st.plotly_chart(fig7)
    fig10=px.histogram(data_frame=df,x="time",y="Profit",title="The time of day when the Profit is highest")
    st.plotly_chart(fig10)


