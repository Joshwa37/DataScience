import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.sort_values("salary",ascending=False,inplace=True)
    employee=employee[~employee.duplicated('salary',keep='first')]
    print(employee)
    a=str(N)
    if(N>len(employee) or N<=0):
        d=np.array([None])
        l=pd.DataFrame(d,columns=['getNthHighestSalary('+a+")"])
        return l
    d=employee.iloc[N-1][['salary']]
    print(d.values)
    l=pd.DataFrame(d.values,columns=['getNthHighestSalary('+a+")"])
    return l