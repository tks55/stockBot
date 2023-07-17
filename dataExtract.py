import yfinance as yf
import pandas as pd
import pandas_ta as ta
import math

#stock backend, developed off of ADTS
def getBalSheet(data):
  data = data.income_stmt
  data.columns = range(data.columns.size)
  return(data)

def getEarningsDate(data, date):
  data = data.earnings_dates
  dateList = list(data.index.values)
  nextDate = 0
  for i in dateList:
    earningsDateIter = pd.to_datetime(i)
    if earningsDateIter > date:
      nextDate = earningsDateIter
    else:
      break
  return(nextDate)

def getRSI(data):
  rsi = data.ta.rsi()
  rsi = rsi.reset_index()
  lenRSI = len(rsi)
  lastRSI = round(rsi.at[lenRSI - 1, "RSI_14"], 2)
  return(lastRSI)

def getStoch(data):
  stoch = data.ta.stoch()
  stoch = stoch.reset_index()
  lenStoch = len(stoch)
  lastStoch = round(stoch.at[lenStoch - 1, "STOCHk_14_3_3"], 2)
  return(lastStoch)

def getKurt(data):
  kurt = data.ta.kurtosis()
  kurt = kurt.reset_index()
  lenKurt = len(kurt)
  lastKurt = round(kurt.at[lenKurt - 1, "KURT_30"], 2)
  return(lastKurt)

def getMACDVal(data):
  data = data.ta.macd()
  macd = data.reset_index()
  lenMACD = len(macd)
  lastMACD = round(macd.at[lenMACD - 1, "MACDh_12_26_9"], 2)
  return(lastMACD)

def getBoP(data):
  bop = data.ta.bop()
  bop = bop.reset_index()
  lenBoP = len(bop)
  lastBoP = round(bop.at[lenBoP - 1, "BOP"], 2)
  return(lastBoP)

def getCFO(data):
  cfo = data.ta.cfo()
  cfo = cfo.reset_index()
  lenCFO = len(cfo)
  lastCFO = round(cfo.at[lenCFO - 1, "CFO_9"], 2)
  return(lastCFO)

def getCMO(data):
  cmo = data.ta.cmo()
  cmo = cmo.reset_index()
  print(cmo)
  lenCMO = len(cmo)
  lastCMO = round(cmo.at[lenCMO - 1, "CMO_14"], 2)
  return(lastCMO)

def getZScore(data):
  zscore = data.ta.zscore()
  zscore = zscore.reset_index()
  print(zscore)
  lenZScore = len(zscore)
  lastZScore = round(zscore.at[lenZScore - 1, "ZS_30"], 2)
  return(lastZScore)

def organizeMACDGraph(macd, pos):
  macdD = macd
  diff = []
  if(pos == True):
    macdD["diff"] = macdD["MACDh_12_26_9"]
    diff = macdD["diff"].values
    for x in range(len(diff)):
      if (math.isnan(diff[x]) or diff[x] > 0):
        diff[x] = diff[x]
      else:
        diff[x] = 0
  else:
    macdD["diff"] = macdD["MACDh_12_26_9"]
    diff = macdD["diff"].values
    for x in range(len(diff)):
      if (math.isnan(diff[x]) or diff[x] < 0):
        diff[x] = diff[x]
      else:
        diff[x] = 0
  return diff