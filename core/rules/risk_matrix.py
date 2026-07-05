RISK_MATRIX = {

"Amount": {
    "severity":"KRİTİK",
    "title_tr":"Fatura Tutarı",
    "title_en":"Invoice Amount",
    "ucp":"UCP600 Madde 18(c)",
    "isbp":"ISBP 821 A23",
    "reservation_probability":98,

    "ucp_tr":"Ticari faturadaki tutar akreditif şartlarına uygun olmalıdır.",

    "isbp_tr":"Faturadaki bilgiler akreditifle çelişmemelidir. Tutar farklılığı rezerv sebebi olabilir.",

    "tr":"Fatura tutarı akreditifte belirtilen tutarla uyumlu değildir.",

    "action":"Fatura düzeltilmeli veya akreditif amendment'i alınmalıdır."
},

"Applicant / Buyer":{
    "severity":"YÜKSEK",
    "title_tr":"Alıcı",
    "title_en":"Applicant / Buyer",
    "ucp":"UCP600 Madde 18",
    "isbp":"ISBP 821 A18",
    "reservation_probability":95,

    "ucp_tr":"Ticari faturadaki alıcı bilgisi akreditifte belirtilen applicant ile uyumlu olmalıdır.",

    "isbp_tr":"İsim farklı yazılabilir ancak farklı tüzel kişilik oluşturacak değişiklik olmamalıdır.",

    "tr":"Applicant bilgisi akreditifle uyuşmuyor.",

    "action":"Alıcı bilgisi kontrol edilmeli, gerekiyorsa belge düzeltilmelidir."
},

"Beneficiary / Seller":{
    "severity":"YÜKSEK",
    "title_tr":"Lehtar",
    "title_en":"Beneficiary / Seller",
    "ucp":"UCP600 Madde 18",
    "isbp":"ISBP 821 A18",
    "reservation_probability":95,

    "ucp_tr":"Faturadaki satıcı, akreditifteki beneficiary olmalıdır.",

    "isbp_tr":"Küçük yazım farklılıkları kabul edilebilir ancak farklı şirket oluşturamaz.",

    "tr":"Lehtar bilgisi uyumsuz.",

    "action":"Satıcı bilgileri düzeltilmelidir."
},

"Goods Description":{
    "severity":"KRİTİK",
    "title_tr":"Mal Tanımı",
    "title_en":"Goods Description",
    "ucp":"UCP600 Madde 18(c)",
    "isbp":"ISBP 821 A23",
    "reservation_probability":99,

    "ucp_tr":"Ticari faturadaki mal tanımı akreditifte yer alan mal tanımıyla uyumlu olmalıdır.",

    "isbp_tr":"Mal tanımı daha ayrıntılı olabilir ancak akreditifle çelişemez.",

    "tr":"Mal tanımı akreditif şartlarıyla uyumsuz.",

    "action":"Mal tanımı tüm belgelerde aynı hale getirilmelidir."
},

"Currency":{
    "severity":"KRİTİK",
    "title_tr":"Para Birimi",
    "title_en":"Currency",
    "ucp":"UCP600 Madde 18",
    "isbp":"ISBP 821",
    "reservation_probability":99,

    "ucp_tr":"Belge üzerindeki para birimi akreditifle aynı olmalıdır.",

    "isbp_tr":"Para birimi farklılığı rezerv oluşturabilir.",

    "tr":"Para birimi akreditifle uyuşmuyor.",

    "action":"Para birimi düzeltilmelidir."
},

"Shipper":{
    "severity":"YÜKSEK",
    "title_tr":"Gönderici",
    "title_en":"Shipper",
    "ucp":"UCP600 Madde 20",
    "isbp":"ISBP 821 D",
    "reservation_probability":90,

    "ucp_tr":"Konşimentodaki shipper bilgisi akreditif şartlarını karşılamalıdır.",

    "isbp_tr":"Shipper bilgisi farklı tüzel kişilik oluşturacak şekilde değişmemelidir.",

    "tr":"Gönderici bilgisi uyumsuz.",

    "action":"Konşimento kontrol edilmelidir."
},

"Consignee":{
    "severity":"YÜKSEK",
    "title_tr":"Consignee",
    "title_en":"Consignee",
    "ucp":"UCP600 Madde 20",
    "isbp":"ISBP 821 D",
    "reservation_probability":90,

    "ucp_tr":"Konşimentodaki consignee bilgisi LC şartlarına uygun olmalıdır.",

    "isbp_tr":"TO ORDER veya banka adına düzenleme LC şartına göre değerlendirilmelidir.",

    "tr":"Consignee bilgisi uyumsuz.",

    "action":"Konşimento yeniden incelenmelidir."
},

"Insured":{
    "severity":"YÜKSEK",
    "title_tr":"Sigortalı",
    "title_en":"Insured",
    "ucp":"UCP600 Madde 28",
    "isbp":"ISBP 821 K",
    "reservation_probability":90,

    "ucp_tr":"Sigorta belgesi akreditifte belirtilen taraf lehine düzenlenmelidir.",

    "isbp_tr":"Sigortalı kişi veya kuruluş LC şartlarına uygun olmalıdır.",

    "tr":"Sigortalı bilgisi akreditifle uyumsuz.",

    "action":"Sigorta belgesi düzeltilmelidir."
}



,
"Latest Shipment Date": {
    "severity":"KRİTİK",
    "title_tr":"Son Yükleme Tarihi",
    "title_en":"Latest Shipment Date",

    "ucp":"UCP600 Madde 20",
    "isbp":"ISBP 821 D",

    "reservation_probability":99,

    "ucp_tr":"Yükleme, akreditifte belirtilen son yükleme tarihinden geç olmamalıdır.",

    "isbp_tr":"Konşimentodaki On Board tarihi latest shipment date'i aşmamalıdır.",

    "tr":"Yükleme tarihi akreditifte izin verilen son tarihten sonra yapılmış.",

    "action":"Konşimento tarihi kontrol edilmeli veya amendment alınmalıdır."
}

}
