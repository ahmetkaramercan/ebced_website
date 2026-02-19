from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from functools import wraps
from ebced import (pin_kodu_hesaplama, chakra_hesapla, yasam_yolu_hesapla,
                  bereket_rakami_bulma, tam_kulvar_bulma,
                  donusum_yillari_bulma, ozellik_hesaplama, cakra_yorumlari)
from hesaplama_merkez_sayi import merkez_sayi_bulma
from iliski_analizi import iliski_pin_kodu_hesaplama
from sureEsma import get_ebced_and_arabic, akil_fikir_sayisi_hesaplama, dogumGunuToplama, en_yakin_esma_bul, en_yakin_sure_bul
from text_yasam_yolu import yasam_yollari
import os
import arabic_reshaper
from bidi.algorithm import get_display
from models import User
from datetime import timedelta, datetime
from veritabani_yonetici import VeriTabaniYonetici

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))

# Oturum ayarları
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)  # 31 günlük oturum süresi
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # CSRF koruması
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=31)  # Remember Me süresi
app.config['REMEMBER_COOKIE_HTTPONLY'] = True
app.config['REMEMBER_COOKIE_SECURE'] = True

# Production ortamında mı yoksa development ortamında mı olduğumuzu kontrol et
is_production = os.environ.get('RENDER', False)  # Render.com'da RENDER environment variable'ı set edilir

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(username):
    return User.get(username)

def reshape_arabic(text):
    """Helper function to reshape Arabic text"""
    if text:
        try:
            reshaped_text = arabic_reshaper.reshape(text)
            bidi_text = get_display(reshaped_text)
            return bidi_text
        except Exception as e:
            print(f"Error reshaping Arabic text: {e}")
            return text
    return ""

