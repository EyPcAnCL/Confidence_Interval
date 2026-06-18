## 📏 Güven Aralığı (Confidence Interval)

Bir örneklemden yola çıkarak ana kütlenin gerçek ortalamasının
hangi aralıkta olduğunu tahmin etmemizi sağlar.

**Formül:**
Güven Aralığı = x̄ ± (t × SE)  →  SE = σ / √n

**Kodda ne yaptım?**
1. Rastgele bir örneklem oluşturdum
2. Örneklemin ortalaması ve standart hatasını hesapladım
3. t dağılımı ile güven aralığını buldum
4. "Gerçek ortalama %95 ihtimalle bu aralıktadır" sonucuna vardım ✅

**Neden t dağılımı?**
Ana kütlenin standart sapmasını bilmediğimiz için t dağılımı
kullanılır. Örneklem büyüdükçe t dağılımı normale yaklaşır.

**Güven Düzeyleri:**
- %90 → Daha dar aralık, daha az emin
- %95 → En çok kullanılan ✅
- %99 → Daha geniş aralık, daha çok emin

**Kullanılan kütüphaneler:** `numpy`, `pandas`, `scipy`
