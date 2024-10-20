import requests

# 公開的 S3 URL
url = 'https://jcardbackend.s3.amazonaws.com/topic_icon/basketball_icon.png'

# 發送 GET 請求
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    # 儲存圖片
    with open('basketball_icon.png', 'wb') as file:
        file.write(response.content)
    print("圖片下載成功！")
else:
    print("無法訪問圖片，HTTP 狀態碼:", response.status_code)