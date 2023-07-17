import dataExtract
from discord.ext import commands
import os
from dotenv import load_dotenv
import discord
import pandas_ta as ta
import pandas as pd
from datetime import datetime
import yfinance as yf
import matplotlib as mpl
import mplfinance as mpf

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive = True)

endingMessage = "\n\nBleep Boop! I am a bot, and this process was completed automatically."
errorMesage = "404: Ticker Not Found\n\nWell Shucks! Your Ticker Is In Another Castle!"
imgErrorMessage = "404: Data Not Found.\n\nPerhaps your ticker is in another castle or you are using too little data to plot!"

#bot commands

@bot.command()
async def hello(ctx):
  await ctx.send("```" + "Hello " + ctx.author.display_name + "!" + "```")

@bot.command()
async def industry(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    industry = info["industry"]
    await ctx.send("```" + name + "'s Industry: " + industry + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def sector(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    sector = info["sector"]
    await ctx.send("```" + name + "'s Sector: " + sector + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def summary(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    summary = info["longBusinessSummary"]
    await ctx.send("```" + name + "'s Summary: " + summary + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def website(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    website = info["website"]
    await ctx.send("```" + name + "'s Website: " + website + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def open(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    open = info["open"]
    await ctx.send("```" + name + "'s Open Price: $" + str(open) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def close(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    close = info["previousClose"]
    await ctx.send("```" + name + "'s Previous Close: $" + str(close) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def currentPrice(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    currPrice = info["currentPrice"]
    await ctx.send("```" + name + "'s Current Price: $" + str(currPrice) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def priceTargets(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    targetLowPrice = info["targetLowPrice"]
    targetHighPrice = info["targetHighPrice"]
    targetMeanPrice = info["targetMeanPrice"]
    targetMedianPrice = info["targetMedianPrice"]
    recMean = info["recommendationMean"]
    recAnalysis = ""
    if(recMean >= 4.1):
      recAnalysis = "Very Poor"
    elif(recMean >= 3.5):
      recAnalysis = "Poor"
    elif(recMean >= 2.5):
      recAnalysis = "Neutral"
    elif(recMean >= 1.9):
      recAnalysis = "Good"
    else:
      recAnalysis = "Very Good"
    await ctx.send("```" + name + " is a " + recAnalysis + " Stock, with an average rating of " + str(recMean) + ".\n\n" + name + "'s Price Targets: " + "\nLow Prediction: $" + str(targetLowPrice) + "\nMean Prediction: $" + str(targetMeanPrice) + "\nMedian Prediction: $" + str(targetMedianPrice) + "\nHigh Prediction: $" + str(targetHighPrice) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")
    
@bot.command()
async def PBRatio(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    pBRatio = info["priceToBook"]
    await ctx.send("```" + name + "'s PB Ratio: " + str(pBRatio) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def PEGRatio(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    pegRatio = info["pegRatio"]
    await ctx.send("```" + name + "'s PEG Ratio: " + str(pegRatio) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")
  
@bot.command()
async def EBITDA(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    balSheet = dataExtract.getBalSheet(data)
    ebitda = balSheet.at["Normalized EBITDA", 0]
    await ctx.send("```" + "Last Normalized EBITDA of " + name + ": " + str(ebitda) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def EPS(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    balSheet = dataExtract.getBalSheet(data)
    eps = balSheet.at["Diluted EPS", 0]
    await ctx.send("```" + "Last Diluted EPS of " + name + ": " + str(eps) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def earningsDate(ctx, ticker):
  try:
    data = yf.Ticker(ticker)
    info = data.info
    name = info["shortName"]
    date = dataExtract.getEarningsDate(data, datetime.today())
    date = date.strftime("%m/%d/%Y")
    await ctx.send("```" + name + "'s Next Earning Date is: " + date + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def RSI(ctx, ticker):
  try:
    tickerInfo = yf.Ticker(ticker)
    info = tickerInfo.info
    name = info["shortName"]
    data = pd.DataFrame()
    data = data.ta.ticker(ticker, start = "2023-01-01")
    lastRSI = dataExtract.getRSI(data)
    await ctx.send("```" + name + "'s Current RSI: " + str(lastRSI) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def stoch(ctx, ticker):
  try:
    tickerInfo = yf.Ticker(ticker)
    info = tickerInfo.info
    name = info["shortName"]
    data = pd.DataFrame()
    data = data.ta.ticker(ticker, start = "2023-01-01")
    lastStoch = dataExtract.getStoch(data)
    await ctx.send("```" + name + "'s Current Stochastic: " + str(lastStoch) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def kurtosis(ctx, ticker):
  try:
    tickerInfo = yf.Ticker(ticker)
    info = tickerInfo.info
    name = info["shortName"]
    data = pd.DataFrame()
    data = data.ta.ticker(ticker, start = "2023-01-01")
    lastKurt = dataExtract.getKurt(data)
    await ctx.send("```" + name + "'s Current Kurtosis: " + str(lastKurt) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def MACD(ctx, ticker):
  try:
    tickerInfo = yf.Ticker(ticker)
    info = tickerInfo.info
    name = info["shortName"]
    data = pd.DataFrame()
    data = data.ta.ticker(ticker, start = "2023-01-01")
    lastMACD = dataExtract.getMACDVal(data)
    macdAnalysis = ""
    if(lastMACD > 0):
      macdAnalysis = "Signalling Positive"
    else:
      macdAnalysis = "Signalling Negative"
    await ctx.send("```" + name + "'s MACD is " + macdAnalysis + " with a current MACD Difference of " + str(lastMACD) + "." + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def BoP(ctx, ticker):
  try:
    tickerInfo = yf.Ticker(ticker)
    info = tickerInfo.info
    name = info["shortName"]
    data = pd.DataFrame()
    data = data.ta.ticker(ticker, start = "2023-01-01")
    lastBoP = dataExtract.getBoP(data)
    await ctx.send("```" + name + "'s Current BoP (Balance of Power): " + str(lastBoP) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def chandef(ctx, ticker):
  try:
    tickerInfo = yf.Ticker(ticker)
    info = tickerInfo.info
    name = info["shortName"]
    data = pd.DataFrame()
    data = data.ta.ticker(ticker, start = "2023-01-01")
    lastCFO = dataExtract.getCFO(data)
    await ctx.send("```" + name + "'s Current Chande Forecast Oscillator: " + str(lastCFO) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def chandem(ctx, ticker):
  try:
    tickerInfo = yf.Ticker(ticker)
    info = tickerInfo.info
    name = info["shortName"]
    data = pd.DataFrame()
    data = data.ta.ticker(ticker, start = "2023-01-01")
    lastCMO = dataExtract.getCMO(data)
    await ctx.send("```" + name + "'s Current Chande Momentum Oscillator: " + str(lastCMO) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def zscore(ctx, ticker):
  try:
    tickerInfo = yf.Ticker(ticker)
    info = tickerInfo.info
    name = info["shortName"]
    data = pd.DataFrame()
    data = data.ta.ticker(ticker, start = "2023-01-01")
    lastZScore = dataExtract.getZScore(data)
    await ctx.send("```" + name + "'s Current Z-Score: " + str(lastZScore) + endingMessage + "```")
  except:
    await ctx.send("```" + errorMesage + endingMessage + "```")

@bot.command()
async def stockImg(ctx, ticker, startDate):
  try:
    tickerInfo = yf.Ticker(ticker)
    info = tickerInfo.info
    name = info["shortName"]
    date = str(startDate)
    data = pd.DataFrame()
    selectedStyle = "yahoo"
    data = data.ta.ticker(ticker, start = startDate)
    ema10 = data.ta.ema(length=10)
    ema10 = ema10.reset_index()
    ema50 = data.ta.ema(length=50)
    ema50 = ema50.reset_index()
    if("EMA_50" not in ema50):
      ema50["EMA_50"] = ema10["EMA_10"].values
    ema200 = data.ta.ema(length = 200)
    ema200 = ema200.reset_index()
    if("EMA_200" not in ema200):
      ema200["EMA_200"] = ema50["EMA_50"].values
    ema10 = ema10["EMA_10"]
    ema50 = ema50["EMA_50"]
    ema200 = ema200["EMA_200"]
    rsi = data.ta.rsi()
    macd = data.ta.macd()
    macd = macd.reset_index()
    macdS = macd["MACD_12_26_9"]
    macdL = macd["MACDs_12_26_9"]
    macdDPos = dataExtract.organizeMACDGraph(macd, True)
    macdDNeg = dataExtract.organizeMACDGraph(macd, False)
    cfo = data.ta.cfo()
    ft = data.ta.fisher()
    spp0 = [mpf.make_addplot(ema200, panel = 0, color = "#1e7543"),
            mpf.make_addplot(ema50, panel = 0, color = "#00ffee"),
            mpf.make_addplot(ema10, panel = 0, color = "#eb344f")]
    
    spp2 = [mpf.make_addplot(rsi, panel = 2, color = "#a60204")]
    
    spp3 = [mpf.make_addplot(cfo, panel = 3, color = "#015e09")]
    
    spp4 = [mpf.make_addplot(macdS, panel = 4, color = "#d9d20f"),
            mpf.make_addplot(macdL, panel = 4, color = "#0300a3"),
            mpf.make_addplot(macdDPos, panel = 4, type="bar", color = "#02cf09"),
            mpf.make_addplot(macdDNeg, panel = 4, type="bar", color = "#cf0502")
    ]
    
    spp5 = [mpf.make_addplot(ft, panel = 5, color = "#0262a6")]
    
    subplots = spp0 + spp2 + spp3 + spp4 + spp5
    
    data = data.ta.ticker(ticker, start = startDate)
    plot, axes = mpf.plot(data, type = "candle", volume = True, closefig = True, style = selectedStyle, addplot = subplots, axtitle = ("Stock Price of " + name + " since " + date), returnfig = True)
    
    axes[0].set_ylabel("Price ($)")
    axes[2].set_ylabel("Vol (M)")
    axes[4].set_ylabel("RSI")
    axes[6].set_ylabel("CFO")
    axes[8].set_ylabel("MACD")
    axes[10].set_ylabel("FT")
    
    axes[0].legend(["_Hidden1", "_Hidden2", "EMA 200", "EMA 50", "EMA 10"])
    
    plot.savefig("temp.png")
    await ctx.send(file = discord.File("temp.png"))
    os.remove("temp.png")
  except:
    await ctx.send("```" + imgErrorMessage + endingMessage + "```")


@bot.command()
async def commands(ctx):
  await ctx.send("```" + "Commands: \n!hello \n!industry TICKER \n!sector TICKER \n!summary TICKER \n!website TICKER \n!open TICKER \n!close TICKER \n!currentPrice TICKER \n!priceTargets TICKER \n!PBRatio TICKER \n!PEGRatio TICKER \n!EBITDA TICKER \n!EPS TICKER \n!earningsDate TICKER \n!RSI TICKER \n!stoch TICKER \n!kurtosis TICKER \n!MACD TICKER \n!BoP TICKER \n!chandef TICKER \n!chandem TICKER \n!zscore TICKER \n!stockImg TICKER START-DATE" + endingMessage + "```")

load_dotenv()
disc_token = os.environ.get("discToken")
bot.run(disc_token)