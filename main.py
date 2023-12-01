import tkinter as tk
import numpy as np

def solve_equations():
    # Lấy dữ liệu đầu vào từ các trường nhập liệu
    coefficients = []
    constants = []
    for i in range(num_equations):
        coeff_row = []
        for j in range(num_variables):
            coeff_row.append(float(entry_vars[i][j].get()))
        coefficients.append(coeff_row)
        constants.append(float(entry_consts[i].get()))

    # Tạo ma trận hệ số và vectơ hằng số từ dữ liệu đầu vào
    A = np.array(coefficients)
    b = np.array(constants)

    # Giải quyết hệ phương trình
    try:
        x = np.linalg.solve(A, b)
        result_label.config(text="Các giá trị của các ẩn:\n{}".format(x))
    except np.linalg.LinAlgError:
        result_label.config(text="Hệ phương trình không có nghiệm.")

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Giải hệ phương trình tuyến tính")
window.geometry("800x800")

# Tạo các nhãn và trường nhập liệu cho số phương trình và số ẩn
label_num_equations = tk.Label(window, text="Số phương trình:")
label_num_equations.pack()

entry_num_equations = tk.Entry(window)
entry_num_equations.pack()

label_num_variables = tk.Label(window, text="Số ẩn:")
label_num_variables.pack()

entry_num_variables = tk.Entry(window)
entry_num_variables.pack()

def create_input_fields():
    global num_equations, num_variables, entry_vars, entry_consts, solve_button, result_label

    # Lấy số phương trình và số ẩn từ trường nhập liệu
    num_equations = int(entry_num_equations.get())
    num_variables = int(entry_num_variables.get())

    # Xóa các trường nhập liệu và nút giải phương trình cũ (nếu có)
    if 'entry_vars' in globals():
        for i in range(num_equations):
            for j in range(num_variables):
                entry_vars[i][j].destroy()
        for i in range(num_equations):
            entry_consts[i].destroy()
        solve_button.destroy()
        result_label.destroy()

    # Tạo lại các trường nhập liệu và nút giải phương trình mới
    entry_vars = []
    entry_consts = []
    for i in range(num_equations):
        label_eq = tk.Label(window, text="Phương trình {}: ".format(i+1))
        label_eq.pack()
        entry_vars_row = []
        for j in range(num_variables):
            entry_var = tk.Entry(window)
            entry_var.pack()
            entry_vars_row.append(entry_var)
        entry_vars.append(entry_vars_row)
        label_const = tk.Label(window, text="Hằng số:")
        label_const.pack()
        entry_const = tk.Entry(window)
        entry_const.pack()
        entry_consts.append(entry_const)

    solve_button = tk.Button(window, text="Giải phương trình", command=solve_equations)
    solve_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()
# Tạo nút tạo các trường nhập liệu và nút giải phương trình
create_fields_button = tk.Button(window, text="Tạo trường nhập liệu", command=create_input_fields)
create_fields_button.pack()

# Chạy giao diện
window.mainloop()