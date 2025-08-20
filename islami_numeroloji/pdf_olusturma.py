from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader, PdfWriter
import fitz  # PyMuPDF
import tempfile
import os
import shutil

# Hesaplama fonksiyonlarını import et
from .hesaplama import (pin_kodu_hesaplama, chakra_hesapla, yasam_yolu_hesapla,
                  donusum_yillari_bulma, pin_kodu_yorumlari_algoritmasi)
from .hesaplama_merkez_sayi import merkez_sayi_bulma, merkez_sayi_aciklamalari
from .hesaplama_cakra import cakra_metin_hesaplamalari, cocuk_cakra_metin_hesaplamalari
from .text import yasam_yollari

# pdf.py dosyasından create_pdf ve replace_name_on_cover fonksiyonlarını import et
# Fonksiyonlar artık bu dosyada tanımlanmıştır

# pdf.py'den alınan fonksiyonlar
def wrap_text(cnv, text, max_width, font_name, font_size, start_x, start_y, line_height, body_text_color):
    """Metni sayfalara bölerek yazdırır, kalan metni döndürür"""
    # Eğer metin zaten işlenmiş satırlar ise, tekrar işleme
    if isinstance(text, list):
        all_lines = text
    else:
        # Önce \n karakterlerini kullanarak paragrafları böl
        paragraphs = text.split('\n')
        all_lines = []
        
        for paragraph in paragraphs:
            if paragraph.strip():  # Boş paragrafları atla
                # Her paragraf için kelime kelime satır oluştur
                words = paragraph.split()
                line = ""
                lines = []
                
                for w in words:
                    test = (line + " " + w).strip() if line else w
                    if cnv.stringWidth(test, font_name, font_size) <= max_width:
                        line = test
                    else:
                        if line:  # Boş satır ekleme
                            lines.append(line)
                        line = w
                
                if line:  # Son satırı ekle
                    lines.append(line)
                
                # Bu paragrafın satırlarını ana listeye ekle
                all_lines.extend(lines)
                # Paragraflar arası boşluk ekle
                if lines:  # Eğer paragraf boş değilse
                    all_lines.append("")  # Boş satır ekle

    # Sayfa yüksekliği hesapla (A4 sayfası için)
    page_height = 842  # A4 yüksekliği (point cinsinden)
    margin_top = 50
    margin_bottom = 50
    
    # Mevcut y pozisyonundan başla
    current_y = start_y
    remaining_text = []
    current_line_index = 0
    
    # Her satırı yazdır
    for i, ln in enumerate(all_lines):
        if ln.strip():  # Boş satırları atla
            # Eğer sayfa sonuna geldiysek kalan metni kaydet
            if current_y < margin_bottom:
                # Kalan metni kaydet
                remaining_text = all_lines[i:]
                print(f"Sayfa doldu, kalan metin için yeni PDF oluşturulacak")
                break
            
            # Metni yazdır
            cnv.setFont(font_name, font_size)
            cnv.setFillColor(colors.HexColor(body_text_color))  # Parametrik metin rengi
            cnv.drawString(start_x, current_y, ln)
        
        current_y -= line_height
    
    # Kalan metni döndür (satır listesi olarak)
    if remaining_text:
        return remaining_text  # Satır listesi olarak döndür
    
    return []  # Kalan metin yok

