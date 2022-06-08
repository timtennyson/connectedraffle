import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from datetime import datetime, timedelta
import pandas as pd
import hashlib

#Added the following imports-- TT

import web3
from web3 import Web3

#Connect to web3 server
# Old Ganache Server w3=Web3(web3.HTTPProvider('http://127.0.0.1:7545'))
#New Ganache Server:
w3=Web3(web3.HTTPProvider('http://127.0.0.1:8545'))

#load accounts
#w3.eth.accounts

#Local contract address from remix when deployed:
contract_address='0xD829f40baBb7E452c3Fd9F2ceCcfe01c6d604ADD'

#import json and open contract_abi.txt (local abi, found in remix under "compile" tab when deployed)
import json
with open('contract_abi.txt') as f: 
    contract_abi=json.load(f)

#set the raffle_contract variable to the local contract address and the contract abi to call the contract
raffle_contract=w3.eth.contract(address=contract_address, abi=contract_abi)

#call the house function to get the house address
#raffle_contract.functions.house().call()


    
#Price per ticket in ETH
price_per_ticket = 1
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#drawing_date = current_date + timedelta(weeks=1)
drawing_date = datetime(2022, 6, 30).strftime("%Y-%m-%d")
pot = 0

#Displaying the name of the site
st.markdown("# Ethereum Raffle")
st.markdown("## Purchase a ticket using Ethereum and win big!")

#Displaying the current time and next drawing
st.sidebar.text(current_date)

#Sidebar to display number of Entries
#Original st.sidebar.text(f"Next Drawing: {drawing_date}")
st.sidebar.text("Drawing will be held when there are 5 entries!")
st.sidebar.text(f"Number of Entries: {raffle_contract.functions.getLength().call()}")

#Set the value to 1 ether
value_wei=w3.toWei(1, 'ether')

st.sidebar.markdown("## Tickets are available at 1 ETH each")

#Creating a streamlit data input  for sender
address_sender = st.sidebar.text_input("Ethereum Address")

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
    st.write(f"Ethereum Address: {address_sender}")
    st.write(f"Number of Tickets: {Tickets}")
    st.write(f"Your total cost is: {Cost} ETH")
    


#Confirmation button
    if st.button("Confirm"):
        st.write(f" Congratulations {address_sender}! You have purchased {Tickets} tickets for {Cost} ETH.")
        st.balloons()
        
        #send the transaction from the input address
        transaction={'from': address_sender, 'value': value_wei*Cost}
        raffle_contract.functions.enter().transact(transaction)

        #Increasing the pot-- no longer needed since we call the getLength function to display number of entries
        #pot += Cost
        #st.session_state.purchased=False

    #Cancel button
    elif st.button("Cancel"):
        st.write("Order Cancelled")
        st.session_state.purchased=False

#Displaying the current pot-- already done through the contract
#st.sidebar.text(f"The current pot is {pot} ETH")
