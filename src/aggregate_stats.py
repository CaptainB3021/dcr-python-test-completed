import json
from db import Country

def main():
    # Create a dictionary to store the aggregated data
    regions = {}

    # Iterate over all countries
    for country in Country.list_all():
        region_name = country.data['region_name']
        if region_name not in regions:
            regions[region_name] = {
                'name': region_name,
                'number_countries': 0,
                'total_population': 0
            }
        
        regions[region_name]['number_countries'] += 1
        regions[region_name]['total_population'] += int(country.data['population'])
    
    # Format the data as specified
    result = {'regions': list(regions.values())}
    
    # Write the results to a JSON file
    with open('region_stats.json', 'w') as file:
        json.dump(result, file, indent=4)

    # Print the results
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()