def create_pdf(output_path="tasarim.pdf", 
               background_color="#0F6A64", 
               panel_color="#F2643D", 
               text_color="#FFFFFF",
               body_text_color="#FFFFFF",
               title="",
               body_text=None,
               is_continuation=False):
    # Türkçe karakter desteği için font yükle
    font_name = "Helvetica"  # Varsayılan font
    
    # macOS için sistem fontlarını dene
    font_paths = [
        "/System/Library/Fonts/Geneva.ttf",  # macOS'ta mevcut
        "/System/Library/Fonts/Monaco.ttf",  # macOS'ta mevcut
        "/System/Library/Fonts/Apple Symbols.ttf",  # macOS'ta mevcut
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # Linux
        "C:\\Windows\\Fonts\\arial.ttf",  # Windows
    ]
    
    for font_path in font_paths:
        if os.path.isfile(font_path):
            try:
                if font_path.endswith('.ttc'):
                    # .ttc dosyaları için özel işlem gerekebilir
                    continue
                pdfmetrics.registerFont(TTFont('TurkishFont', font_path))
                font_name = 'TurkishFont'
                print(f"Türkçe font yüklendi: {font_path}")
                break
            except Exception as e:
                print(f"Font yükleme hatası ({font_path}): {e}")
                continue
    
    if font_name == "Helvetica":
        print("Türkçe font bulunamadı, varsayılan font kullanılıyor")

    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    # Arka plan (parametre olarak verilen renk)
    c.setFillColor(colors.HexColor(background_color))
    c.rect(0, 0, width, height, fill=1, stroke=0)

    # Orta tarafta panel (parametre olarak verilen renk)
    panel_w = width * 0.82
    panel_h = height * 0.92
    panel_x = width * 0.00
    panel_y = height * 0.0
    c.setFillColor(colors.HexColor(panel_color))
    c.roundRect(panel_x, panel_y, panel_w, panel_h, radius=20, fill=1, stroke=0)

    # Başlık (parametre olarak verilen renk)
    c.setFillColor(colors.HexColor(text_color))
    c.setFont(font_name, 42)  # 36'dan 48'e çıkarıldı
    c.drawString(panel_x + 30, panel_y + panel_h - 70, title)

    # Gövde/metin
    c.setFont(font_name, 26)  # 20'den 28'e çıkarıldı 
    
    
    wrap_max = panel_w - 36
    if len(title) > 1:
        baslangic = panel_y + panel_h - 110
    else: 
        baslangic = panel_y + panel_h - 50
    
    # Metni yazdır ve gerekirse yeni sayfalar oluştur
    remaining_text = wrap_text(c, body_text, wrap_max, font_name, 24, panel_x + 18, baslangic, 28, body_text_color)
    
    c.save()
    
    # Eğer kalan metin varsa, yeni PDF oluştur (recursive olarak)
    if remaining_text and len(remaining_text) > 0:
        print(f"Kalan metin için yeni PDF oluşturuluyor...")
        
        # Yeni PDF için dosya adı oluştur
        base_name = output_path.rsplit('.', 1)[0]
        extension = output_path.rsplit('.', 1)[1]
        
        # Kaçıncı devam sayfası olduğunu bul
        if "_devam" in base_name:
            # Zaten devam sayfası ise, sayıyı artır
            parts = base_name.split("_devam")
            if len(parts) > 1 and parts[1].isdigit():
                page_num = int(parts[1]) + 1
                new_output_path = f"{parts[0]}_devam{page_num}.{extension}"
            else:
                new_output_path = f"{base_name}_devam1.{extension}"
        else:
            # İlk devam sayfası
            new_output_path = f"{base_name}_devam1.{extension}"
        
        # Kalan metin için yeni PDF oluştur (recursive call)
        # remaining_text zaten satır listesi, tekrar işleme
        additional_pdfs = create_pdf(
            output_path=new_output_path,
            background_color=background_color,
            panel_color=panel_color,
            text_color=text_color,
            body_text_color=body_text_color,
            title="",
            body_text=remaining_text,  # Zaten işlenmiş satır listesi
            is_continuation=True  # Devam sayfası olduğunu belirt
        )
        
        # Tüm PDF'leri birleştir
        all_pdfs = [output_path] + additional_pdfs
        return all_pdfs
    
    return [output_path]  # Tek PDF oluşturuldu

