import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values("score",ascending=False,inplace=True)
    df=scores['score'].rank(axis=0, method='dense', ascending=False)
    scores["rank"]=df
    return scores[['score','rank']]

#for using the rank method it that the method argument as lot of types each has its own 
#way of handling ranking.for dense if they find same value they give it same rank like 1 and for the ext value it stat from 2
#not like 1 1 3 it will be 1 1 2
#and for min it will give same rank to same value but the next value will be incremented by the number of same values
#like 1 1 3
#and for max it will give same rank to same value but the next value will be incremented by 1 from the highest rank of the same values  
#like 1 1 4
#and for average it will give same rank to same value but the next value will be the average of the ranks of the same values
#like 1 1 2.5 
#and for first it will give rank based on the occurrence of the value in the dataframe
#like 1 2 3
#so based on the requirement we can use any of these methods
#also note that the rank method returns a float value so if we want integer value we need to convert it to int
