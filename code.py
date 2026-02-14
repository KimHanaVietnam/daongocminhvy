import json
import os
os.makedirs("data", exist_ok=True)
#books
books = {
    "books": [
        {"id": "B01",
         "title": "Miền Nam trong trái tim Hồ Chí Minh",
         "author": "Trần Văn Giàu",
         "category": "Lịch sử",
         "code": "MS1001",
         "total_quantity": 10,
         "available_quantity": 2,
         "image": "images/books/b01.jpg",
         "rate": 4.4},
        {"id": "B02",
        "title": "Tổng hành dinh trong mùa xuân toàn thắng",
        "author": "Đại tướng Võ Nguyên Giáp",
        "category": "Lịch sử",
        "code": "MS1002",
        "total_quantity": 3,
        "available_quantity": 0,
        "image": "images/books/b02.jpg",
        "rate": 5.0},
        {"id": "B03",
        "title": "Kỹ năng vận dụng pháp luật lao động tại doanh nghiệp",
        "author": "Nguyễn Thị Hồng",
        "category": "Pháp luật",
        "code": "MS1003",
        "total_quantity": 7,
        "available_quantity": 1,
        "image": "images/books/b03.jpg",
        "rate": 4.2},
        {"id": "B04",
        "title": "Nguyễn An Ninh: ”Không ăn mày tự do”",
        "author": "Trần Viết Nghĩa",
        "category": "Chính luận",
        "code": "MS1004",
        "total_quantity": 5,
        "available_quantity": 5,
        "image": "images/books/b04.jpg",
        "rate": 4.8},
        {"id": "B05",
        "title": "Ngôi làng cổ mộ",
        "author": "Thục Linh",
        "category": "Văn học",
        "code": "MS1005",
        "total_quantity": 1,
        "available_quantity": 1,
        "image": "images/books/b05.jpg",
        "rate": 3.7},
        {"id": "B06",
        "title": "Giáo trình cơ sở thiết kế vi mạch",
        "author": "Hoàng Trang",
        "category": "Công nghệ",
        "code": "MS1006",
        "total_quantity": 7,
        "available_quantity": 3,
        "image": "images/books/b06.jpg",
        "rate": 3.9}
    ]
}
with open('data/books.json','w',encoding='utf-8') as file:
    json.dump(books, file, ensure_ascii=False, indent=4)

#borrow_record
borrow_record = {
    "borrow_record": [
        {"id": "BR01",
        "student_id": "DG01",
        "book_id": "B04",
        "borrow_date": "08/02/2026",
        "due_date": "31/03/2026",
        "status":"borrowing"},
        {"id": "BR02",
        "student_id": "DG03",
        "book_id": "CB02",
        "borrow_date": "23/12/2025",
        "due_date": "09/01/2026",
        "status":"overdue"},
        {"id": "BR03",
        "student_id": "DG01",
        "book_id": "CB04",
        "borrow_date": "15/01/2026",
        "due_date": "15/02/2026",
        "status":"returned"},
        {"id": "BR04",
        "student_id": "DG02",
        "book_id": "B04",
        "borrow_date": "29/01/2026",
        "due_date": "11/02/2026",
        "status":"returned"}
    ]
}
with open('data/borrow_record.json','w',encoding='utf-8') as file:
    json.dump(borrow_record, file, ensure_ascii=False, indent=4)

#community_books
community_books = {
    "community_books": [
        {"id": "CB01",
        "title": "Bear town 2 - Chúng tôi đối đầu với các bạn",
        "author": "Fredrik Backman",
        "owner": "DG01",
        "category": "Văn học",
        "status": "available",
        "image": "images/community_books/cb01.jpg"},
        {"id": "CB02",
        "title": "Cuộc đấu trí ở tầm cao của trí tuệ Việt Nam",
        "author": "Trần Nhâm",
        "owner": "DG03",
        "category": "Lịch sử",
        "status": "borrowed",
        "image": "images/community_books/cb02.jpg"},
        {"id": "CB03",
        "title": "50 ý tưởng lớn bạn thực sự cần biết",
        "author": "Ben Dupré",
        "owner": "ADMIN",
        "category": "Khoa học",
        "status": "requested",
        "image": "images/community_books/cb03.jpg"},
        {"id": "CB04",
        "title": "Kinh tế học vi mô",
        "author": "N Gregory Mankiw",
        "owner": "ADMIN",
        "category": "Kinh tế",
        "status": "available",
        "image": "images/community_books/cb04.jpg"}
    ]
}
with open('data/community_books.json','w',encoding='utf-8') as file:
    json.dump(community_books, file, ensure_ascii=False, indent=4)