def replace_name_on_cover(input_pdf, output_pdf, new_name, x, y, w=350, h=100, fontsize=28):
    # x,y: metnin yazılacağı noktaların sol-alt köşesi (points)
    # w,h: temizlemek için kapatacağımız alanın boyutu (bu alanı kapatır, sonra metin ekleriz)
    doc = fitz.open(input_pdf)
    page = doc[0]
    
    # Yeni metnin arkasını turuncu renkle doldur (kenar çizgisi olmadan)
    rect = fitz.Rect(x, y, x + w, y + h)
    page.draw_rect(rect, fill=(251/255, 100/255, 62/255), stroke_opacity=0)  # #fb643e RGB değerleri, kenar çizgisi yok
    
    # Türkçe karakter desteği için font yükle
    try:
        # Sistem fontlarını dene
        font_paths = [
            "/System/Library/Fonts/Arial.ttf",  # macOS
            "/System/Library/Fonts/Helvetica.ttc",  # macOS
            "/System/Library/Fonts/Geneva.ttf",  # macOS
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # Linux
            "C:/Windows/Fonts/arial.ttf",  # Windows
        ]
        
        turkish_font = None
        for font_path in font_paths:
            if os.path.exists(font_path):
                try:
                    if font_path.endswith('.ttc'):
                        # .ttc dosyaları için özel işlem gerekebilir
                        continue
                    turkish_font = font_path
                    break
                except:
                    continue
        
        if turkish_font:
            print(f"Türkçe font bulundu: {turkish_font}")
        else:
            print("Türkçe font bulunamadı, varsayılan font kullanılıyor")
            
    except Exception as e:
        print(f"Font yükleme hatası: {e}")
    
    # Metni akıllı satır sarma ile böl
    lines = []
    
    # Metni \n karakterine göre satırlara böl
    print(f"Debug: Gelen metin: '{new_name}'")
    
    # \n ile ayrılmış satırları al
    raw_lines = new_name.split('\n')
    print(f"Debug: Bölünen satırlar: {raw_lines}")
    
    # Her satırı ayrı ayrı işle
    for raw_line in raw_lines:
        if raw_line.strip():  # Boş satırları atla
            print(f"Debug: Satır işleniyor: '{raw_line}'")
            lines.append(raw_line.strip())
    
    print(f"Debug: Final lines: {lines}")
    
    # Metni ortalayarak yaz
    line_height = fontsize * 1.2
    total_height = len(lines) * line_height
    start_y = y + h - (h - total_height) / 2 - line_height  # Dikey ortalama
    
    for i, line in enumerate(lines):
        # Her satırı yatay olarak ortala
        text_width = len(line) * fontsize * 0.6  # Yaklaşık metin genişliği
        text_x = x + (w - text_width) / 2  # Yatay ortalama
        
        # Türkçe karakter desteği için font adını değiştir
        if turkish_font:
            page.insert_text((text_x, start_y - i * line_height), line, fontsize=fontsize, fontname="helv", color=(0, 0, 0))
        else:
            page.insert_text((text_x, start_y - i * line_height), line, fontsize=fontsize, fontname="helv", color=(0, 0, 0))
    
    doc.save(output_pdf)

# Türkçe karakter desteği için font tanımla
def setup_turkish_fonts():
    """Türkçe karakter desteği için fontları ayarlar"""
    try:
        # Sistem fontlarını dene
        font_paths = [
            "/System/Library/Fonts/Arial.ttf",  # macOS
            "/System/Library/Fonts/Helvetica.ttc",  # macOS
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",  # Linux
            "C:/Windows/Fonts/arial.ttf",  # Windows
        ]
        
        for font_path in font_paths:
            if os.path.exists(font_path):
                pdfmetrics.registerFont(TTFont('TurkishFont', font_path))
                print(f"Font yüklendi: {font_path}")
                return True
        
        # Eğer sistem fontları bulunamazsa, varsayılan fontu kullan
        print("Sistem fontları bulunamadı, varsayılan font kullanılıyor")
        return False
        
    except Exception as e:
        print(f"Font yükleme hatası: {e}")
        return False

