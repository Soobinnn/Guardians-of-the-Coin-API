import pyupbit
import time
from itertools import islice
import pandas as pd

#거래대금이 많은 순으로 코인 리스트를 얻는다. 첫번째 : Interval기간(day,week,minute15 ....), 두번째 : 몇개까지 
def GetTopAmountCoinList(interval,top):
    print("--------------GetTopCoinList Start-------------------")
    #원화 마켓의 코인 티커를 리스트로 담아요.
    Tickers = pyupbit.get_tickers("KRW")

    #딕셔너리를 하나 만듭니다.
    dic_coin_money = dict()

    #for문을 돌면서 모든 코인들을 순회합니다.
    for ticker in Tickers:
        try:
            #캔들 정보를 가져와서 
            df = pyupbit.get_ohlcv(ticker,interval)
            #최근 2개 캔들의 종가와 거래량을 곱하여 대략의 거래대금을 구합니다.
            volume_money = (df['close'][-1] * df['volume'][-1]) + (df['close'][-2] * df['volume'][-2])
            #volume_money = float(df['value'][-1]) + float(df['value'][-2]) #거래대금!
            #이걸 위에서 만든 딕셔너리에 넣어줍니다. Key는 코인의 티커, Value는 위에서 구한 거래대금 
            dic_coin_money[ticker] = volume_money
            #출력해 봅니다.
            print(ticker, dic_coin_money[ticker])
            #반드시 이렇게 쉬어줘야 합니다. 안그럼 에러가.. 시간조절을 해보시며 최적의 시간을 찾아보세요 전 일단 0.1로 수정했어요!
            time.sleep(0.1)

        except Exception as e:
            print("exception:",e)

    #딕셔너리를 값으로 정렬하되 숫자가 큰 순서대로 정렬합니다.
    dic_sorted_coin_money = sorted(dic_coin_money.items(), key = lambda x : x[1], reverse= True)

    print("--------------GetTopCoinList End-------------------")

    #코인 리스트를 리턴해 줍니다.
    return dict(islice(dic_sorted_coin_money,top))

#RSI지표 수치를 구해준다. 첫번째: 분봉/일봉 정보, 두번째: 기간, 세번째: 기준 날짜
# rsi60_min = GetRSI(df_60,14,-1) #현재 캔들 RSI지표
def GetRSI(ticker, interval, period, st):
    ohlcv = pyupbit.get_ohlcv(ticker,interval)
    ohlcv["close"] = ohlcv["close"]
    delta = ohlcv["close"].diff()
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    _gain = up.ewm(com=(period - 1), min_periods=period).mean()
    _loss = down.abs().ewm(com=(period - 1), min_periods=period).mean()
    RS = _gain / _loss
    
    return float(pd.Series(100 - (100 / (1 + RS)), name="RSI").iloc[st])

#이동평균선 수치를 구해준다 첫번째: 분봉/일봉 정보, 두번째: 기간, 세번째: 기준 날짜

def GetMA(ohlcv,period,st):
    #이 역시 이동평균선을 제대로 구해줍니다.
    close = ohlcv["close"]
    ma = close.rolling(period).mean()
    return float(ma[st])

