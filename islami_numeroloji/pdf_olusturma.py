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
import tempfile
import os
import shutil

# Hesaplama fonksiyonlarını import et
from hesaplama import (pin_kodu_hesaplama, chakra_hesapla, yasam_yolu_hesapla,
                  merkez_sayi_bulma, donusum_yillari_bulma, ozellik_hesaplama, pin_kodu_yorumlari_algoritmasi)
from hesaplama_cakra import cakra_metin_hesaplamalari
from text import yasam_yollari, merkez_sayi_aciklamalari

# pdf.py dosyasından create_pdf ve replace_name_on_cover fonksiyonlarını import et
from pdf import create_pdf, replace_name_on_cover

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
    cakra_metinleri = cakra_metin_hesaplamalari(arti_sistemi, cinsiyet)
    # Merkez sayının tuple değerini al
    merkez_sayi_detay, merkez_sayi_integer = merkez_sayi_bulma(isim_soyisim)

    donusum_yillari = donusum_yillari_bulma(dogum_gunu)
    pin_kodu_ozellikleri = ozellik_hesaplama(pin_kodu)

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
        'pin_kodu_dizilimi': pin_kodu,
        'pin_kodu_yorumlari': pin_kodu_yorumlari,
        'chakra': chakra_result,
        'cakra_metinleri': cakra_metinleri,
        'yasam_yolu': yasam_yolu,
        'yasam_yolu_aciklama': yasam_yolu_aciklama,
        'merkez_sayi': merkez_sayi_detay,
        'merkez_sayi_integer': merkez_sayi_integer,
        'merkez_sayi_aciklama': merkez_sayi_aciklama,
        'donusum_yillari': donusum_yillari,
        'pin_kodu_ozellikleri': pin_kodu_ozellikleri
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
        final_pdf_path = f"birlesik_{output_pdf_path}"
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
    
    # Çakra metinleri için içerik
    if results['cakra_metinleri']:
        for i, metin in enumerate(results['cakra_metinleri']):
            cakra_content = {
                'type': 'cakra',
                'title': "", #f"{i+1}. ÇAKRA METNİ",
                'body_text': metin,
                'background_color': "#F8F9F",  #  tema
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
            
            # Çakra sayfalarını ekle (ilk 9 content)
            cakra_count = 0
            for i, content in enumerate(additional_content):
                if content['type'] == 'cakra':
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
                    if cakra_count >= 9:  # İlk 9 çakra sayfasından sonra dur
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
                if content['type'] != 'cakra':  # Çakra olmayan sayfalar
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