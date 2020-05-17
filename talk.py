import json
import requests

url = "http://localhost:5005/model/parse"
data = {"text": "how many death"}
data = json.dumps(data, ensure_ascii=False)
data = data.encode(encoding="utf-8")  # 如果text带中文需要转编码
r = requests.post(url=url, data=data)
print(json.loads(r.text))