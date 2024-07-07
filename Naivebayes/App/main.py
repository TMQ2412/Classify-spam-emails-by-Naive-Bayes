import tkinter as tk
from algorithms import ALGORITHMS


def hide_widgets(widget_list):
    for widget in widget_list:
        widget.grid_remove()


def show_widgets(widget_list):
    for widget in widget_list:
        widget.grid()


if __name__ == "__main__":
    variables = {}

    def create_input_fields(content, active_algorithm):
        # Ẩn các widget hiện tại thay vì hủy bỏ chúng
        hide_widgets(content.winfo_children())

        if not active_algorithm:
            return None
        if active_algorithm == "Naive Bayes":
            variables.update({
                # TODO: Thêm các đặc trưng giải thuật vào đây
                "Email cần phân loại:" : tk.StringVar()
            })
            
            row = 0
            for name, variable in variables.items():
                label = tk.Label(content, text=name)
                label.grid(row=row, column=0, pady=10)

                entry = tk.Entry(content, textvariable=variable)
                entry.grid(row=row, column=1, pady=10, ipadx=500, ipady= 100)
                row += 1
            button = tk.Button(content, text="Kiểm tra",
                               command=lambda: run_algorithm(content, active_algorithm, variables))
            button.grid(row=row, column=0, columnspan=10, pady=10)

    def run_algorithm(content, active_algorithm, variables):
        if active_algorithm == "Naive Bayes":
            from algorithms.naive_bayes import main
            spam_dat = variables["Email cần phân loại:"].get()
            # TODO: hàm main của giải thuật trả về kết quả để hiển thị
            result = main(email=spam_dat)
            label = tk.Label(content, text="Kết quả: {}".format(result))
            label.grid(row=len(variables) + 2, column=0, columnspan=2, pady=10)
    root = tk.Tk()
    active_algorithm = tk.StringVar()
    root.title("Ứng dụng lọc email spam")
    # Căn giữa màn hình
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int((screen_width / 2) - (800 / 2))
    y = int((screen_height / 2) - (600 / 2))
    root.geometry("800x600+{}+{}".format(x, y))

    # Tạo Sidebar
    sidebar = tk.Frame(root, bg="#6272a4", width=300, height=600)
    sidebar.pack(side="left", fill="y")

    for name, algorithm in ALGORITHMS.items():
        button = tk.Button(sidebar, text=name,
                           command=lambda n=name, a=algorithm: create_input_fields(content, n))
        button.config(width=20, height=2)
        button.pack(pady=10, fill="x")

    # Tạo ContentWindow
    content = tk.Frame(root, width=500, height=600)
    content.pack(side="right", fill="both", expand=True)
    root.mainloop()