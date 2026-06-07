import pandas as pd
from sklearn.preprocessing import StandardScaler
from pathlib import Path

# ==========================================
# 1. 動態路徑解析 (核心關鍵)
# ==========================================
# __file__ 代表這個腳本自己 (src/cleaning.py)
# .resolve() 取得絕對路徑
# .parent 往上一層推。推一次到 src/，推兩次就到了專案根目錄！
BASE_DIR = Path(__file__).resolve().parent.parent

# 利用 / 符號直接拼接路徑，它會自動處理 Windows(\) 和 Mac/Linux(/) 的斜線差異
file_path = BASE_DIR / 'data' / 'raw' / 'global_climate_events_economic_impact_2020_2025.csv'
output_path = BASE_DIR / 'data' / 'processed' / 'global_climate_events_economic_impact_2020_2025_processed.csv'
output_path_standardized = BASE_DIR / 'data' / 'standardized' / 'global_climate_events_economic_impact_2020_2025_standardized.csv'

# ==========================================
# 2. 執行資料清洗流程
# ==========================================
def clean_data():
    print(f"準備讀取檔案: {file_path}")
    
    # 檢查原始檔案是否存在
    if not file_path.exists():
        raise FileNotFoundError(f"找不到檔案，請確認 CSV 是否已放入: {file_path}")

    # 讀取資料
    df = pd.read_csv(file_path)
    print("\n原始資料維度:", df.shape)

    # 處理缺失值
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    cat_cols = df.select_dtypes(include=['object']).columns
    #數值型用中位數填補，類別型用眾數填補
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    for col in cat_cols:
        if df[col].isnull().sum() > 0:
            df[col] = df[col].fillna(df[col].mode()[0])

    # 確保 processed 資料夾存在，若沒有則自動建立
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 匯出資料
    df.to_csv(output_path, index=False)
    print(f"\n 資料清洗完成！已儲存至: {output_path}")

    # 標準化
    scaler = StandardScaler()
    df[num_cols] = scaler.fit_transform(df[num_cols])

    # 確保 standardized 資料夾存在，若沒有則自動建立
    output_path_standardized.parent.mkdir(parents=True, exist_ok=True)
    
    # 再次儲存標準化後的資料
    df.to_csv(output_path_standardized, index=False)
    print(f"\n資料標準化完成！已儲存至: {output_path_standardized}")

# 當這個腳本被直接執行時，觸發清洗流程
if __name__ == "__main__":
    clean_data()