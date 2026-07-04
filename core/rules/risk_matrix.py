RISK_MATRIX = {

    "Amount": {
        "severity":"CRITICAL",
        "ucp":"UCP600 Art.18(c)",
        "isbp":"ISBP 821 para A18",
        "tr":"Fatura tutarı kredi şartlarına uygun olmalıdır."
    },

    "Currency":{
        "severity":"CRITICAL",
        "ucp":"UCP600 Art.18",
        "isbp":"ISBP 821 A18",
        "tr":"Para birimi kredi ile aynı olmalıdır."
    },

    "Applicant / Buyer":{
        "severity":"HIGH",
        "ucp":"UCP600 Art.14",
        "isbp":"ISBP 821 A23",
        "tr":"Alıcı bilgileri belgeler arasında çelişmemelidir."
    },

    "Beneficiary / Seller":{
        "severity":"HIGH",
        "ucp":"UCP600 Art.14",
        "isbp":"ISBP 821 A23",
        "tr":"Lehtar bilgileri belgeler arasında tutarlı olmalıdır."
    },

    "Goods Description":{
        "severity":"CRITICAL",
        "ucp":"UCP600 Art.18(c)",
        "isbp":"ISBP 821 A23",
        "tr":"Mal tanımı kredi şartları ile çelişmemelidir."
    },

    "Shipper":{
        "severity":"HIGH",
        "ucp":"UCP600 Art.20",
        "isbp":"ISBP 821 E",
        "tr":"Taşıtan bilgisi kredi şartlarına uygun olmalıdır."
    },

    "Consignee":{
        "severity":"HIGH",
        "ucp":"UCP600 Art.20",
        "isbp":"ISBP 821 E",
        "tr":"Consignee bilgisi kredi talimatına uygun olmalıdır."
    },

    "Country Of Origin":{
        "severity":"MEDIUM",
        "ucp":"UCP600 Art.14",
        "isbp":"ISBP 821 K",
        "tr":"Menşe ülke bilgisi destekleyici belgelerle uyumlu olmalıdır."
    },

    "Gross Weight":{
        "severity":"LOW",
        "ucp":"UCP600 Art.14(d)",
        "isbp":"ISBP 821 A23",
        "tr":"Ağırlık farklı yazım biçiminde olabilir ancak anlam değişmemelidir."
    },

    "Packages":{
        "severity":"LOW",
        "ucp":"UCP600 Art.14(d)",
        "isbp":"ISBP 821 A23",
        "tr":"Paket sayısı belgeler arasında tutarlı olmalıdır."
    }
}
