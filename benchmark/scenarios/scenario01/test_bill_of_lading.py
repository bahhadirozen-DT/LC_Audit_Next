from core.parsers.bill_of_lading_parser import parse_bill_of_lading


def test_basic_bol_parse():
    sample = """
    Bill of Lading No: TEST123

    Shipper: A COMPANY
    Consignee: TO ORDER
    Notify Party: BANK

    Shipped on Board: Date: 29.06.2026
    Vessel: MAERSK ISTANBUL

    Port of Loading: ISTANBUL
    Port of Discharge: ROTTERDAM
    """

    m = parse_bill_of_lading(sample)

    assert m.bl_number == "TEST123"
    assert m.consignee == "TO ORDER"
    assert m.vessel == "MAERSK ISTANBUL"
    assert m.shipment_date == "29.06.2026"
