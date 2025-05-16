import pandas as pd
import os

def preprocess_student_data(input_path, output_path):
    # Membaca dataset
    df = pd.read_csv(input_path)

    # Menghitung rata-rata skor dari tiga mata pelajaran
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

    # Membuat label performa berdasarkan average_score
    def classify_performance(score):
        if score >= 85:
            return 'A'
        elif score >= 75:
            return 'B'
        elif score >= 60:
            return 'C'
        elif score >= 50:
            return 'D'
        else:
            return 'E'

    df['performance_level'] = df['average_score'].apply(classify_performance)

    # One-hot encoding untuk semua fitur kategorikal
    df_encoded = pd.get_dummies(df, columns=[
        'gender',
        'race/ethnicity',
        'parental level of education',
        'lunch',
        'test preparation course'
    ])

    # Menyimpan hasil preprocessing
    df_encoded.to_csv(output_path, index=False)
    print(f"Hasil preprocessing disimpan di: {output_path}")

if __name__ == "__main__":
    # Lokasi file input dan output
    input_csv = os.path.join("..", "students_performance.csv")
    output_csv = "students_preprocessing_automated.csv"

    preprocess_student_data(input_csv, output_csv)
