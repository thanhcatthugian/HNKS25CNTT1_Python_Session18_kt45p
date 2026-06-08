products = [
    {'id': 'P01', 'name': 'Coca Cola', 'price': 15000},
    {'id': 'P02', 'name': 'Bánh mì', 'price': 20000}
]

def show_products(products_list):
    print("--- DANH SÁCH SẢN PHẨM ---\n"
          "ID       | Tên sản phẩm      | Giá bán\n"
          "--------------------------------------\n"
          )
    for i in products_list:
        print(f"{i["id"]}       | {i["name"]}      | {i["price"]}")
    print("--------------------------------------\n")


def add_product(products_list):
    print("--- THÊM SẢN PHẨM MỚI ---")
    while True:
        found = False
        new_id = input("Nhập id sản phẩm: ").strip().upper()
        if new_id == "":
            print("Không được để trống id sản phẩm")
        else:
            for i in products_list:
                if new_id == i["id"]:
                    found = True
                    print("Id sản phẩm đã tồn tại")
            if not found:
                break
    while True:
        new_name = input("Nhập tên sản phẩm: ").strip().title()
        if new_name == "":
            print("Không được đẻ trống tên sản phẩm")
        else:
            break
    while True:
        new_price = input("Nhập giá sản phẩm: ").strip()
        if new_price == "":
            print("Không được để trống giá sản phẩm")
        elif not new_price.isdigit():
            print("Giá sản phẩm cần là một só lớn hơn 0")
        else:
            price = float(new_price)
            if price <= 0:
                print("Giá sản phẩm cần là một só lớn hơn 0")
            else:
                break
    products_list.append({'id': new_id, 'name': new_name, 'price': price})
    print("Thêm sản phẩm thành công!")

def update_price(products_list):
    print("--- CẬP NHẬT GIÁ SẢN PHẨM ---")
    while True:
        found = False
        new_id = input("Nhập id sản phẩm: ").strip().upper()
        if new_id == "":
            print("Không được để trống id sản phẩm")
        else:
            for i in products_list:
                if new_id == i["id"]:
                    found = True
                    print(f"Tìm thấy sản phẩm: {i["name"]} (Giá hiện tại: {i["price"]})")
                    while True:
                        new_price = input("Nhập giá sản phẩm: ").strip()
                        if new_price == "":
                            print("Không được để trống giá sản phẩm")
                        elif not new_price.isdigit():
                            print("Giá sản phẩm cần là một só lớn hơn 0")
                        else:
                            price = float(new_price)
                            if price <= 0:
                                print("Giá sản phẩm cần là một só lớn hơn 0")
                            else:
                                i["price"] = price
                                break
            if not found:
                print(f"Không tìm thấy sản phẩm có mã {new_id}!")
            else:
                print("Cập nhật giá thành công!")
                break

while True:
    check_decision = input("=========================================\n"
                           "        QUẢN LÍ CỦA HÀNG - MINI STORE    \n"
                           "=========================================\n"
                           "1. Xem danh sách sản phẩm hiện có\n"
                           "2. Thêm mới một sản phẩm \n"
                           "3. Cập nhật giá sản phẩm theo id\n"
                           "4. Thoát chương trình \n"
                           "=========================================\n"
                           "Mời bạn chọn chức năng (1-4): "
                           ).strip()
    if check_decision == "":
        print("Lựa chọn không hợp lệ, chọn lại 1- 4")
    elif not check_decision.isdigit():
        print("Lựa chọn không hợp lệ, chọn lại 1- 4")
    else:
        decision = int(check_decision)
        match decision:
            case 1:
                if len(products)<=0:
                    print("Cửa hàng hiện chưa có sản phẩm nào!")
                else:
                    show_products(products)
            case 2:
                add_product(products)
            case 3:
                update_price(products)
            case 4:
                print("Cảm ơn bạn đã sử dụng phần mềm!\n"
                      "[Chương trình kết thúc]"
                      )
                break
            case _:
                print("Lựa chọn không hợp lệ, chọn lại 1- 4")