def admin_required(f):
    """Admin kontrolü için decorator"""
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        if current_user.username != 'ahmet':
            flash('Bu sayfaya erişim yetkiniz yok.', 'error')
            return redirect(url_for('bireysel_analiz'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('bireysel_analiz'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember', False)
        
        # Debug için
        print(f"Login attempt for user: {username}")
        print(f"Remember me checked: {remember}")
        
        if not username or not password:
            flash('Kullanıcı adı ve şifre gereklidir', 'error')
            return render_template('login.html')
        
        # Önce şifre kontrolü yap
        vt = VeriTabaniYonetici()
        vt.cursor.execute('SELECT sifre, bitis_tarihi FROM kullanicilar WHERE kullanici_adi = ?', (username,))
        user_data = vt.cursor.fetchone()
        
        if not user_data:
            print(f"User not found: {username}")
            flash('Geçersiz kullanıcı adı veya şifre', 'error')
            return render_template('login.html')
        
        if user_data[0] != password:
            print(f"Invalid password for user: {username}")
            flash('Geçersiz kullanıcı adı veya şifre', 'error')
            return render_template('login.html')
        
        # Bitiş tarihi kontrolü (admin kullanıcısı hariç)
        if username != 'ahmet' and user_data[1]:  # bitis_tarihi varsa ve admin değilse
            try:
                bitis_tarihi = datetime.strptime(user_data[1], '%Y-%m-%d %H:%M:%S')
                if bitis_tarihi < datetime.now():
                    flash('Üyelik süreniz dolmuştur. Lütfen yönetici ile iletişime geçin. 0501 139 9717', 'error')
                    return render_template('login.html')
            except:
                pass  # Tarih formatı hatalıysa devam et
        
        user = User.get(username)
        if user is None:
            print(f"User not found or expired: {username}")
            flash('Geçersiz kullanıcı adı veya şifre', 'error')
            return render_template('login.html')
        
        try:
            # Oturumu kalıcı yap
            session.permanent = True
            # Kullanıcıyı hatırla seçeneği ile giriş yap
            login_user(user, remember=remember, duration=timedelta(days=31))
            print(f"Login successful for user: {username}")
            
            next_page = request.args.get('next')
            return redirect(next_page or url_for('bireysel_analiz'))
        except Exception as e:
            print(f"Error during login: {str(e)}")
            flash('Giriş yapılırken bir hata oluştu. Lütfen tekrar deneyin.', 'error')
            return render_template('login.html')
            
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'username':
            new_username = request.form.get('new_username')
            confirm_username = request.form.get('confirm_username')
            
            if new_username != confirm_username:
                flash('Yeni kullanıcı adları eşleşmiyor', 'error')
            else:
                if current_user.change_username(new_username):
                    flash('Kullanıcı adınız başarıyla değiştirildi', 'success')
                    return redirect(url_for('login'))
                else:
                    flash('Bu kullanıcı adı zaten kullanımda', 'error')
        
        elif action == 'password':
            new_password = request.form.get('new_password')
            confirm_password = request.form.get('confirm_password')
            
            if new_password != confirm_password:
                flash('Yeni şifreler eşleşmiyor', 'error')
            else:
                current_user.change_password(new_password)
                flash('Şifreniz başarıyla değiştirildi', 'success')
                return redirect(url_for('login'))
            
    return render_template('profile.html')

@app.route('/')
def index():
    return redirect(url_for('bireysel_analiz'))

@app.route('/bireysel_analiz', methods=['GET', 'POST'])
@login_required
def bireysel_analiz():
    results = None
    if request.method == 'POST':
        try:
            # Sorgu sayısını artır
            vt = VeriTabaniYonetici()
            vt.sorgu_sayisi_artir(current_user.username)
            input_dogum_gunu = request.form.get('dogum_gunu', '').strip()
            isim_soyisim = request.form.get('isim_soyisim', '').strip()
            eklenen_isim = request.form.get('eklenen_isim', '').strip()
            
            # Boş alan kontrolü
            if not input_dogum_gunu:
                flash('Doğum tarihi gereklidir.', 'error')
                return render_template('bireysel_analiz.html', results=None)
            
            if not isim_soyisim:
                flash('İsim soyisim gereklidir.', 'error')
                return render_template('bireysel_analiz.html', results=None)
            
            dogum_gunu = input_dogum_gunu.replace('.', ' ').replace('/', ' ')
            dogum_gunu = ' '.join(dogum_gunu.split())

            pin_kodu, pin_kodu_yorumlari = pin_kodu_hesaplama(dogum_gunu)
            
            # Hata kontrolü - pin_kodu_hesaplama hata durumunda string döndürür
            if isinstance(pin_kodu, str) and pin_kodu_yorumlari is None:
                flash(f'Hatalı giriş: {pin_kodu}', 'error')
                return render_template('bireysel_analiz.html', results=None)
            
            arti_sistemi, chakra_result = chakra_hesapla(pin_kodu, isim_soyisim, eklenen_isim)
            chakra_yorumlari = cakra_yorumlari(arti_sistemi)

            yasam_yolu = yasam_yolu_hesapla(dogum_gunu)
            yasam_yolu_aciklama = yasam_yollari.get(yasam_yolu, "Bu yaşam yolu için açıklama bulunamadı.")
            bereket_sayisi = bereket_rakami_bulma(dogum_gunu)
            tam_kulvar = tam_kulvar_bulma(isim_soyisim)
            merkez_sayi_sonuc, merkez_sayi = merkez_sayi_bulma(isim_soyisim)
            donusum_yillari = donusum_yillari_bulma(dogum_gunu)
            pin_kodu_ozellikleri = ozellik_hesaplama(pin_kodu)
            
            results = {
                'input_dogum_gunu': input_dogum_gunu,
                'isim_soyisim': isim_soyisim,
                'eklenen_isim': eklenen_isim,
                'dogum_gunu': dogum_gunu,  # Orijinal formatı template'e gönder
                'pin_kodu_dizilimi': pin_kodu,
                'pin_kodu_yorumlari': pin_kodu_yorumlari,
                'chakra': chakra_result,
                'chakra_yorumlari': chakra_yorumlari,
                'yasam_yolu': yasam_yolu,
                'yasam_yolu_aciklama': yasam_yolu_aciklama,
                'bereket_sayisi': bereket_sayisi,
                'tam_kulvar': tam_kulvar,
                'merkez_sayi_sonuc': merkez_sayi_sonuc,
                'merkez_sayi': merkez_sayi,
                'donusum_yillari': donusum_yillari,
                'pin_kodu_ozellikleri': pin_kodu_ozellikleri
            }
        except Exception as e:
            flash(f'Hatalı giriş: {str(e)}', 'error')
            return render_template('bireysel_analiz.html', results=None)
    
    return render_template('bireysel_analiz.html', results=results)


@app.route('/iliski_analizi', methods=['GET', 'POST'])
@login_required
def iliski_analizi():
    results = None
    if request.method == 'POST':
        try:
            # Sorgu sayısını artır
            vt = VeriTabaniYonetici()
            vt.sorgu_sayisi_artir(current_user.username)
            # Form verilerini al
            dogum_gunu1 = request.form.get('dogum_gunu1', '').strip()
            dogum_gunu2 = request.form.get('dogum_gunu2', '').strip()
            isim_soyisim1 = request.form.get('isim_soyisim1', '').strip()
            isim_soyisim2 = request.form.get('isim_soyisim2', '').strip()
            eklenen_isim1 = request.form.get('eklenen_isim1', '').strip()
            eklenen_isim2 = request.form.get('eklenen_isim2', '').strip()
            
            # Boş alan kontrolü
            if not dogum_gunu1 or not dogum_gunu2:
                flash('Her iki kişi için de doğum tarihi gereklidir.', 'error')
                return render_template('iliski_analizi.html', results=None)
            
            if not isim_soyisim1 or not isim_soyisim2:
                flash('Her iki kişi için de isim soyisim gereklidir.', 'error')
                return render_template('iliski_analizi.html', results=None)
            
            dogum_gunu1 = dogum_gunu1.replace('.', ' ').replace('/', ' ')
            dogum_gunu1 = ' '.join(dogum_gunu1.split())
            
            dogum_gunu2 = dogum_gunu2.replace('.', ' ').replace('/', ' ')
            dogum_gunu2 = ' '.join(dogum_gunu2.split())
            
            # Bireysel pin kodu dizilimlerini hesapla
            k_values_1, _ = pin_kodu_hesaplama(dogum_gunu1)
            k_values_2, _ = pin_kodu_hesaplama(dogum_gunu2)
            
            # Hata kontrolü
            if isinstance(k_values_1, str):
                flash(f'1. kişi için hatalı giriş: {k_values_1}', 'error')
                return render_template('iliski_analizi.html', results=None)
            
            if isinstance(k_values_2, str):
                flash(f'2. kişi için hatalı giriş: {k_values_2}', 'error')
                return render_template('iliski_analizi.html', results=None)

            # Her kişi için çakra hesaplaması
            arti_sistemi_1, chakra_result_1 = chakra_hesapla(k_values_1, isim_soyisim1, eklenen_isim1)
            arti_sistemi_2, chakra_result_2 = chakra_hesapla(k_values_2, isim_soyisim2, eklenen_isim2)

            # Her kişi için yaşam yolu ve merkez sayı hesaplaması
            yasam_yolu_1 = yasam_yolu_hesapla(dogum_gunu1)
            yasam_yolu_2 = yasam_yolu_hesapla(dogum_gunu2)
            
            merkez_sayi_sonuc_1, merkez_sayi_1 = merkez_sayi_bulma(isim_soyisim1)
            merkez_sayi_sonuc_2, merkez_sayi_2 = merkez_sayi_bulma(isim_soyisim2)

            # İlişki analizi sonuçlarını hesapla
            results = iliski_pin_kodu_hesaplama(dogum_gunu1, dogum_gunu2)

            # Sonuçlara bireysel pin kodu dizilimlerini ve çakra bilgilerini ekle
            if isinstance(results, dict):
                results['pin_kodu_dizilimi_1'] = k_values_1
                results['pin_kodu_dizilimi_2'] = k_values_2
                results['chakra_1'] = chakra_result_1
                results['chakra_2'] = chakra_result_2
                results['isim_soyisim1'] = isim_soyisim1
                results['isim_soyisim2'] = isim_soyisim2
                results['eklenen_isim1'] = eklenen_isim1
                results['eklenen_isim2'] = eklenen_isim2
                results['dogum_gunu1'] = dogum_gunu1
                results['dogum_gunu2'] = dogum_gunu2
                results['yasam_yolu_1'] = yasam_yolu_1
                results['yasam_yolu_2'] = yasam_yolu_2
                results['merkez_sayi_1'] = merkez_sayi_1
                results['merkez_sayi_2'] = merkez_sayi_2
        except Exception as e:
            flash(f'Hatalı giriş: {str(e)}', 'error')
            return render_template('iliski_analizi.html', results=None)
        
    return render_template('iliski_analizi.html', results=results)

@app.route('/sure_hesaplama', methods=['GET', 'POST'])
@login_required
def sure_hesaplama():
    results = None
    
    if request.method == 'POST':
        try:
            # Sorgu sayısını artır
            vt = VeriTabaniYonetici()
            vt.sorgu_sayisi_artir(current_user.username)
            dogum_gunu = request.form.get('dogum_gunu', '').strip()
            name = request.form.get('isim', '').strip()
            mother_name = request.form.get('anne_ismi', '').strip()
            father_name = request.form.get('baba_ismi', '').strip()
            
            # Boş alan kontrolü
            if not dogum_gunu:
                flash('Doğum tarihi gereklidir.', 'error')
                return render_template('sure_hesaplama.html', results=None)
            
            if not name or not mother_name or not father_name:
                flash('Tüm alanlar gereklidir.', 'error')
                return render_template('sure_hesaplama.html', results=None)
            
            dogum_gunu = dogum_gunu.replace('.', ' ').replace('/', ' ')
            dogum_gunu = ' '.join(dogum_gunu.split())
            
            # Kişi bilgileri
            if (not name.isdigit()):
                kisi_ebced, kisi_arabic = get_ebced_and_arabic(name)
                kisi_arabic = reshape_arabic(kisi_arabic)
            else:
                kisi_ebced = int(name)
                kisi_arabic = ""
            
            # Anne bilgileri
            if (not mother_name.isdigit()):
                anne_ebced, anne_arabic = get_ebced_and_arabic(mother_name)
                anne_arabic = reshape_arabic(anne_arabic)
            else:
                anne_ebced = int(mother_name)
                anne_arabic = ""
            
            # Baba bilgileri
            if (not father_name.isdigit()):
                baba_ebced, baba_arabic = get_ebced_and_arabic(father_name)
                baba_arabic = reshape_arabic(baba_arabic)
            else:
                baba_ebced = int(father_name)
                baba_arabic = ""
            
            # Doğum günü toplamı
            dogum_gunu_toplam = dogumGunuToplama(dogum_gunu)
            
            # Akıl ve fikir sayıları
            akil_sayisi = akil_fikir_sayisi_hesaplama(kisi_ebced, anne_ebced)
            fikir_sayisi = akil_fikir_sayisi_hesaplama(kisi_ebced, baba_ebced)
            
            # En yakın esma ve sure hesaplama
            en_yakin_esma = en_yakin_esma_bul(kisi_ebced, anne_ebced, dogum_gunu_toplam)
            en_yakin_sure = en_yakin_sure_bul(kisi_ebced, anne_ebced, dogum_gunu_toplam)
            
            results = {
                'kisi': {
                    'isim': name,
                    'ebced_value': kisi_ebced,
                    'arabic_text': kisi_arabic
                },
                'anne': {
                    'isim': mother_name,
                    'ebced_value': anne_ebced,
                    'arabic_text': anne_arabic
                },
                'baba': {
                    'isim': father_name,
                    'ebced_value': baba_ebced,
                    'arabic_text': baba_arabic
                },
                'akil_sayisi': akil_sayisi,
                'fikir_sayisi': fikir_sayisi,
                'en_yakin_esma': en_yakin_esma,
                'en_yakin_sure': en_yakin_sure
            }
        except Exception as e:
            flash(f'Hatalı giriş: {str(e)}', 'error')
            return render_template('sure_hesaplama.html', results=None)
    
    return render_template('sure_hesaplama.html', results=results)

@app.route('/admin')
@admin_required
def admin():
    """Admin paneli ana sayfası"""
    return render_template('admin.html')

@app.route('/admin/kullanicilar', methods=['GET'])
@admin_required
def admin_kullanicilar():
    """Tüm kullanıcıları listele"""
    vt = VeriTabaniYonetici()
    vt.cursor.execute('SELECT kullanici_adi, sifre, aktiflik, tarih, bitis_tarihi, sorgu_sayisi, son_sorgu_tarihi FROM kullanicilar')
    kullanicilar = vt.cursor.fetchall()
    
    kullanici_listesi = []
    for kullanici in kullanicilar:
        kullanici_listesi.append({
            'kullanici_adi': kullanici[0],
            'sifre': kullanici[1],
            'aktiflik': 'Aktif' if kullanici[2] == 1 else 'Deaktif',
            'baslangic_tarihi': kullanici[3],
            'bitis_tarihi': kullanici[4] if kullanici[4] else 'Belirtilmemiş',
            'sorgu_sayisi': kullanici[5] if kullanici[5] is not None else 0,
            'son_sorgu_tarihi': kullanici[6] if kullanici[6] else 'Belirtilmemiş'
        })
    
    return jsonify({'kullanicilar': kullanici_listesi})

@app.route('/admin/kullanici_ekle', methods=['POST'])
@admin_required
def admin_kullanici_ekle():
    """Yeni kullanıcı ekle"""
    data = request.get_json()
    kullanici_adi = data.get('kullanici_adi', '').strip()
    sifre = data.get('sifre', '').strip()
    ay_sayisi = data.get('ay_sayisi', 12)
    
    if not kullanici_adi or not sifre:
        return jsonify({'success': False, 'message': 'Kullanıcı adı ve şifre gereklidir'}), 400
    
    try:
        ay_sayisi = int(ay_sayisi)
        if ay_sayisi < 1 or ay_sayisi > 12:
            return jsonify({'success': False, 'message': 'Ay sayısı 1-12 arasında olmalıdır'}), 400
    except ValueError:
        return jsonify({'success': False, 'message': 'Geçerli bir ay sayısı giriniz'}), 400
    
    vt = VeriTabaniYonetici()
    if vt.kullanici_ekle(kullanici_adi, sifre, ay_sayisi):
        return jsonify({'success': True, 'message': f'Kullanıcı {kullanici_adi} başarıyla eklendi'})
    else:
        return jsonify({'success': False, 'message': f'{kullanici_adi} kullanıcı adı zaten mevcut'}), 400

@app.route('/admin/kullanici_sil', methods=['POST'])
@admin_required
def admin_kullanici_sil():
    """Kullanıcı sil"""
    data = request.get_json()
    kullanici_adi = data.get('kullanici_adi', '').strip()
    
    if not kullanici_adi:
        return jsonify({'success': False, 'message': 'Kullanıcı adı gereklidir'}), 400
    
    if kullanici_adi == 'ahmet':
        return jsonify({'success': False, 'message': 'Admin kullanıcısı silinemez'}), 400
    
    vt = VeriTabaniYonetici()
    if vt.kullanici_sil(kullanici_adi):
        return jsonify({'success': True, 'message': f'Kullanıcı {kullanici_adi} başarıyla silindi'})
    else:
        return jsonify({'success': False, 'message': f'{kullanici_adi} kullanıcısı bulunamadı'}), 400

@app.route('/admin/kullanici_deaktive', methods=['POST'])
@admin_required
def admin_kullanici_deaktive():
    """Kullanıcıyı deaktive et"""
    data = request.get_json()
    kullanici_adi = data.get('kullanici_adi', '').strip()
    
    if not kullanici_adi:
        return jsonify({'success': False, 'message': 'Kullanıcı adı gereklidir'}), 400
    
    vt = VeriTabaniYonetici()
    if vt.kullaniciyi_deaktive_et(kullanici_adi):
        return jsonify({'success': True, 'message': f'Kullanıcı {kullanici_adi} deaktive edildi'})
    else:
        return jsonify({'success': False, 'message': f'{kullanici_adi} kullanıcısı bulunamadı'}), 400

@app.route('/admin/kullanici_sure_uzat', methods=['POST'])
@admin_required
def admin_kullanici_sure_uzat():
    """Kullanıcı süresini uzat"""
    data = request.get_json()
    kullanici_adi = data.get('kullanici_adi', '').strip()
    ay_sayisi = data.get('ay_sayisi', 1)
    
    if not kullanici_adi:
        return jsonify({'success': False, 'message': 'Kullanıcı adı gereklidir'}), 400
    
    try:
        ay_sayisi = int(ay_sayisi)
        if ay_sayisi < 1 or ay_sayisi > 12:
            return jsonify({'success': False, 'message': 'Ay sayısı 1-12 arasında olmalıdır'}), 400
    except ValueError:
        return jsonify({'success': False, 'message': 'Geçerli bir ay sayısı giriniz'}), 400
    
    vt = VeriTabaniYonetici()
    if vt.kullanici_suresini_uzat(kullanici_adi, ay_sayisi):
        return jsonify({'success': True, 'message': f'Kullanıcı {kullanici_adi} süresi {ay_sayisi} ay uzatıldı'})
    else:
        return jsonify({'success': False, 'message': f'{kullanici_adi} kullanıcısı bulunamadı'}), 400

if __name__ == '__main__':
    # Development server
    app.run(debug=False, host='0.0.0.0', port=8080) 