#requests
requests = {
    "requests": [
        {"id": "R01",
        "student_id": "DG01",
        "book_id": "CB02",
        "time": "19:35 08/02/2026",
        "status": "pending"},
        {"id": "R02",
        "student_id": "DG03",
        "book_id": "B02",
        "time": "10:04 08/02/2026",
        "status": "rejected"},
        {"id": "R03",
        "student_id": "DG01",
        "book_id": "CB04",
        "time": "05:36 08/02/2026",
        "status": "approved"},
        {"id": "R04",
        "student_id": "DG04",
        "book_id": "B02",
        "time": "18:59 08/02/2026",
        "status": "pending"}
    ]
}
with open('data/requests.json','w',encoding='utf-8') as file:
    json.dump(requests, file, ensure_ascii=False, indent=4)

#students
students = {
    "students": [
        {"id": "DG01",
        "name": "Đào Ngọc Minh Vy",
        "email": "vydao@uel.edu.vn",
        "mssv": "K254060738",
        "major": "Hệ thống thông tin quản lý",
        "join_date":"10/02/2026",
        "status": "active"},
        {"id": "DG02",
        "name": "Trần Võ Thu Trang",
        "email": "trangtran@uel.edu.vn",
        "mssv": "K254060730",
        "major": "Luật kinh tế",
        "join_date": "15/09/2025",
        "status": "inactive"},
        {"id": "DG03",
        "name": "Đặng Phương Vy",
        "email": "vydang@uel.edu.vn",
        "mssv": "K254060739",
        "major": "Hệ thống thông tin quản lý",
        "join_date": "08/01/2026",
        "status": "active"},
        {"id": "DG04",
        "name": "Lê Đình Quý Phương",
        "email": "phuongle@uel.edu.vn",
        "mssv": "K254060720",
        "major": "Kinh tế đối ngoại",
        "join_date": "13/10/2025",
        "status": "active"},
        {"id": "DG05",
        "name": "Trịnh Lê Tú",
        "email": "tutrinh@uel.edu.vn",
        "mssv": "K24409123",
        "major": "Kiểm toán",
        "join_date": "09/12/2024",
        "status": "active"}
    ]
}
with open('data/students.json','w',encoding='utf-8') as file:
    json.dump(students, file, ensure_ascii=False, indent=4)

#users
users = {
    "users": [
        {"id": "DG01",
        "emal": "vydao@uel.edu.vn",
        "password": "vydao1234",
        "name": "Đào Ngọc Minh Vy",
        "role": "student",
        "status": "active"},
        {"id": "DG02",
        "email": "trangtran@uel.edu.vn",
        "password": "tranghihi_",
        "name": "Trần Võ Thu Trang",
        "role": "student",
        "status": "inactive"},
        {"id": "DG03",
        "email": "vydang@uel.edu.vn",
        "password": "PHUONGVY8386",
        "name": "Đặng Phương Vy",
        "role": "student",
        "status": "active"},
        {"id": "DG04",
        "email": "phuongle@uel.edu.vn",
        "password": "071013@",
        "name": "Lê Đình Quý Phương",
        "role": "student",
        "status": "active"},
        {"id": "DG05",
        "email": "tutrinh@uel.edu.vn",
        "password": "244466666",
        "name": "Trịnh Lê Tú",
        "role": "student",
        "status": "active"},
        {"id": "ADMIN",
        "email": "admin.uel@gmail.com",
        "password": "k25406",
        "name": "AD",
        "role": "admin",
        "status": "active"}
    ]
}
with open('data/users.json','w',encoding='utf-8') as file:
    json.dump(users, file, ensure_ascii=False, indent=4)