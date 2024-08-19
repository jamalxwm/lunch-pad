from enum import Enum 

class PriceLevelIndicators(Enum):
    PRICE_LEVEL_UNSPECIFIED = None
    PRICE_LEVEL_FREE = 0
    PRICE_LEVEL_INEXPENSIVE = 1
    PRICE_LEVEL_MODERATE = 2
    PRICE_LEVEL_EXPENSIVE = 3
    PRICE_LEVEL_VERY_EXPENSIVE = 4

def map_price_symbol_to_enum(symbol):
    symbol_to_enum = {
        "$": PriceLevelIndicators.PRICE_LEVEL_INEXPENSIVE,
        "$$": PriceLevelIndicators.PRICE_LEVEL_MODERATE,
        "$$$": PriceLevelIndicators.PRICE_LEVEL_EXPENSIVE,
        "$$$$": PriceLevelIndicators.PRICE_LEVEL_VERY_EXPENSIVE,
    }
    return symbol_to_enum.get(symbol)

def average_price_level(google_price=None, yelp_price=None, tripadvisor_price=None):
    values = []

    if google_price is not None:
        values.append(google_price.value)
    if yelp_price is not None:
        values.append(yelp_price.value)
    if tripadvisor_price is not None:
        values.append(tripadvisor_price.value)

    if not values:
        return None
    
    return sum(values) / len(values)

yelp_value = "$$$"
google_level = PriceLevelIndicators.PRICE_LEVEL_MODERATE
yelp_level = map_price_symbol_to_enum(yelp_value)
tripadvisor_level = None

average = average_price_level(google_level, yelp_level, tripadvisor_level)
print(average)