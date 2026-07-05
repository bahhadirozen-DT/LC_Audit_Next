RULE_LIBRARY = {

    "UCP600 Madde 18(c)": {
        "title": "Commercial Invoice",

        "official_en":
            "The description of the goods, services or performance in a commercial invoice must correspond with that appearing in the credit.",

        "official_tr":
            "Ticari faturadaki mal veya hizmet tanımı akreditifte belirtilen tanımla uyumlu olmalıdır.",

        "bank_comment":
            (
                "Mal tanımı birebir aynı olmak zorunda değildir. "
                "Daha ayrıntılı olabilir ancak akreditifle çelişemez."
            ),

        "reservation":
            (
                "Mal tanımı farklı ürünü ifade ediyorsa banka rezerv koyabilir."
            ),
    },

    "UCP600 Madde 20": {

        "title":"Bill of Lading",

        "official_en":
            "A bill of lading must appear to indicate shipment by the carrier.",

        "official_tr":
            "Konşimento taşıyıcı tarafından düzenlenmiş görünmelidir.",

        "bank_comment":
            (
                "Shipper, Consignee, Notify Party ve liman bilgileri "
                "akreditifle uyumlu olmalıdır."
            ),

        "reservation":
            "Eksik veya farklı bilgiler rezerv oluşturabilir.",
    },

    "UCP600 Madde 28": {

        "title":"Insurance",

        "official_en":
            "Insurance document must comply with the credit.",

        "official_tr":
            "Sigorta belgesi akreditif şartlarına uygun olmalıdır.",

        "bank_comment":
            (
                "Sigortalı, para birimi ve sigorta tutarı "
                "kontrol edilmelidir."
            ),

        "reservation":
            "Sigorta bilgilerindeki farklılık rezerv oluşturabilir.",
    },

    "ISBP 821 A23": {

        "title":"Commercial Invoice Description",

        "official_en":
            (
                "The description of goods may be more detailed than the credit "
                "provided it does not conflict."
            ),

        "official_tr":
            (
                "Mal tanımı akreditiften daha ayrıntılı olabilir. "
                "Ancak akreditifle çelişmemelidir."
            ),

        "bank_comment":
            (
                "Örneğin MT700'de 'TEXTILE FABRICS' yazarken "
                "'TEXTILE FABRICS 65% COTTON' yazılması genellikle "
                "rezerv oluşturmaz."
            ),

        "reservation":
            (
                "Farklı ürün tanımı rezerv sebebi olabilir."
            ),
    },

    "ISBP 821 A18": {

        "title":"Applicant",

        "official_en":
            "Applicant information should not conflict with the credit.",

        "official_tr":
            "Applicant bilgisi akreditifle çelişmemelidir.",

        "bank_comment":
            (
                "Kısaltmalar veya noktalama farkları genellikle kabul edilir."
            ),

        "reservation":
            (
                "Farklı şirket ismi rezerv oluşturabilir."
            ),
    }

}

print("Rule Library loaded:", len(RULE_LIBRARY))
