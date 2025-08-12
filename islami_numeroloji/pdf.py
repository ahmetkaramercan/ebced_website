# save as tuklu_pdf.py
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import fitz  # PyMuPDF
import os

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
    
    """
    # Eğer başlık varsa dekoratif çizgi ekle
    if len(title) > 1:
        # Basit dekoratif çizgi/oval (parametre olarak verilen renk)
        c.setStrokeColor(colors.HexColor(text_color))
        c.setLineWidth(2)
        # Basit bir kıvrım oluşturalım (path kullanımı)
        path = c.beginPath()
        path.moveTo(width - 120, height - 120)
        path.curveTo(width - 60, height - 160, width - 20, height - 80, width - 60, height - 40)
        c.drawPath(path)
    """
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
                        # .ttc dosyaları için özel işlem
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

# Kullanım (koordinatları kapaktaki konuma göre ayarla)
# A4 boyutunda, metin sol üst kısmına yakın bir yerdeyse örnek koordinatlar veriyorum
# replace_name_on_cover(
#     input_pdf="kapak.pdf",
#     output_pdf="kapak_degistirilmis.pdf",
#     new_name="AHMET KARAMERCAN",
#     x=40,          # sol kenardan px/pt cinsinden
#     y=700,         # alt kenardan yukarı doğru konum (PDF koordinatı bottom-left)
#     w=520, h=40,   # temizleme alanı büyüklüğü
#     fontsize=28
# )



if __name__ == "__main__":
    # Varsayılan renklerle PDF oluştur
    create_pdf("tasarim.pdf")
    
    # Farklı renklerle örnek PDF'ler oluştur
    # create_pdf("mavi_tema.pdf", 
    #            background_color="#1E3A8A", 
    #            panel_color="#3B82F6", 
    #            text_color="#FFFFFF",
    #            title="MİSTİK NUMEROLOJİ")
    
    # create_pdf("yesil_tema.pdf", 
    #            background_color="#065F46", 
    #            panel_color="#10B981", 
    #            text_color="#FFFFFF",
    #            title="DOĞAL NUMEROLOJİ")
