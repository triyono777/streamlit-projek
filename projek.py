# Impor library yang diperlukan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Buat dataset palsu sebagai contoh
data = {
    'Tanggal': pd.date_range(start='2023-01-01', end='2023-12-31', freq='D'),
    'Produk': np.random.choice(['Produk A', 'Produk B', 'Produk C'], size=365),
    'Harga': np.random.randint(10, 100, size=365),
    'Jumlah': np.random.randint(1, 10, size=365),
}
df = pd.DataFrame(data)

# Pemrosesan data
# Hitung total penjualan harian
daily_sales = df.groupby('Tanggal')['Harga'].sum()

# Identifikasi produk terlaris
best_selling_product = df.groupby('Produk')['Jumlah'].sum().idxmax()

# Visualisasi data
plt.figure(figsize=(12, 6))
plt.plot(daily_sales.index, daily_sales.values, label='Total Penjualan Harian', marker='o')
plt.title('Grafik Penjualan Harian')
plt.xlabel('Tanggal')
plt.ylabel('Total Penjualan')
plt.legend()

# Tampilkan produk terlaris
print(f'Produk terlaris: {best_selling_product}')

# Tampilkan profil pelanggan (contoh usia)
customer_profile = df.groupby('Produk')['Harga'].mean()
print('Profil Pelanggan (Rata-rata Harga):')
print(customer_profile)

# Tampilkan grafik produk terlaris
plt.figure(figsize=(8, 8))
product_sales = df[df['Produk'] == best_selling_product]
plt.pie(product_sales['Jumlah'].sum(), labels=[best_selling_product, 'Lainnya'], autopct='%1.1f%%')
plt.title(f'Penjualan Produk Terlaris: {best_selling_product}')
plt.show()
