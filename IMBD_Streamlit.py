import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Correct connection 
connection_string = 'mysql+pymysql://root:Sqlbr*123@localhost/IMBD_Movies_project1'

# Create the SQLAlchemy 
engine = create_engine(connection_string)

#  MySQL database using pandas
df = pd.read_sql('SELECT * FROM movie', engine)

# Streamlit app layout
st.title('IMDb 2024 Movie Analysis')

# Filtering options
genre_filter = st.selectbox('Select Genre', df['Genre'].unique())
rating_filter = st.slider('Select Rating Range', 0, 10, (0, 10))

# Filter data based on user input
filtered_df = df[(df['Genre'] == genre_filter) & 
                 (df['Rating'] >= rating_filter[0]) & 
                 (df['Rating'] <= rating_filter[1])]

# Display filtered data
st.write(filtered_df)

#Plotting the top-rated movies
top_rated = df.nlargest(10, 'Rating')

# Create a bar chart for the top 10 rated movies
fig, ax = plt.subplots()
ax.bar(top_rated['Name'], top_rated['Rating'])  
ax.set_xlabel('Movies')  
ax.set_ylabel('Rating')  
ax.set_title('Top 10 Rated Movies')  
plt.xticks(rotation=45, ha='right')  
st.pyplot(fig)


st.subheader('Rating Distribution')  
rating_counts = filtered_df['Rating'].value_counts().sort_index()  
st.bar_chart(rating_counts)  