import json
from system_prompt.system_prompt import REPORT_GENERATOR_SYSTEM_PROMPT

def generate_system_prompt_from_config(file_path):
    with open(file_path, 'r') as file:
        property_data = json.load(file)
    system_prompt = generate_system_prompt(property_data)
    return system_prompt

def generate_system_prompt(property_data):
        property_details = property_data["property_details"][0]
        nearby_amenities = property_data["nearby_amenities"][0]
        safety = property_data["safety"][0]
        considerations = property_data["considerations"][0]

        system_prompt = (REPORT_GENERATOR_SYSTEM_PROMPT
                .replace("{location}", property_details["location"])
                .replace("{land_size}", property_details["land_size"])
                .replace("{bedrooms}", property_details["bedrooms"])
                .replace("{bathrooms}", property_details["bathrooms"])
                .replace("{orientation}", property_details["orientation"])
                .replace("{frontage}", property_details["frontage"])
                .replace("{zoning}", property_details["zoning"])
                .replace("{overlays}", property_details["overlays"])
                .replace("{schools}", nearby_amenities["schools"])
                .replace("{transport}", nearby_amenities["transport"])
                .replace("{other}", nearby_amenities["other"])
                .replace("{safety_stats}", safety["safety_stats"])
                .replace("{considerations}", considerations["considerations"])                
                )
        return system_prompt