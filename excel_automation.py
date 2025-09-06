import pandas as pd

# 建立兩個模擬的 Excel 表格
df1 = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Score": [85, 90]
})
df2 = pd.DataFrame({
    "Name": ["Charlie", "David"],
    "Score": [78, 88]
})

df1.to_excel("data1.xlsx", index=False)
df2.to_excel("data2.xlsx", index=False)

# 自動化流程：合併兩份資料
merged = pd.concat([df1, df2])
merged["Score"] = merged["Score"].astype(int)

# 計算平均分數
avg_score = merged["Score"].mean()

# 存成新的 Excel
merged.to_excel("merged.xlsx", index=False)

print("Excel automation complete. Average Score:", avg_score)
