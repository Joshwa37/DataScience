import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    li=[]
    def va(val):
        if(not val['managerId'] is np.nan):
            ids=val['managerId']
            ta=employee[employee['id']==ids]
            print(ta)
            if(len(ta)==1):
                sal=ta['salary'].iloc[0]
                if(sal<val['salary']):
                    print(sal,val['salary'])
                    li.append(val['name'])
    employee.apply(va,axis=1)
    print(li)
    out=pd.DataFrame(li,columns=['Employee'])
    return out