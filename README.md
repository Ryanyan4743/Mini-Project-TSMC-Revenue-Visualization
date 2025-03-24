# Mini-Project: TSMC Revenue Visualization

## 專案簡介  
本專案旨在透過 Python 分析與視覺化台積電 (TSMC) 的營收趨勢，幫助使用者理解其成長變化與影響因素。

## 專案目錄結構  
```plaintext
TSMC_Revenue_Visualization/
├──  data            # 存放數據檔案
├──  reports         # 產生的報告或視覺化結果
├──  scripts         # Python 分析與視覺化程式碼
├──  .gitignore      # 忽略不必要的檔案
├──  main.py         # 主程式入口
├──  README.md       # 專案說明文件
├──  requirements.txt # 依賴套件清單
```

## 我學到的內容  
- 使用 `pandas` 進行資料處理  
- 使用 `matplotlib` 進行數據視覺化  
- `git` 的基本操作，包括 `git init`、`git add`、`git commit`、`git push`  
- 撰寫 `.gitignore` 來忽略不必要的檔案  
- 使用 `os` 來操作文件與路徑管理  

## 如何運行專案  

### 1. 安裝必要套件  
請確保已安裝 Python，然後執行以下指令安裝所需套件：  

```sh
pip install -r requirements.txt
```

### 2. 執行分析腳本  
在終端機 (Terminal) 或命令提示字元 (CMD) 中執行：  

```sh
python main.py
```

## 依賴環境  
- Python 3.x  
- pandas  
- matplotlib  
- os（Python 內建模組）  

## 未來改進方向  
- 增加更多財報數據分析，如淨利、毛利率變化  
- 加入互動式視覺化 (`Plotly` / `Dash`)  
- 自動抓取最新財報數據  

## 資料來源  
台積電官方歷史財報:
https://investor.tsmc.com/chinese/historical-information

> **備註**：本專案僅供學習用途，數據來自公開來源。
