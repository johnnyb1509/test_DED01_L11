# FILE: test_app.py
import pytest
from app import parse_fx_json

# Kịch bản 1: Dữ liệu chuẩn (Happy Path)
def test_parse_fx_json_valid_data():
    mock_json = {
        "base": "USD",
        "rates": {"VND": 25400.0}
    }
    result = parse_fx_json(mock_json)
    
    # Kiểm chứng
    assert result["Original_Rate"] == 25400.0
    assert result["Base"] == "USD"
    assert "Simulated_Rate" in result # Phải sinh ra được trường này

# Kịch bản 2: Dữ liệu bị thiếu Key (Lỗi thay đổi cấu trúc API)
def test_parse_fx_json_missing_key():
    # Cố tình truyền thiếu "VND" trong "rates"
    mock_json = {
        "base": "USD",
        "rates": {"EUR": 0.9} 
    }
    # Mong đợi code sẽ ném ra lỗi KeyError
    with pytest.raises(KeyError, match="thiếu Key"):
        parse_fx_json(mock_json)

# Kịch bản 3: Dữ liệu dị thường (Số âm)
def test_parse_fx_json_negative_rate():
    mock_json = {
        "base": "USD",
        "rates": {"VND": -500.0}
    }
    # Mong đợi code sẽ chặn lại bằng ValueError
    with pytest.raises(ValueError, match="số âm"):
        parse_fx_json(mock_json)