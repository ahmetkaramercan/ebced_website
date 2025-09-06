from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from ebced import (pin_kodu_hesaplama, chakra_hesapla, yasam_yolu_hesapla,
                  bereket_rakami_bulma, ana_kulvar_bulma, yan_kulvar_bulma,
                  donusum_yillari_bulma, ozellik_hesaplama)
from iliski_analizi import iliski_pin_kodu_hesaplama
from sureEsma import get_ebced_and_arabic, akil_fikir_sayisi_hesaplama, dogumGunuToplama, en_yakin_esma_bul, en_yakin_sure_bul
import os
import arabic_reshaper
from bidi.algorithm import get_display
from models import User
from datetime import timedelta

# İslami numeroloji blueprint'ini import et
from islami_numeroloji.routes import islami_numeroloji_bp

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', os.urandom(24))

# Blueprint'i register et
app.register_blueprint(islami_numeroloji_bp)

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
        
        user = User.get(username)
        if user is None:
            print(f"User not found: {username}")
            flash('Geçersiz kullanıcı adı veya şifre', 'error')
            return render_template('login.html')
            
        if not user.check_password(password):
            print(f"Invalid password for user: {username}")
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
        input_dogum_gunu = request.form['dogum_gunu'] 
        dogum_gunu = input_dogum_gunu.replace('.', ' ').replace('/', ' ')
        dogum_gunu = ' '.join(dogum_gunu.split())
        isim_soyisim = request.form['isim_soyisim']
        eklenen_isim = request.form['eklenen_isim']

        pin_kodu, pin_kodu_yorumlari  = pin_kodu_hesaplama(dogum_gunu)
        arti_sistemi, chakra_result = chakra_hesapla(pin_kodu, isim_soyisim, eklenen_isim)

        yasam_yolu = yasam_yolu_hesapla(dogum_gunu)
        bereket_sayisi = bereket_rakami_bulma(dogum_gunu)
        ana_kulvar = ana_kulvar_bulma(isim_soyisim)
        yan_kulvar = yan_kulvar_bulma(isim_soyisim)
        donusum_yillari = donusum_yillari_bulma(dogum_gunu)
        pin_kodu_ozellikleri = ozellik_hesaplama(pin_kodu)
        
        results = {
            'dogum_gunu': dogum_gunu,  # Orijinal formatı template'e gönder
            'pin_kodu_dizilimi': pin_kodu,
            'pin_kodu_yorumlari': pin_kodu_yorumlari,
            'chakra': chakra_result,
            'yasam_yolu': yasam_yolu,
            'bereket_sayisi': bereket_sayisi,
            'ana_kulvar': ana_kulvar,
            'yan_kulvar': yan_kulvar,
            'donusum_yillari': donusum_yillari,
            'pin_kodu_ozellikleri': pin_kodu_ozellikleri
        }
    
    return render_template('bireysel_analiz.html', results=results)


@app.route('/iliski_analizi', methods=['GET', 'POST'])
@login_required
def iliski_analizi():
    results = None
    if request.method == 'POST':
        dogum_gunu1 = request.form['dogum_gunu1']
        dogum_gunu1 = dogum_gunu1.replace('.', ' ').replace('/', ' ')
        dogum_gunu1 = ' '.join(dogum_gunu1.split())
        dogum_gunu2 = request.form['dogum_gunu2']
        dogum_gunu2 = dogum_gunu2.replace('.', ' ').replace('/', ' ')
        dogum_gunu2 = ' '.join(dogum_gunu2.split())
        
        # Bireysel pin kodu dizilimlerini hesapla
        k_values_1, _ = pin_kodu_hesaplama(dogum_gunu1)
        k_values_2, _ = pin_kodu_hesaplama(dogum_gunu2)

        # İlişki analizi sonuçlarını hesapla
        results = iliski_pin_kodu_hesaplama(dogum_gunu1, dogum_gunu2)

        # Sonuçlara bireysel pin kodu dizilimlerini ekle
        if isinstance(results, dict):
            results['pin_kodu_dizilimi_1'] = k_values_1
            results['pin_kodu_dizilimi_2'] = k_values_2
        
    return render_template('iliski_analizi.html', results=results)

@app.route('/sure_hesaplama', methods=['GET', 'POST'])
@login_required
def sure_hesaplama():
    results = None
    
    if request.method == 'POST':
        dogum_gunu = request.form['dogum_gunu'].replace('.', ' ').replace('/', ' ')
        dogum_gunu = ' '.join(dogum_gunu.split())
        name = request.form['isim'].strip()
        mother_name = request.form['anne_ismi'].strip()
        father_name = request.form['baba_ismi'].strip()
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
    
    return render_template('sure_hesaplama.html', results=results)

if __name__ == '__main__':
    # Development server
    app.run(debug=False, host='0.0.0.0', port=8080) 