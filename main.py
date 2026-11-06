import streamlit as st
import random

# --- 1. PAGE CONFIGURATION & LIGHT THEME ---
st.set_page_config(
    page_title="Tezkiye-i Nefs | Self-Purification Library",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Eye-friendly bright theme and copy protection CSS & JS
st.markdown("""
    <style>
    * {
        -webkit-user-select: none !important;
        -moz-user-select: none !important;
        -ms-user-select: none !important;
        user-select: none !important;
    }
    .stApp {
        background-color: #f8f9fa;
        color: #1a252f;
    }
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e9ecef;
    }
    .panel-header {
        background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.03);
    }
    .spiritual-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
    }
    .arabic-text {
        font-family: 'Amiri', serif, sans-serif;
        font-size: 1.3rem;
        color: #0f172a;
        text-align: right;
        direction: rtl;
        background: #f1f5f9;
        padding: 12px 16px;
        border-radius: 8px;
        border-right: 4px solid #d4af37;
        margin-bottom: 12px;
        line-height: 2;
    }
    .quote-text {
        font-size: 1.02rem;
        color: #334155;
        font-style: italic;
        margin-bottom: 12px;
    }
    .source-text {
        color: #b8860b;
        font-size: 0.9rem;
        margin-bottom: 8px;
        font-weight: bold;
    }
    .exp-text {
        font-size: 0.88rem;
        color: #475569;
        background: #f8fafc;
        padding: 10px;
        border-radius: 6px;
        border-left: 3px solid #10b981;
    }
    </style>

    <script>
    document.addEventListener('contextmenu', e => e.preventDefault());
    document.addEventListener('keydown', e => {
        if (e.ctrlKey && (e.key === 'c' || e.key === 'u' || e.key === 's' || e.key === 'a' || e.key === 'p') || e.key === 'F12') {
            e.preventDefault();
            alert('Tefekkür Modu / Contemplation Mode: İçerik manevi paylaşım amaçlıdır, kopyalama kapalıdır.');
        }
    });
    </script>
""", unsafe_allow_html=True)

# --- 2. MULTILINGUAL DATABASE ---
db = {
    "tr": {
        "title": "TEZKİYE-İ NEFS KÜTÜPHANESİ",
        "subtitle": "Saf Manevi Gelişim ve Nefis Terbiyesi Arşivi",
        "search_label": "Kütüphanede Ayet, Hadis veya Hikmet Arayın...",
        "tabs": ["Ayet-i Kerimeler (25)", "Hadîs-i Şerifler (25)", "Bediüzzaman Said Nursi (25)", "Büyük Veliler (25)", "Ameli Terbiye Rehberi (25)", "Murakabe Çetelesi", "📋 Paylaşım Esasları"],
        "sidebar_title": "📌 Modüller",
        "sleep_note": "💡 *Not:* Bu uygulama ücretsiz sunucularda barındırılmaktadır. Uzun süre işlem yapılmadığında uygulama uyku moduna geçebilir (ekranda 'Zzzz' simgesi çıkabilir).\n\n💤 Eğer böyle bir ekranla karşılaşırsanız, ekranda beliren mavi renkli *'Yes, get this app back up!'* butonuna tıklayın ve 15-30 saniye bekleyin.",
        "notice_title": "📜 Paylaşım İlke ve Esasları",
        "notice_p1": "Bu dijital arşiv kütüphanesi; ilmi derlemelerin, manevi metinlerin ve kişisel gelişim rehberlerinin eğitim, tefekkür ve bireysel manevi farkındalık amacıyla sunulması için tasarlanmıştır.",
        "notice_p2": "**1. Kullanım Kapsamı:** İşbu içerikler kişisel tefekkür, öğrenme ve manevi gelişim süreçlerini desteklemek amacıyla paylaşılmaktadır.",
        "notice_p3": "**2. Paylaşım Bilinci:** Bu uygulama tamamen bireysel öğrenme ve toplumsal fayda odaklıdır; ticari amaç gütmez ve herhangi bir ticari faaliyette kullanılamaz.",
        "notice_p4": "**3. Sorumluluk Hatırlatması:** Sunulan içerikler tamamen bireysel manevi terbiye ve kişisel değerlendirme amaçlı olup, kullanıcıların kendi içsel yolculuklarına rehberlik etmesi için derlenmiştir.",
        "checklist_title": "📊 Günlük Murakabe ve Nefis Çetelesi",
        "checklist_desc": "Nefsinizi her akşam aşağıdaki sorular doğrultusunda değerlendirin.",
        "checklist_btn": "Murakabe Raporunu Kaydet",
        "checklist_success": "Nefis muhasebeniz kaydedildi. Allah Tealâ nefs-i mutmainne makamına ermeyi nasip eylesin.",
        "source_label": "Kaynak",
        "lesson_label": "Manevi Ders",
        "ayet": [
            {"id": 1, "ar": "وَمَا أُبَرِّئُ نَفْسِي إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ إِلَّا مَا رَحِمَ رَبِّي", "text": "Ben nefsimi temize çıkarmam. Çünkü nefis, Rabbimin merhamet ettiği hariç, daima kötülüğü emreder.", "src": "Yûsuf Sûresi, 53", "exp": "Ders: Nefse asla güvenmemek ve kusuru daima onda görmek terbiye başlangıcıdır."},
            {"id": 2, "ar": "وَنَهَى النَّفْسَ عَنِ الْهَوَى فَإِنَّ الْجَنَّةَ هِيَ الْمَأْوَى", "text": "Kim de Rabbine kavuşmaktan korkup nefsini kötü arzulardan alıkoyarsa, şüphesiz barınacağı yer cennettir.", "src": "Nâzi'ât Sûresi, 40-41", "exp": "Ders: Cennetin yolu nefsin hevalarına engel olmaktan geçer."},
            {"id": 3, "ar": "قَدْ أَفْلَحَ مَن زَكَّاهَا وَقَدْ خَابَ مَن دَسَّاهَا", "text": "Nefsini arındıran kurtuluşa ermiştir. Onu kötülüklere gömen ise ziyana uğramıştır.", "src": "Şems Sûresi, 9-10", "exp": "Ders: Başarı makamda değil, ruhu temizlemeliktedir."},
            {"id": 4, "ar": "يَا أَيَّتُهَا النَّفْسُ الْمُطْمَئِنَّةُ ارْجِعِي إِلَى رَبِّكِ رَاضِيَةً مَّرْضِيَّةً", "text": "Ey huzura kavuşmuş nefis! Sen O'ndan razı, O da senden razı olarak Rabbine dön!", "src": "Fecr Sûresi, 27-28", "exp": "Ders: Rıza makamı nefsin terbiyesi ile mümkündür."},
            {"id": 5, "ar": "وَلَا أُقْسِمُ بِالنَّفْسِ اللَّوَّامَةِ", "text": "Kendini kınayan nefse ant olsun.", "src": "Kıyâme Sûresi, 2", "exp": "Ders: Öz eleştiri müminin en büyük kalkanıdır."},
            {"id": 6, "ar": "أَفَرَأَيْتَ مَنِ اتَّخَذَ إِلَهَهُ هَوَاهُ", "text": "Nefsinin arzusunu ilah edineni gördün mü?", "src": "Câsiye Sûresi, 23", "exp": "Ders: Nefsin her istediğini yapmak gizli bir kulluk tehlikesidir."},
            {"id": 7, "ar": "وَاعْلَمُوا أَنَّ اللَّهَ يَعْلَمُ مَا فِي أَنفُسِكُمْ فَاحْذَرُوهُ", "text": "Bilin ki Allah içinizden geçeni bilir, O'ndan sakının.", "src": "Bakara Sûresi, 235", "exp": "Ders: Kalbi vesvese ve nefsi gizli planlardan arındırmak gerekir."},
            {"id": 8, "ar": "وَالَّذِينَ جَاهَدُوا فِينَا لَنَهْدِيَنَّهُمْ سُبُلَنَا", "text": "Bizim uğrumuzda cihat edenleri elbette yollarımıza iletiriz.", "src": "Ankebût Sûresi, 69", "exp": "Ders: Nefisle mücadele edene İlahi hidayet kapıları açılır."},
            {"id": 9, "ar": "الَّذِي خَلَقَ الْمَوْتَ وَالْحَيَاةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًا", "text": "O, hanginizin daha güzel amel yapacağını sınamak için ölümü ve hayatı yarattı.", "src": "Mülk Sûresi, 2", "exp": "Ders: Hayat nefis imtihanından ibarettir."},
            {"id": 10, "ar": "وَفِي أَنفُسِكُمْ أَفَلَا تُبْصِرُونَ", "text": "Kendi nefislerinizde de ayetler var, halâ görmüyor musunuz?", "src": "Zâriyât Sûresi, 21", "exp": "Ders: İç dünyamıza tefekkürle bakmalıyız."},
            {"id": 11, "ar": "إِنَّ اللَّهَ لَا يُغَيِّرُ مَا بِقَوْمٍ حَتَّى يُغَيِّرُوا مَا بِأَنفُسِهِمْ", "text": "Bir toplum kendi özündekini değiştirmedikçe Allah onların durumunu değiştirmez.", "src": "Ra'd Sûresi, 11", "exp": "Ders: Dış dünyayı düzeltmek iç dünyayı düzeltmekle başlar."},
            {"id": 12, "ar": "يَا أَيُّهَا الَّذِينَ آمَنُوا اتَّقُوا اللَّهَ وَلْتَنظُرْ نَفْسٌ مَّا قَدَّمَتْ لِغَدٍ", "text": "Ey iman edenler! Allah'a karşı gelmekten sakının ve herkes yarın için ne hazırladığına baksın.", "src": "Haşr Sûresi, 18", "exp": "Ders: Yarın ahiret bilinciyle nefsi hesaba çekmek şarttır."},
            {"id": 13, "ar": "مَّا أَصَابَكَ مِنْ حَسَنَةٍ فَمِنَ اللَّهِ وَمَا أَصَابَكَ مِن سَيِّئَةٍ فَمِن نَّفْسِكَ", "text": "Sana gelen her iyilik Allah'tandır, sana gelen her kötülük ise kendi nefsindendir.", "src": "Nisâ Sûresi, 79", "exp": "Ders: İyiliği Allah'tan bilip, hatayı nefsine yüklemek gerektir."},
            {"id": 14, "ar": "وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِ وَنَهَى النَّفْسَ عَنِ الْهَوَى", "text": "Kim Rabbine saygıdan korkup nefsine dur derse...", "src": "Nâzi'ât Sûresi, 40", "exp": "Ders: Allah korkusu nefsin en büyük frenidir."},
            {"id": 15, "ar": "وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُ عَن ذِكْرِنَا وَاتَّبَعَ هَوَاهُ", "text": "Kalbini bizi anmaktan gafil kıldığımız ve arzularına uyan kimseye uyma.", "src": "Kehf Sûresi, 28", "exp": "Ders: Nefsinin esiri olmuş kişilerden uzak durulmalıdır."},
            {"id": 16, "ar": "بَلِ الْإِنسَانُ عَلَى نَفْسِهِ بَصِيرَةٌ", "text": "Doğrusu insan kendi nefsine karşı bir şahittir.", "src": "Kıyâme Sûresi, 14", "exp": "Ders: İnsan kendi kusurlarını en iyi bilendir."},
            {"id": 17, "ar": "وَاصْبِرْ نَفْسَكَ مَعَ الَّذِينَ يَدْعُونَ رَبَّهُم", "text": "Sabah akşam Rablerine dua edenlerle beraber sabret.", "src": "Kehf Sûresi, 28", "exp": "Ders: Nefsi terbiye etmek için salihlerle arkadaşlık gerekir."},
            {"id": 18, "ar": "مَن كَفَرَ فَعَلَيْهِ كُفْرُهُ وَمَنْ عَمِلَ صَالِحًا فَلِأَنفُسِهِمْ يَمْهَدُونَ", "text": "Kim salih amel işlerse kendi nefsi lehine hazırlık yapmış olur.", "src": "Rûm Sûresi, 44", "exp": "Ders: Yapılan her hayır nefsin ebedi kurtuluş yatırımıdır."},
            {"id": 19, "ar": "وَاللَّهُ يَدْعُو إِلَى دَارِ السَّلَامِ", "text": "Allah huzur evine (Cennete) çağırıyor.", "src": "Yûnus Sûresi, 25", "exp": "Ders: Nefsin geçici lezzetleri yerine ebedi huzur seçilmelidir."},
            {"id": 20, "ar": "إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ", "text": "Nefis daima kötülüğü emreder.", "src": "Yûsuf Sûresi, 53", "exp": "Ders: Düşmanın en tehlikelisi içimizdeki nefistir."},
            {"id": 21, "ar": "يَا أَيُّهَا النَّاسُ اتَّقُوا رَبَّكُمْ وَاخْشَوْا يَوْمًا لَّا يَجْزِي وَالِدٌ عَن وَلَدِهِ", "text": "Ey insanlar! Rabbinizden sakının ve hiçbir babanın evladından yarار sağlayamayacağı günden korkun.", "src": "Lokmân Sûresi, 33", "exp": "Ders: Kişinin nefsini kurtarması her şeyden önemlidir."},
            {"id": 22, "ar": "وَاتَّقُوا يَوْمًا تُرْجَعُونَ فِيهِ إِلَى اللَّهِ", "text": "Öyle bir günden sakının ki, o gün hepiniz Allah'a döndürüleceksiniz.", "src": "Bakara Sûresi, 281", "exp": "Ders: Hesap günü bilinciyle nefis dizginlenir."},
            {"id": 23, "ar": "وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ", "text": "Kim Allah'tan sakınırsa, Allah ona bir çıkış yolu açar ve ummadığı yerden rızıklandırır.", "src": "Talâk Sûresi, 2-3", "exp": "Ders: Takva sahibi olana ilahi kapılar açılır."},
            {"id": 24, "ar": "وَمَن يُوقَ شُحَّ نَفْسِهِ فَأُولَئِكَ هُمُ الْمُفْلِحُونَ", "text": "Kim nefsinin cimriliğinden korunursa, işte onlar kurtuluşa erenlerin ta kendileridir.", "src": "Haşr Sûresi, 9", "exp": "Ders: Cömertlik nefsin en büyük düşmanıdır."},
            {"id": 25, "ar": "وَاعْلَمُوا أَنَّ اللَّهَ يَحُولُ بَيْنَ الْمَرْءِ وَقَلْبِهِ", "text": "Bilin ki Allah, kişi ile kalbi arasına girer.", "src": "Enfâl Sûresi, 24", "exp": "Ders: Kalplerin hakimi yalnız Allah'tır, kalbi O'na bağlamalıdır."}
        ],
        "hadis": [
            {"id": 1, "ar": "الْكَيِّسُ مَنْ دَانَ نَفْسَهُ وَعَمِلَ لِمَا بَعْدَ الْمَوْتِ", "text": "Akıllı kişi, nefsini hesaba çeken ve ölümden sonrası için çalışandır.", "src": "Tirmizî", "exp": "Ders: Hakiki akıllılık nefsi kontrol altına almakla ölçülür."},
            {"id": 2, "ar": "رَجَعْنَا مِنَ الْجِهَادِ الأَصْغَرِ إِلَى الْجِهَادِ الأَكْبَرِ", "text": "Küçük cihaddan en büyük cihada (nefis mücadelesine) döndük.", "src": "Beyhakî", "exp": "Ders: En çetin savaş insanın iç dünyasında nefsiyle yaptığı savaştır."},
            {"id": 3, "ar": "أَعْدَى عَدُوِّكَ نَفْسُكَ الَّتِي بَيْنَ جَنْبَيْكَ", "text": "En şiddetli düşmanın, iki yanın arasında bulunan nefsindir.", "src": "Aclûnî", "exp": "Ders: İnsanın en büyük rakibi kendi içindeki arzularıdır."},
            {"id": 4, "ar": "لاَ يُؤْمِنُ أَحَدُكُمْ حَتَّى يَكُونَ هَوَاهُ تَبَعًا لِمَا جِئْتُ بِهِ", "text": "Hiçbiriniz, arzuları benim getirdiğime tabi olmadıkça hakiki iman etmiş olmaz.", "src": "Nevevî", "exp": "Ders: İman, nefsin isteklerini Sünnete feda etmeyi gerektirir."},
            {"id": 5, "ar": "أَفْضَلُ الْجِهَادِ أَنْ يُجَاهِدَ الرَّجُلُ نَفْسَهُ وَهَوَاهُ", "text": "Cihadın en faziletlisi, kişinin kendi nefsine ve arzularına karşı cihad etmesidir.", "src": "İbn Naccâr", "exp": "Ders: Manevi kahramanlık nefsi yenmektir."},
            {"id": 6, "ar": "المُجَاهِدُ مَنْ جَاهَدَ نَفْسَهُ فِي طَاعَةِ اللَّهِ", "text": "Mücahid, Allah'a itaatte nefsine karşı cihad eden kimsedir.", "src": "Tirmizî", "exp": "Ders: İbadetlerde devamlılık nefsi baskılamakla mümkündür."},
            {"id": 7, "ar": "لَيْسَ الشَّدِيدُ بِالصُُّرَعَةِ...", "text": "Güreşte rakibini yenen kuvvetli değildir; asıl kuvvetli, öfke anında nefsine hakim olandır.", "src": "Buhârî", "exp": "Ders: Öfke nefsani bir patlamadır, onu yenmek güç göstergesidir."},
            {"id": 8, "ar": "مَنْ حَفِظَ مَا بَيْنَ لَحْيَيْهِ وَرِجْلَيْهِ...", "text": "Kim dilini ve iffetini nefsinden korursa cennete girer.", "src": "Buhârî", "exp": "Ders: Dil ve şehvet nefs terbiyesinin kilit noktalarıdır."},
            {"id": 9, "ar": "ثَلاَثٌ مُهْلِكَاتٌ...", "text": "İnsanı felakete sürükleyen üç şey: İtaat edilen cimrilik, heva ve ucub (kendini beğenme).", "src": "Taberânî", "exp": "Ders: Ucub ve hırs nefsin helak edici tuzaklarıdır."},
            {"id": 10, "ar": "احْذَرُوا الظَّنَّ...", "text": "Zandan sakının, çünkü zan sözlerin en yalanıdır.", "src": "Buhârî", "exp": "Ders: Nefsin hüsn-i zan yerine su-i zanna yönelmesini engelleyin."},
            {"id": 11, "ar": "طُوبَى لِمَنْ شَغَلَهُ عَيْبُهُ...", "text": "Kendi kusurları ile uğraşmaktan insanların kusurlarını görmeye vakit bulamayana müjdeler olsun.", "src": "Bazzâr", "exp": "Ders: Nefis terbiyesi başkasını değil kendini incelemektir."},
            {"id": 12, "ar": "لاَ غَضَبْ وَلَكَ الْجَنَّةُ", "text": "Öfkelenme, cennet senindir.", "src": "Taberânî", "exp": "Ders: Nefsi öfke anında dizginlemek cennet vesilesidir."},
            {"id": 13, "ar": "مِنْ حُسْنِ إِسْلاَمِ الْمَرْءِ...", "text": "Kişinin malayani (faydasız) şeyleri terk etmesi İslam'ının güzelliğindendir.", "src": "Tirmizî", "exp": "Ders: Nefsi boş şeylerden çekmek manevi dinginlik verir."},
            {"id": 14, "ar": "حُفَّتِ الْجَنَّةُ بِالْمَكَارِهِ...", "text": "Cennet nefsin hoşuna gitmeyen şeylerle, cehennem ise nefsin arzularıyla çevrilmiştir.", "src": "Müslim", "exp": "Ders: Nefsin zorlandığı ameller cennetin anahtarıdır."},
            {"id": 15, "ar": "اتَّقِ اللَّهَ حَيْثُمَا كُنْتَ...", "text": "Nerede olursan ol Allah'tan kork ve kötülüğün ardından hemen iyilik yap.", "src": "Tirmizî", "exp": "Ders: Nefsin günahını hemen iyilikle telafi etmelidir."},
            {"id": 16, "ar": "الظُّلمُ ظُلُمَاتٌ...", "text": "Zulüm, kıyamet gününde karanlıklardır.", "src": "Buhârî", "exp": "Ders: Nefse uymak insana ve başkalarına zulümdür."},
            {"id": 17, "ar": "إِنَّ الصَّدَقَةَ لَتُطْفِئُ...", "text": "Şüphesiz sadaka Rabbin öfkesini söndürür.", "src": "Tirmizî", "exp": "Ders: Cömertlik nefsin cimriliğini kıran ilaçtır."},
            {"id": 18, "ar": "مَنْ تَوَاضَعَ لِلَّهِ...", "text": "Kim Allah için tevazu gösterirse Allah onu yükseltir.", "src": "Müslim", "exp": "Ders: Nefsi küçültmek manevi makamı büyütür."},
            {"id": 19, "ar": "إِيَّاكُمْ وَالْحَسَدَ...", "text": "Hasetten sakının, çünkü haset iyilikleri yer bitirir.", "src": "Ebû Dâvûd", "exp": "Ders: Nefsin kıskançlığı amelleri mahveder."},
            {"id": 20, "ar": "مَنْ صَمَتَ نَجَا", "text": "Susan kurtulmuştur.", "src": "Tirmizî", "exp": "Ders: Nefsin boş konuşma arzusunu sükutla yen."},
            {"id": 21, "ar": "إِنَّ العَبْدَ لَيَتَكَلَّمُ بِالكَلِمَةِ...", "text": "Kul, Allah'ın razı olmadığı bir sözü önemsemeden söyler de bu yüzden cehennemin dibine yuvarlanır.", "src": "Buhârî", "exp": "Ders: Dilin afetlerden nefsi korumak hayati önem taşır."},
            {"id": 22, "ar": "مَنْ كَانَ يُؤْمِنُ بِاللَّهِ...", "text": "Kim Allah'a ve ahiret gününe inanıyorsa ya hayır söylesin ya da sussun.", "src": "Buhârî", "exp": "Ders: Sükut nefsin en büyük sığınağıdır."},
            {"id": 23, "ar": "حَاسِبُوا أَنْفُسَكُمْ...", "text": "Hesaba çekilmeden önce nefsinizi hesaba çekin.", "src": "Tirmizî", "exp": "Ders: Öz denetim müminin her an şiarı olmalıdır."},
            {"id": 24, "ar": "الْتَّائِبُ مِنَ الذَّنْبِ...", "text": "Tövbe eden kimse hiç günah işlememiş gibidir.", "src": "İbn Mâce", "exp": "Ders: Tövbe kapısı nefsi her an temizleme imkanı sunar."},
            {"id": 25, "ar": "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِن عَجْزٍ وَكَسَلٍ", "text": "Allah'ım! Acizlikten ve tembellikten sana sığınırım.", "src": "Müslim", "exp": "Ders: Nefsin tembellik damarı dua ile kırılmalıdır."}
        ],
        "bediuzzaman": [
            {"id": 1, "ar": "Risale-i Nur - Sözler", "text": "Nefsini ıslah etmeyen, başkasını ıslah edemez. Öyle ise ilk önce kendi nefsinden başla!", "src": "21. Söz", "exp": "Ders: Başkasına nasihat etmeden önce kendi nefsimizi terbiye etmeliyiz."},
            {"id": 2, "ar": "Risale-i Nur - Sözler", "text": "Ey nefsim! Deme: 'Zaman değişmiş, asır başkalaşmış, herkes dünyaya daldı.' Ölüm değişmemiş.", "src": "14. Söz", "exp": "Ders: Zamanın bozulması nefsin bahanelerine mazeret olamaz."},
            {"id": 3, "ar": "Risale-i Nur - Lem'alar", "text": "Nefis daima kendisini tebrie etmek ister. Hatta en büyük kusuru görse, yüz tevil ile haklı çıkarır.", "src": "13. Lem'a", "exp": "Ders: Nefsin avukatlığını değil, savcılığını yapmak gerekir."},
            {"id": 4, "ar": "Risale-i Nur - Mektubat", "text": "Nefsini ittiham eden, kusurunu görür. Kusurunu gören istiğfar eder, istiğfar eden afvolunur.", "src": "26. Mektup", "exp": "Ders: Kurtuluş nefsini suçlu bilip tövbe etmektir."},
            {"id": 5, "ar": "Risale-i Nur - Sözler", "text": "Nefis ihlası bozar. İhlası kazanmanın çaresi, nefsin arzu ve hülyalarını kırmaktır.", "src": "21. Lem'a", "exp": "Ders: İhlas nefsi ayaklar altına almakla kazanılır."},
            {"id": 6, "ar": "Risale-i Nur - Şualar", "text": "Nefis, kendini hür ve müstakil bilir. Oysa o bir memurdur ve aciz bir kuldur.", "src": "15. Şua", "exp": "Ders: Hakiki hürriyet Allah'a kul olmakla nefse gem vurmaktır."},
            {"id": 7, "ar": "Risale-i Nur - Sözler", "text": "Nefis firavunlaşmak ister; ona verilecek en iyi ders, acz ve fakrını tanıtmaktır.", "src": "23. Söz", "exp": "Ders: İnsanın hakiki mahiyeti acziyet ve fakriyettir."},
            {"id": 8, "ar": "Risale-i Nur - Kastamonu", "text": "Nefsi emmareye itimat edilmez. Her an insanı günaha sevk edebilir.", "src": "Kastamonu Lahikası", "exp": "Ders: Son nefese kadar nefse karşı teyakkuzda olunmalıdır."},
            {"id": 9, "ar": "Risale-i Nur - Lem'alar", "text": "Nefis lezzeti ister; fakat o lezzetin içinde zehirli bir elem olduğunu bilmez.", "src": "17. Lem'a", "exp": "Ders: Haramlardaki geçici lezzet kalbi öldürür."},
            {"id": 10, "ar": "Risale-i Nur - Sözler", "text": "Nefis, ücreti peşin ister; vazifeyi ise tehir etmek ister.", "src": "21. Söz", "exp": "Ders: Nefsin tembellik ve peşincilik damarı kırılmalıdır."},
            {"id": 11, "ar": "Risale-i Nur - Mektubat", "text": "Nefis terbiyesi, onu öldürmekle değil, hayırlı işlere sevk etmekle olur.", "src": "Mektubat", "exp": "Ders: Nefsin enerjisi ibadete dönüştürülmelidir."},
            {"id": 12, "ar": "Risale-i Nur - Şualar", "text": "Nefsin en büyük bir hilesi, kendini kusursuz zannettirmektir.", "src": "Şualar", "exp": "Ders: Kusurunu bilmek en büyük kemalattır."},
            {"id": 13, "ar": "Risale-i Nur - Sözler", "text": "Dünyanın lezzetleri, zehirli bala benzer. Lezzeti kadar elemi vardır.", "src": "Sözler", "exp": "Ders: Nefsin dünyevi arzuları aldatıcıdır."},
            {"id": 14, "ar": "Risale-i Nur - Lem'alar", "text": "Ey nefsim! İbadet yapmak zor geliyorsa, kabrin darlığını ve ebedi azabı düşün.", "src": "Lem'alar", "exp": "Ders: İbadetlerin zorluğuna sabır nefse galip gelmektir."},
            {"id": 15, "ar": "Risale-i Nur - Tarihçe", "text": "Ben kendi nefsimi herkesten daha ziyade nasihate muhtaç görüyorum.", "src": "Tarihçe", "exp": "Ders: Tevazu nefis terbiyesinin meyvesidir."},
            {"id": 16, "ar": "Risale-i Nur - Sözler", "text": "Nefis, kendisini malik zanneder. Oysa her şeyin maliki Allah'tır.", "src": "30. Söz", "exp": "Ders: Sahiplik duygusundan vazgeçilmelidir."},
            {"id": 17, "ar": "Risale-i Nur - Lem'alar", "text": "Nefis terbiyesinde en kuvvetli siper rabıta-i mevt yani ölümü düşünmektir.", "src": "21. Lem'a", "exp": "Ders: Ölümü hatırlamak nefsi heveslerden vazgeçirir."},
            {"id": 18, "ar": "Risale-i Nur - Barla", "text": "Nefsin arzuları bir bahr-i bîpâyândır (uçsuz bucaksız denizdir), doyurulmaz.", "src": "Barla Lahikası", "exp": "Ders: Nefsin isteklerini doyurmaya çalışmak imkansızdır."},
            {"id": 19, "ar": "Risale-i Nur - Sözler", "text": "Cenab-ı Hakka vasıl olacak en kısa ve emniyetli yol: Acz, fakr, şefkat ve tefekkürdür.", "src": "26. Söz", "exp": "Ders: Nefsin gururunu acziyet bilinci kırar."},
            {"id": 20, "ar": "Risale-i Nur - Mektubat", "text": "Hakiki lezzet, acı çeken nefsi terbiye etmekte ve onu Hakk'a ram etmektedir.", "src": "Mektubat", "exp": "Ders: Ruhun lezzeti nefsin dizginlenmesindedir."},
            {"id": 21, "ar": "Risale-i Nur - Mesnevi-i Nuriye", "text": "Nefis, tarziye ve taltif istedikçe, onu şükür ve kanaat kamçısıyla tahdit et.", "src": "Mesnevi-i Nuriye", "exp": "Ders: Kanaat nefsin doyumsuzluğunu durdurur."},
            {"id": 22, "ar": "Risale-i Nur - Lem'alar", "text": "Ey insan! Nefis ve şeytan seni aldatmasın. Hakiki saadet Allah'a abd olmaktadır.", "src": "Lem'alar", "exp": "Ders: Kulluk şerefi her makamın üstündedir."},
            {"id": 23, "ar": "Risale-i Nur - Sözler", "text": "Nefsine rıza gösteren, başka kimseden razı olamaz.", "src": "Sözler", "exp": "Ders: Başkalarını eleştirmek yerine nefsi ıslah et."},
            {"id": 24, "ar": "Risale-i Nur - Mektubat", "text": "İnsanın en büyük hilesi, gurur ve enaniyet perdesi altında kusurunu örtmesidir.", "src": "Mektubat", "exp": "Ders: Gurur, manevi terakkinin en büyük engelidir."},
            {"id": 25, "ar": "Risale-i Nur - Şualar", "text": "Nefsin mizaç ve hevesine tabi olan, hidayet yolunu kaybeder.", "src": "Şualar", "exp": "Ders: Heva ve heves rehber edinilemez."}
        ],
        "veliler": [
            {"id": 1, "ar": "İmam-ı Gazalî (r.a.)", "text": "Nefsini terbiye etmeyen kimseden hakiki dost olmaz. Nefis bin bir hileli bir yılandır.", "src": "İhyâ", "exp": "Ders: Nefis sürekli kontrol edilmesi gereken tehlikeli bir güçtür."},
            {"id": 2, "ar": "Hz. Mevlânâ (k.s.)", "text": "Nefis bir ejderhadır, donmuş görünür ama fırsat bulunca hemen canlanır. Riyazetle erit.", "src": "Mesnevî", "exp": "Ders: Nefsin durgun görünmesine aldanılmamalıdır."},
            {"id": 3, "ar": "Şah-ı Nakşibend (k.s.)", "text": "Bizim yolumuz nefsine muhalefet etme yoludur. Nefis ne isterse zıddını yapmak hakikattir.", "src": "Risale-i Kudsiyye", "exp": "Ders: Nefsin isteklerine muhalefet ruhu yüceltir."},
            {"id": 4, "ar": "Abdülkâdir-i Geylânî (k.s.)", "text": "Nefsine galip gelen kimse, bütün dünyayı fethetsen daha büyüktür.", "src": "Fütûhu'l-Gayb", "exp": "Ders: İçsel zafer dışsal zaferlerin üstündedir."},
            {"id": 5, "ar": "Hasan-ı Basrî (r.h.)", "text": "Nefse gem vurmak, onu kılıçla doğramaktan daha zordur.", "src": "Hikmetler", "exp": "Ders: Nefisle mücadele sürekli ve kararlı sabır ister."},
            {"id": 6, "ar": "İbn-i Ataullah (k.s.)", "text": "Nefsinin gizli şehvetlerinden biri de yaptığı ibadetle gururlanmasıdır.", "src": "Hıkem", "exp": "Ders: İbadetlere güvenmek nefsin ince bir tuzağıdır."},
            {"id": 7, "ar": "İbrahim b. Edhem (k.s.)", "text": "Nefsini açlıkla terbiye etmeyen, onun hevasını kıramaz.", "src": "Siyer", "exp": "Ders: Az yemek nefsani tutkuları zayıflatır."},
            {"id": 8, "ar": "Yunus Emre (r.h.)", "text": "Nefstir seni yolda koyan, nefsine uyma ey can!", "src": "Divan", "exp": "Ders: Manevi yolculuğun tek engeli nefistir."},
            {"id": 9, "ar": "Ahmet Yesevî (k.s.)", "text": "Nefsi kırıp mütevazı olmak er kişinin kârıdır.", "src": "Divan-ı Hikmet", "exp": "Ders: Tevazu nefsin ilacıdır."},
            {"id": 10, "ar": "Bişr-i Hafî (k.s.)", "text": "Nefsim benden bir şey istediğinde ona vermemek için direnirim.", "src": "Tabakat", "exp": "Ders: Nefse 'hayır' diyebilmek ruhu özgürleştirir."},
            {"id": 11, "ar": "Cüneyd-i Bağdâdî (k.s.)", "text": "Nefsin arzusuna uymak, kalbi karartan en büyük perdedir.", "src": "Risale", "exp": "Ders: Günahlar kalp gözünü kapatır."},
            {"id": 12, "ar": "Zünnûn-ı Mısrî (k.s.)", "text": "Nefsin helaki, onun her istediğini ona vermektir.", "src": "Hikmetler", "exp": "Ders: Nefsi şımartmak onu felakete götürür."},
            {"id": 13, "ar": "Bayezid-i Bistâmî (k.s.)", "text": "Nefsimi Hakk'a çağırdım, direndi. Ben de onu dünyadan mahrum bıraktım.", "src": "Tazkirat", "exp": "Ders: Nefsi terbiye için kararlı duruş şarttır."},
            {"id": 14, "ar": "İmam Rabbani (k.s.)", "text": "Nefsin arzuları Allah'ın rızasına zıttır. İki zıt bir arada olamaz.", "src": "Mektubat", "exp": "Ders: Allah'ın rızası nefse muhalefettedir."},
            {"id": 15, "ar": "Fudayl b. İyâz (k.s.)", "text": "İnsanların en acizi, nefsini dizginlemekten aciz olan kimsedir.", "src": "Zühd", "exp": "Ders: Gerçek zayıflık nefse yenilmektir."},
            {"id": 16, "ar": "Sırrı-yı Sekatî (k.s.)", "text": "Nefsine uyan kimseden hikmet beklenmez.", "src": "Tabakat", "exp": "Ders: Hikmet temiz bir nefiste tecelli eder."},
            {"id": 17, "ar": "Yahya b. Muaz (k.s.)", "text": "Nefsinle cihad et; onun en büyük silahı cehalettir.", "src": "Hikmetler", "exp": "Ders: Nefsi ilim ve irfanla mağlup et."},
            {"id": 18, "ar": "Ömer b. Abdülaziz (r.h.)", "text": "Nefsini hesaba çeken karlı çıkar, gafil olan zarara uğrar.", "src": "Siyer", "exp": "Ders: Günlük nefis muhasebesi kurtuluş yoludur."},
            {"id": 19, "ar": "İmam-ı Şafiî (r.h.)", "text": "Sen nefsini hak ile meşgul etmezsen, o seni batıl ile meşgul eder.", "src": "Divan", "exp": "Ders: Boş kalmamak, hayırla meşgul olmak gerekir."},
            {"id": 20, "ar": "Aziz Mahmud Hüdayi (k.s.)", "text": "Nefsin sarayını yık ki, ruhun sarayı inşa olsun.", "src": "Hikmetler", "exp": "Ders: Nefsi arzuları terk etmek ruhu diriltir."},
            {"id": 21, "ar": "Şeyh Şaban-ı Veli (k.s.)", "text": "Gelişiniz güle güle, gidişiniz güle güle, her işiniz Allah ile olsun.", "src": "Hikmetler", "exp": "Ders: Bütün amellerde Allah rızası gözetilmelidir."},
            {"id": 22, "ar": "Hacı Bektaş-ı Veli (k.s.)", "text": "Nefsini bilen, Rabbini bilir. Eline, beline, diline sahip ol.", "src": "Makalat", "exp": "Ders: Ahlakın temeli nefsani zaafları denetlemektir."},
            {"id": 23, "ar": "Somuncu Baba (k.s.)", "text": "İnsanların en hayırlısı, nefsini en çok tenkit eden ve hesaba çekendir.", "src": "Tabakat", "exp": "Ders: Öz eleştiri kamil insanların özelliğidir."},
            {"id": 24, "ar": "Ebu Bekir Sıddık (r.a.)", "text": "Dilinizi tutun; çünkü bu dünyada insanı en çok hataya düşüren şey dildir.", "src": "Siyer", "exp": "Ders: Sükut en büyük koruyucudur."},
            {"id": 25, "ar": "Ömer b. Hattâb (r.a.)", "text": "Hesaba çekilmeden önce kendinizi hesaba çekin ve amellerinizi tartın.", "src": "Tarih", "exp": "Ders: Daimi murakabe ruhu diri tutar."}
        ],
        "ameli": [
            {"id": 1, "ar": "Pratik Adım 1: Sükut ve Dili Koruma", "text": "Günde en az 1 saat lüzumsuz konuşmayı kes. Gıybet nefsi besler.", "src": "Dil Terbiyesi", "exp": "Uygulama: Konuşmadan önce 'Bu sözde Allah rızası var mı?' diye sor."},
            {"id": 2, "ar": "Pratik Adım 2: Göz İffeti", "text": "Haram veya malayani görsellere bakmaktan sakın. Göz nefsin en açık kapısıdır.", "src": "Göz Terbiyesi", "exp": "Uygulama: Bakışını hemen başka yöne çevir ve istigfar et."},
            {"id": 3, "ar": "Pratik Adım 3: Az Yemek (Kıllet-i Taam)", "text": "Mideyi tam doldurmama prensibini uygula. Doymadan sofradan kalk.", "src": "Mide Terbiyesi", "exp": "Uygulama: Haftada 1-2 gün oruç tut veya hafif geçir."},
            {"id": 4, "ar": "Pratik Adım 4: Gece İbadeti (Teheccüd)", "text": "Nefsin uykuda olduğu saatlerde kalkıp 2 rekat dahi olsa namaz kıl.", "src": "Ruh Terbiyesi", "exp": "Uygulama: Gece nefsini uykudan söküp almak onun belini kırar."},
            {"id": 5, "ar": "Pratik Adım 5: Sadaka ve İnfak", "text": "Nefsin en çok sevdiği malı Allah yolunda karşılıksız ver.", "src": "Mal Terbiyesi", "exp": "Uygulama: Cimrilik hissettiğin an gizlice sadaka ver."},
            {"id": 6, "ar": "Pratik Adım 6: Öfke Kontrolü", "text": "Öfkelendiğin an duruşunu değiştir; ayaktaysan otur, abdest al.", "src": "Halkla İlişkiler", "exp": "Uygulama: Haklı olsan dahi tartışmayı uzatma."},
            {"id": 7, "ar": "Pratik Adım 7: Rabıta-i Mevt", "text": "Her gün 5 dakika kendi cenaze namazının kılındığını ve kabre konduğunu hayal et.", "src": "Tefekkür", "exp": "Uygulama: Tûl-i emeli kırar."},
            {"id": 8, "ar": "Pratik Adım 8: Kendi Kusurlarını Listele", "text": "Başkasını eleştirmeyi bırak. Bir deftere kendi 5 olumsuz huyunu yaz.", "src": "Muhasebe", "exp": "Uygulama: Kibirden kurtulmanın en pratik yoludur."},
            {"id": 9, "ar": "Pratik Adım 9: Nefse Muhalefet Tekniği", "text": "Nefsin canı ne zaman boş bir şey yapmak isterse, ona 2 rekat namaz kılma cezası ver.", "src": "Disiplin", "exp": "Uygulama: Nefis ceza alacağını anlayınca pes eder."},
            {"id": 10, "ar": "Pratik Adım 10: Tevazu Eylemleri", "text": "Toplumda kendinden alt konumdaki kişilere hizmet et, alçakgönüllü işler yap.", "src": "Ahlak", "exp": "Uygulama: Gurur ve kibri doğrudan yok eder."},
            {"id": 11, "ar": "Pratik Adım 11: Zikirle Kalbi Diri Tutmak", "text": "Günde en az 100 defa 'La ilahe illallah' ve 'Estagfirullah' çek.", "src": "Kalp Terbiyesi", "exp": "Uygulama: Kalp zikirle nurlanır, nefis zayıflar."},
            {"id": 12, "ar": "Pratik Adım 12: Şikayet Etmeyi Bırakmak", "text": "Başına gelen sıkıntılarda insanlara şikayetçi olma, sadece Allah'a iltica et.", "src": "Sabır", "exp": "Uygulama: Rıza makamına ulaştırır."},
            {"id": 13, "ar": "Pratik Adım 13: Salihlerle Beraber Olmak", "text": "Maneviyatı yüksek insanlarla vakit geçir, gafil ortamlardan uzak dur.", "src": "Çevre Terbiyesi", "exp": "Uygulama: Çevre nefsi doğrudan etkiler."},
            {"id": 14, "ar": "Pratik Adım 14: İyiliğe Karşılık Beklememek", "text": "Yaptığın hiçbir hayır için teşekkür veya övgü bekleme.", "src": "İhlas", "exp": "Uygulama: Ucub hastalığını engeller."},
            {"id": 15, "ar": "Pratik Adım 15: Ekran ve Medya Diyeti", "text": "Sosyal medya ve lüzumsuz dijital içerik kullanımını günde 30 dakikaya indir.", "src": "Dijital Terbiye", "exp": "Uygulama: Zihni gereksiz görsellerden temizler."},
            {"id": 16, "ar": "Pratik Adım 16: Affetme Egzersizi", "text": "Sana kötülük eden kimseden nefsin intikam almak istediğinde onu Allah için affet.", "src": "Ahlak", "exp": "Uygulama: Nefsin kin duygusunu yok eder."},
            {"id": 17, "ar": "Pratik Adım 17: Vakit Disiplini", "text": "Günün 24 saatini planla. Boş vakit nefsin en büyük oyun alanıdır.", "src": "Zaman Yönetimi", "exp": "Uygulama: Boş duranı şeytan işgal eder."},
            {"id": 18, "ar": "Pratik Adım 18: Şüpheli Şeylerden Kaçınmak", "text": "Sadece haramdan değil, harama düşme riski olan şüpheli şeylerden uzak dur.", "src": "Takva", "exp": "Uygulama: Hakiki takva şüpheliyi terk etmektir."},
            {"id": 19, "ar": "Pratik Adım 19: İbadetleri Huşu İle Yapmak", "text": "Namaz kılarken son namazınmış gibi kıl, ayetlerin manasını düşün.", "src": "Huşu", "exp": "Uygulama: Şekilsel ibadetten ruha geçiştir."},
            {"id": 20, "ar": "Pratik Adım 20: Daimi Dua Ve İltica", "text": "Her gün: 'Allah'ım! Nefsimi bana bir göz kırpması kadar bile bırakma!' diye dua et.", "src": "Dua", "exp": "Uygulama: Peygamberimizin en çok yaptığı duadır."},
            {"id": 21, "ar": "Pratik Adım 21: Açlık ve Riyazet", "text": "Ayda en az birkaç gün az yemek yiyerek nefsin şehvet damarlarını kurut.", "src": "Riyazet", "exp": "Uygulama: Tokluk nefsi azdırır, açlık incesini inceltir."},
            {"id": 22, "ar": "Pratik Adım 22: Gece Yalnızlığı (Halvet)", "text": "Gecenin karanlığında teheccüt vakti Rabbi ile baş başa kal.", "src": "Halvet", "exp": "Uygulama: Kalbin gözü yalnızlıkta açılır."},
            {"id": 23, "ar": "Pratik Adım 23: İtiraf ve Pişmanlık", "text": "Günün sonunda secdeye kapanıp hatalarını itiraf et.", "src": "Tövbe", "exp": "Uygulama: Secde nefsani gururu yere serer."},
            {"id": 24, "ar": "Pratik Adım 24: Kötülüğe İyilikle Karşılık", "text": "Sana kötülük edene dua et, mukabelede bulunma.", "src": "Ahlak-ı Muhammedi", "exp": "Uygulama: Kalpteki düşmanlık tohumlarını kurutur."},
            {"id": 25, "ar": "Pratik Adım 25: Hamd ve Şükür Murakabesi", "text": "Sahip olduğun nimetleri say ve her nefes için şükret.", "src": "Şükür", "exp": "Uygulama: Şükür nimeti artırır, nefsi kanaatkar kılar."}
        ],
        "cetel": [
            "Bugün 5 vakit namazımı huşu içinde kıldım mı?",
            "Bugün dilimi gıybet, yalan ve boş konuşmaktan korudum mu?",
            "Bugün haram ve malayani görsellere bakmaktan gözümü sakındım mı?",
            "Bugün öfkelendiğim an nefsime hakim olabildim mi?",
            "Bugün nefsime muhalefet edip az yemek ve cömertlik gösterdim mi?",
            "Bugün Kur'an-ı Kerim okuyup manasını tefekkür ettim mi?",
            "Bugün ölümü ve kabir hayatını zihninizden geçirdiniz mi?",
            "Bugün amellerimde riya ve ucubtan uzak durup ihlası aradım mı?",
            "Bugün insanlara karşı mütevazı olup kibrimi kırdım mı?",
            "Bugün yatmadan önce günün muhasebesini yapıp tövbe ettim mi?"
        ]
    },
    "en": {
        "title": "SELF-PURIFICATION LIBRARY",
        "subtitle": "Spiritual Growth & Ego Discipline Archive",
        "search_label": "Search for Verses, Hadiths or Wisdom...",
        "tabs": ["Quranic Verses (25)", "Hadiths (25)", "Bediuzzaman Said Nursi (25)", "Saints Wisdom (25)", "Practical Discipline Guide (25)", "Murakaba Checklist", "📋 Sharing Guidelines"],
        "sidebar_title": "📌 Modules",
        "sleep_note": "💡 *Note:* This web application is hosted on free servers. When left inactive for a long time, the app may go to sleep (showing a 'Zzzz' icon on the screen).\n\n💤 If you encounter such a screen, click the blue *'Yes, get this app back up!'* button and wait 15-30 seconds for it to wake up.",
        "notice_title": "📜 Sharing Principles & Guidelines",
        "notice_p1": "This digital archive library has been designed to provide scholarly compilations, spiritual texts, and personal development guides for educational, contemplative, and individual spiritual awareness purposes.",
        "notice_p2": "**1. Scope of Use:** These contents are shared to support personal contemplation, learning, and spiritual growth processes.",
        "notice_p3": "**2. Sharing Mindset:** This application is entirely focused on individual learning and social benefit; it is non-commercial and not intended for commercial activities.",
        "notice_p4": "**3. Reminder:** The provided contents are solely for individual spiritual discipline and personal reflection, curated to guide users on their inner journeys.",
        "checklist_title": "📊 Daily Murakaba & Ego Audit Checklist",
        "checklist_desc": "Evaluate your soul at the end of each day based on the following criteria:",
        "checklist_btn": "Save Murakaba Audit Report",
        "checklist_success": "Your spiritual audit has been saved. May Allah grant you the station of the reassured soul (Nefs-i Mutmainne).",
        "source_label": "Source",
        "lesson_label": "Spiritual Lesson",
        "ayet": [
            {"id": 1, "ar": "وَمَا أُبَرِّئُ نَفْسِي إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ إِلَّا مَا رَحِمَ رَبِّي", "text": "And I do not acquit myself. Indeed, the soul is a persistent enjoiner of evil.", "src": "Surah Yusuf, 53", "exp": "Lesson: Never trust the ego; recognizing its flaws is the beginning of purification."},
            {"id": 2, "ar": "وَنَهَى النَّفْسَ عَنِ الْهَوَى فَإِنَّ الْجَنَّةَ هِيَ الْمَأْوَى", "text": "And restrained the soul from lower desire, then indeed, Paradise will be the refuge.", "src": "Surah An-Nazi'at, 40-41", "exp": "Lesson: The path to Paradise requires guarding against lower desires."},
            {"id": 3, "ar": "قَدْ أَفْلَحَ مَن زَكَّاهَا وَقَدْ خَابَ مَن دَسَّاهَا", "text": "He has succeeded who purifies it, and he has failed who instills it with corruption.", "src": "Surah Ash-Shams, 9-10", "exp": "Lesson: True success lies in cleansing the inner self."},
            {"id": 4, "ar": "يَا أَيَّتُهَا النَّفْسُ الْمُطْمَئِنَّةُ ارْجِعِي إِلَى رَبِّكِ رَاضِيَةً مَّرْضِيَّةً", "text": "O reassured soul, return to your Lord, well-pleased and pleasing!", "src": "Surah Al-Fajr, 27-28", "exp": "Lesson: Inner peace and divine consent are achieved through self-discipline."},
            {"id": 5, "ar": "وَلَا أُقْسِمُ بِالنَّفْسِ اللَّوَّامَةِ", "text": "And I swear by the self-reproaching soul.", "src": "Surah Al-Qiyamah, 2", "exp": "Lesson: Self-criticism and moral accountability are a believer's shield."},
            {"id": 6, "ar": "أَفَرَأَيْتَ مَنِ اتَّخَذَ إِلَهَهُ هَوَاهُ", "text": "Have you seen he who has taken as his god his own desire?", "src": "Surah Al-Jathiyah, 23", "exp": "Lesson: Unchecked ego obedience resembles hidden idolatry."},
            {"id": 7, "ar": "وَاعْلَمُوا أَنَّ اللَّهَ يَعْلَمُ مَا فِي أَنفُسِكُمْ فَاحْذَرُوهُ", "text": "And know that Allah knows what is within yourselves, so beware of Him.", "src": "Surah Al-Baqarah, 235", "exp": "Lesson: Keep your heart and inner thoughts pure from hidden malice."},
            {"id": 8, "ar": "وَالَّذِينَ جَاهَدُوا فِينَا لَنَهْدِيَنَّهُمْ سُبُلَنَا", "text": "And those who strive for Us - We will surely guide them to Our ways.", "src": "Surah Al-Ankabut, 69", "exp": "Lesson: Striving against the ego opens the doors of divine guidance."},
            {"id": 9, "ar": "الَّذِي خَلَقَ الْمَوْتَ وَالْحَيَاةَ لِيَبْلُوَكُمْ أَيُّكُمْ أَحْسَنُ عَمَلًا", "text": "Who created death and life to test you as to which of you is best in deed.", "src": "Surah Al-Mulk, 2", "exp": "Lesson: Earthly life is an ongoing trial of mastering the self."},
            {"id": 10, "ar": "وَفِي أَنفُسِكُمْ أَفَلَا تُبْصِرُونَ", "text": "And in yourselves. Then will you not see?", "src": "Surah Adh-Dhariyat, 21", "exp": "Lesson: Reflect deeply on your inner spiritual state."},
            {"id": 11, "ar": "إِنَّ اللَّهَ لَا يُغَيِّرُ مَا بِقَوْمٍ حَتَّى يُغَيِّرُوا مَا بِأَنفُسِهِمْ", "text": "Indeed, Allah will not change a people's condition until they change what is in themselves.", "src": "Surah Ar-Ra'd, 11", "exp": "Lesson: Reforming the outer world begins with inner transformation."},
            {"id": 12, "ar": "يَا أَيُّهَا الَّذِينَ آمَنُوا اتَّقُوا اللَّهَ وَلْتَنظُرْ نَفْسٌ مَّا قَدَّمَتْ لِغَدٍ", "text": "O you who have believed, fear Allah. And let every soul look to what it has put forth for tomorrow.", "src": "Surah Al-Hashr, 18", "exp": "Lesson: Constantly audit yourself for the Hereafter."},
            {"id": 13, "ar": "مَّا أَصَابَكَ مِنْ حَسَنَةٍ فَمِنَ اللَّهِ وَمَا أَصَابَكَ مِن سَيِّئَةٍ فَمِن نَّفْسِكَ", "text": "What comes to you of good is from Allah, but what comes to you of evil, is from yourself.", "src": "Surah An-Nisa, 79", "exp": "Lesson: Attribute virtues to God and shortcomings to your ego."},
            {"id": 14, "ar": "وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِ وَنَهَى النَّفْسَ عَنِ الْهَوَى", "text": "But as for he who feared the position of his Lord and prevented the soul from lower desire...", "src": "Surah An-Nazi'at, 40", "exp": "Lesson: Fear of God is the greatest brake on the ego."},
            {"id": 15, "ar": "وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُ عَن ذِكْرِنَا وَاتَّبَعَ هَوَاهُ", "text": "And do not obey one whose heart We have made heedless of Our remembrance and who follows his desire.", "src": "Surah Al-Kahf, 28", "exp": "Lesson: Distance yourself from those enslaved by vain desires."},
            {"id": 16, "ar": "بَلِ الْإِنسَانُ عَلَى نَفْسِهِ بَصِيرَةٌ", "text": "Rather, man, against himself, will be a witness.", "src": "Surah Al-Qiyamah, 14", "exp": "Lesson: Everyone is ultimately aware of their own hidden faults."},
            {"id": 17, "ar": "وَاصْبِرْ نَفْسَكَ مَعَ الَّذِينَ يَدْعُونَ رَبَّهُم", "text": "And keep yourself patient [by being] with those who call upon their Lord morning and evening.", "src": "Surah Al-Kahf, 28", "exp": "Lesson: Righteous companionship helps tame the ego."},
            {"id": 18, "ar": "مَن كَفَرَ فَعَلَيْهِ كُفْرُهُ وَمَنْ عَمِلَ صَالِحًا فَلِأَنفُسِهِمْ يَمْهَدُونَ", "text": "Whoever disbelieves - upon him is [the consequence of] his disbelief. And whoever does righteousness - for themselves they are preparing.", "src": "Surah Ar-Rum, 44", "exp": "Lesson: Every good deed is an investment in your soul's salvation."},
            {"id": 19, "ar": "وَاللَّهُ يَدْعُو إِلَى دَارِ السَّلَامِ", "text": "And Allah invites to the Home of Peace (Paradise).", "src": "Surah Yunus, 25", "exp": "Lesson: Choose eternal peace over transient ego pleasures."},
            {"id": 20, "ar": "إِنَّ النَّفْسَ لَأَمَّارَةٌ بِالسُّوءِ", "text": "Indeed, the soul is a persistent enjoiner of evil.", "src": "Surah Yusuf, 53", "exp": "Lesson: Your most dangerous adversary is within."},
            {"id": 21, "ar": "يَا أَيُّهَا النَّاسُ اتَّقُوا رَبَّكُمْ وَاخْشَوْا يَوْمًا لَّا يَجْزِي وَالِدٌ عَن وَلَدِهِ", "text": "O people, fear your Lord and fear a Day when no father will recompense his son.", "src": "Surah Luqman, 33", "exp": "Lesson: Saving one's own soul is the ultimate priority."},
            {"id": 22, "ar": "وَاتَّقُوا يَوْمًا تُرْجَعُونَ فِيهِ إِلَى اللَّهِ", "text": "And fear a Day in which you will be returned to Allah.", "src": "Surah Al-Baqarah, 281", "exp": "Lesson: Mindfulness of final accountability curbs the ego."},
            {"id": 23, "ar": "وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ", "text": "And whoever fears Allah - He will make for him a way out and provide for him from where he does not expect.", "src": "Surah At-Talaq, 2-3", "exp": "Lesson: God opens pathways for those with inner piety."},
            {"id": 24, "ar": "وَمَن يُوقَ شُحَّ نَفْسِهِ فَأُولَئِكَ هُمُ الْمُفْلِحُونَ", "text": "And whoever is protected from the stinginess of his soul - it is those who will be the successful.", "src": "Surah Al-Hashr, 9", "exp": "Lesson: Generosity is the cure for egoistic greed."},
            {"id": 25, "ar": "وَاعْلَمُوا أَنَّ اللَّهَ يَحُولُ بَيْنَ الْمَرْءِ وَقَلْبِهِ", "text": "And know that Allah intervenes between a man and his heart.", "src": "Surah Al-Anfal, 24", "exp": "Lesson: Hearts are in God's hands; surrender your heart to Him."}
        ],
        "hadis": [
            {"id": 1, "ar": "الْكَيِّسُ مَنْ دَانَ نَفْسَهُ وَعَمِلَ لِمَا بَعْدَ الْمَوْتِ", "text": "The wise person is one who holds himself accountable and works for what comes after death.", "src": "Tirmidhi", "exp": "Lesson: True intelligence is mastering your ego."},
            {"id": 2, "ar": "رَجَعْنَا مِنَ الْجِهَادِ الأَصْغَرِ إِلَى الْجِهَادِ الأَكْبَرِ", "text": "We have returned from the lesser jihad to the greater jihad (the struggle against the self).", "src": "Bayhaqi", "exp": "Lesson: The most challenging battle is the internal struggle against desires."},
            {"id": 3, "ar": "أَعْدَى عَدُوِّكَ نَفْسُكَ الَّتِي بَيْنَ جَنْبَيْكَ", "text": "Your greatest enemy is your ego which is between your sides.", "src": "Ajluni", "exp": "Lesson: Human beings' fiercest rival resides within themselves."},
            {"id": 4, "ar": "لاَ يُؤْمِنُ أَحَدُكُمْ حَتَّى يَكُونَ هَوَاهُ تَبَعًا لِمَا جِئْتُ بِهِ", "text": "None of you truly believes until his desires conform to what I have brought.", "src": "Nawawi", "exp": "Lesson: True faith requires subordinating personal desires to divine guidance."},
            {"id": 5, "ar": "أَفْضَلُ الْجِهَادِ أَنْ يُجَاهِدَ الرَّجُلُ نَفْسَهُ وَهَوَاهُ", "text": "The best jihad is when a man strives against his own self and desires for the sake of Allah.", "src": "Ibn Najjar", "exp": "Lesson: Spiritual heroism is conquering your internal impulses."},
            {"id": 6, "ar": "المُجَاهِدُ مَنْ جَاهَدَ نَفْسَهُ فِي طَاعَةِ اللَّهِ", "text": "The true mujahid is the one who strives against his ego in obedience to Allah.", "src": "Tirmidhi", "exp": "Lesson: Steadfastness in worship requires suppressing egoistic resistance."},
            {"id": 7, "ar": "لَيْسَ الشَّدِيدُ بِالصُُّرَعَةِ...", "text": "The strong person is not the one who overcomes people in wrestling, but the one who controls himself when angry.", "src": "Bukhari", "exp": "Lesson: Managing anger demonstrates real inner strength."},
            {"id": 8, "ar": "مَنْ حَفِظَ مَا بَيْنَ لَحْيَيْهِ وَرِجْلَيْهِ...", "text": "Whoever protects what is between his jaws (tongue) and what is between his legs (chastity) will enter Paradise.", "src": "Bukhari", "exp": "Lesson: Controlling speech and desires are keys to spiritual safety."},
            {"id": 9, "ar": "ثَلاَثٌ مُهْلِكَاتٌ...", "text": "Three things are destructive: greed that is obeyed, desires that are followed, and a person's self-admiration.", "src": "Tabarani", "exp": "Lesson: Arrogance and greed ruin spiritual growth."},
            {"id": 10, "ar": "احْذَرُوا الظَّنَّ...", "text": "Beware of suspicion, for suspicion is the falsest of speech.", "src": "Bukhari", "exp": "Lesson: Prevent your ego from leaning towards unfounded assumptions."},
            {"id": 11, "ar": "طُوبَى لِمَنْ شَغَلَهُ عَيْبُهُ...", "text": "Glad tidings to the one whose own faults keep him too busy to notice the faults of others.", "src": "Bazzar", "exp": "Lesson: Self-examination is far more fruitful than judging others."},
            {"id": 12, "ar": "لاَ غَضَبْ وَلَكَ الْجَنَّةُ", "text": "Do not become angry, and Paradise will be yours.", "src": "Tabarani", "exp": "Lesson: Curbing anger at the moment of provocation earns Paradise."},
            {"id": 13, "ar": "مِنْ حُسْنِ إِسْلاَمِ الْمَرْءِ...", "text": "An aspect of a person's good Islam is leaving alone that which does not concern him.", "src": "Tirmidhi", "exp": "Lesson: Detaching from idle matters brings inner peace."},
            {"id": 14, "ar": "حُفَّتِ الْجَنَّةُ بِالْمَكَارِهِ...", "text": "Paradise is surrounded by adversities, and Hellfire is surrounded by desires.", "src": "Muslim", "exp": "Lesson: Enduring what the ego dislikes leads to Paradise."},
            {"id": 15, "ar": "اتَّقِ اللَّهَ حَيْثُمَا كُنْتَ...", "text": "Fear Allah wherever you are, and follow up a bad deed with a good deed so as to wipe it out.", "src": "Tirmidhi", "exp": "Lesson: Immediately offset any lapse with virtue."},
            {"id": 16, "ar": "الظُّلمُ ظُلُمَاتٌ...", "text": "Injustice will be darkness on the Day of Resurrection.", "src": "Bukhari", "exp": "Lesson: Submitting to selfish desires results in inner and outer injustice."},
            {"id": 17, "ar": "إِنَّ الصَّدَقَةَ لَتُطْفِئُ...", "text": "Indeed, charity extinguishes the anger of the Lord.", "src": "Tirmidhi", "exp": "Lesson: Generosity breaks the stinginess of the ego."},
            {"id": 18, "ar": "مَنْ تَوَاضَعَ لِلَّهِ...", "text": "Whoever humbles himself for the sake of Allah, Allah elevates him.", "src": "Muslim", "exp": "Lesson: Lowering your ego before God elevates your spiritual rank."},
            {"id": 19, "ar": "إِيَّاكُمْ وَالْحَسَدَ...", "text": "Beware of envy, for envy consumes good deeds just as fire consumes wood.", "src": "Abu Dawud", "exp": "Lesson: Jealousy destroys spiritual achievements."},
            {"id": 20, "ar": "مَنْ صَمَتَ نَجَا", "text": "Whoever remains silent is saved.", "src": "Tirmidhi", "exp": "Lesson: Silence conquers the ego's urge to boast."},
            {"id": 21, "ar": "إِنَّ العَبْدَ لَيَتَكَلَّمُ بِالكَلِمَةِ...", "text": "A servant speaks a word that displeases Allah without paying heed to it, and because of it he slips down into Hell.", "src": "Bukhari", "exp": "Lesson: Guarding your tongue is of vital importance."},
            {"id": 22, "ar": "مَنْ كَانَ يُؤْمِنُ بِاللَّهِ...", "text": "Whoever believes in Allah and the Last Day, let him speak good or remain silent.", "src": "Bukhari", "exp": "Lesson: Silence is the safest refuge for the soul."},
            {"id": 23, "ar": "حَاسِبُوا أَنْفُسَكُمْ...", "text": "Call yourselves to account before you are called to account.", "src": "Tirmidhi", "exp": "Lesson: Ongoing self-audit should be a believer's habit."},
            {"id": 24, "ar": "الْتَّائِبُ مِنَ الذَّنْبِ...", "text": "The one who repents from sin is like one who has committed no sin.", "src": "Ibn Majah", "exp": "Lesson: Repentance offers a fresh start every moment."},
            {"id": 25, "ar": "اللَّهُمَّ إِنِّي أَعُوذُ بِكَ مِن عَجْزٍ وَكَسَلٍ", "text": "O Allah, I seek refuge in You from helplessness and laziness.", "src": "Muslim", "exp": "Lesson: Overcome sluggishness and spiritual inertia through prayer."}
        ],
        "bediuzzaman": [
            {"id": 1, "ar": "Risale-i Nur - The Words", "text": "He who cannot reform his own self cannot reform others. Therefore, begin with your own self!", "src": "The Twenty-First Word", "exp": "Lesson: Self-correction must precede guiding others."},
            {"id": 2, "ar": "Risale-i Nur - The Words", "text": "O my soul! Do not say: 'Times have changed, everyone is drowned in worldliness.' For death has not changed.", "src": "The Fourteenth Word", "exp": "Lesson: Societal decline is no excuse for spiritual negligence."},
            {"id": 3, "ar": "Risale-i Nur - The Flashes", "text": "The ego always wants to justify itself, defending its flaws with a hundred excuses.", "src": "The Thirteenth Flash", "exp": "Lesson: Be your ego's prosecutor, not its defense attorney."},
            {"id": 4, "ar": "Risale-i Nur - The Letters", "text": "He who accuses his ego sees his flaws. He who sees his flaws seeks forgiveness, and he who seeks forgiveness finds salvation.", "src": "The Twenty-Sixth Letter", "exp": "Lesson: True redemption comes from acknowledging personal weakness."},
            {"id": 5, "ar": "Risale-i Nur - The Words", "text": "The ego destroys sincerity. The remedy is crushing the ego's illusions and desires.", "src": "The Twenty-First Flash", "exp": "Lesson: Sincerity is achieved by humbling the ego."},
            {"id": 6, "ar": "Risale-i Nur - The Rays", "text": "The ego considers itself independent, whereas it is merely a helpless servant.", "src": "The Fifteenth Ray", "exp": "Lesson: True freedom is found in submitting to the Creator."},
            {"id": 7, "ar": "Risale-i Nur - The Words", "text": "The ego wishes to act like Pharaoh; the best remedy is recognizing one's absolute helplessness and poverty before God.", "src": "The Twenty-Third Word", "exp": "Lesson: Human dignity lies in recognizing absolute dependence on God."},
            {"id": 8, "ar": "Risale-i Nur - Kastamonu", "text": "The evil-commanding ego cannot be trusted. It can drive a person to wrongdoing at any moment.", "src": "Kastamonu Lahikasi", "exp": "Lesson: Remain vigilant against the promptings of the ego until the end."},
            {"id": 9, "ar": "Risale-i Nur - The Flashes", "text": "The ego desires instant pleasure, failing to realize the poisonous pain hidden inside.", "src": "The Seventeenth Flash", "exp": "Lesson: Forbidden pleasures carry heavy spiritual consequences."},
            {"id": 10, "ar": "Risale-i Nur - The Words", "text": "The ego demands immediate rewards while postponing its duties.", "src": "The Twenty-First Word", "exp": "Lesson: Overcome procrastination and laziness of the self."},
            {"id": 11, "ar": "Risale-i Nur - The Letters", "text": "Purification of the ego means channeling its energy toward righteous deeds rather than destroying it.", "src": "The Letters", "exp": "Lesson: Direct natural inclinations toward divine obedience."},
            {"id": 12, "ar": "Risale-i Nur - The Rays", "text": "The greatest trick of the ego is making one believe they are faultless.", "src": "The Rays", "exp": "Lesson: Recognizing one's own defects is true perfection."},
            {"id": 13, "ar": "Risale-i Nur - The Words", "text": "Worldly pleasures resemble poisoned honey; their delight is matched by their pain.", "src": "The Words", "exp": "Lesson: Do not be deceived by temporary worldly temptations."},
            {"id": 14, "ar": "Risale-i Nur - The Flashes", "text": "O my soul! If performing worship feels heavy, contemplate the narrowness of the grave.", "src": "The Flashes", "exp": "Lesson: Remembering mortality cures sluggishness in worship."},
            {"id": 15, "ar": "Risale-i Nur - Biography", "text": "I see my own self as being more in need of advice than anyone else.", "src": "Tarihce-i Hayat", "exp": "Lesson: Profound humility is the hallmark of maturity."},
            {"id": 16, "ar": "Risale-i Nur - The Words", "text": "The ego assumes ownership. The true Owner of everything is Allah.", "src": "The Thirtieth Word", "exp": "Lesson: Relinquish the illusion of absolute possession."},
            {"id": 17, "ar": "Risale-i Nur - The Flashes", "text": "The strongest shield against the ego is contemplating death.", "src": "The Twenty-First Flash", "exp": "Lesson: Remembering death cuts short vain ambitions."},
            {"id": 18, "ar": "Risale-i Nur - Barla", "text": "The desires of the ego are like an endless ocean; they can never be fully satisfied.", "src": "Barla Lahikasi", "exp": "Lesson: Trying to satisfy every whim of the ego is an endless trap."},
            {"id": 19, "ar": "Risale-i Nur - The Words", "text": "The shortest and safest path to reach Allah is through acknowledging one's helplessness and poverty.", "src": "The Twenty-Sixth Word", "exp": "Lesson: Pride vanishes when human weakness is embraced."},
            {"id": 20, "ar": "Risale-i Nur - The Letters", "text": "True delight is found in disciplining the rebellious ego and submitting it to the Truth.", "src": "The Letters", "exp": "Lesson: The soul finds ultimate joy in self-mastery."},
            {"id": 21, "ar": "Risale-i Nur - Mesnevi-i Nuriye", "text": "Whenever the ego demands pampering, restrict it with the reins of gratitude and contentment.", "src": "Mesnevi-i Nuriye", "exp": "Lesson: Contentment halts the insatiable demands of the ego."},
            {"id": 22, "ar": "Risale-i Nur - The Flashes", "text": "O man! Do not let your ego and Satan deceive you. True honor is being a sincere servant to Allah.", "src": "The Flashes", "exp": "Lesson: Servitude to God is the highest possible dignity."},
            {"id": 23, "ar": "Risale-i Nur - The Words", "text": "He who is pleased with his own ego cannot be truly pleased with anyone else.", "src": "The Words", "exp": "Lesson: Focus on reforming yourself rather than finding fault in others."},
            {"id": 24, "ar": "Risale-i Nur - The Letters", "text": "Arrogance is a subtle trap that hides personal flaws behind a mask of pride.", "src": "The Letters", "exp": "Lesson: Overcome self-conceit through introspection."},
            {"id": 25, "ar": "Risale-i Nur - The Rays", "text": "Whoever follows the whims of his ego strays far from divine guidance.", "src": "The Rays", "exp": "Lesson: Desire cannot be a reliable guide for life."}
        ],
        "veliler": [
            {"id": 1, "ar": "Imam Al-Ghazali", "text": "A person who has not disciplined his ego cannot be a true friend. The ego is a serpent with a thousand tricks.", "src": "Ihya Ulum al-Din", "exp": "Lesson: The ego is a dangerous force that requires constant supervision."},
            {"id": 2, "ar": "Rumi", "text": "The ego is a dragon; it may look frozen, but when it finds an opportunity, it wreaks havoc. Melt it with spiritual discipline.", "src": "Masnavi", "exp": "Lesson: Never be deceived when the ego appears dormant."},
            {"id": 3, "ar": "Shah Naqshband", "text": "Our path is the path of opposing the ego. Doing the exact opposite of what the ego craves is the essence of truth.", "src": "Risalah al-Qudsiyyah", "exp": "Lesson: Going against carnal inclinations elevates the spirit."},
            {"id": 4, "ar": "Abdul Qadir Gilani", "text": "The one who conquers his own ego is greater than the one who conquers the entire world.", "src": "Futuh al-Ghayb", "exp": "Lesson: Internal victory surpasses any external triumph."},
            {"id": 5, "ar": "Hasan al-Basri", "text": "Bridling the ego is more difficult than striking with a sword.", "src": "Wisdoms", "exp": "Lesson: Managing oneself requires relentless and steadfast patience."},
            {"id": 6, "ar": "Ibn Ataillah al-Sakandari", "text": "One of the subtle lusts of the ego is taking pride in one's own worship and acts of obedience.", "src": "Al-Hikam", "exp": "Lesson: Self-admiration in worship is a hidden trap of the ego."},
            {"id": 7, "ar": "Ibrahim ibn Adham", "text": "He who does not discipline his ego with hunger and fasting can never break its desires.", "src": "Siyar", "exp": "Lesson: Reducing food intake weakens carnal impulses."},
            {"id": 8, "ar": "Yunus Emre", "text": "It is your ego that stands in your way on the journey; do not obey your ego, dear soul!", "src": "Divan", "exp": "Lesson: The sole barrier in spiritual travel is one's own ego."},
            {"id": 9, "ar": "Ahmad Yasawi", "text": "Crushing the ego and remaining humble is the hallmark of a true seeker.", "src": "Divan-ı Hikmet", "exp": "Lesson: Humility is the ultimate remedy for pride."},
            {"id": 10, "ar": "Bishr al-Hafi", "text": "Whenever my ego craves something, I intentionally resist giving it to it.", "src": "Tabaqat", "exp": "Lesson: Practicing self-denial liberates the spirit."},
            {"id": 11, "ar": "Junayd of Baghdad", "text": "Following the ego's impulses is the thickest veil that darkens the heart.", "src": "Epistles", "exp": "Lesson: Giving into sin closes the eye of the heart."},
            {"id": 12, "ar": "Dhu al-Nun al-Misri", "text": "The ruin of the soul comes from gratifying its every whim.", "src": "Wisdoms", "exp": "Lesson: Pampering the ego leads to spiritual destruction."},
            {"id": 13, "ar": "Bayazid Bastami", "text": "I invited my soul to Truth, and it resisted. So I deprived it of worldly comforts until it submitted.", "src": "Tazkirat", "exp": "Lesson: Firm discipline is required to train the ego."},
            {"id": 14, "ar": "Imam Rabbani", "text": "The desires of the ego are diametrically opposed to the pleasure of Allah. Two opposites cannot coexist.", "src": "Maktubat", "exp": "Lesson: Achieving divine pleasure requires opposing the ego."},
            {"id": 15, "ar": "Fudayl ibn Iyad", "text": "The weakest of people is the one who is incapable of restraining his own ego.", "src": "Zuhd", "exp": "Lesson: True weakness is succumbing to carnal desires."},
            {"id": 16, "ar": "Sari al-Saqati", "text": "Wisdom can never be expected from one who obeys his ego.", "src": "Tabaqat", "exp": "Lesson: True wisdom only shines in a purified heart."},
            {"id": 17, "ar": "Yahya ibn Mu'adh", "text": "Fight against your ego; its most powerful weapon is ignorance.", "src": "Wisdoms", "exp": "Lesson: Defeat the ego through knowledge and self-awareness."},
            {"id": 18, "ar": "Umar ibn Abd al-Aziz", "text": "Whoever holds himself accountable profits, while the heedless person incurs utter loss.", "src": "Siyar", "exp": "Lesson: Daily self-examination is the roadmap to salvation."},
            {"id": 19, "ar": "Imam Al-Shafi'i", "text": "If you do not occupy your ego with truth, it will occupy you with falsehood.", "src": "Divan", "exp": "Lesson: Keep yourself busy with righteous deeds to prevent idleness."},
            {"id": 20, "ar": "Aziz Mahmud Hudayi", "text": "Demolish the palace of the ego so that the palace of the spirit may be built.", "src": "Wisdoms", "exp": "Lesson: Abandoning selfish desires revitalizes the soul."},
            {"id": 21, "ar": "Shaykh Shaban-i Veli", "text": "May your coming be blessed, your going be blessed, and every action of yours be for Allah.", "src": "Wisdoms", "exp": "Lesson: Pure intention for God should guide every move."},
            {"id": 22, "ar": "Haji Bektash Veli", "text": "Know your ego, and you will know your Lord. Guard your hands, your loins, and your tongue.", "src": "Makalat", "exp": "Lesson: Morality begins with policing your physical actions."},
            {"id": 23, "ar": "Somuncu Baba", "text": "The best of people is the one who criticizes and audits his ego the most.", "src": "Tabaqat", "exp": "Lesson: Self-criticism distinguishes exemplary people."},
            {"id": 24, "ar": "Abu Bakr as-Siddiq", "text": "Hold fast to your tongue; nothing in this world leads human beings into error more than the tongue.", "src": "Siyar", "exp": "Lesson: Silence is the ultimate guard against slips."},
            {"id": 25, "ar": "Umar ibn al-Khattab", "text": "Hold yourselves to account before you are called to account, and weigh your deeds before they are weighed for you.", "src": "History", "exp": "Lesson: Proactive self-reckoning keeps the soul alive."}
        ],
        "ameli": [
            {"id": 1, "ar": "Practical Step 1: Guarding the Tongue", "text": "Refrain from idle talk for at least 1 hour daily. Backbiting feeds the ego.", "src": "Speech Discipline", "exp": "Practice: Ask yourself 'Does this speech please Allah?' before speaking."},
            {"id": 2, "ar": "Practical Step 2: Guarding the Gaze", "text": "Avoid looking at forbidden or useless visuals. The eyes are the ego's gateway.", "src": "Sight Discipline", "exp": "Practice: Lower your gaze immediately and seek forgiveness."},
            {"id": 3, "ar": "Practical Step 3: Moderation in Eating", "text": "Practice the principle of not filling the stomach entirely. Leave the table before full satiety.", "src": "Stomach Discipline", "exp": "Practice: Fast 1-2 days a week or eat very lightly."},
            {"id": 4, "ar": "Practical Step 4: Night Prayer (Tahajjud)", "text": "Wake up during the quiet hours of the night when the ego loves sleep and pray.", "src": "Soul Discipline", "exp": "Practice: Pulling the ego out of sleep breaks its stubbornness."},
            {"id": 5, "ar": "Practical Step 5: Anonymous Charity", "text": "Give away what your ego loves most for the sake of Allah without expecting recognition.", "src": "Wealth Discipline", "exp": "Practice: Give secretly whenever you feel stinginess arise."},
            {"id": 6, "ar": "Practical Step 6: Anger Control", "text": "Whenever you feel angry, change your posture; sit down if standing, and make ablution.", "src": "Interpersonal Ethics", "exp": "Practice: Do not prolong arguments even if you are right."},
            {"id": 7, "ar": "Practical Step 7: Contemplation of Death", "text": "Spend 5 minutes daily imagining your funeral and being placed in the grave.", "src": "Meditation", "exp": "Practice: Shatters long-term worldly ambitions."},
            {"id": 8, "ar": "Practical Step 8: Listing Personal Faults", "text": "Stop criticizing others. Write down your own 5 negative traits in a notebook.", "src": "Self-Audit", "exp": "Practice: The most practical way to cure arrogance."},
            {"id": 9, "ar": "Practical Step 9: Countering Ego Impulses", "text": "Whenever your ego urges you toward idleness, penalize it with extra prayers.", "src": "Discipline", "exp": "Practice: The ego backs down when it realizes it faces discipline."},
            {"id": 10, "ar": "Practical Step 10: Acts of Humility", "text": "Voluntarily perform humble chores and serve those in lower positions.", "src": "Character", "exp": "Practice: Directly eradicates pride and conceit."},
            {"id": 11, "ar": "Practical Step 11: Heart Dhikr", "text": "Recite 'La ilaha illallah' and 'Astaghfirullah' at least 100 times daily.", "src": "Heart Training", "exp": "Practice: Remembrance illuminates the heart and weakens the ego."},
            {"id": 12, "ar": "Practical Step 12: Stopping Complaints", "text": "Stop complaining to people about your hardships; turn solely to Allah.", "src": "Patience", "exp": "Practice: Elevates you to the station of contentment."},
            {"id": 13, "ar": "Practical Step 13: Righteous Companionship", "text": "Spend time with spiritually uplifting people and avoid heedless environments.", "src": "Environment", "exp": "Practice: Your surroundings directly shape your inner state."},
            {"id": 14, "ar": "Practical Step 14: Expecting No Reward", "text": "Do not expect thanks, praise, or validation for any good deed you do.", "src": "Sincerity", "exp": "Practice: Prevents the spiritual disease of vanity."},
            {"id": 15, "ar": "Practical Step 15: Digital Fasting", "text": "Limit social media and useless digital consumption to 30 minutes a day.", "src": "Digital Diet", "exp": "Practice: Cleanses the mind from sensory overload."},
            {"id": 16, "ar": "Practical Step 16: The Art of Forgiveness", "text": "When your ego demands revenge against someone who wronged you, pardon them for Allah's sake.", "src": "Ethics", "exp": "Practice: Eradicates harboring resentment."},
            {"id": 17, "ar": "Practical Step 17: Time Management", "text": "Plan your 24 hours. Idle time is the playground of the ego.", "src": "Time Control", "exp": "Practice: An occupied mind leaves no room for idle promptings."},
            {"id": 18, "ar": "Practical Step 18: Avoiding Doubtful Matters", "text": "Stay away not only from clear prohibitions but also from doubtful grey areas.", "src": "Piety (Taqwa)", "exp": "Practice: True caution leaves what is ambiguous."},
            {"id": 19, "ar": "Practical Step 19: Mindful Worship", "text": "Perform your prayers as if it were your final prayer on earth.", "src": "Focus (Khushu)", "exp": "Practice: Elevates mechanical rituals into spiritual experiences."},
            {"id": 20, "ar": "Practical Step 20: Constant Supplication", "text": "Daily pray: 'O Allah, do not leave me to my ego even for the blink of an eye!'", "src": "Supplication", "exp": "Practice: Follows the most frequent prayer of the Prophet."},
            {"id": 21, "ar": "Practical Step 21: Ascetic Discipline", "text": "Reduce consumption periodically to dry out carnal urges.", "src": "Riyaza", "exp": "Practice: Over-eating empowers the ego; hunger softens it."},
            {"id": 22, "ar": "Practical Step 22: Solitude at Night", "text": "Spend quiet moments alone with your Creator in the stillness of the night.", "src": "Halwat", "exp": "Practice: The eye of the heart opens in solitude."},
            {"id": 23, "ar": "Practical Step 23: Confession and Repentance", "text": "Fall into prostration at the end of the day and confess your failings.", "src": "Repentance", "exp": "Practice: Prostration humbles the ego's pride into the dust."},
            {"id": 24, "ar": "Practical Step 24: Repaying Evil with Good", "text": "Pray for those who mistreat you instead of retaliating.", "src": "Prophetic Ethics", "exp": "Practice: Dries out the seeds of enmity in the heart."},
            {"id": 25, "ar": "Practical Step 25: Gratitude Audit", "text": "Count your blessings daily and express gratitude for every single breath.", "src": "Gratitude", "exp": "Practice: Gratitude increases blessings and fosters contentment."}
        ],
        "cetel": [
            "Did I perform my 5 daily prayers with focus and presence today?",
            "Did I guard my tongue from backbiting, lying, and idle chatter?",
            "Did I protect my eyes from forbidden and useless content?",
            "Did I manage to control my ego when provoked by anger today?",
            "Did I oppose my ego by practicing moderation and charity?",
            "Did I read the Quran and reflect upon its deep meanings?",
            "Did I keep the reality of death and the grave in my mind?",
            "Did I strive for sincerity while guarding against ostentation?",
            "Was I humble towards others, successfully crushing my pride?",
            "Did I conduct a sincere self-audit and repent before sleeping?"
        ]
    }
}

# --- 3. STREAMLIT SIDEBAR & LANGUAGE SELECTOR ---
dil_secimi = st.sidebar.selectbox(
    "Dil / Language:", 
    ["tr", "en"], 
    format_func=lambda x: "Türkçe 🇹🇷" if x == "tr" else "English 🇬🇧"
)

t = db[dil_secimi]

st.sidebar.title(t["sidebar_title"])

secilen_modul = st.sidebar.radio(
    "Arşiv seçin / Select module:",
    t["tabs"]
)

st.sidebar.markdown("---")
st.sidebar.info(t["sleep_note"])

# --- 4. MAIN PANEL & SEARCH ---
st.markdown(
    f"""<div class="panel-header">
        <h1 style="color: #0f172a; font-family: 'Amiri', serif; margin-bottom: 5px; text-align: center;">{t['title']}</h1>
        <p style="color: #64748b; text-align: center; font-size: 1.1rem; margin-top: 0;">{t['subtitle']}</p>
    </div>""", 
    unsafe_allow_html=True
)

# Arama çubuğu kontrolü
if "Paylaşım" not in secilen_modul and "Guidelines" not in secilen_modul and "Murakabe" not in secilen_modul and "Checklist" not in secilen_modul:
    arama = st.text_input("", placeholder=t["search_label"], label_visibility="collapsed")
else:
    arama = ""

# --- KARTLARI GÜVENLİ VE HATASIZ RENDER EDEN FONKSİYON ---
def kartlari_goster(liste, goster_arapca=True):
    for item in liste:
        if (arama.lower() in item.get("text", "").lower() or 
            arama.lower() in item.get("ar", "").lower() or 
            arama.lower() in item.get("src", "").lower() or
            arama.lower() in item.get("exp", "").lower()):
            
            st.markdown('<div class="spiritual-card">', unsafe_allow_html=True)
            
            if goster_arapca and "ar" in item and item["ar"]:
                st.markdown(f'<div class="arabic-text">{item["ar"]}</div>', unsafe_allow_html=True)
            
            if "text" in item and item["text"]:
                st.markdown(f'<div class="quote-text">"{item["text"]}"</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="color: #0f172a; font-weight: bold; margin-bottom: 8px;">{item.get("ar", "")}</div>', unsafe_allow_html=True)
                
            if "src" in item and item["src"]:
                st.markdown(f'<div class="source-text">{t["source_label"]}: {item["src"]}</div>', unsafe_allow_html=True)
                
            if "exp" in item and item["exp"]:
                st.markdown(f'<div class="exp-text"><b>{t["lesson_label"]}:</b> {item["exp"]}</div>', unsafe_allow_html=True)
                
            st.markdown('</div>', unsafe_allow_html=True)

# --- 5. CONTENT ROUTING ---
if "Ayet" in secilen_modul or "Quranic" in secilen_modul:
    kartlari_goster(t["ayet"])

elif "Hadîs" in secilen_modul or "Hadiths" in secilen_modul:
    kartlari_goster(t["hadis"])

elif "Bediüzzaman" in secilen_modul or "Bediuzzaman" in secilen_modul:
    kartlari_goster(t["bediuzzaman"])

elif "Veliler" in secilen_modul or "Saints" in secilen_modul:
    kartlari_goster(t["veliler"])

elif "Ameli" in secilen_modul or "Practical" in secilen_modul:
    kartlari_goster(t["ameli"], goster_arapca=False)

elif "Murakabe" in secilen_modul or "Checklist" in secilen_modul:
    st.markdown(
        f"""<div class="spiritual-card">
            <h3>{t['checklist_title']}</h3>
            <p>{t['checklist_desc']}</p>
        </div>""", 
        unsafe_allow_html=True
    )
    
    for idx, soru in enumerate(t["cetel"]):
        st.checkbox(soru, key=f"chk_{idx}")
        
    if st.button(t["checklist_btn"]):
        st.success(t["checklist_success"])

elif "Paylaşım" in secilen_modul or "Guidelines" in secilen_modul:
    st.markdown('<div class="spiritual-card" style="border-left: 5px solid #d4af37; padding: 30px;">', unsafe_allow_html=True)
    st.markdown(f"## {t['notice_title']}")
    st.markdown("---")
    st.markdown(t["notice_p1"])
    st.markdown("")
    st.markdown(t["notice_p2"])
    st.markdown(t["notice_p3"])
    st.markdown(t["notice_p4"])
    st.markdown('</div>', unsafe_allow_html=True)

# --- 6. FOOTER NOTICE ---
st.markdown("---")
st.markdown('<div class="spiritual-card" style="border-left: 4px solid #3b82f6; padding: 15px;">', unsafe_allow_html=True)
st.markdown(f"#### {t['notice_title']}")
st.markdown(t["notice_p1"])
st.markdown('</div>', unsafe_allow_html=True)