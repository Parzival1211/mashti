import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_google_suggestions(keyword):
    """برای یک کلمه، پیشنهادات جستجو رو از گوگل می‌گیره."""
    url = f"https://www.google.com/complete/search?q={keyword}&cp=1&client=psy-ab"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # پارس کردن HTML و استخراج پیشنهادات
        suggestions = response.json()[1]
        return suggestions
    else:
        return []

def save_to_excel(data, filename="C:/Users/amirm/Desktop/all_suggestions.xlsx"):
    """داده‌ها رو به صورت مرتب و خوانا در فایل اکسل ذخیره می‌کنه."""
    # تبدیل داده‌ها به DataFrame pandas
    df = pd.DataFrame(data, columns=["Original Keyword", "Suggested Keyword"])

    # ذخیره کردن داده‌ها در فایل اکسل
    df.to_excel(filename,engine='openpyxl')

    print(f"✅ فایل اکسل ذخیره شد: {filename}")

def run_keyword_suggestions(keywords):
    """برای هر کلمه، پیشنهادات گوگل رو گرفته و ذخیره می‌کنه."""
    all_results = []
    
    for keyword in keywords:
        print(f"در حال استخراج پیشنهادات برای: {keyword}")
        suggestions = get_google_suggestions(keyword)
        
        for suggestion in suggestions:
            all_results.append([keyword, suggestion])
    
    # ذخیره‌سازی پیشنهادات در فایل اکسل
    save_to_excel(all_results)

# ورودی کلمات از کاربر
keywords = input("لطفاً کلمات کلیدی خود را وارد کنید (با فاصله از هم جدا کنید): ").split()

# اجرای کد برای استخراج پیشنهادات
print (1)

