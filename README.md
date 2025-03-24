# Mini-Project: TSMC Revenue Visualization

## 專案簡介  

本專案利用 Python 分析與視覺化台積電 (TSMC) 的營收趨勢，幫助使用者了解其成長變化，並觀察可能影響業績的因素。例如，不同季度的營收變動是否與全球半導體市場趨勢相關？此專案提供視覺化圖表，使數據變得更直觀易讀。  

## 我學到的內容  

- **數據處理**：使用 `pandas` 讀取、清理與處理財報數據  
- **數據視覺化**：透過 `matplotlib` 繪製折線圖，展示台積電營收趨勢  
- **版本控制**：學會使用 Git 進行專案管理，包含 `git init`、`git add`、`git commit`、`git push`  
- **最佳化專案結構**：撰寫 `.gitignore` 忽略不必要的檔案，確保專案乾淨且易於維護  
- **檔案管理**：利用 `os` 操作文件與路徑  

## 如何運行專案  

### 1. 安裝必要套件  
請先確保已安裝 Python，然後執行：  

```sh
pip install pandas matplotlib
2. 執行分析腳本
在專案目錄下執行：

sh
複製
編輯
python main.py
3. 專案結構
plaintext
複製
編輯
TSMC_Revenue_Visualization/
│── data/                  # 儲存台積電歷史財報數據
    ├── raw/
│── scripts/               # Python 分析腳本
│   ├── data_processing.py   # 數據處理、分析、畫圖
│── results/               # 儲存分析結果（圖表等）
│── main.py                # 主程式，負責執行整個分析流程
│── requirements.txt       # 依賴套件
│── README.md              # 專案說明文件
│── .gitignore             # Git 忽略規則
依賴環境
Python 3.x

pandas

matplotlib

os（內建模組，無需額外安裝）

未來改進方向
擴展財報數據範圍 → 分析淨利、毛利率變化，提供更完整的財務分析

提升互動性 → 加入 Plotly 或 Dash，讓使用者能夠動態篩選數據

自動更新數據 → 透過爬蟲或 API，每季自動抓取最新財報，確保數據即時性

資料來源
數據來自 台積電官方歷史財報，本專案目前僅分析「合併財務報表」。

⚠️ 備註：
本專案僅供學習用途，數據來自公開來源，分析結果不應作為投資決策依據。
