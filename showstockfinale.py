import pandas as pd
import numpy as np

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:
    def ope(val):
        ch=0
        if(val['operation']=='Sell'):
            ch=val['price']
        else:
            ch=-1*val['price']
        return ch
    df=stocks.apply(ope,axis=1)
    stocks['capital_gain_loss']=df
    s=stocks[['stock_name','capital_gain_loss']]
    p=s.pivot_table(index='stock_name',aggfunc="sum")
    p=p.reset_index()
    p.sort_values('capital_gain_loss',ascending=False,inplace=True)
    return p