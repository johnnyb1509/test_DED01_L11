import os
import requests
import pandas as pd
import random
from datetime import datetime

# ==========================================
# 1. HÀM PURE LOGIC (DÀNH ĐỂ VIẾT UNIT TEST)
# ==========================================
def parse_fx_json(data_json):
    """
    Hàm bóc tách JSON thuần túy. 
    Chỉ nhận Input là một biến Dictionary và trả về Dictionary, không gọi mạng Internet.
    """
    # Xử lý ngoại lệ: Bắt lỗi thiếu Key
    if "rates" not in data_json or "VND" not in data_json["rates"]:
        raise KeyError("Dữ liệu JSON bị thiếu Key 'rates' hoặc 'VND'")
    
    base_rate = float(data_json["rates"]["VND"])
    
    # Xử lý ngoại lệ: Bắt lỗi số âm vô lý
    if base_rate < 0:
        raise ValueError("Lỗi Dữ Liệu: Tỷ giá không được là số âm!")
        
    fluctuation = random.uniform(-50.0, 50.0)
    simulated_rate = round(base_rate + fluctuation, 2)
    
    return {
        "Base": data_json.get("base", "USD"),
        "Original_Rate": base_rate,
        "Simulated_Rate": simulated_rate,
        "Fluctuation": round(fluctuation, 2)
    }

# ==========================================
# 2. HÀM GIAO TIẾP MẠNG (KHÔNG CẦN UNIT TEST Ở ĐÂY)
# ==========================================
def get_fx_data():
    print("Đang gọi API lấy tỷ giá...")
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    response.raise_for_status()
    raw_json = response.json()
    
    # Gọi hàm xử lý logic đã được bóc tách ở trên
    parsed_data = parse_fx_json(raw_json)
    parsed_data["Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    df = pd.DataFrame([parsed_data])
    return df