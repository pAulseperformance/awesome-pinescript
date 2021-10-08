# awesome-pinescript
**A Comprehensive Collection of Everything Related to Tradingview Pine Script.**

## Table of Contents
- [Official Resources](#Official-Resources)
- [Indicators](#Indicators)
- [Strategies](#Strategies)
- [Automated Order Execution](#Automation)
- [Conventions & Rules](#Conventions-rules)
- [Education](#Education)
- [Other Resources](#Other-Resources)
- [Contributing](#Contributing)


<a name="Official-Resources" />

## Official Resources
 - [Language Reference Manual](https://www.tradingview.com/pine-script-reference/v4/) - *An Index of built-in variables, functions and language operators.*
 - [Pine Script v4 User Manual](https://www.tradingview.com/pine-script-docs/en/v4/index.html) - *Official Documentation on Pine Script Version 4.*
 - [Pine Script v5 User Manual](https://www.tradingview.com/pine-script-docs/en/v5/index.html) - *Official Documentation on Pine Script Version 5.*
 - [Pine Script Chat Room](https://www.tradingview.com/chat/#BfmVowG1TZkKO235) - *TradingView public chat dedicated to Pine Script where active developers of the community help each other out.*
 - [TV Blog](https://www.tradingview.com/blog/en/category/market-analysis/pine/) - *Information about major releases and modifications to Pine Script (as well as other features.)*
 - [TV Public Scripts](https://www.tradingview.com/scripts/) - *TradingView’s Public Library contains all user-published scripts.*
 - [Editors Picks](https://www.tradingview.com/scripts/editors-picks/) - *TV's curated list of best indicators*



<a name="Indicators" />

## Indicators
### Collections
- [Pine Script Indicators Collection](https://github.com/everget/tradingview-pinescript-indicators) - *A collection of various technical indicators.*
- [Pine Coders Publications](https://www.tradingview.com/u/PineCoders/#published-scripts) - *A plethora of useful techniques developed by the Pine Coders Account*

### Volume
- [Raindrops](https://www.tradingview.com/script/dJr8hv4v-Raindrops-Makit0/) - *Custom Volume profiles on user defined periods.*

### Screeners
Scan multiple charts with a single indicator

- [Indices Sector Sigma Spikes](https://www.tradingview.com/script/B3aLMAHh-Indices-Sector-SigmaSpikes/) - *This screener aims to provide Bird-Eye view across sector indices, to find which sector is having significant or 'out-of-norm' move in either direction.* #stocks
- [Mean Reversion Channel](https://www.tradingview.com/script/Lr5QD0kK-Screener-Mean-Reversion-Channel/) - *The screener works by scanning through up to 40 symbols and list down symbols that are currently within Overbought/Oversold Zone as defined by Mean Reversion Channel indicator.*

### Math
- [Black Scholes](https://www.tradingview.com/script/dgMumvhd-Black-Scholes-Options-Pricing-Model/) - *The Black-Scholes model is a mathematical model used for pricing options. From this model you can derive the theoretical fair value of an options contract. Additionally, you can derive various risk parameters called Greeks. This indicator includes three types of data: Theoretical Option Price (blue), the Greeks (green), and implied volatility (red); their values are presented in that order.* #options

### Tools
 - [Script Stopwatch](https://www.tradingview.com/script/rRmrkRDr-Script-Stopwatch-PineCoders-FAQ/) - *Measure the performance of your scripts*
 - [Filter Response](https://www.tradingview.com/script/oTEP9DJF-Filter-Information-Box-PineCoders-FAQ/) - *Analyze the characteristics of your filters, with DSP*



<a name="Strategies" />

## Strategies
 - [Stop Loss and Take Profit](https://www.tradingview.com/script/IHVPG6TS-Stop-loss-and-Take-Profit-in-example/) - Educational
 - [Stepped Trailing Stop Loss](https://www.tradingview.com/script/jjhUHcje-Stepped-trailing-strategy-example/) - Educational
 - [Portfolio Backtesting Engine](https://www.tradingview.com/script/fhTLDun5-Portfolio-Backtester-Engine/) - Portfolio Backtesting
 
 
<a name="Automation" />

## Automated Order Execution
Need to automate your Pine script for real order execution?

### Open Source
#### Python
 - [Python Pine Bot Client](https://github.com/kzh-dev/pine-bot-client) - *Client implementation of trading bot that uses Pine Script and Python.*
 - [Python TradingView TA](https://github.com/deathlyface/python-tradingview-ta) - *Unofficial TradingView technical analysis API wrapper.*
 - [Python Bybit Pine Bot](https://github.com/Mtemi/Bybit-Auto-Trading-Bot-Ordes-placed-via-TradingView-Webhook) - *Python based Trading Bot that uses TradingView.com webhook JSON alerts to place orders(buy/sell/close/manage positions/TP/SL/TS etc.) on Bybit.com.*
 - [Python Webhook Alert Provider](https://github.com/fabston/TradingView-Webhook-Bot) - *The TradingView Webhook Bot listens to TradingView alerts via webhooks using flask. All alerts can be instantly sent to Telegram, Discord, Twitter and/or Email.*
 - [OctoBot](https://octobot.online/) - *Open-source cryptocurrency trading robot can receive alerts and turn them into order on your favorite crypto exchanges.*

#### Javascript
- [Instabot Trader](https://github.com/ottodevs/instabot-trader) - *Server Side bot that powers Alertatron. A simple tool to convert text messages sent over HTTP or via a Telegram bot into a set of trading orders, to a variety of exchanges (Bitfinex, Deribit and Coinbase Pro).*
- [Frostybot-js](https://github.com/CryptoMF/frostybot-js) - *Frostybot-JS is a cryptocurrency trading API endpoint, designed to execute webhook or REST requests as orders on a variety of well-known exchanges. While primarily designed to automate your Tradingview strategies, Frostybot can also be integrated with any other software using webhooks or REST. Bitmex, FTX, Deribit and Binance are supported.*
- [Fundingrate Backend](https://github.com/tacyarg/tradingview-webhooks) - *Backend service converting tradingview alerts into action.*
#### PHP
- [Frostybot-php](https://github.com/CryptoMF/frostybot-php) - *FrostyBot is a minimal endpoint that is designed to be used with webhooks in Tradingview alerts. It is designed to work cryptocurrency exchanges, specifically Bitmex, Deribit, FTX and Binance Futures*

#### Google Chrome 
- [Autoview Chrome Docker Bot](https://github.com/IAMtheIAM/autoview-tradingview-chrome-docker-bot) - *Dockerized Autoview Extension on a VPS.*

### Closed Source
- [3Commas](https://3commas.io/) - *Can receive TV alerts and connect them to their bots to execute simple orders on crypto exchanges.*
- [Alertatron](https://alertatron.com/) - *A service that allows you to relay TradingView alerts to Telegram, Discord, Slack, Email or webhooks, with a chart snapshot attached. The developer is well-known in the PineCoders community.*
- [AutoView](https://autoview.with.pink/) - *Google Chrome extension that receives TV alerts and relays orders to crypto exchanges.*
- [Cryptohopper](https://www.cryptohopper.com/) - *Use Cryptohopper with the TradingView webhook URL to send TV alerts to your bots, for automated order execution on one or multiple exchanges.*
- [ProfitView](https://wiki.profitview.app/home) - *Google Chrome extension that receives TV alerts and relays orders to crypto exchanges. Among PineCoders, has the reputation of being better than AutoView.*
- [TradingConnector](https://www.tradingconnector.com/) - *TradingView alerts to MT4/MT5 receives TV alerts and converts them into instant orders on MT4/MT5 in forex, indices and commodities markets. Latency is below 1 second.*
- [Fundingrate](https://github.com/tacyarg/fundingrate.io) - *Fundingrate is a software as a service platform that allows vendors to collect empirical data on live market conditions.* 


<a name="Conventions-rules" />

## Pine Script Conventions and Rules For Developers
- [Writing A Good Description](https://www.pinecoders.com/techniques/script_description/) - *How to write a good description when publishing your Pine.*
- [Writing Good Pine](https://www.pinecoders.com/coding_conventions/) - *How to write good clean code.*
- [Script Moderation](https://www.tradingview.com/chart/SSP/bquN1v9X-Script-Moderation-Q-A/) - *How to not get banned.*


<a name="Education" />

## Education
- [Digital Signal Processing](https://www.pinecoders.com/techniques/dsp/) - *Digital Signal Procession Techniques in Pine.*
- [FAQ](https://www.pinecoders.com/faq_and_code/) - *A powerful, curated list of frequently asked questions. Bookmark this.*
- [What is Repainting?](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html) - *It's not fun. You should learn about it.*



<a name="Other-Resources" />

## Other Resources
 - [Pine Coders Utils](https://github.com/pinecoders/pine-utils) - *Reusable code snippets, tricks & tips.*
 - [Pine Coders Website](https://www.pinecoders.com/) - *Useful information for Pine coders.*
 - [Kodify](https://kodify.net/tradingview-programming-articles/) - *Tutorials on various topics for beginners and more experienced coders alike.*
 - [Backtest Rookies](https://backtest-rookies.com/category/tradingview/) - *Good quality blog articles focusing on realizing specific tasks in Pine.*
 - [Stack Overflow](https://stackoverflow.com/questions/tagged/pine-script) - *Ask questions tagged with pine-script.* 
 

<a name="Contributing" />

## Contributing
 - [Pine Script Docs](https://github.com/tradingview/pine_script_docs) - *Found a typo or a bug in the Official Pine Script Documentaion? Drop a PR here.*
 
