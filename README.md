# Kişisel Görev Takip Uygulaması

Django ile yapılmış, kullanıcıların kendi görevlerini ve kategorilerini yönettiği bir web uygulaması.

## Özellikler
- Kayıt, giriş ve çıkış
- Görev ekleme, listeleme, düzenleme, silme
- Kategori oluşturma ve silme
- Görev durumu (beklemede, devam ediyor, tamamlandı, iptal edildi) ve acil işareti
- Arama, durum ve kategoriye göre filtreleme
- Son tarihe kalan gün gösterimi
- Her kullanıcı yalnızca kendi verilerini görür
- Django admin paneli

## Kurulum
1. Depoyu klonla: `git clone <repo-adresi>` ve klasöre gir
2. Sanal ortam oluştur: `python -m venv venv`
3. Aktifleştir (Windows): `venv\Scripts\activate`
4. Paketleri kur: `pip install -r requirements.txt`
5. Veritabanını oluştur: `python manage.py migrate`
6. Admin hesabı oluştur: `python manage.py createsuperuser`
7. Sunucuyu başlat: `python manage.py runserver`

Uygulama: http://127.0.0.1:8000/
Admin paneli: http://127.0.0.1:8000/admin/

## Teknolojiler
Python, Django 5.2, SQLite