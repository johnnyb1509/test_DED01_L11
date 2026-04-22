# ------------------------------------------------------------------------------
# FILE 3: Dockerfile (Trái tim của bài học - File cấu hình Docker)
# ------------------------------------------------------------------------------
# Bước 1: Khai báo Base Image (Mượn một hệ điều hành Linux có sẵn Python 3.10 cực nhẹ)
FROM python:3.10-slim

# Bước 2: Khai báo thư mục làm việc bên trong Container
WORKDIR /app

# Bước 3: Copy file requirements từ máy tính của bạn vào trong Container
COPY requirements.txt .

# Bước 4: Chạy lệnh cài đặt thư viện bên trong Hộp
RUN pip install --no-cache-dir -r requirements.txt

# Bước 5: Copy toàn bộ code (app.py) vào trong Container
COPY app.py .

# Bước 6: Khai báo lệnh sẽ chạy khi cái Container được bật lên (Khởi động Container)
CMD ["python", "app.py"]

