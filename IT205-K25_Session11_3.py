# 1. PHÂN TÍCH INPUT/OUTPUT
# Input:
# - Lựa chọn menu: Chuỗi ký tự (str)
# - Mã sản phẩm: Chuỗi ký tự (str)
# - Tên sản phẩm: Chuỗi ký tự (str)
# - Giá bán, Số lượng: Chuỗi ký tự (str), sau đó ép kiểu sang số nguyên (int)
# Output:
# - Danh sách sản phẩm định dạng chuỗi hoặc thông báo trống
# - Các thông báo thành công hoặc thông báo lỗi tương ứng với từng bẫy dữ liệu
#
# 2. ĐỀ XUẤT GIẢI PHÁP
# - Quản lý luồng: Dùng vòng lặp 'while True' để hiển thị menu liên tục
# - Chuẩn hóa chuỗi: Dùng phương thức '.strip().upper()' xử lý khoảng trắng và chữ hoa
# - Kiểm tra số hợp lệ: Dùng '.isdigit()' kết hợp ép kiểu 'int()' để đảm bảo giá trị > 0
# - Kiểm tra tồn tại/Trùng mã: Áp dụng vòng lặp 'for-else' tối giản của Python
#
# 1. THIẾT KẾ THUẬT TOÁN
# Bước 1: Khởi tạo danh sách 'product_list' chứa 3 sản phẩm ban đầu
# Bước 2: Vào vòng lặp menu, nhận lựa chọn từ người dùng
# Bước 3: Rẽ nhánh xử lý theo lựa chọn (1-5):
#   - Chức năng 1: Nếu danh sách rỗng thì báo trống, ngược lại dùng 'for' in ra
#   - Chức năng 2: Nhập mã -> Nếu trùng thì báo lỗi; Nhập tên, giá, số lượng -> Nếu không phải số nguyên dương (>0) thì báo lỗi; Hợp lệ thì '.append()'
#   - Chức năng 3: Nhập mã cần sửa -> Dùng 'for-else' tìm sản phẩm; Nếu thấy thì nhập thông tin mới -> Kiểm tra số hợp lệ -> Cập nhật trực tiếp vào dictionary
#   - Chức năng 4: Nhập mã cần xóa -> Dùng 'for-else' tìm sản phẩm; Nếu thấy thì '.remove()' khỏi danh sách; Không thấy thì báo lỗi
#   - Chức năng 5: In thông báo thoát và gọi lệnh 'break'
#   - Lựa chọn sai: In thông báo yêu cầu nhập lại


product_list = [
    {
        "product_id": "SP001",
        "product_name": "Áo polo nam",
        "price": 299000,
        "quantity": 20
    },
    {
        "product_id": "SP002",
        "product_name": "Quần kaki nam",
        "price": 399000,
        "quantity": 15
    },
    {
        "product_id": "SP003",
        "product_name": "Váy công sở nữ",
        "price": 459000,
        "quantity": 10
    }
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM YODY =====")
    print("1. Hiển thị danh sách sản phẩm")
    print("2. Thêm sản phẩm mới")
    print("3. Cập nhật thông tin sản phẩm")
    print("4. Xóa sản phẩm theo mã")
    print("5. Thoát chương trình")
    
    choice = input("Nhập lựa chọn (1-5): ")
    
    if choice == "1":
        if not product_list:
            print("Danh sách sản phẩm hiện đang trống.")
        else:
            print("Danh sách sản phẩm hiện tại:")
            for index, p in enumerate(product_list, start=1):
                print(f"{index}. Mã SP: {p['product_id']} | Tên: {p['product_name']} | Giá: {p['price']} | Số lượng: {p['quantity']}")
                
    elif choice == "2":
        product_id = input("Nhập mã sản phẩm: ").strip().upper()
        product_name = input("Nhập tên sản phẩm: ").strip()
        price = input("Nhập giá sản phẩm: ").strip()
        quantity = input("Nhập số lượng sản phẩm: ").strip()
        
        if not price.isdigit() or not quantity.isdigit() or int(price) <= 0 or int(quantity) <= 0:
            print("Giá/Số lượng không hợp lệ")
            continue
            
        product_list.append({
            "product_id": product_id,
            "product_name": product_name,
            "price": int(price),
            "quantity": int(quantity)
        })
        print("Thêm sản phẩm thành công")
        

    elif choice == "3":
        product_id = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        
        for i in product_list:
            if i["product_id"] == product_id:
                break
        else:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")
            continue
            
        new_name = input("Nhập tên sản phẩm mới: ").strip()
        price = input("Nhập giá sản phẩm mới: ").strip()
        quantity = input("Nhập số lượng tồn kho mới: ").strip()
        
        if not price.isdigit() or not quantity.isdigit() or int(price) <= 0 or int(quantity) <= 0:
            print("Giá/Số lượng không hợp lệ")
            continue
            
        i["product_name"] = new_name
        i["price"] = int(price)
        i["quantity"] = int(quantity)
        print("Cập nhật thông tin sản phẩm thành công")

    elif choice == "4":
        product_id = input("Nhập mã sản phẩm cần xóa: ").strip().upper()

        for i in product_list:
            if i["product_id"] == product_id:
                break
        else:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")
            continue
            
        product_list.remove(i)
        print("Xóa sản phẩm thành công")
        

    elif choice == "5":
        print("Thoát chương trình.")
        break
        
    else:
        print('Lựa chọn không hợp lệ, vui lòng nhập lại!')