def create_custom_pdf():
    # Türkçe font desteğini kur
    setup_turkish_fonts()
    
    # Kullanıcı verileri
    dogum_gunu = "09 08 2001"  # Eksik olan değişkeni tanımladık
    isim_soyisim = "ahmet karamercan"
    eklenen_isim = ""  # İsteğe bağlı alan
    cinsiyet = "erkek"

    # Hesaplamalar
    yasam_yolu = yasam_yolu_hesapla(dogum_gunu)
    pin_kodu = pin_kodu_hesaplama(dogum_gunu)
    arti_sistemi, chakra_result = chakra_hesapla(pin_kodu, isim_soyisim, eklenen_isim)
    pin_kodu_yorumlari = pin_kodu_yorumlari_algoritmasi(pin_kodu, arti_sistemi, cinsiyet, yasam_yolu)
    
    # Yaş hesapla
    from datetime import datetime
    try:
        dogum_parcalari = dogum_gunu.split()
        if len(dogum_parcalari) == 3:
            gun, ay, yil = int(dogum_parcalari[0]), int(dogum_parcalari[1]), int(dogum_parcalari[2])
            dogum_tarihi = datetime(yil, ay, gun)
            bugun = datetime.now()
            
            yas = bugun.year - dogum_tarihi.year
            if bugun.month < dogum_tarihi.month or (bugun.month == dogum_tarihi.month and bugun.day < dogum_tarihi.day):
                yas -= 1
        else:
            yas = None
    except:
        yas = None
    
    # Yaşa göre çakra hesaplama seç
    if yas is not None and yas <= 5:
        cakra_metinleri = cocuk_cakra_metin_hesaplamalari(arti_sistemi)
        cakra_tipi = "Çocuk çakra hesaplaması"
    else:
        cakra_metinleri = cakra_metin_hesaplamalari(arti_sistemi, cinsiyet)
        cakra_tipi = "Çakra hesaplaması"
    # Merkez sayının tuple değerini al
    merkez_sayi_detay, merkez_sayi_integer = merkez_sayi_bulma(isim_soyisim)

    donusum_yillari = donusum_yillari_bulma(dogum_gunu)

    # Yaşam yolu açıklamasını al
    yasam_yolu_aciklama = yasam_yollari.get(yasam_yolu, "Bu yaşam yolu için açıklama bulunamadı.")

    # Merkez sayı açıklaması - dictionary'den al veya varsayılan mesaj
    merkez_sayi_aciklama = merkez_sayi_aciklamalari.get(str(merkez_sayi_integer))
    if merkez_sayi_aciklama and "******" in merkez_sayi_aciklama:
        merkez_sayi_aciklama = merkez_sayi_aciklama.replace("******", isim_soyisim)

    results = {
        'dogum_gunu': dogum_gunu,
        'isim_soyisim': isim_soyisim,
        'eklenen_isim': eklenen_isim,
        'cinsiyet': cinsiyet,
        'yas': yas,
        'pin_kodu_dizilimi': pin_kodu,
        'pin_kodu_yorumlari': pin_kodu_yorumlari,
        'chakra': chakra_result,
        'cakra_metinleri': cakra_metinleri,
        'cakra_tipi': cakra_tipi,
        'yasam_yolu': yasam_yolu,
        'yasam_yolu_aciklama': yasam_yolu_aciklama,
        'merkez_sayi': merkez_sayi_detay,
        'merkez_sayi_integer': merkez_sayi_integer,
        'merkez_sayi_aciklama': merkez_sayi_aciklama,
        'donusum_yillari': donusum_yillari
    }

    # PDF dosya yolları
    ornek_pdf_path = "örnek.pdf"
    output_pdf_path = f"islami_numeroloji_analiz_{isim_soyisim.replace(' ', '_')}.pdf"
    
    try:
        # Önce örnek PDF'in ilk 12 sayfasını kopyala (0-11 arası, 12 sayfa)
        copy_specific_pages(ornek_pdf_path, output_pdf_path, list(range(12)))
        
        # Ek sayfa içeriklerini al
        additional_content = create_additional_pages_content(results)
        
        # Direkt birleşik PDF oluştur
        final_pdf_path = f"{output_pdf_path}"
        create_unified_pdf(output_pdf_path, additional_content, final_pdf_path, results)
        
        print(f"Birleşik PDF başarıyla oluşturuldu: {final_pdf_path}")
        return final_pdf_path
        
    except Exception as e:
        print(f"PDF oluşturulurken hata: {e}")
        return None

def copy_specific_pages(source_pdf, output_pdf, page_numbers):
    """Örnek PDF'in belirtilen sayfalarını kopyalar"""
    try:
        with open(source_pdf, 'rb') as infile:
            reader = PdfReader(infile)
            writer = PdfWriter()
            
            # Belirtilen sayfaları ekle
            for page_num in page_numbers:
                if page_num < len(reader.pages):
                    try:
                        page = reader.pages[page_num]
                        writer.add_page(page)
                        print(f"Sayfa {page_num + 1} kopyalandı")
                    except Exception as e:
                        print(f"Sayfa {page_num + 1} kopyalanırken hata: {e}")
                        continue
                else:
                    print(f"Sayfa {page_num + 1} mevcut değil, atlanıyor")
            
            # Geçici dosyaya yaz
            with open(output_pdf, 'wb') as outfile:
                writer.write(outfile)
                print(f"PDF başarıyla kaydedildi: {output_pdf}")
                
    except Exception as e:
        print(f"PDF kopyalama hatası: {e}")
        # Eğer kopyalama başarısız olursa, boş bir PDF oluştur
        create_empty_pdf(output_pdf)

