import re

def convert_arabic_float_to_english(arabic_float_str):
    mapping = {'٠':'0','١':'1','٢':'2','٣':'3','٤':'4',
               '٥':'5','٦':'6','٧':'7','٨':'8','٩':'9', ',':'.'}
    try:
        if not arabic_float_str:
            return 0.0
        english = ''.join(mapping.get(c, c) for c in arabic_float_str)
        return float(english)
    except:
        return 0.0

def extract_number_from_response(response):
    match = re.search(r"\b(\d+)\b", response)
    return int(match.group(1)) if match else None
