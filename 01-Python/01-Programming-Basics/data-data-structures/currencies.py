# pylint: disable=missing-docstring

RATES = {
    "USDEUR": 0.85,   # 1 USD = 0.85 EUR
    "GBPEUR": 1.13,   # 1 GBP = 1.13 EUR
    "CHFEUR": 0.86,   # 1 CHF = 0.86 EUR
    "EURGBP": 0.885   # 1 EUR = 0.885 GBP
}

def convert(amount, currency):
    """
    Returns the converted amount into the target currency.
    amount is a tuple like (100, "USD")
    currency is the target currency, like "EUR"
    """
    # $CHALLENGIFY_BEGIN

    # This loop iterates over all rate keys and checks two cases:
    # 1. If the source currency matches the first 3 letters of the key and target is EUR 
    # #→ multiply
    # 2. If the source currency matches the last 3 letters of the key and target matches first 3 → divide
    # Example: convert((100, "USD"), "EUR") → use USDEUR and multiply
    #          convert((100, "EUR"), "USD") → not in rates, so will be skipped
    #          convert((100, "EUR"), "GBP") → uses EURGBP and multiplies

    for key, value in RATES.items():
        # Direct conversion to EUR, e.g. USD → EUR
        if amount[1] == key[0:3] and currency == "EUR":
            return round(value * amount[0])

        # Inverse conversion from EUR to something else, e.g. EUR → USD
        if amount[1] == key[3:6] and currency == key[0:3]:
            return round(amount[0] / value)#

    return None  # Ensures all code paths return a value
    # $CHALLENGIFY_END
