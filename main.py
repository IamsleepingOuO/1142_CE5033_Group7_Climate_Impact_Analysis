import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import joblib  # 🚨 新增：專門用來儲存與讀取機器學習模型的套件

from src.cleaning import clean_data
from src.modeling import run_random_forest_classification

def main():
    print("開始執行氣候災損預測管線...\n")
    
    # 1. 執行資料清洗
    clean_data()
    
    # 2. 讀取清洗後的資料
    BASE_DIR = Path(__file__).resolve().parent
    file_path = BASE_DIR / 'data' / 'processed' / 'global_climate_events_economic_impact_2020_2025.csv'
    df = pd.read_csv(file_path)
    
    # 3. 定義標籤與特徵
    threshold = df['economic_impact_million_usd'].quantile(0.80)
    df['is_extreme_disaster'] = (df['economic_impact_million_usd'] >= threshold).astype(int)
    
    features_to_drop = [
        'economic_impact_million_usd', 'is_extreme_disaster', 
        'injuries', 'international_aid_million_usd', 
        'aid_percentage', 'event_id', 'date'
    ]
    X = df.drop(columns=features_to_drop, errors='ignore')
    X = pd.get_dummies(X, drop_first=True)
    y = df['is_extreme_disaster']
    
    # 4. 執行模型訓練
    rf_model, feature_importances = run_random_forest_classification(X, y)
    
    # ==========================================
    # 5. 將產出物存入 output 資料夾
    # ==========================================
    print("\n=== 正在儲存專案產出物 ===")
    output_dir = BASE_DIR / 'output'
    
    # 確保資料夾存在，不存在則自動建立
    (output_dir / 'models').mkdir(parents=True, exist_ok=True)
    (output_dir / 'figures').mkdir(parents=True, exist_ok=True)

    # 儲存模型 (.pkl)
    model_path = output_dir / 'models' / 'rf_climate_model.pkl'
    joblib.dump(rf_model, model_path)
    print(f"模型已儲存至: {model_path}")

    # 儲存特徵重要性圖表 (.png)
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(10, 6))
    
    sns.barplot(
        data=feature_importances.head(10), 
        x='Importance', 
        y='Feature', 
        hue='Feature', 
        palette='viridis', 
        legend=False
    )
    plt.title('預測極端氣候災損：前十大關鍵特徵', fontsize=16)
    plt.tight_layout()
    
    # 儲存成高畫質圖片 (dpi=300)
    fig_path = output_dir / 'figures' / 'feature_importance_top10.png'
    plt.savefig(fig_path, dpi=300)
    print(f"圖表已儲存至: {fig_path}")

    print("\n執行完畢！所有產出皆已就緒。")

if __name__ == "__main__":
    main()