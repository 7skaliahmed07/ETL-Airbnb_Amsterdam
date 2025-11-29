import streamlit as st
import pandas as pd
import requests
import streamlit as st
from io import BytesIO

@st.cache_data(ttl=60*60)  # cache for 1 hour
def fetch_image(url):
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return BytesIO(resp.content)



def show():
    st.markdown("""
<style>
.metric-card {
    background: #f5f5f5;
    padding: 16px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #e0e0e0;
}
.metric-card h3 {
    margin: 0;
    font-size: 14px;
    color: #555;
}
.metric-card h2 {
    margin: 4px 0 0 0;
    font-size: 28px;
    font-weight: 600;
    color: #222;
}
.big-font {
    font-size: 36px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

    st.markdown('<p class="big-font">Amsterdam Airbnb Dashboard</p>', unsafe_allow_html=True)
    st.markdown("### Real-time insights from 10,480+ listings • 3.8M availability records • ML-powered pricing")
    
    col1, col2, col3, col4 = st.columns(4)
    df = pd.read_gbq("SELECT AVG(price) as avg_price, COUNT(*) as listings FROM `airbnb-amsterdam-479622.amsterdam_airbnb.listings`")
    avg_price = round(df["avg_price"].iloc[0])
    print(f"==>> avg_price: {avg_price}")
    listings = int(df["listings"].iloc[0])
    print(f"==>> listings: {listings}")

    # with col1:
    #     st.markdown('<div class="metric-card"><h3>Avg Price</h3><h2>€236</h2></div>', unsafe_allow_html=True)
    # with col2:
    #     st.markdown('<div class="metric-card"><h3>Total Listings</h3><h2>10,480</h2></div>', unsafe_allow_html=True)
    with col1:
        st.markdown(f'<div class="metric-card"><h3>Avg Price</h3><h2>€{avg_price}</h2></div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div class="metric-card"><h3>Total Listings</h3><h2>{listings}</h2></div>', unsafe_allow_html=True)

    
    with col3:
        st.markdown('<div class="metric-card"><h3>Superhosts</h3><h2>~28%</h2></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><h3>Data Updated</h3><h2>Today</h2></div>', unsafe_allow_html=True)
    
    st.markdown("<div style='height:30px;'></div>", unsafe_allow_html=True)

    
    img_url = "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?q=80&w=1740&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    img_bytes = fetch_image(img_url)
    st.image(img_bytes, use_container_width=True, caption="Amsterdam canal")
    
    st.caption("Built with: Python • BigQuery • Streamlit • scikit-learn • Plotly : By Uzair")