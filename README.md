# decentralized_raffle
Our decentralized raffle smart contract provides a transparent, on-chain tool for companies and blockchain protocols to run trusted contests to promote their products and reach new clients. 

---
## Key Functionality:
This is open-source smart contract based platform that provides a raffle engine and user interface that can be used to hold trustless, permissionless contests with verifiable results. Key functionality includes:
- Entries are escrowed by the smart contract, no need for a 3rd party to hold funds
- Payouts are issued immediately upon the conclusion of the contest
- Results are verifiable on the blockchain
- Entrants can maintain anonymity (only the wallet address is utilized)
---

## Technologies/Imports
- Remix IDE - Smart Contract Engine (Solidity 0.8.0)
- Streamlit - FrontEnd/UI
- Ganache - Test Network
- Hardhat Network-  allows you to print logging messages and contract variables by calling console.log() from your Solidity code. To use it, you simply import hardhat/console.sol and call it.
- Python web3
---

## Front End: User Experience
Users can interact with the smart contract using the streamlit web application.
The sidebar asks for two inputs: 
- Identification, and the number of Tickets the user would like to purchase, which cost a preset price.
- Next, the application asks you to confirm your purchase before adding the amount to the pot.

**Welcome Screen:**
!['Welcome'](https://github.com/hugokos/decentralized_raffle/blob/master/Screen%20Shots/Streamlit_Screenshot.png)

**Sucessful Entry Screen:**
!['Success'](https://github.com/hugokos/decentralized_raffle/blob/master/Screen%20Shots/Streamlit_Success_Screen.png)

---

## Back End: Interact with Smart Contract
Launch solidity code in Remix IDE to deploy and run transactions on the blockchain

**Deploy and Compile Code on Remix:**
!['Remix'](https://github.com/hugokos/decentralized_raffle/blob/master/Screen%20Shots/Deploy_and_compile_on_remix.png)

**Use Metamask to Connect Remix to Ganache:**
!['Metamask'](https://github.com/hugokos/decentralized_raffle/blob/master/Screen%20Shots/Connect_Remix_to_Metamask.png)

**Leverage Ganache to test Lottery Engine:**
!['Ganache'](https://github.com/hugokos/decentralized_raffle/blob/master/Screen%20Shots/Ganache%20Example.png)


## Sample Code: Raffle Engine
```
contract Raffle {
 // House address for fees
    address house =

 // Stores entered public addresses
    address[] entries;

    constructor() {
        console.log("Deployed!");
    }
 // This function returns a random number between 0 and the # of entries to select a winner
    function pickWinner() private view returns (uint) {
        uint random = uint(keccak256(abi.encodePacked(block.difficulty, block.timestamp, entries)));
        uint index = random % entries.length;
        return index;
    }
 // Public function can be called outside the contract with Remix, payable indicates that we can transfer eth to this contract when called
    function enter() public payable {
        require(msg.value >= 1 ether, "Pay 1 Ether or more to enter the raffle");

        entries.push(msg.sender);
 //When the raffle hits the number of entries (in this case 5) it triggers the pick winner array
        if (entries.length >= 5) {
            uint winnerIndex = pickWinner();
            address winner = entries[winnerIndex];
            console.log(winner);
        //Charges a 1% fee for the house along with the amount
            uint256 feeAmount = (address(this).balance / 100);
            (bool success, ) = (house).call{value: feeAmount}(""); 
            require(success, "Failed to withdraw money from the contact");
        // Gets the remaining prize amount
            uint256 prizeAmount = address(this).balance;
        // Sends the money to the winners address with the prize amount
            (bool success, ) = (winner).call{value: prizeAmount}(""); 
            require(success, "Failed to withdraw money from the contact");
        

            delete entries;
        }
    }
```


---

## Contributors

Hugo Kostelni, Nima Harirchian, Nick Danialy, Tim Tennyson

---

## License

Open Source





---
