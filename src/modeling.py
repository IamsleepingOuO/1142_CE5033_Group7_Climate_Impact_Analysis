import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

def run_random_forest_classification(X, y, test_size=0.2, random_state=42):
    """
    執行隨機森林分類模型的完整流程，包含切分資料、訓練與成效評估。
    
    :param X: 特徵矩陣 (DataFrame)
    :param y: 目標標籤 (Series)
    :param test_size: 測試集比例
    :param random_state: 隨機種子 (確保結果可重現)
    :return: 訓練好的模型與特徵重要性
    """
    print("=== 開始訓練隨機森林分類模型 ===")
    
    # 1. 切割訓練集與測試集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    print(f"資料切割完成: 訓練集 {X_train.shape[0]} 筆, 測試集 {X_test.shape[0]} 筆")
    
    # 2. 初始化與訓練模型
    # n_estimators=100 代表使用 100 棵決策樹
    rf_model = RandomForestClassifier(n_estimators=100, random_state=random_state)
    rf_model.fit(X_train, y_train)
    print("模型訓練完成！\n")
    
    # 3. 進行預測
    y_pred = rf_model.predict(X_test)
    
    # 4. 輸出成效評估指標
    print("=== 模型評估報告 ===")
    print(f"整體準確率 (Accuracy): {accuracy_score(y_test, y_pred):.4f}\n")
    
    print("分類報告 (Classification Report):")
    print(classification_report(y_test, y_pred))
    
    # 5. 提取特徵重要性 (Feature Importance)
    feature_importances = pd.DataFrame({
        'Feature': X.columns,
        'Importance': rf_model.feature_importances_
    }).sort_values(by='Importance', ascending=False)
    
    return rf_model, feature_importances