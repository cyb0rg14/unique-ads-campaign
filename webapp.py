from datetime import datetime

import streamlit as st

from constants import *

# set page configuraiton
st.set_page_config(
    page_title="Unique Ads Campaign",
    page_icon=":bar_chart:",
)

# set homepage
st.title("Unique Ads Campaign")
st.error("Please fill all the details carefully!")

# divide into two columns
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", datetime.today())
with col2:
    end_date = st.date_input("End Date", datetime.today())

# take inputs from user
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

# more input from users about ads
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

# way to connect with users
st.divider()
st.markdown("### Connect with your potential customers:")
phone_no = st.text_input(
    "Enter your phone no:", placeholder="+91 9625XXXXXX (Optional)"
)
email = st.text_input("Enter your email:", placeholder="youremail@mail.com (Optional)")

# copyright
st.markdown("# ")
st.markdown("# ")
copyright = "&copy; 2024 Unique Ads Campaign. All rights reserved."
st.markdown(f'<p style="text-align:center;">{copyright}</p>', unsafe_allow_html=True)
