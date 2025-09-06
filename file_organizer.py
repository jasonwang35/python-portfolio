import os
import shutil
from pathlib import Path

# 想整理的資料夾（預設用桌面上的 "to_sort" 資料夾）
base = Path.home() / "Desktop" / "to_sort"
base.mkdir(exist_ok=True)  # 如果沒有就建立

# 可自行增減副檔名
RULES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".heic"],
    "Docs":   [".pdf", ".docx", ".doc", ".txt", ".md", ".rtf"],
    "Sheets": [".xlsx", ".xls", ".csv"],
    "Media":  [".mp3", ".wav", ".mp4", ".mov", ".m4v"],
    "Zips":   [".zip", ".rar", ".7z"],
}

def categorize(path: Path) -> str:
    ext = path.suffix.lower()
    for folder, exts in RULES.items():
        if ext in exts:
            return folder
    return "Others"

def organize(folder: Path):
    moved = 0
    for item in folder.iterdir():
        if item.is_file():
            dest_folder = folder / categorize(item)
            dest_folder.mkdir(exist_ok=True)
            shutil.move(str(item), dest_folder / item.name)
            moved += 1
    return moved

if __name__ == "__main__":
    print(f"Sorting folder: {base}")
    count = organize(base)
    print(f"Done. Moved {count} files.")
