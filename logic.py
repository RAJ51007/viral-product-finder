def run_bot(keyword):
    sample_ads = [
        {"product": f"{keyword} Pro Max", "duration": 35, "countries": 4, "ad_copy": "50% OFF - Viral!"},
        {"product": f"{keyword} Ultra", "duration": 12, "countries": 1, "ad_copy": "Best Seller of 2025!"},
        {"product": f"Smart {keyword}", "duration": 22, "countries": 3, "ad_copy": "🔥 Just Launched! Free Shipping."},
    ]
    for ad in sample_ads:
        score = ad['duration'] * 2 + ad['countries'] * 10
        if "viral" in ad['ad_copy'].lower():
            score += 20
        ad['score'] = score
    return sorted(sample_ads, key=lambda x: x['score'], reverse=True)
