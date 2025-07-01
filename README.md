# awesome-pinescript  [![Visitors](https://komarev.com/ghpvc/?username=pAulseperformance&repo=awesome-pinescript)](https://github.com/pAulseperformance/awesome-pinescript) [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub last commit](https://img.shields.io/github/last-commit/pAulseperformance/awesome-pinescript.svg)](https://github.com/pAulseperformance/awesome-pinescript/commits/master)


**A Comprehensive Collection of Everything Related to Tradingview Pine Script.**

## Table of Contents
- [awesome-pinescript      ](#awesome-pinescript------)
  - [Table of Contents](#table-of-contents)
  - [Official Resources](#official-resources)
  - [Community](#community)
  - [Indicators](#indicators)
    - [Interesting](#interesting)
    - [Collections](#collections)
    - [Volume](#volume)
    - [Screeners](#screeners)
    - [Math](#math)
    - [Tools](#tools)
  - [Strategies](#strategies)
  - [Libraries](#libraries)
  - [Automated Order Execution](#automated-order-execution)
    - [Open Source](#open-source)
      - [Python](#python)
      - [Javascript](#javascript)
      - [PHP](#php)
      - [Google Chrome](#google-chrome)
    - [Closed Source](#closed-source)
  - [Development Tools](#development-tools)
  - [Style Guides \& Best Practices](#style-guides--best-practices)
  - [Learning Resources](#learning-resources)
  - [Contributing](#contributing)
  - [License](#license)


<a name="Official-Resources" />

## Official Resources
 - [Language Reference Manual](https://www.tradingview.com/pine-script-reference/v4/) - *An Index of built-in variables, functions and language operators.*
 - [Pine Script v4 User Manual](https://www.tradingview.com/pine-script-docs/en/v4/index.html) - *Official Documentation on Pine Script Version 4.*
 - [Pine Script v5 User Manual](https://www.tradingview.com/pine-script-docs/en/v5/index.html) - *Official Documentation on Pine Script Version 5.*
 - [Pine Script v6 User Manual](https://www.tradingview.com/pine-script-docs/welcome/) - *Official Documentation on Pine Script Version 6.*
 - [TV Blog](https://www.tradingview.com/blog/en/category/market-analysis/pine/) - *Information about major releases and modifications to Pine Script (as well as other features.)*


<a name="Community" />

## Community
 - [Pine Script Chat Room](https://www.tradingview.com/chat/#BfmVowG1TZkKO235) - *TradingView public chat dedicated to Pine Script where active developers of the community help each other out.*
 - [TV Public Scripts](https://www.tradingview.com/scripts/) - *TradingView’s Public Library contains all user-published scripts.*
 - [Editors Picks](https://www.tradingview.com/scripts/editors-picks/) - *TV's curated list of best indicators*



<a name="Indicators" />

## Indicators
### Interesting
- [Cycles Analysis](https://www.tradingview.com/script/fqnXJggs-Cycles-Analysis/) - *Gives a visual representation of bull/bear markets and gives a prediction based on the previous data. * 
- [Developing Market Profile](https://www.tradingview.com/script/XMKe97Vn-Developing-Market-Profile-TPO-Honestcowboy/) - *Developing Market Profile will change bar by bar and display PRICE in relation to TIME for a user specified number of past bars.*
- [Flag Finder](https://www.tradingview.com/script/DU228Vjm-Flag-Finder/) - *Flag Finder Indicator is a technical analysis tool to identify bull and bear flags.*
- [Fundamentals Graphing](https://www.tradingview.com/script/7qjXp2op-Fundamentals-Graphing-Kioseff-Trading/) - *Really cool way of graphing with Pine Script!*
- [ICT Killzones Pivots TFO](https://www.tradingview.com/script/nW5oGfdO-ICT-Killzones-Pivots-TFO/) - *the purpose of this script is to identify ICT Killzones while also storing their highs and lows for future reference, until traded through.*
- [Trend Correlation Heatmap](https://www.tradingview.com/script/96Cld5iS-Trend-Correlation-Heatmap/) - *This indicator displays the correlation of different assets over several timeframes on the chart.*
- [TTP VIX Spy](https://www.tradingview.com/script/Rv3pibXO-TTP-VIX-Spy/) - *TTP VIX Spy is an indicator that uses data from VIX to better time entries in the market.*


### Collections
- [Pine Coders Publications](https://www.tradingview.com/u/PineCoders/#published-scripts) - *A plethora of useful techniques developed by the Pine Coders Account*
- [Pine Script Indicators Collection](https://github.com/everget/tradingview-pinescript-indicators) - *A collection of various technical indicators.*
- [Pine Script To ThinkScript Repo](https://github.com/bingit2/TradingView-to-ThinkorSwim) - *Repository of Pine Script Indicators converted to TOS ThinkScript*
- [Traderslist](https://www.traderslist.io) - *Discover trading indicators Trading Indicators, Tools & Algorithms*

### Volume
- [Liquidity Sentiment Profile](https://www.tradingview.com/script/asr7nOb2-Liquidity-Sentiment-Profile-LuxAlgo/) - *The Liquidity Sentiment Profile is an advanced charting tool that measures by combining PRICE and VOLUME data over specified anchored periods and highlights within a sequence of profiles the distribution of the liquidity and the market sentiment at specific price levels.*
- [Raindrops](https://www.tradingview.com/script/dJr8hv4v-Raindrops-Makit0/) - *Custom Volume profiles on user defined periods.*


### Screeners
- [Indices Sector Sigma Spikes](https://www.tradingview.com/script/B3aLMAHh-Indices-Sector-SigmaSpikes/) - *This screener aims to provide Bird-Eye view across sector indices, to find which sector is having significant or \'out-of-norm\' move in either direction.*
- [Mean Reversion Channel](https://www.tradingview.com/script/Lr5QD0kK-Screener-Mean-Reversion-Channel/) - *The screener works by scanning through up to 40 symbols and list down symbols that are currently within Overbought/Oversold Zone as defined by Mean Reversion Channel indicator.*
- [120 ticker Screener](https://www.tradingview.com/script/0h0gKNcy-120x-ticker-screener-composite-tickers/) - *In specific circumstances, it is possible to extract data, far above the 40 \`request.*()\` call limit for 1 single script.*
- [TradingView-Screener](https://github.com/shner-elmo/TradingView-Screener) - *A Python package that lets you create TradingView screeners by interacting directly with TradingView\'s API.*

### Math
- [Black Scholes](https://www.tradingview.com/script/dgMumvhd-Black-Scholes-Options-Pricing-Model/) - *The Black-Scholes model is a mathematical model used for pricing options. From this model you can derive the theoretical fair value of an options contract.*

### Tools
- [Script Stopwatch](https://www.tradingview.com/script/rRmrkRDr-Script-Stopwatch-PineCoders-FAQ/) - *Measure the performance of your scripts*
- [Filter Response](https://www.tradingview.com/script/oTEP9DJF-Filter-Information-Box-PineCoders-FAQ/) - *Analyze the characteristics of your filters, with DSP*
- [Signal Generator](https://www.tradingview.com/script/p3Bqr6fq-pp-Signal-Generator/) - *Debug and test indicators and strategies that accept exernal inputs.*
- [Interactive Motive Wave Checklist](https://www.tradingview.com/script/ypAxpurY-Interactive-Motive-Wave-Checklist/) - *an interactive tool that can be used for learning a bit about Elliott Waves*
- [Textmate Language for Pine Script v5 2023-05](https://www.tradingview.com/script/O6LCkLTf-Textmate-Language-for-Pine-Script-v5-2023-05/) - *Syntax Highlighter for Textmate vscode*


<a name="Strategies" />

## Strategies
- [MACD Trend Following](https://www.tradingview.com/script/8j6YH6gD-MACD-Trend-Following/) - *A simple MACD trend following strategy.*
- [Moving Average Crossover](https://www.tradingview.com/script/2j6YH6gD-Moving-Average-Crossover/) - *A basic moving average crossover strategy.*
- [Portfolio Backtesting Engine](https://www.tradingview.com/script/fhTLDun5-Portfolio-Backtester-Engine/) - *Portfolio Backtesting*
- [RSI Strategy](https://www.tradingview.com/script/3j6YH6gD-RSI-Strategy/) - *A simple strategy using the RSI indicator.*
- [Stepped Trailing Stop Loss](https://www.tradingview.com/script/jjhUHcje-Stepped-trailing-strategy-example/) - *Educational*
- [Stop Loss and Take Profit](https://www.tradingview.com/script/IHVPG6TS-Stop-loss-and-Take-Profit-in-example/) - *Educational*


<a name="Libraries" />

## Libraries
- [Pine Script Libraries](https://www.tradingview.com/script/4j6YH6gD-Pine-Script-Libraries/) - *A collection of useful Pine Script libraries.*
- [Script Stopwatch](https://www.tradingview.com/script/xTHx0lQy-LibraryStopwatch/) - *Measure the performance of your scripts*


<a name="Automated-Order-Execution" />

## Automated Order Execution
- [PSStrategyX](https://www.tradingview.com/script/ZUqQdIKU-pAulseperformance-PSStrategyX/) - *Backtests and Automates Indicators Automatically*

### Open Source

#### Python
- [Python Pine Bot Client](https://github.com/kzh-dev/pine-bot-client) - *Client implementation of trading bot that uses Pine Script and Python.*
- [Python TradingView TA](https://github.com/deathlyface/python-tradingview-ta) - *Unofficial TradingView technical analysis API wrapper.*
- [Python Bybit Pine Bot](https://github.com/Mtemi/Bybit-Auto-Trading-Bot-Ordes-placed-via-TradingView-Webhook) - *Python based Trading Bot that uses TradingView.com webhook JSON alerts to place orders(buy/sell/close/manage positions/TP/SL/TS etc.) on Bybit.com.*
- [Python Webhook Alert Provider](https://github.com/fabston/TradingView-Webhook-Bot) - *The TradingView Webhook Bot listens to TradingView alerts via webhooks using flask. All alerts can be instantly sent to Telegram, Discord, Twitter and/or Email.*
- [OctoBot](https://octobot.online/) - *Open-source cryptocurrency trading robot can receive alerts and turn them into order on your favorite crypto exchanges.*
- [Misc Collection](https://github.com/Roibal/Cryptocurrency-Trading-Bots-Python-Beginner-Advance) - *This repo includes various python crypto bots with a tradingview alert bot.*
- [Quantium Signal](https://github.com/quantium-ai/signal) - *Quantium Signal is a self-hosted SMTP server that allows the use of TradingView alerts without the premium plan.*

#### Javascript
- [Instabot Trader](https://github.com/ottodevs/instabot-trader) - *Server Side bot that powers Alertatron. A simple tool to convert text messages sent over HTTP or via a Telegram bot into a set of trading orders, to a variety of exchanges (Bitfinex, Deribit and Coinbase Pro).*
- [Frostybot-js](https://github.com/CryptoMF/frostybot-js) - *Frostybot-JS is a cryptocurrency trading API endpoint, designed to execute webhook or REST requests as orders on a variety of well-known exchanges.*
- [Fundingrate Backend](https://github.com/tacyarg/tradingview-webhooks) - *Backend service converting tradingview alerts into action.*

#### PHP
- [Frostybot-php](https://github.com/CryptoMF/frostybot-php) - *FrostyBot is a minimal endpoint that is designed to be used with webhooks in Tradingview alerts.*

#### Google Chrome
- [Autoview Chrome Docker Bot](https://github.com/IAMtheIAM/autoview-tradingview-chrome-docker-bot) - *Dockerized Autoview Extension on a VPS.*

### Closed Source
- [3Commas](https://3commas.io/) - *Can receive TV alerts and connect them to their bots to execute simple orders on crypto exchanges.*
- [Alertatron](https://alertatron.com/) - *A service that allows you to relay TradingView alerts to Telegram, Discord, Slack, Email or webhooks, with a chart snapshot attached.*
- [Altrady](https://www.altrady.com/features/signal-bot) - *You can run pine script strategies on TradingView that will automatically open positions based on the signal. *
- [AutoView](https://autoview.with.pink/) - *Free For Testnets! Google Chrome extension that receives TV alerts and relays orders to crypto exchanges.*
- [Capitalise.ai](https://capitalise.ai/) - *Code Free Trading Automation that accepts simple [TV Webhook Automation](https://support.capitalise.ai/en/articles/5638761-using-tradingview-alerts-to-trigger-strategies)*
- [Cornix](https://cornix.io/) - *Automated crypto trading for everyone*
- [Cryptohopper](https://www.cryptohopper.com/) - *Use Cryptohopper with the TradingView webhook URL to send TV alerts to your bots, for automated order execution on one or multiple exchanges.*
- [Mizar](https://www.mizar.com/) - *Can run your TV strategies via webhooks with the fast and reliable execution across several crypto exchanges.*
- [PickMyTrade](https://pickmytrade.trade/) - *PickMyTrade empowers traders by automating TradingView strategies/Indicator for futures, seamlessly connecting TradingView with Tradovate and Rithmic*
- [Pine Connector](https://www.pineconnector.com/) - *Auto-execute your TradingView alerts to MetaTrader 4 & 5*
- [Pineify](https://pineify.app/) - *Pineify is a tool for tradingview traders that allows them to build TradingView indicators through visualization tools.*
- [ProfitView](https://wiki.profitview.app/home) - *Google Chrome extension that receives TV alerts and relays orders to crypto exchanges.*
- [PSStrategyX](https://pinescriptstrategy.com/psstrategyx/) - *Pine Script Indicator that automatically connects to AutoView so you don't have to write alert syntax.*
- [Tickerly](https://tickerly.net/?partner=1898) - *Tickerly’s fast and flexible service enables you to effortlessly automate any strategy on forex, stock, futures or cryptocurrency assets.*
- [TradeSanta](https://www.tradingview.com/script/10j6YH6gD-TradeSanta/) - *Automated trading software for TradingView.*
- [Tradelab.ai](https://tradelab.ai/) - *Free TradingView Bot Builder.Build the strategy you want. No compromises. No code skills required. Get started for free.*
- [TradersPost](https://traderspost.io/?via=1) - *Stocks, Options, Futures, Crypto and Paper trading with TradingView Webhooks*
- [TradingConnector](https://www.tradingconnector.com/) - *TradingView alerts to MT4/MT5 receives TV alerts and converts them into instant orders on MT4/MT5 in forex, indices and commodities markets.*
- [TradingView.to](https://tradingview.to/) - *The simplest, most affordable and reliable automation tool*
- [Tuned](https://app.tuned.com) - *Use PineScript to run fully-automated batch experiments with powerful backtesting, paper trading, and even live trading.*
- [TV Hub](https://www.tv-hub.org/) - *Convert every TradingView alert into a trade within seconds.*
- [Webook Alerts](https://webhookalerts.com/) - *Send all your TradingView alerts to Telegram, Discord, Slack and Twitter along with a full screenshot of the chart*


<a name="Development-Tools" />

## Development Tools
- [pine-script-linter](https://www.npmjs.com/package/pinescript-linter) - *A linter for Pine Script to enforce coding standards and catch common errors.*
- [pine-script-visual-studio-code](https://github.com/pine-language-tools/pine-script-visual-studio-code) - *Sublime Text/VSCode package for Pine Script v5 with a few VSCode-specific features added.*


<a name="Style-Guides-Best-Practices" />

## Style Guides & Best Practices
- [Script Moderation](https://www.tradingview.com/chart/SSP/bquN1v9X-Script-Moderation-Q-A/) - *How to not get banned.*
- [Writing A Good Description](https://www.pinecoders.com/techniques/script_description/) - *How to write a good description when publishing your Pine.*
- [Writing Good Pine](https://www.pinecoders.com/coding_conventions/) - *How to write good clean code.*


<a name="Learning-Resources" />

## Learning Resources
- [Backtest Rookies](https://backtest-rookies.com/category/tradingview/) - *Good quality blog articles focusing on realizing specific tasks in Pine.*
- [Digital Signal Processing](https://www.pinecoders.com/techniques/dsp/) - *Digital Signal Procession Techniques in Pine.*
- [FAQ](https://www.pinecoders.com/faq_and_code/) - *A powerful, curated list of frequently asked questions. Bookmark this.*
- [Kodify](https://kodify.net/tradingview-programming-articles/) - *Tutorials on various topics for beginners and more experienced coders alike.*
- [Pine Coders Utils](https://github.com/pinecoders/pine-utils) - *Reusable code snippets, tricks & tips.*
- [Pine Coders Website](https://www.pinecoders.com/) - *Useful information for Pine coders.*
- [Stack Overflow](https://stackoverflow.com/questions/tagged/pine-script) - *Ask questions tagged with pine-script.* 
- [What is Repainting?](https://www.tradingview.com/pine-script-docs/en/v5/concepts/Repainting.html) - *It's not fun. You should learn about it.*

<a name="Contributing" />

## Contributing
- [How to Contribute](https://github.com/pAulseperformance/awesome-pinescript/blob/master/.github/CONTRIBUTING.md) - *Read this if you want to contribute to the repository.*
- [Translation Guide](https://github.com/pAulseperformance/awesome-pinescript/blob/master/.github/TRANSLATION.md) - *Read this if you want to help translate the repository to your language.*
- [Pine Script Docs](https://github.com/tradingview/pine_script_docs) - *Found a typo or a bug in the Official Pine Script Documentaion? Drop a PR here.*


<a name="License" />

## License
- [MIT License](https://github.com/pAulseperformance/awesome-pinescript/blob/master/LICENSE) - *The code and content in this repository is licensed under the MIT License. See the LICENSE file for more information.*
