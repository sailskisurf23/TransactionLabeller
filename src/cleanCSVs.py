import pandas as pd
import numpy as np

def clean_all(df_all):
    df_all['Category'] = df_all['Category'].replace('Shit','Stuff')
    return df_all[['date','amount','description','Category']]

def clean_wf(df_wf):
    df_wf.columns = ['date','amount','drop1','drop2','description']
    df_wf.drop(['drop1','drop2'],axis=1,inplace=True)
    df_wf = df_wf[df_wf['amount'] < 0]
    return df_wf

def clean_chase(df_chase):
    df_chase.columns = ['drop1','date','drop2','description','amount']
    df_chase.drop(['drop1','drop2'],axis=1,inplace=True)
    df_chase = df_chase[df_chase['amount'] < 0]
    return df_chase[['date','amount','description']]

def clean_read(path, fmt):
    '''
    Read in CC transactions from CSV to Pandas DF.

    INPUT
    path (str): filepath
    fmt (str): 'all','chase' or 'wf'

    OUTPUT
    df_clean (pandas DF)
    feature columns: ('date','amount','description')
    label column: (Category)
    '''
    if fmt == 'all':
        return clean_all(pd.read_csv(path))
    if fmt == 'chase':
        return clean_chase(pd.read_csv(path))
    if fmt == 'wf':
        return clean_wf(pd.read_csv(path, header=None))

if __name__ == '__main__':
    path_all = '../data/all_trans.csv'
    path_chase = '../data/chase_cc.csv'
    path_wf1 = '../data/cc1028.csv'
    path_wf2 = '../data/checking1028.csv'

    df_all = clean_read(path_all,'all')
    df_chase = clean_read(path_chase,'chase')
    df_wf1 = clean_read(path_wf1,'wf')
    df_wf2 = clean_read(path_wf2,'wf')

    dfs = [df_chase,df_wf1,df_wf2]
    df_unlabeled = pd.concat(dfs)

    df_all.to_csv('../data/labelled_clean.csv',index=False)
    df_unlabeled.to_csv('../data/unlabelled_clean.csv',index=False)
