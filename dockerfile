# 使用 Ubuntu 作為基礎映像
FROM ubuntu:20.04

# 設定工作目錄
WORKDIR /app

# 更新套件並安裝 Python 和 pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip zip && \
    apt-get clean

# 複製專案文件
COPY . .

# 安裝相依套件
RUN pip3 install --no-cache-dir -r requirements.txt

# 啟動應用程式
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"] 

#相當於輸入python3 manage.py runserver 0.0.0.0:8000
