# 使用 python:3.10.12-slim-buster 作為基礎映像
FROM python:3.10.12-slim-buster

# 設置工作目錄
WORKDIR /grabbing_django

COPY requirements.txt .

# 安裝所需的包
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install

# 安裝必要的系統庫
RUN apt-get update 
RUN apt-get install -y libgl1-mesa-glx
RUN apt-get install -y libglib2.0-0

# 複製當前目錄內容到容器中的工作目錄
COPY . .

EXPOSE 8000

CMD gunicorn --workers=3 --bind 0.0.0.0:8000 grabbing_django.wsgi:application
