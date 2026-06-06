# 1. 使用官方 Python 3.11 精簡版作為基底
FROM python:3.11-slim

# 2. 設定容器內的工作目錄（進去後的預設資料夾）
WORKDIR /workspace

# 3. 先把 requirements.txt 複製到容器內
COPY requirements.txt .

# 4. 執行安裝！這一步會被 Docker 永久快取（Cache）下來
# 只要你的 requirements.txt 沒有改，之後 build 都不用重新下載
RUN pip install --no-cache-dir -r requirements.txt

# 5. 為了讓你像虛擬機一樣互動，我們讓它預設開啟 bash 終端機
CMD ["bash"]