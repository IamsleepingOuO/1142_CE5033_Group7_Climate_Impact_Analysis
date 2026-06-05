import numpy as np

def calculate_cohens_d(group1, group2):
    """
    計算兩組獨立樣本的 Cohen's d 效應量
    :param group1: 樣本群體 1 (array-like)
    :param group2: 樣本群體 2 (array-like)
    :return: Cohen's d 數值 (float)
    """
    n1, n2 = len(group1), len(group2)
    var1, var2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    
    # 計算合併變異數 (Pooled Variance)
    pooled_var = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)
    
    # 計算 Cohen's d
    d = (np.mean(group1) - np.mean(group2)) / np.sqrt(pooled_var)
    return d