FROM python:3.11-slim

# 設定工作目錄
WORKDIR /app

# 安裝套件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 複製專案程式碼
COPY . .

# 環境變數（可選）：在容器裡用這個設定 DATABASE_URL
# 也可以改成用 docker run 的 -e 來覆蓋
ENV DATABASE_URL="mysql+mysqlconnector://shared_user:Annie5822!@host.docker.internal:3306/shared_budget"

# 對外開放的 port（文件用）
EXPOSE 8000

# 啟動 FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
