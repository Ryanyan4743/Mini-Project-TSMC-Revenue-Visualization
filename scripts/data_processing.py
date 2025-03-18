import pandas as pd
import matplotlib.pyplot as plt
import os

def process_data():
    #env\Scripts\activate
    
    #找路徑並讀檔
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # scripts的上層,專案目錄
    file_path = os.path.join(base_dir, 'data', 'raw', 'data.xlsx')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"找不到檔案: {file_path}")
    
    df = pd.read_excel(file_path, sheet_name='Annual (IS)', header=None)

    #找年份那列
    year_row_index = None
    for idx, row in df.iterrows():
        year_count = sum(1 for cell in row if str(cell).isdigit() and 2000 <= int(cell) <= 2100)
        if year_count >= 4:
            year_row_index = idx
            break

    #設定正確的標題（年份）
    df.columns = df.iloc[year_row_index]
    df = df.iloc[year_row_index + 1:].reset_index(drop=True)

    #找Net Revenue那行
    revenue_row = df[df.iloc[:, 0].str.contains("Net Revenue", case=False, na=False)].squeeze()

    #整理年份和營收數據
    years = [col for col in df.columns[1:] if str(col).isdigit()]
    revenue = [revenue_row[year] for year in years]

    #設定中文顯示
    plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"]
    plt.rcParams["axes.unicode_minus"] = False

    #繪圖
    plt.figure(figsize=(12, 6))
    plt.plot(years, revenue, marker="o", linestyle="-", color="b", label="營收")

    #標註每個點的數字
    for x, y in zip(years, revenue):
        plt.text(x, y, f'{y:,}', fontsize=8, ha='center', va='bottom')

    #設定標題與標籤
    plt.title("台積電營收趨勢", fontsize=16)
    plt.xlabel("年份", fontsize=12)
    plt.ylabel("營收 (新台幣百萬元)", fontsize=12)

    #微調圖例與網格
    plt.legend(loc='upper left', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)

    #顯示圖表
    plt.show()

