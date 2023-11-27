import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load data
all_df = pd.read_csv("main_data.csv")

# Sidebar
st.sidebar.title("Dashboard Options")
selected_chart = st.sidebar.radio(
    "Select Chart", ["Average Delivery Time", "Percentage of Delayed Orders"])

# Main content
st.title("Delivery Analysis Dashboard")

# Question 1: Berapa waktu rata-rata pengiriman di berbagai negara bagian customer?
if selected_chart == "Average Delivery Time":
    # Kalkulasi
    average_delivery_time = all_df.groupby('customer_state')[
        'delivery_time'].mean().sort_values()

    # Plot
    st.subheader("Average Delivery Time by Customer State")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x=average_delivery_time.index,
                y=average_delivery_time.values,
                palette='viridis',
                hue=average_delivery_time.index,
                legend=False, ax=ax)
    plt.title('Average Delivery Time by Customer State')
    plt.xlabel('Customer State')
    plt.ylabel('Average Delivery Time (Days)')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Question 2: Seberapa sering pengiriman mengalami keterlambatan di berbagai negara bagian customer?
elif selected_chart == "Percentage of Delayed Orders":
    # Kalkulasi
    total_orders_count = all_df.groupby('customer_state')['order_id'].count()
    delayed_orders_count = all_df.groupby('customer_state')['delayed'].sum()
    delayed_percentage = (delayed_orders_count / total_orders_count) * 100
    not_delayed_percentage = 100 - delayed_percentage

    # Plot
    st.subheader(
        "Percentage of Delayed and Not Delayed Orders by Customer State")
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.bar(delayed_percentage.index, delayed_percentage,
            color='red', label='Delayed')
    plt.bar(not_delayed_percentage.index, not_delayed_percentage,
            bottom=delayed_percentage, color='green', label='Not Delayed')
    plt.title('Percentage of Delayed and Not Delayed Orders by Customer State')
    plt.xlabel('Customer State')
    plt.ylabel('Percentage')
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(fig)