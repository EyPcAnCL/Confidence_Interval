import numpy as np
import pandas as pd
from scipy import stats

# Her çalıştırmada farklı veri!
n = np.random.randint(30, 100)                    # Örneklem büyüklüğü
veriler = pd.Series(np.random.randint(1, 100, size=n))
guven_duzeyi = np.random.choice([0.90, 0.95, 0.99])  # Güven düzeyi

# Hesaplamalar
ort = veriler.mean()
std = veriler.std()
se  = std / np.sqrt(n)                            # Standart Hata

# Güven Aralığı
alt, ust = stats.t.interval(
    confidence=guven_duzeyi,
    df=n-1,          # Serbestlik derecesi
    loc=ort,
    scale=se
)

print("=" * 48)
print("📌 GÜVEN ARALIĞI (Confidence Interval)")
print("=" * 48)
print(f"Örneklem Büyüklüğü (n)   : {n}")
print(f"Örneklem Ortalaması      : {ort:.2f}")
print(f"Standart Sapma           : {std:.2f}")
print(f"Standart Hata (SE)       : {se:.2f}")
print(f"Güven Düzeyi             : %{int(guven_duzeyi * 100)}")
print("-" * 48)
print(f"Alt Sınır                : {alt:.2f}")
print(f"Üst Sınır                : {ust:.2f}")
print("-" * 48)
print(f"✅ Gerçek ortalama %{int(guven_duzeyi*100)} ihtimalle")
print(f"   {alt:.2f} ile {ust:.2f} arasındadır!")
print("=" * 48)
