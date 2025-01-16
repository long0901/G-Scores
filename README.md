# G_score

## Giới thiệu
Ứng dụng giúp tra cứu điểm thi THPT 2024, báo cáo thống kê điểm số và danh sách 10 học sinh đứng đầu khối A gồm (toán, vật lý, hóa học)

## Yêu cầu
- Python 3.8 trở lên
- Django 5.1.4
- Thư viện Pandas
- Thư viện khác được liệt kê trong `requirements.txt`

## Các bước thiết lập

### 1. Clone dự án
Sử dụng lệnh sau để clone dự án về máy tính của bạn:

```bash
git clone https://github.com/long0901/G-Scores
```

### 2. Tạo và kích hoạt môi trường ảo
Tạo một môi trường ảo để quản lý các gói phụ thuộc:

```bash
python -m venv venv

venv\Scripts\activate 
```

### 3. Thực hiện các migrations
Chạy lệnh sau để tạo các bảng trong cơ sở dữ liệu:
```bash
python manage.py migrate
```
### 4. Chạy máy chủ phát triển và truy cập localhost
```bash
python manage.py runserver 
```

## Một số hình ảnh về project
![Ảnh 1](g_score/images/image1.png)
