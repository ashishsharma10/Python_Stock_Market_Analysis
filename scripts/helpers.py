import locale

def format_Mcap(value):
    if value is None:
        return None

    # Convert market cap to crore
    marketCap = value / 1e7

    # Format market cap with commas
    formatted_market_cap = locale.format_string("%.2f", marketCap, grouping=True)

    # Add the Indian currency symbol and 'Cr' suffix
    formatted_market_cap_with_currency = f"₹ {formatted_market_cap} Cr"

    return formatted_market_cap_with_currency

# Set the locale to Indian English
locale.setlocale(locale.LC_NUMERIC, 'en_IN.UTF-8')


def format_recommendation(recommendation):
    
    # Split the string by underscores and capitalize each word
    words = recommendation.split('_') if recommendation is not None else None
    if not words:
        return None
        
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words with a space
    formatted_recommendation = ' '.join(capitalized_words)

    return formatted_recommendation