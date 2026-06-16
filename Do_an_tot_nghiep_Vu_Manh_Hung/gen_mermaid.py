import base64
import zlib
import urllib.request

fsm_mermaid = '''stateDiagram-v2
    [*] --> STATE_INIT : Bật nguồn
    STATE_INIT --> STATE_CONNECTING : Khởi tạo phần cứng xong
    
    STATE_CONNECTING --> STATE_NORMAL : Kết nối WiFi/4G & MQTT OK
    STATE_CONNECTING --> STATE_ERROR : Lỗi mạng / Timeout
    
    STATE_NORMAL --> STATE_STREAMING : Lệnh START_STREAM
    STATE_STREAMING --> STATE_NORMAL : Lệnh STOP_STREAM
    
    STATE_NORMAL --> STATE_OTA : Lệnh cấu hình OTA
    STATE_NORMAL --> STATE_ERROR : Lỗi I2C / Cảm biến
    
    STATE_ERROR --> STATE_INIT : Tự động Reset
'''

compressed = zlib.compress(fsm_mermaid.encode('utf-8'), 9)
b64 = base64.urlsafe_b64encode(compressed).decode('utf-8')
url = f'https://kroki.io/mermaid/png/{b64}'
out_path = r'd:\datn\report\Do_an_tot_nghiep_Vu_Manh_Hung\Hinhve\fsm.png'

print(f"Downloading fsm.png...")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response, open(out_path, 'wb') as out_file:
    out_file.write(response.read())
print(f'Saved fsm.png')
