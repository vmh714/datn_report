import base64
import zlib
import urllib.request
import os

mermaid_src = """erDiagram
    ORGANIZATIONS ||--o{ USERS : has
    ORGANIZATIONS ||--o{ WEARERS : manages
    ORGANIZATIONS ||--o{ DEVICES : owns
    DEVICES ||--o{ ALERTS : generates
    DEVICES ||--o{ DEVICE_EVENTS : logs
    WEARERS ||--o{ ALERTS : has
    WEARERS ||--o{ DEVICE_EVENTS : has

    USERS {
        uuid id PK
        string username
        string password_hash
        string role 
        uuid org_id FK
    }

    WEARERS {
        uuid id PK
        string full_name
        float height_cm
        uuid org_id FK
    }

    DEVICES {
        string device_id PK 
        string firmware_version
        uuid current_wearer_id FK 
        boolean is_active
        integer battery_pct 
        datetime last_online
    }
    
    ALERTS {
        uuid id PK
        string device_id FK
        uuid wearer_id FK
        string alert_type 
        float confidence
        boolean is_resolved
        datetime created_at
    }
    
    DEVICE_EVENTS {
        uuid id PK
        string device_id FK
        uuid wearer_id FK
        string event_type 
        string description 
        datetime created_at
    }
"""

compressed = zlib.compress(mermaid_src.encode('utf-8'), 9)
b64 = base64.urlsafe_b64encode(compressed).decode('utf-8')
url = f'https://kroki.io/mermaid/png/{b64}'
out_path = r'd:\datn\report\Do_an_tot_nghiep_Vu_Manh_Hung\Hinhve\erd.png'

print(f"Downloading from {url}")
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response, open(out_path, 'wb') as out_file:
    out_file.write(response.read())

print(f'Saved to {out_path}')
