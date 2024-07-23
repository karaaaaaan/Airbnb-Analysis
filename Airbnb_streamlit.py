import pandas as pd
import streamlit as st
import plotly.express as px

# Function to load data
@st.cache
def load_data():
    df = pd.read_csv("C:/Users/karan/OneDrive/Pictures/Desktop/AIRBNB/Airbnb_Open_Data.csv")
    return df

# Streamlit setup
st.set_page_config(layout="wide")
st.title("AIRBNB DATA ANALYSIS")

def main():
    df = load_data()

    # Sidebar menu
    select = st.sidebar.selectbox("Main Menu", ["Home", "Data Exploration", "About"])

    if select == "Home":
        st.header("About Airbnb")
        st.write("")
        st.write('''***Airbnb is an online marketplace that connects people who want to rent out
                  their property with people who are looking for accommodations,
                  typically for short stays. Airbnb offers hosts a relatively easy way to
                  earn some income from their property. Guests often find that Airbnb rentals
                  are cheaper and homier than hotels.***''')
        st.write("")
        st.write('''***Airbnb Inc (Airbnb) operates an online platform for hospitality services.
                      The company provides a mobile application (app) that enables users to list,
                      discover, and book unique accommodations across the world.
                      The app allows hosts to list their properties for lease,
                      and enables guests to rent or lease on a short-term basis,
                      which includes vacation rentals, apartment rentals, homestays, castles,
                      tree houses and hotel rooms. The company has presence in China, India, Japan,
                      Australia, Canada, Austria, Germany, Switzerland, Belgium, Denmark, France, Italy,
                      Norway, Portugal, Russia, Spain, Sweden, the UK, and others.
                      Airbnb is headquartered in San Francisco, California, the US.***''')
        
        st.header("Background of Airbnb")
        st.write("")
        st.write('''***Airbnb was born in 2007 when two Hosts welcomed three guests to their
                  San Francisco home, and has since grown to over 4 million Hosts who have
                  welcomed over 1.5 billion guest arrivals in almost every country across the globe.***''')

    elif select == "Data Exploration":
        st.title("Data Exploration")
        if 'country' not in df.columns:
            st.error("Data does not contain 'country' column.")
            return
        
        country_options = df["country"].unique()
        country = st.selectbox("Select the Country", country_options)
        df_country = df[df["country"] == country]

        st.header("PRICE ANALYSIS")
        room_type = st.selectbox("Select the Room Type", df_country["room_type"].unique())
        df_room = df_country[df_country["room_type"] == room_type]
        fig_price = px.bar(df_room, x='property_type', y='price', title='Average Price by Property Type',
                           hover_data=["number_of_reviews", "review_scores"], color='price',
                           color_continuous_scale='RdBu', width=800, height=600)
        st.plotly_chart(fig_price)

        st.header("AVAILABILITY ANALYSIS")
        fig_avail = px.sunburst(df_country, path=['room_type', 'bed_type', 'is_location_exact'], values='availability_365',
                                title='Availability Distribution', width=800, height=600)
        st.plotly_chart(fig_avail)

        st.header("LOCATION BASED ANALYSIS")
        fig_map = px.scatter_mapbox(df_country, lat='latitude', lon='longitude', color='price',
                                    hover_name='name', hover_data=['room_type', 'property_type'],
                                    mapbox_style='open-street-map', zoom=1)
        st.plotly_chart(fig_map)

        st.header("GEOSPATIAL VISUALIZATION")
        fig_geo = px.scatter_geo(df_country, lat='latitude', lon='longitude', color='price',
                                 hover_name='name', size='accommodates', projection='natural earth')
        st.plotly_chart(fig_geo)

        st.header("TOP CHARTS")
        fig_top = px.bar(df_country.nlargest(10, 'price'), x='name', y='price', color='price',
                         hover_data=['room_type', 'property_type'], title='Top 10 Highest Priced Listings')
        st.plotly_chart(fig_top)

    elif select == "About":
        st.header("About This Project")
        st.subheader("1. Data Collection:")
        st.write('''***Gather data from Airbnb's public API or other available sources.
                  Collect information on listings, hosts, reviews, pricing, and location data.***''')

        st.subheader("2. Data Cleaning and Preprocessing:")
        st.write('''***Clean and preprocess the data to handle missing values, outliers, and ensure data quality.
                  Convert data types, handle duplicates, and standardize formats.***''')

        st.subheader("3. Exploratory Data Analysis (EDA):")
        st.write('''***Conduct exploratory data analysis to understand the distribution and patterns in the data.
                  Explore relationships between variables and identify potential insights.***''')

        st.subheader("4. Visualization:")
        st.write('''***Create visualizations to represent key metrics and trends.
                  Use charts, graphs, and maps to convey information effectively.
                  Consider using tools like Matplotlib, Seaborn, or Plotly for visualizations.***''')

        st.subheader("5. Geospatial Analysis:")
        st.write('''***Utilize geospatial analysis to understand the geographical distribution of listings.
                  Map out popular areas, analyze neighborhood characteristics, and visualize pricing variations.***''')


if __name__ == "__main__":
    main()
