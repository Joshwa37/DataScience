import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    va=orders['customerId'].values
    li=[]
    for i in customers.values:
        if(i[0] not in va):
            li.append(i[1])
    return pd.DataFrame(li,columns=['Customers'])
    