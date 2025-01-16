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
git clone https://github.com/long0901/G-Scores.git
```

### 2. Tạo và kích hoạt môi trường ảo
Tạo một môi trường ảo để quản lý các gói phụ thuộc:

```bash
python -m venv venv

venv\Scripts\activate
cd G-Scores
cd g_score
```
### 3. Cài đặt các phụ thuộc cần thiết
```bash
pip install -r requirements.txt
```

### 4. Thực hiện các migrations
Chạy lệnh sau để tạo các bảng trong cơ sở dữ liệu:
```bash
python manage.py migrate
```
### 5. Chạy máy chủ phát triển và truy cập localhost
```bash
python manage.py runserver 
```

## Một số hình ảnh về project

Dashboard
![image](https://github.com/user-attachments/assets/1b7c155b-5878-44c1-930d-bcf028246e3b)

Check your scores: Nhập một sbd trong dataset để tra cứu điểm 
![image](https://github.com/user-attachments/assets/9c2bffa5-e997-4cff-8a72-a8058b3800c1)

Score Distribution by Subject: Thống kê số học sinh đạt điểm ở 4 cấp độ theo môn học.
![image](https://github.com/user-attachments/assets/d5692882-8867-4a75-9ad9-27152f96491c)

Top 10 students: Danh sách 10 học sinh đứng đầu khối A gồm (toán, vật lý, hóa học)
![image](https://github.com/user-attachments/assets/938c01c3-f8bc-45e5-9fe6-d5eb3af8070d)



