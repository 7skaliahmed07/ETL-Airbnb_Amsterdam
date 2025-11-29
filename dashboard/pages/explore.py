import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data(ttl=3600)
def load_data():
    return pd.read_gbq(
        """
        SELECT name, neighbourhood_cleansed, price, room_type, 
               accommodates, review_scores_rating, latitude, longitude
        FROM `airbnb-amsterdam-479622.amsterdam_airbnb.listings`
        WHERE latitude IS NOT NULL AND longitude IS NOT NULL
    """
    )


def show():
    st.header("Interactive Exploration")
    df = load_data()

    col1, col2 = st.columns([3, 1])
    with col1:
        fig = px.scatter_mapbox(
            df.sample(5000),
            lat="latitude",
            lon="longitude",
            color="price",
            size="accommodates",
            hover_name="name",
            hover_data=["room_type", "price"],
            color_continuous_scale="OrRd",
            zoom=11,
            height=600,
        )
        # fig.update_layout(mapbox_style="carto-positron", margin={"margin": {"r":0,"t":0,"l":0,"b":0}})
        fig.update_layout(
            mapbox_style="carto-positron", margin={"r": 0, "t": 0, "l": 0, "b": 0}
        )

        st.plotly_chart(fig, use_container_width=True)
    with col2:
        st.metric("Cheapest", f"€{df.price.min()}")
        st.metric("Most Expensive", f"€{df.price.max()}")
        st.metric("Median", f"€{df.price.median():.0f}")

    neighbourhood = st.selectbox(
        "Neighbourhood", sorted(df.neighbourhood_cleansed.unique())
    )
    filtered = df[df.neighbourhood_cleansed == neighbourhood]
    st.write(
        f"**{len(filtered)} listings in {neighbourhood}** • Avg €{filtered.price.mean():.0f}"
    )
