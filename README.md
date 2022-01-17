# No Mo' Crypto FOMO

Stay up to date with crypto conversations happening around the Internet!

## User Story

**As a** Crypto enthusiast
**I want to** keep up with trending discussions online
**So that** I can stay in the loop and keep learning

## v1.0 Functionality

GIVEN I am a Crypto enthusiast
WHEN I run this Python script
THEN I will create a text file that contains an ordered list of the week's most engaging crypto/web3 discussions on Reddit*


Note: "Most engaging" is a very subjective definition. This is the method that I'm using for now:
1. Retrieve top 10 weekly posts from each of the following subreddits via Reddit API:
	- /r/Bitcoin
	- /r/Ethereum
	- /r/Solana
	- /r/Stellar
	- /r/CryptoCurrency
	- /r/CryptoCurrencies
	- /r/DeFi
	- /r/Web3
2. Give each post an *engagement score,* defined as numComments / numSubredditSubscribers
3. Sort the list by engagement score
4. Get text and URL of the top 10 posts across all off the subreddits
5. Pipe to a text file called *top-10-weekly-[year]-[month]-[day].txt*