def create_empty_pdf(output_pdf):
    """Boş bir PDF oluşturur"""
    doc = SimpleDocTemplate(output_pdf, pagesize=A4)
    story = [Paragraph("İslami Numeroloji Analizi", getSampleStyleSheet()['Title'])]
    doc.build(story)

def add_custom_pages(existing_pdf, results):
    """Mevcut PDF'e özel sayfalar ekler"""
    # Geçici dosya oluştur
    temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    temp_pdf_path = temp_pdf.name
    temp_pdf.close()
    
    try:
        # Yeni sayfalar oluştur
        create_additional_pages(temp_pdf_path, results)
        
        # Mevcut PDF'i oku
        with open(existing_pdf, 'rb') as existing_file:
            existing_reader = PdfReader(existing_file)
            
            # Yeni sayfaları oku
            with open(temp_pdf_path, 'rb') as new_file:
                new_reader = PdfReader(new_file)
                
                # Birleştir
                writer = PdfWriter()
                
                # Mevcut sayfaları ekle
                for page in existing_reader.pages:
                    writer.add_page(page)
                
                # Yeni sayfaları ekle
                for page in new_reader.pages:
                    writer.add_page(page)
                
                # Son dosyayı yaz
                with open(existing_pdf, 'wb') as output_file:
                    writer.write(output_file)
                    
    finally:
        # Geçici dosyayı temizle
        if os.path.exists(temp_pdf_path):
            os.unlink(temp_pdf_path)

