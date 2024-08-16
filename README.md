# Vehicle Insurance Claim - Fraud Detection
**Abstrak:**
Penelitian ini bertujuan untuk mengembangkan model pembelajaran mesin yang dapat mendeteksi penipuan pada klaim asuransi kendaraan. Dataset yang digunakan dalam penelitian ini merupakan dataset klaim asuransi kendaraan, yang secara khusus diproses untuk tujuan ini. Tantangan utama dalam pengembangan model ini adalah ketidakseimbangan data, di mana klaim yang sah jauh lebih banyak dibandingkan klaim yang diduga penipuan.

**Metodologi:**
Penelitian ini dimulai dengan tahap pra-pemrosesan data, yang melibatkan seleksi fitur menggunakan teknik berbasis fitur untuk memastikan hanya fitur-fitur yang relevan yang digunakan dalam proses pemodelan. Untuk mengatasi masalah ketidakseimbangan data, metode SMOTE (Synthetic Minority Over-sampling Technique) diterapkan, yang memungkinkan peningkatan representasi sampel minoritas dalam data pelatihan.
Selanjutnya, berbagai algoritma pembelajaran mesin dikomparasikan untuk menentukan model yang paling efektif dalam mendeteksi penipuan. Algoritma yang diuji meliputi Logistic Regression, Gradient Boosting, XGBoost, K-Nearest Neighbors (KNN), AdaBoost, dan Naive Bayes. Dari hasil komparasi, XGBoost menunjukkan performa terbaik dengan tingkat akurasi sebesar 84%.

**Hasil dan Implementasi:**
Model XGBoost yang terpilih kemudian diimplementasikan dalam aplikasi berbasis web menggunakan Streamlit. Aplikasi ini memungkinkan pengguna untuk melakukan deteksi penipuan klaim asuransi kendaraan secara cepat dan akurat, dengan antarmuka yang mudah digunakan.

**Kesimpulan:**
Penelitian ini membuktikan bahwa XGBoost merupakan model yang efektif dalam mendeteksi penipuan pada klaim asuransi kendaraan, terutama setelah dilakukan seleksi fitur dan penyeimbangan data. Implementasi model ini dalam aplikasi web memberikan kontribusi signifikan dalam upaya meningkatkan efisiensi dan akurasi dalam proses verifikasi klaim asuransi.

## 🖥️ Streamlit Deployment

[Try Here](https://fraud-detection---vehicle-insurance-claim-jajzvgcuuepuvlytceat.streamlit.app/)

## 📷 Screenshot
![Streamlit Screenshoot](/Screenshot_Streamlit app.jpg)

## ✨ Authors

|         Name         |        
| -------------------- | 
| Duta Firdaus Wicaksono |

Digital Talent Scholarship - Fresh Graduate Academy - Big Data using Python
