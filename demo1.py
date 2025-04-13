import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
# Đọc dữ liệu từ file Excel
df = pd.read_excel("D:/du_lieu_cong_suat_chi_phi_dien.xlsx")
print(df)

# Đổi tên cột cho dễ thao tác
df.columns = ['cong_suat', 'chi_phi_dien']

# Chuẩn bị dữ liệu
X = df[['cong_suat']].values  # Đầu vào (2D)
y = df['chi_phi_dien'].values  # Đầu ra
# Tạo mô hình hồi quy tuyến tính và huấn luyện
model = LinearRegression()
model.fit(X, y)

# Lấy hệ số hồi quy
slope = model.coef_[0]
intercept = model.intercept_

print(f"Hàm hồi quy: chi_phi_dien = {slope:.2f} * cong_suat + {intercept:.2f}")

# Vẽ biểu đồ
X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_pred = model.predict(X_range)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Dữ liệu thực tế')
plt.plot(X_range, y_pred, color='red', label='Đường hồi quy')
plt.xlabel('Công suất (kW)')
plt.ylabel('Chi phí điện')
plt.title('Hồi quy tuyến tính giữa Công suất và Chi phí điện')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()