def create_additional_pages_content(results):
    """Ek sayfaların içeriğini oluşturur ve döndürür"""
    additional_content = []
    
    # Çakra renkleri için array
    cakra_colors = [
        {
            'background_color': "#F8F9FA",  # Açık gri arka plan
            'panel_color': "#DC2626",  # Kırmızı (1. Çakra)
            'text_color': "#000000"
        },
        {
            'background_color': "#F8F9FA",
            'panel_color': "#FB923C",  # Turuncu (2. Çakra) 
            'text_color': "#000000"
        },
        {
            'background_color': "#F8F9FA",
            'panel_color': "#FB923C",  # Turuncu (2. Çakra) 
            'text_color': "#000000"
        },
        {
            'background_color': "#F8F9FA",
            'panel_color': "#FCD34D",  # Sarı (3. Çakra)
            'text_color': "#000000"
        },
        {
            'background_color': "#F8F9FA", 
            'panel_color': "#22C55E",  # Yeşil (4. Çakra)
            'text_color': "#000000"
        },
        {
            'background_color': "#F8F9FA",
            'panel_color': "#3B82F6",  # Mavi (5. Çakra)
            'text_color': "#000000"
        },
        {
            'background_color': "#F8F9FA",
            'panel_color': "#6366F1",  # İndigo (6. Çakra)
            'text_color': "#000000"
        },
        {
            'background_color': "#F8F9FA",
            'panel_color': "#A855F7",  # Mor (7. Çakra)
            'text_color': "#000000"
        },
        {
            'background_color': "#F8F9FA",
            'panel_color': "#EC4899",  # Pembe (8. Çakra)
            'text_color': "#000000"
        },
        {
            'background_color': "#F8F9FA",
            'panel_color': "#8B5CF6",  # Eflatun (9. Çakra)
            'text_color': "#000000"
        }
    ]
    
    # Çakra metinleri için içerik - İlk kısım (açıklama ve durum)
    if results['cakra_metinleri']:
        for i, metin in enumerate(results['cakra_metinleri']):
            # Metni iki kısma ayır
            metin_parcalari = metin.split("~~~")
            
            if len(metin_parcalari) >= 2:
                # İlk kısım: Çakra açıklaması ve durumu
                ilk_kisim = metin_parcalari[0].strip()
                # İkinci kısım: ~~~ olmadan sadece sonrası
                ikinci_kisim = metin_parcalari[1].strip()
                
                # İlk kısım için içerik (1. sayfa)
                cakra_content_ilk = {
                    'type': 'cakra_ilk',
                    'title': "",
                    'body_text': ilk_kisim,
                    'background_color': "#065F46",  # Daha koyu gri arka plan
                    'panel_color': cakra_colors[i]['panel_color'],
                    'text_color': "#FFFFFF"
                }
                additional_content.append(cakra_content_ilk)
                
                # İkinci kısım için içerik (2. sayfa)
                cakra_content_ikinci = {
                    'type': 'cakra_ikinci',
                    'title': "",
                    'body_text': ikinci_kisim,
                    'background_color': "#065F46",  # Daha koyu gri arka plan
                    'panel_color': cakra_colors[i]['panel_color'],
                    'text_color': "#FFFFFF"
                }
                additional_content.append(cakra_content_ikinci)
            else:
                # Eğer "~~~" bulunamazsa, metni olduğu gibi ekle
                cakra_content = {
                    'type': 'cakra',
                    'title': f"Alma verme dengeniz",
                    'body_text': metin,
                    'background_color': "#065F46",  # Daha koyu gri arka plan
                    'panel_color': cakra_colors[i]['panel_color'],
                    'text_color': "#FFFFFF"
                }
                additional_content.append(cakra_content)
    
    # Pin kodu yorumları için içerik
    if results['pin_kodu_yorumlari']:
        pin_text = ""
        if isinstance(results['pin_kodu_yorumlari'], list):
            for j, yorum in enumerate(results['pin_kodu_yorumlari']):
                pin_text += f"{yorum}\n\n"
        else:
            pin_text = str(results['pin_kodu_yorumlari'])
        
        pin_content = {
            'type': 'pin_kodu',
            'title': "PIN KODU YORUMLARI",
            'body_text': pin_text,
            'background_color': "#065F46",  # Yeşil tema
            'panel_color': "#10B981",
            'text_color': "#FFFFFF"
        }
        additional_content.append(pin_content)
    
    # Yaşam yolu için içerik
    if results['yasam_yolu_aciklama']:
        yasam_text = f"Yaşam Yolu Sayınız: {results['yasam_yolu']}\n\n{results['yasam_yolu_aciklama']}"
        
        yasam_content = {
            'type': 'yasam_yolu',
            'title': "YAŞAM YOLU ANALİZİ",
            'body_text': yasam_text,
            'background_color': "#7C2D12",  # Kahverengi tema
            'panel_color': "#F59E0B",
            'text_color': "#FFFFFF"
        }
        additional_content.append(yasam_content)
    
    # Merkez sayı için içerik
    if results['merkez_sayi_aciklama']:
        merkez_text = f"Merkez Sayınız: {results['merkez_sayi']}\n\n{results['merkez_sayi_aciklama']}"
        
        merkez_content = {
            'type': 'merkez_sayi',
            'title': "MERKEZ SAYI ANALİZİ",
            'body_text': merkez_text,
            'background_color': "#581C87",  # Mor tema
            'panel_color': "#8B5CF6",
            'text_color': "#FFFFFF"
        }
        additional_content.append(merkez_content)
    
    print(f"Toplam {len(additional_content)} ek sayfa içeriği hazırlandı")
    return additional_content

