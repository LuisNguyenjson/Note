import json
import os

FILE_NAME = "data.json"

# ---------------------------
# LOAD & SAVE DATA
# ---------------------------
def load_data():
    if not os.path.exists(FILE_NAME):
        return {
            "schedule": {},
            "notes": []
        }
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# ---------------------------
# SCHEDULE FUNCTIONS
# ---------------------------
def show_schedule(data):
    if not data["schedule"]:
        print("📭 Chưa có thời khóa biểu")
        return

    print("\n📅 THỜI KHÓA BIỂU")
    for day, subjects in data["schedule"].items():
        print(f"{day}: {', '.join(subjects)}")


def add_subject(data):
    day = input("Nhập ngày (VD: Thứ 2): ")
    subject = input("Nhập tên môn học: ")

    if day not in data["schedule"]:
        data["schedule"][day] = []

    data["schedule"][day].append(subject)
    print("✅ Đã thêm môn học")


def edit_subject(data):
    day = input("Nhập ngày cần sửa: ")

    if day not in data["schedule"]:
        print("❌ Không tồn tại ngày này")
        return

    subjects = data["schedule"][day]
    for i, sub in enumerate(subjects):
        print(f"{i + 1}. {sub}")

    index = int(input("Chọn môn cần sửa: ")) - 1
    new_subject = input("Nhập tên môn mới: ")

    subjects[index] = new_subject
    print("✏️ Đã sửa môn học")


def delete_subject(data):
    day = input("Nhập ngày cần xóa môn: ")

    if day not in data["schedule"]:
        print("❌ Không tồn tại ngày này")
        return

    subjects = data["schedule"][day]
    for i, sub in enumerate(subjects):
        print(f"{i + 1}. {sub}")

    index = int(input("Chọn môn cần xóa: ")) - 1
    subjects.pop(index)

    if not subjects:
        del data["schedule"][day]

    print("🗑️ Đã xóa môn học")


# ---------------------------
# NOTE FUNCTIONS
# ---------------------------
def show_notes(data):
    if not data["notes"]:
        print("📭 Chưa có ghi chú")
        return

    print("\n📝 DANH SÁCH GHI CHÚ")
    for i, note in enumerate(data["notes"]):
        print(f"{i + 1}. {note}")


def add_note(data):
    note = input("Nhập nội dung ghi chú: ")
    data["notes"].append(note)
    print("✅ Đã thêm ghi chú")


def edit_note(data):
    show_notes(data)
    index = int(input("Chọn ghi chú cần sửa: ")) - 1
    new_note = input("Nhập nội dung mới: ")
    data["notes"][index] = new_note
    print("✏️ Đã sửa ghi chú")


def delete_note(data):
    show_notes(data)
    index = int(input("Chọn ghi chú cần xóa: ")) - 1
    data["notes"].pop(index)
    print("🗑️ Đã xóa ghi chú")


# ---------------------------
# MENU
# ---------------------------
def main_menu():
    print("""
======== NOTE & THỜI KHÓA BIỂU ========
1. Xem thời khóa biểu
2. Thêm môn học
3. Sửa môn học
4. Xóa môn học
--------------------------------------
5. Xem ghi chú
6. Thêm ghi chú
7. Sửa ghi chú
8. Xóa ghi chú
--------------------------------------
0. Thoát
""")


def main():
    data = load_data()

    while True:
        main_menu()
        choice = input("Chọn chức năng: ")

        if choice == "1":
            show_schedule(data)
        elif choice == "2":
            add_subject(data)
        elif choice == "3":
            edit_subject(data)
        elif choice == "4":
            delete_subject(data)
        elif choice == "5":
            show_notes(data)
        elif choice == "6":
            add_note(data)
        elif choice == "7":
            edit_note(data)
        elif choice == "8":
            delete_note(data)
        elif choice == "0":
            save_data(data)
            print("👋 Tạm biệt!")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")

        save_data(data)


# ---------------------------
# RUN
# ---------------------------
main()
