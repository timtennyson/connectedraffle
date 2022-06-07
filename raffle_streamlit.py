import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from datetime import datetime, timedelta
import pandas as pd
import hashlib


#Price per ticket in Pwei
price_per_ticket = 1
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#drawing_date = current_date + timedelta(weeks=1)
drawing_date = datetime(2022, 6, 30).strftime("%Y-%m-%d")
pot = 0

#Displaying the name of the site
st.markdown("# Ethereum Raffle")
st.markdown("## Purchase a ticket using ethereum and win big!")

#Displaying the current time and next drawing
st.sidebar.text(current_date)
st.sidebar.text(f"Next drawing: {drawing_date}")

st.sidebar.markdown("## Tickets are available at 1 Pwei")

#Creating a streamlit data input  for sender
address = st.sidebar.text_input("Ethereum Address")

#Creating a streamlit data input  for Receiver
Tickets = st.sidebar.number_input("Tickets",min_value=1,step=1)

#Creating a streamlit data input  for Amount
Cost = (Tickets*price_per_ticket)

if 'purchased' not in st.session_state: 
    st.session_state.purchased=False

def callback(): 
    st.session_state.purchased=True

#Displaying the purchase button and asking for confirmation
purchased = st.sidebar.button("Purchase", on_click=callback)
if purchased or st.session_state.purchased:
    st.write("Please confirm the following information:")
    st.write(f"Ethereum Address: {address}")
    st.write(f"Number of Tickets: {Tickets}")
    st.write(f"Your total cost is: {Cost} ETH")

#Confirmation button
    if st.button("Confirm"):
        st.write(f" Congratulations {address}! You have purchased {Tickets} tickets for {Cost} ETH.")
        st.balloons()

        #Increasing the pot
        pot += Cost
        st.session_state.purchased=False

    #Cancel button
    elif st.button("Cancel"):
        st.write("Order Cancelled")
        st.session_state.purchased=False

#Displaying the current pot
st.sidebar.text(f"The current pot is {pot} ETH")
