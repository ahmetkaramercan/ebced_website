from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from ebced import (pin_kodu_hesaplama, chakra_hesapla, yasam_yolu_hesapla,
                  bereket_rakami_bulma, ana_kulvar_bulma, yan_kulvar_bulma,
                  donusum_yillari_bulma, ozellik_hesaplama)
from iliski_analizi import iliski_pin_kodu_hesaplama
from sureEsma import calculate_sure_esma, get_ebced_and_arabic, akil_fikir_sayisi_hesaplama, dogumGunuToplama, en_yakin_esma_bul, en_yakin_sure_bul
import os
import arabic_reshaper
from bidi.algorithm import get_display
from models import User

app = Flask(__name__)
app.secret_key = os.urandom(24)

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
        reshaped_text = arabic_reshaper.reshape(text)
        return get_display(reshaped_text)
    return ""

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('bireysel_analiz'))
        
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        remember = request.form.get('remember', False)
        
        user = User.get(username)
        if user and user.check_password(password):
            login_user(user, remember=remember)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('bireysel_analiz'))
        else:
            flash('Geçersiz kullanıcı adı veya şifre', 'error')
            
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
        dogum_gunu = request.form['dogum_gunu']
        dogum_gunu = dogum_gunu.replace('.', ' ').replace('/', ' ')
        dogum_gunu = ' '.join(dogum_gunu.split())
        isim_soyisim = request.form['isim_soyisim']
        
        pin_kodu_result, k_values = pin_kodu_hesaplama(dogum_gunu)
        chakra_result = chakra_hesapla(k_values, isim_soyisim)
        yasam_yolu = yasam_yolu_hesapla(dogum_gunu)
        bereket_sayisi = bereket_rakami_bulma(dogum_gunu)
        ana_kulvar = ana_kulvar_bulma(isim_soyisim)
        yan_kulvar = yan_kulvar_bulma(isim_soyisim)
        donusum_yillari = donusum_yillari_bulma(dogum_gunu)
        pin_kodu_ozellikleri = ozellik_hesaplama(k_values)
        
        results = {
            'pin_kodu': pin_kodu_result,
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
        
        iliski_pin_kodu = iliski_pin_kodu_hesaplama(dogum_gunu1, dogum_gunu2)
        
        results = {
            'iliski_pin_kodu': iliski_pin_kodu
        }
    return render_template('iliski_analizi.html', results=results)

@app.route('/sure_hesaplama', methods=['GET', 'POST'])
@login_required
def sure_hesaplama():
    url = "https://www.ozgulyildiz.com/araclar/ebced/"
    results = None
    
    if request.method == 'POST':
        dogum_gunu = request.form['dogum_gunu'].replace('.', ' ').replace('/', ' ')
        dogum_gunu = ' '.join(dogum_gunu.split())
        name = request.form['isim']
        mother_name = request.form['anne_ismi']
        father_name = request.form['baba_ismi']
        
        results = {
            'kisi': {'isim': name, 'arabic_text': '', 'ebced_value': ''},
            'anne': {'isim': mother_name, 'arabic_text': '', 'ebced_value': ''},
            'baba': {'isim': father_name, 'arabic_text': '', 'ebced_value': ''},
            'akil_sayisi': '',
            'fikir_sayisi': '',
            'en_yakin_esma': '',
            'en_yakin_sure': ''
        }
        
        if name:
            results['kisi']['ebced_value'], arabic_text = get_ebced_and_arabic(url + name)
            results['kisi']['arabic_text'] = reshape_arabic(arabic_text)

        if name and mother_name:
            results['anne']['ebced_value'], arabic_text = get_ebced_and_arabic(url + mother_name)
            results['anne']['arabic_text'] = reshape_arabic(arabic_text)
            results['akil_sayisi'] = akil_fikir_sayisi_hesaplama(
                results['kisi']['ebced_value'], 
                results['anne']['ebced_value']
            )

        if name and father_name:
            results['baba']['ebced_value'], arabic_text = get_ebced_and_arabic(url + father_name)
            results['baba']['arabic_text'] = reshape_arabic(arabic_text)
            results['fikir_sayisi'] = akil_fikir_sayisi_hesaplama(
                results['kisi']['ebced_value'], 
                results['baba']['ebced_value']
            )

        if dogum_gunu and name and mother_name:
            dgToplam = dogumGunuToplama(dogum_gunu)
            results['en_yakin_esma'] = en_yakin_esma_bul(
                results['kisi']['ebced_value'], 
                results['anne']['ebced_value'], 
                dgToplam
            )
            results['en_yakin_sure'] = en_yakin_sure_bul(
                results['kisi']['ebced_value'], 
                results['anne']['ebced_value'], 
                dgToplam
            )
    
    return render_template('sure_hesaplama.html', results=results)

if __name__ == '__main__':
    app.run(debug=True, port=5001) 