def create_unified_pdf(base_pdf_path, additional_content, output_path, results):
    """Tüm sayfaları tek PDF'de birleşik olarak oluşturur"""
    try:
        # Önce mevcut PDF'i kopyala
        with open(base_pdf_path, 'rb') as source_file:
            reader = PdfReader(source_file)
            writer = PdfWriter()
            
            # Mevcut PDF'in tüm sayfalarını ekle (ilk 12 sayfa)
            for page in reader.pages:
                writer.add_page(page)
            print(f"Ana PDF'den {len(reader.pages)} sayfa kopyalandı")
            
            # Çakra sayfalarını ekle (ilk kısım ve ikinci kısım)
            cakra_count = 0
            for i, content in enumerate(additional_content):
                if content['type'] in ['cakra', 'cakra_ilk', 'cakra_ikinci']:
                    # Her çakra sayfası için direkt PDF oluştur
                    output_pdf_path = f"content_{i}.pdf"
                    created_pdfs = create_pdf(
                        output_path=output_pdf_path,
                        background_color=content['background_color'],
                        panel_color=content['panel_color'],
                        text_color=content['text_color'],
                        body_text_color=content['text_color'],
                        title=content['title'],
                        body_text=content['body_text']
                    )
                    
                    # Oluşturulan tüm PDF'leri oku ve ana PDF'e ekle
                    for pdf_path in created_pdfs:
                        with open(pdf_path, 'rb') as temp_file:
                            temp_reader = PdfReader(temp_file)
                            for page in temp_reader.pages:
                                writer.add_page(page)
                                print(f"Çakra sayfası eklendi: {content['title']} - {pdf_path}")
                        
                        # Dosyayı sil
                        os.remove(pdf_path)
                    
                    cakra_count += 1
                    if cakra_count >= 18:  # İlk 9 çakra için 18 sayfa (her çakra 2 sayfa)
                        break
            
            # 35. sayfayı örnek.pdf'den kopyala
            try:
                with open("örnek.pdf", 'rb') as ornek_file:
                    ornek_reader = PdfReader(ornek_file)
                    if 34 < len(ornek_reader.pages):  # 35. sayfa (index 34)
                        writer.add_page(ornek_reader.pages[34])
                        print("35. sayfa örnek.pdf'den kopyalandı")
                    else:
                        print("35. sayfa örnek.pdf'de mevcut değil")
            except Exception as e:
                print(f"35. sayfa kopyalama hatası: {e}")
            
            # Kalan içerik sayfalarını ekle (PIN kodu, yaşam yolu, merkez sayı)
            for i, content in enumerate(additional_content):
                if content['type'] not in ['cakra', 'cakra_ilk', 'cakra_ikinci']:  # Çakra olmayan sayfalar
                    output_pdf_path = f"content_{i}.pdf"
                    created_pdfs = create_pdf(
                        output_path=output_pdf_path,
                        background_color=content['background_color'],
                        panel_color=content['panel_color'],
                        text_color=content['text_color'],
                        body_text_color=content['text_color'],
                        title=content['title'],
                        body_text=content['body_text']
                    )
                    
                    # Oluşturulan tüm PDF'leri oku ve ana PDF'e ekle
                    for pdf_path in created_pdfs:
                        with open(pdf_path, 'rb') as temp_file:
                            temp_reader = PdfReader(temp_file)
                            for page in temp_reader.pages:
                                writer.add_page(page)
                                print(f"İçerik sayfası eklendi: {content['title']} - {pdf_path}")
                        
                        # Dosyayı sil
                        os.remove(pdf_path)
            
            # Son olarak 45, 46, 47, 48. sayfaları örnek.pdf'den kopyala
            try:
                with open("örnek.pdf", 'rb') as ornek_file:
                    ornek_reader = PdfReader(ornek_file)
                    for page_num in [44, 45, 46, 47]:  # 45, 46, 47, 48. sayfalar (index 44-47)
                        if page_num < len(ornek_reader.pages):
                            writer.add_page(ornek_reader.pages[page_num])
                            print(f"{page_num + 1}. sayfa örnek.pdf'den kopyalandı")
                        else:
                            print(f"{page_num + 1}. sayfa örnek.pdf'de mevcut değil")
            except Exception as e:
                print(f"Son sayfalar kopyalama hatası: {e}")
            
            # Birleşik PDF'i kaydet
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            print(f"Birleşik PDF oluşturuldu: {output_path}")
            print(f"Toplam {len(writer.pages)} sayfa")
            
            # İlk sayfadaki ismi değiştir
            try:
                # Geçici dosya oluştur
                temp_output = output_path.replace('.pdf', '_temp.pdf')
                
                # İsmi ve alt metni ayrı ayrı hazırla
                isim = results['isim_soyisim'].title()
                alt_metin = "İçsel Yolculuğudur"
                
                # İki satırlı metin oluştur
                tam_metin = f"{isim}\n{alt_metin}"
                replace_name_on_cover(output_path, temp_output, tam_metin, 30, 600)
                
                # Geçici dosyayı ana dosya ile değiştir
                os.remove(output_path)
                os.rename(temp_output, output_path)
                print(f"İlk sayfadaki isim '{results['isim_soyisim'].title()}' olarak değiştirildi")
            except Exception as e:
                print(f"İsim değiştirme hatası: {e}")
            
            return output_path
        
    except Exception as e:
        print(f"Birleşik PDF oluşturma hatası: {e}")
        raise
    # PDF'i oluştur
    doc.build(story)

if __name__ == "__main__":
    create_custom_pdf()