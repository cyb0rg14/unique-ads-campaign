from datetime import datetime
import streamlit as st
import pandas as pd
import os

# Import your constants from the constants module
from constants import indian_states_and_ut

# Set page configuration
st.set_page_config(
    page_title="Unique Ads Campaign",
    page_icon=":bar_chart:",
)

# Set homepage
st.title("Unique Ads Campaign")
st.error("Please fill all the details carefully!")

# Divide into two columns
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", datetime.today())
with col2:
    end_date = st.date_input("End Date", datetime.today())

# Take inputs from user
ad_campaign_name = st.text_input("Set a name for your ad campaign:")
cost_per_click = st.slider(
    "Set a CPC (Cost Per Click) for your ad:", min_value=8, max_value=20
)
daily_budget = st.text_input(
    "Set a daily budget for your ad (in Rs):", placeholder=1000
)
target_location = st.multiselect(
    "Select the target locations for your ad:", indian_states_and_ut
)

# More input from users about ads
st.divider()
st.markdown("### Tell us more about your ad:")
headline = st.text_input("Set a headline for your ad:")
primary_text = st.text_input("Set primary text for your ad:")
description = st.text_area("Set a description for your ad:")
website_url = st.text_input(
    "Enter your website URL:", placeholder="www.yourwebsite.com"
)
your_website = st.text_input(
    "Enter the URL (where you want your customers to redirect):",
    placeholder="www.yourwebsite.com/signup",
)

# Way to connect with users
st.divider()
st.markdown("### Connect with your potential customers:")
phone_no = st.text_input(
    "Enter your phone no:", placeholder="+91 9625XXXXXX (Optional)"
)
email = st.text_input("Enter your email:", placeholder="youremail@mail.com (Optional)")

# Submit button
if st.button("Submit"):
    # Check for required fields
    if not ad_campaign_name:
        st.error("Ad campaign name is required.")
    elif not daily_budget:
        st.error("Daily budget is required.")
    elif not target_location:
        st.error("At least one target location is required.")
    elif not headline:
        st.error("Ad headline is required.")
    elif not primary_text:
        st.error("Primary text is required.")
    elif not description:
        st.error("Description is required.")
    elif not website_url:
        st.error("Website URL is required.")
    elif not your_website:
        st.error("Redirection URL is required.")
    else:
        # All required fields are filled, prepare to save data
        data = {
            "Start Date": [start_date],
            "End Date": [end_date],
            "Ad Campaign Name": [ad_campaign_name],
            "Cost Per Click": [cost_per_click],
            "Daily Budget": [daily_budget],
            "Target Locations": [", ".join(target_location)],
            "Headline": [headline],
            "Primary Text": [primary_text],
            "Description": [description],
            "Website URL": [website_url],
            "Redirection URL": [your_website],
            "Phone No": [phone_no],
            "Email": [email]
        }
        
        df = pd.DataFrame(data)

        # Save to CSV
        if not os.path.exists('ads_campaigns.csv'):
            df.to_csv('ads_campaigns.csv', index=False)
        else:
            df.to_csv('ads_campaigns.csv', mode='a', header=False, index=False)

        st.success("Ad campaign details have been saved successfully!")

# Copyright
st.markdown("# ")
st.markdown("# ")
copyright = "&copy; 2024 Unique Ads Campaign. All rights reserved."
st.markdown(f'<p style="text-align:center;">{copyright}</p>', unsafe_allow_html=True)
