class ValuationEngine:
    def setup_engine(self, api_key):
        self.api_key = api_key
        print(f"[VAULT LOGIC] Valuation Engine processing pipeline active.")

    def calculate_asset_value(self, card_name, grade, current_market_price):
        print(f"[VALUATION] Calculating valuation for {card_name} | Grade: {grade}...")
        
        # Adjust premium based on grade tier
        if "PSA 10" in grade or "BGS 10" in grade:
            grade_multiplier = 1.25  # Gem Mint Premium
        elif "BGS 9.5" in grade:
            grade_multiplier = 1.00  # Standard Baseline Comps
        else:
            grade_multiplier = 0.85  # Lower Tier Adjustment
            
        final_valuation = round(current_market_price * grade_multiplier, 2)
        print(f"[VALUATION] Calculation finalized: ${final_valuation:,}")
        return final_valuation