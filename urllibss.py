# coding:utf-8
def freqDist(strs):
    freq={}
    for token in strs:
        if token in freq:
            freq[token] +=1
        else:
            freq[token]=1
    return freq

import urllib2,re,operator,nltk
req=urllib2.urlopen("http://www.yahyakesenek.com")
html=req.read()
tokens=re.split("\W+",html)
htmls=["div","script","body","html","title","Content","DOCTYPE","","head","link","href","stylesheet","type","css","src",
       "Script",".js","form","legend","input","Site","rel","javascript","a","i","method","action","post","get",
       "p","br","image","h1","h2","h3","h4","h5","h6","id","name","ckeditor"]
#cleaned=nltk.clean_html(html)
#print cleaned
#dst=nltk.FreqDist(tokens)
#print dst
#for tag,freq in dst.items():
#    print  tag
#    print freq
#dst.plot(50,cumulative=False)
#exit()
tokens=[token for token in tokens if token not in htmls]
print tokens
distance=freqDist(tokens)
distance=sorted(distance.items(),key=operator.itemgetter(1),reverse=True)
print distance
'''[('a', 251), ('form', 162),
('p', 154), ('i', 112), ('type', 100),
('Home', 99), ('n', 94), ('div', 89), ('input', 89),
('title', 87), ('src', 84), ('in', 83), ('z', 83),
('resim', 82), ('t', 82), ('method', 81), ('action', 81),
('post', 81), ('Detay', 77), ('Index', 76), ('klay', 76),
('jpg', 76), ('okjpg', 76), ('image', 76), ('href', 49),
('h3', 28), ('id', 27), ('quot', 26), ('gt', 25),
('252', 25), ('br', 24), ('label', 22), ('b', 21),
('3', 21), ('1', 20), ('text', 20), ('lt', 19),
('li', 18), ('name', 17), ('color', 17),
('script', 16), ('ile', 16), ('ccedil', 16),
('zerinde', 14), ('class', 14), ('bir', 14),
('style', 13), ('tabs', 13), ('uuml', 13),
('tr', 12), ('html', 12), ('olu', 12),
('tabindex', 11), ('2', 11),
('yorum', 10), ('g', 10), ('Kivy', 10),
('sonYazilar', 10), ('r', 10), ('Asp', 10),
('m', 10), ('ouml', 10), ('border', 9), ('4', 9),
('background', 9), ('Net', 9), ('220', 9), ('td', 8),
('fieldset', 8), ('body', 8), ('legend', 8), ('nbsp', 8),
('JQuery', 8), ('yanyana', 8), ('textarea', 8), ('radius', 8),
('javascript', 8), ('c', 8), ('Bu', 8), ('strong', 8), ('head', 8),
('kategoriyeGoreIcerikListele', 8), ('Mvc', 7), ('231', 7), ('Yellow', 7),
('246', 7), ('olarak', 7), ('5px', 7), ('ve', 7), ('y', 7), ('Gray', 7), ('5', 7),
('test', 7), ('baslik', 6), ('css', 6), ('400', 6), ('l', 6), ('G', 6),
('JPG', 6), ('de', 6), ('Android', 6), ('value', 6), ('rel', 5), ('net', 5),
('men', 5), ('k', 5), ('30', 5), ('mvc', 5), ('10', 5), ('false', 5),
('KESENEK', 5), ('Twisted', 5), ('Yahya', 5), ('C', 5), ('js', 5), ('Server', 5),
('kullan', 5), ('yap', 5), ('page', 5), ('Java', 5), ('for', 5), ('turulmu', 5),
('submit', 5), ('al', 5), ('th', 4), ('199', 4), ('Form', 4), ('section', 4),
('39', 4), ('DOCTYPE', 4), ('RenderSection', 4), ('none', 4), ('tbody', 4), ('lar', 4),
('turma', 4), ('cols', 4), ('asp', 4), ('ajax', 4), ('jquery', 4), ('turulmas', 4),
('width', 4), ('projesinin', 4), ('height', 4), ('table', 4), ('thead', 4),
('Olu', 4), ('9', 4), ('Y', 4), ('ba', 4), ('bu', 4), ('nder', 4),
('rows', 4), ('true', 4), ('ul', 4), ('ad', 4), ('Ad', 4), ('alt', 3),
('0', 3), ('Render', 3), ('sayfa', 3), ('visual', 3), ('MVC', 3),
('sonra', 3), ('lemi', 3), ('data', 3), ('ss', 3), ('nderir', 3),
('imi', 3), ('ise', 3), ('yorumuz', 3), ('17', 3), ('min', 3), ('Login', 3),
('Almak', 3), ('Web', 3), ('font', 3), ('8', 3), ('metotla', 3), ('Metotlar', 3),
('btn', 3), ('S', 3), ('le', 3), ('img', 3), ('mvc3', 3), ('accordion', 3), ('s', 3),
('yaz', 3), ('frm', 3), ('Dosya', 3), ('decoration', 3), ('Python', 3), ('lemleri', 3),
('eri', 3), ('yorumEkle', 3), ('web', 3), ('Yorum', 3), ('leti', 3), ('d', 3),
('ResultAction', 3), ('projesi', 3), ('default', 3), ('Scripts', 3), ('nt', 3), ('Engine', 3),
('Windows', 3), ('', 2), ('Razor', 2), ('aranan', 2), ('hata', 2), ('tfoot', 2), ('dosyalar', 2),
('Ayarlar', 2), ('rma', 2), ('Otomatik', 2), ('K', 2), ('studio', 2), ('Faces', 2), ('kategoriler', 2),
('stylesheet', 2), ('Application', 2), ('scope', 2), ('Ben', 2), ('Default', 2), ('Ekran', 2), ('DataTable', 2),
('Content', 2), ('f', 2), ('setup', 2), ('RenderPage', 2), ('mnvok', 2), ('zelle', 2), ('imza', 2), ('JavaScript', 2),
('MediaPlayer', 2), ('Dijital', 2), ('sayfalar', 2), ('klenen', 2), ('140', 2), ('sa', 2), ('se', 2), ('133', 2),
('132', 2), ('137', 2), ('135', 2), ('134', 2), ('139', 2), ('138', 2), ('konu', 2), ('27', 2), ('20', 2), ('23', 2),
('_Layout', 2), ('Mobile', 2), ('er', 2), ('Captcha', 2), ('141', 2), ('7', 2), ('Veri', 2), ('ncelikle', 2), ('turu', 2),
('RenderBody', 2), ('icerik', 2), ('Partial', 2), ('ckeditor', 2), ('Apk', 2), ('Servera', 2), ('size', 2), ('dahil', 2),
('Screenshot', 2), ('Post', 2), ('19', 2), ('18', 2), ('edilebilir', 2), ('new', 2), ('sertifika', 2), ('programc', 2),
('ka', 2), ('Bir', 2), ('WEB', 2), ('Account', 2), ('Paketleme', 2), ('136', 2), ('sahip', 2), ('inno', 2), ('mvcc', 2),
('ui', 2), ('email', 2), ('Exe', 2), ('dijital', 2), ('Daha', 2), ('com', 2), ('col', 2), ('sayfas', 2), ('Custom', 2),
('mvc3yazi', 2), ('margin', 2), ('erik', 2), ('Selenium', 2), ('im', 2), ('Panel', 2), ('http', 2), ('payla', 2),
('Ve', 2), ('Giri', 2), ('Formu', 2), ('Sitenin', 2), ('ffffff', 2), ('Setup', 2), ('hayat', 2), ('zden', 2), ('Ara', 2),
 ('Jquery', 2), ('uygulamalar', 2), ('nda', 2), ('yla', 2), ('h2', 2), ('h1', 2), ('h6', 2), ('Upload', 2), ('span', 2),
('start', 2), ('link', 2), ('sonuc', 2), ('Doldurucu', 2), ('Ayar', 2), ('11', 2), ('na', 2), ('41', 2),
('Kontrol', 2), ('E', 2), ('imzalama', 2), ('partial', 1), ('Accordion', 1), ('global', 1), ('Desktop', 1),
('ge', 1), ('Linkler', 1), ('Javascript', 1), ('ti', 1), ('te', 1), ('turur', 1), ('ta', 1), ('gereken', 1),
('kutucuk', 1), ('kurulum', 1), ('ndaki', 1), ('eklinde', 1), ('AjaxBegin', 1), ('Cihazlarada', 1),
('kontrol', 1), ('ArrayList', 1), ('Tag', 1), ('Multipart', 1), ('rmak', 1), ('ml', 1), ('zda', 1), ('za', 1),
('Anasayfa', 1), ('trafigini', 1), ('Red', 1), ('bold', 1), ('nen', 1), ('stemek', 1), ('Temizle', 1),
('Visual', 1), ('version', 1), ('yahya', 1), ('Dosyas', 1), ('wingtsunkutahya', 1), ('widget', 1),
('daha', 1), ('beraber', 1), ('108', 1), ('102', 1), ('103', 1), ('100', 1), ('101', 1), ('106', 1),
('104', 1), ('105', 1), ('38', 1), ('insan', 1), ('RedirectResult', 1), ('33', 1), ('32', 1),
('37', 1), ('36', 1), ('35', 1), ('34', 1), ('Session', 1), ('nlendirme', 1), ('scrollbar', 1),
('timestamp', 1), ('iciler', 1), ('Silme', 1), ('replace', 1), ('Spinner', 1), ('dinleme', 1),
('treeView', 1), ('linkler', 1), ('live', 1), ('istekleri', 1), ('setUser', 1), ('Rss', 1),
('bilgi', 1), ('iletisim', 1), ('malar', 1), ('flar', 1), ('sitenin', 1), ('programlama', 1),
('oyun', 1), ('partial_ismi', 1), ('masterPage', 1), ('kacak', 1), ('91', 1), ('ListBox', 1),
('Se', 1), ('sevin', 1), ('sysntax', 1), ('Zaman', 1), ('sitesinde', 1), ('Metinleri', 1),
('ula', 1), ('App', 1), ('amada', 1), ('links', 1), ('erisindeki', 1), ('tan', 1), ('belirlenir', 1),
('ziyaret', 1), ('siz', 1), ('namespace', 1), ('kadar', 1), ('suz', 1), ('yoksa', 1), ('Kat', 1), ('UI', 1),
('Kay', 1), ('kurulu', 1), ('Kelime', 1), ('Silinmesi', 1), ('sizlere', 1), ('Boyutland', 1), ('lad', 1),
('unobtrusive', 1), ('BANA', 1), ('dosyas', 1), ('cshtml', 1), ('Jenerik', 1), ('mak', 1),
('View', 1), ('120', 1), ('EmptyResult', 1), ('ahsen', 1), ('SAYFAM', 1), ('mdan', 1),
('File', 1), ('Developer', 1), ('FileResult', 1), ('Uzun', 1), ('IsSectionDefined', 1),
('sterir', 1), ('131', 1), ('haz', 1), ('dizisi', 1), ('24', 1), ('21', 1), ('22', 1),
('28', 1), ('29', 1), ('tweets', 1), ('mail', 1), ('gelmemektedir', 1), ('labilir', 1),
('yo', 1), ('HttpUnAuthorizedResult', 1), ('dan', 1), ('Register', 1), ('Cracker', 1), ('lator', 1), ('Yap', 1), ('yoruz', 1), ('dar', 1), ('isel', 1), ('form0', 1), ('mode', 1), ('Adroid', 1), ('Hata', 1), ('profile', 1), ('Strogly', 1), ('weight', 1), ('Veritaban', 1), ('mda', 1), ('birden', 1), ('loga', 1), ('logo', 1), ('Type', 1), ('87', 1), ('tirme', 1), ('ntemiyle', 1), ('Yetkisiz', 1), ('content', 1), ('tahya', 1), ('ra', 1), ('IP', 1), ('maktan', 1), ('Class', 1), ('olmad', 1), ('projesine', 1), ('4aed05', 1), ('sizlerle', 1), ('duyuyorum', 1), ('Em', 1), ('bilgisayar', 1), ('JsonResult', 1), ('insanlara', 1), ('oklu', 1), ('kimden', 1), ('SSH', 1), ('Chat', 1), ('features', 1), ('450', 1), ('almak', 1), ('Program', 1), ('333333', 1), ('FileUploader', 1), ('lacak', 1), ('oldu', 1), ('sm', 1), ('top', 1), ('kod', 1), ('widgets', 1), ('Cookie', 1), ('SEL', 1), ('kleme', 1), ('shell', 1), ('SelecManyMenu', 1), ('ARAMA', 1), ('liste', 1), ('nca', 1), ('IsectionDefined', 1), ('sayfada', 1), ('Animasyon', 1), ('Dosyadan', 1), ('project', 1), ('PhoneGap', 1), ('lmas', 1), ('izinlerine', 1), ('zenleme', 1), ('erinde', 1), ('GetEnumerator', 1), ('hashtags', 1), ('98', 1), ('nayabiliriz', 1), ('Mail', 1), ('sitede', 1), ('sonucu', 1), ('Sayfadaki', 1), ('Arad', 1), ('farkl', 1), ('Php', 1), ('sadece', 1), ('plar', 1), ('Componentlere', 1), ('kal', 1), ('kar', 1), ('render', 1), ('elbette', 1), ('serok', 1), ('veritaban', 1), ('exe', 1), ('ki', 1), ('107', 1), ('Serverdan', 1), ('yana', 1), ('left', 1), ('microsoft', 1), ('takip', 1), ('Kullanarak', 1), ('ContentResult', 1), ('erlisiniz', 1), ('istenen', 1), ('theme', 1), ('Studio', 1), ('Byte', 1), ('GridView', 1), ('dosyan', 1), ('yeni', 1), ('klerken', 1), ('unuz', 1), ('Bilgilerini', 1), ('Tasar', 1), ('122', 1), ('Widget', 1), ('127', 1), ('129', 1), ('listeleme', 1), ('Hakk', 1), ('130', 1), ('Resmi', 1), ('Kullan', 1), ('Konu', 1), ('layan', 1), ('kesenek', 1), ('kullanabilirsiniz', 1), ('faydal', 1), ('ekillenecek', 1), ('kuruyoruz', 1), ('Popup', 1), ('Ekleme', 1), ('Uygulamas', 1), ('stermek', 1), ('ken', 1), ('Eklemek', 1), ('25', 1), ('26', 1), ('Tablolara', 1), ('unla', 1), ('yelik', 1), ('Authorize', 1), ('mvc2', 1), ('ederek', 1), ('109', 1), ('hedefin', 1), ('genel', 1), ('login', 1), ('rpp', 1), ('Bo', 1), ('Her', 1), ('ListView', 1), ('header', 1), ('250', 1), ('nderimi', 1), ('600', 1), ('Bilgi', 1), ('nelerek', 1), ('java', 1), ('sayfam', 1), ('Ajax', 1), ('gelmesine', 1), ('yapmakt', 1), ('tablar', 1), ('XML', 1), ('indirip', 1), ('gibidir', 1), ('aktarma', 1), ('Resim', 1), ('bulu', 1), ('else', 1), ('alaca', 1), ('erisinden', 1), ('imdilere', 1), ('behavior', 1), ('31', 1), ('loop', 1), ('yolunu', 1), ('zamanla', 1), ('ip', 1), ('ir', 1), ('site', 1), ('Init', 1), ('ready', 1), ('D', 1), ('TWTR', 1), ('Beraber', 1), ('rarak', 1), ('Anas', 1), ('yapmas', 1), ('sistemine', 1), ('IN', 1), ('Intranet', 1), ('ConfirmDialog', 1), ('sayfa_ismi', 1), ('ndan', 1), ('ncel', 1), ('10px', 1), ('bulunabilir', 1), ('47', 1), ('geriye', 1), ('geldiniz', 1), ('214', 1), ('Loading', 1), ('zaman', 1), ('nd', 1), ('Internet', 1), ('twimg', 1), ('gunce', 1), ('hal', 1), ('ele', 1), ('blog', 1), ('ger', 1), ('JavaScriptResult', 1), ('colspan', 1), ('detay', 1), ('enek', 1), ('Bilgisayar', 1), ('okumak', 1), ('retmesi', 1), ('aray', 1), ('rlamak', 1), ('sayfaya', 1), ('avatars', 1), ('Wing', 1), ('Art', 1), ('Etkile', 1), ('54', 1), ('56', 1), ('51', 1), ('53', 1), ('52', 1), ('ye', 1), ('www', 1), ('12px', 1), ('Yeni', 1), ('Section', 1), ('Reader', 1), ('ekten', 1), ('50', 1), ('115', 1), ('uygulamas', 1), ('117', 1), ('116', 1), ('111', 1), ('113', 1), ('118', 1), ('Men', 1), ('bloklar', 1), ('Rootkit', 1), ('Ho', 1), ('Kronometre', 1), ('Drop', 1), ('Bubble', 1), ('bo', 1), ('Html', 1), ('if', 1), ('kullanaca', 1), ('retmemesi', 1), ('aca', 1), ('55', 1), ('karak', 1), ('guncel', 1), ('section_ismi', 1), ('Static', 1), ('DEVELOPER', 1), ('BeautifulSoup', 1), ('Dns', 1), ('NET', 1), ('Empty', 1), ('Dropdown', 1), ('tsun', 1), ('Drag', 1), ('custom', 1), ('yahyakesenek', 1), ('Farkl', 1), ('siteleri', 1), ('function', 1), ('fazla', 1), ('olup', 1), ('veya', 1), ('lemeyi', 1), ('Ula', 1), ('reset', 1), ('000000', 1), ('114', 1), ('j', 1), ('Json', 1), ('un', 1), ('fakat', 1), ('yapar', 1), ('yapt', 1), ('110', 1), ('interval', 1), ('istatistikleri', 1), ('Smtp', 1), ('uri', 1), ('Uygulama', 1), ('ar', 1), ('Arama', 1), ('file', 1), ('adreslerini', 1), ('ine', 1), ('gelince', 1), ('nk', 1), ('48', 1), ('49', 1), ('46', 1), ('44', 1), ('45', 1), ('42', 1), ('43', 1), ('40', 1), ('sectionismi', 1), ('14px', 1), ('Metro', 1), ('MVC3', 1), ('update', 1), ('Fonksiyonlar', 1), ('ULA', 1), ('Metodu', 1), ('retecektir', 1), ('99', 1),
('Aspx', 1), ('Ag', 1), ('atama', 1), ('Site', 1), ('sonucunda', 1), ('As', 1), ('Fitresini', 1)]
'''
