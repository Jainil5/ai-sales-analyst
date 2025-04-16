import streamlit as st
import requests
import plotly.express as px

# API Endpoints
API_URL = "http://127.0.0.1:5000/api/sales-data"
CHATBOT_URL = "http://127.0.0.1:5000/api/chatbot"

# Function to fetch data from API
def fetch_metrics_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

def fetch_chatbot_response(message):
    try:
        response = requests.post(CHATBOT_URL, json={"message": message})
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching chatbot response: {e}")
        return "Error: Unable to get response from chatbot."

# Streamlit App Configuration
st.set_page_config(page_title="Sales Metrics Dashboard", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .metric-card {
        background-color: #f0f8ff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .metric-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .metric-value {
        font-size: 24px;
        color: #3366cc;
    }
    .chart-container {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 10px;
        margin-bottom: 20px;
        background-color: white;
    }
    .chatbot-container {
        margin-top: 30px;
        border-top: 1px solid #eee;
        padding-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main App
st.title("📊 Sales Metrics Dashboard")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Home", "Month-on-Month", "Year-on-Year", "Top Products"])

# Home Tab
with tab1:
    metrics_data = fetch_metrics_data()
    if metrics_data:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Men Sales</div><div class='metric-value'>{metrics_data['men_sales']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Top Sold Product</div><div class='metric-value'>{metrics_data['top_sold_product']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Top State Sales</div><div class='metric-value'>{metrics_data['top_state_sales']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Top Revenue Sub-Type</div><div class='metric-value'>{metrics_data['top_revenue_sub_type']}</div></div>", unsafe_allow_html=True)

        with col2:
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Men Revenue</div><div class='metric-value'>{metrics_data['men_revenue']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Top Revenue Product</div><div class='metric-value'>{metrics_data['top_revenue_product']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Top State Revenue</div><div class='metric-value'>{metrics_data['top_state_revenue']}</div></div>", unsafe_allow_html=True)

        with col3:
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Women Sales</div><div class='metric-value'>{metrics_data['women_sales']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Top Sold Type</div><div class='metric-value'>{metrics_data['top_sold_type']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Top Sold Sub-Type</div><div class='metric-value'>{metrics_data['top_sold_sub_type']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Top Revenue Type</div><div class='metric-value'>{metrics_data['top_revenue_type']}</div></div>", unsafe_allow_html=True)

    else:
        st.write("Failed to fetch data from API. Please check the API endpoint and ensure the server is running.")

# Month-on-Month Tab
with tab2:
    st.header("Month-on-Month Sales Analysis")
    metrics_data = fetch_metrics_data()
    if metrics_data:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Top Month Sales</div><div class='metric-value'>{metrics_data['top_month_sales']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Least Month Sales</div><div class='metric-value'>{metrics_data['least_month_sales']}</div></div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Top Month Revenue</div><div class='metric-value'>{metrics_data['top_month_revenue']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>Least Month Revenue</div><div class='metric-value'>{metrics_data['least_month_revenue']}</div></div>", unsafe_allow_html=True)

# Year-on-Year Tab
with tab3:
    st.header("Year-on-Year Sales Analysis")
    metrics_data = fetch_metrics_data()
    if metrics_data:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"<div class='metric-card'><div class='metric-title'>2021 Units Sold</div><div class='metric-value'>{metrics_data['units_2021']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>2020 Units Sold</div><div class='metric-value'>{metrics_data['units_2020']}</div></div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='metric-card'><div class='metric-title'>2021 Revenue</div><div class='metric-value'>{metrics_data['revenue_2021']}</div></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='metric-card'><div class='metric-title'>2020 Revenue</div><div class='metric-value'>{metrics_data['revenue_2020']}</div></div>", unsafe_allow_html=True)

# Top Products Tab
with tab4:
    st.header("Top Products Analysis")
    # Add your top products analysis here (graphs, cards, etc.)

# Chatbot Section (Bottom of every page)
st.markdown("<div class='chatbot-container'>", unsafe_allow_html=True)
st.header("Sales Chatbot")
chat_input = st.text_input("Ask a question about sales data:", placeholder="Enter your question here...")
if st.button("Send"):
    if chat_input:
        response = fetch_chatbot_response(chat_input)
        st.markdown(f"<div class='metric-card'>{response}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)