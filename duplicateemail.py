import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    person=person.rename(columns={'email':'Email'})
    df=person[person.duplicated(['Email'])][['Email']]
    if(len(df)==0):
        return pd.DataFrame(person[person.duplicated(['Email'])][['Email']].values,columns=['Email'])
    return pd.DataFrame(df['Email'].unique(),columns=['Email'])
    