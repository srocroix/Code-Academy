# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1 Function that returns a new list of updated damages where the recorded data is converted to float values:
def update_dmg(damages):
    new_dmg = []
    conversion = {"M": 1000000,
              "B": 1000000000}
    for damage in damages: 
        if damage == 'Damages not recorded':
            new_dmg.append(damage)
        elif damage[-1] in conversion.keys():
            new_value = float(damage[:-1]) * conversion[damage[-1]]
            new_dmg.append(new_value)
    return new_dmg

# Update Recorded Damages
updated_damages = update_dmg(damages)
print('List of updated damages:')
print(updated_damages)


# 2 Function that constructs a dictionary made out of the lists where the keys are the names of the hurricanes & the values are dictionaries themselves containing a key for each piece of data:
hurricanes = {}


def create_hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    for i in range(len(names)):
        hurricanes[names[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i], 'Area Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]}
    return hurricanes

create_hurricanes_dictionary(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print('\n')
print('Hurricanes dictionary:')
print(hurricanes)
print('\n')
print(hurricanes['New England'])

# 3 Function that converts the current dictionary of hurricanes to a new dictionary where keys are years:
def create_hurricanes_dictionary_by_year(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths):
    hurricanes_by_year = {}
    for i in range(len(years)):
        hurricanes_by_year[years[i]] = {'Name': names[i], 'Month': months[i], 'Year': years[i], 'Max Sustained Wind': max_sustained_winds[i],
                                'Area Affected': areas_affected[i], 'Damage': updated_damages[i], 'Deaths': deaths[i]}
    return hurricanes_by_year


hurricanes_by_year = create_hurricanes_dictionary_by_year(names, months, years, max_sustained_winds, areas_affected, updated_damages, deaths)
print('\n')
print('Hurricanes by year dictionnary:')
print(hurricanes_by_year)
print('\n')
print(hurricanes_by_year[1932])

# 4 Function that counts how often each area is listed as an affected area of a hurricane and store and return the results in a dictionary:
areas_count = {}

def create_areas_count_dict(dict):
    for element in dict:
        for area in dict[element]['Area Affected']:
            if area not in areas_count:
                areas_count[area] = 1
            else:
                areas_count[area] += 1
    return areas_count

create_areas_count_dict(hurricanes)

print('\n')
print('Areas count dictionary:')
print(areas_count)

# 5 Function that finds the area affected by the most hurricanes, and how often it was hit:
def return_the_most_hurricanes_area(dict):
    counter = 0
    area_to_return = None
    for k, v in dict.items():
        if v > counter:
            area_to_return = k
            counter = v
    return 'The area affected by the most hurricanes is ' + str(area_to_return) + ' with a total of ' + str(counter) + ' hurricanes.'

the_most_hurricanes_area = return_the_most_hurricanes_area(areas_count)
print('\n')
print(the_most_hurricanes_area)

# 6 Function that finds the hurricane that caused the greatest number of deaths & how many deaths it caused:
def return_greatest_number_of_deaths_hurricane(dict):
    max_num_of_deaths = 0
    the_deadliest_hurricane = ''
    for element in dict:
        if dict[element]['Deaths'] > max_num_of_deaths:
            the_deadliest_hurricane = element
            max_num_of_deaths = dict[element]['Deaths']
    return the_deadliest_hurricane, max_num_of_deaths

the_deadliest_hurricane, max_num_of_deaths = return_greatest_number_of_deaths_hurricane(hurricanes)
print('\n')
print('The deadliest hurricane is ' + str(the_deadliest_hurricane) + ' with a total of ' + str(max_num_of_deaths) + ' deaths.')

# 7 Function that rates hurricanes on a mortality scale and sotre the hurricanes in a new dictionary where the keys are mortality ratings:
def return_hurricanes_by_mortality(dict):
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for element in dict:
        if dict[element]['Deaths'] == 0:
            hurricanes_by_mortality[0].append(element)
        elif dict[element]['Deaths'] > 0 and dict[element]['Deaths'] <= 100:
            hurricanes_by_mortality[1].append(element)
        elif dict[element]['Deaths'] > 100 and dict[element]['Deaths'] <= 500:
            hurricanes_by_mortality[2].append(element)
        elif dict[element]['Deaths'] > 500 and dict[element]['Deaths'] <= 1000:
            hurricanes_by_mortality[3].append(element)
        elif dict[element]['Deaths'] > 1000 and dict[element]['Deaths'] <= 10000:
            hurricanes_by_mortality[4].append(element)
        else:
            hurricanes_by_mortality[5].append(element)   
    return hurricanes_by_mortality

hurricanes_by_mortality = return_hurricanes_by_mortality(hurricanes)
print('\n')
print('Hurricanes by mortality dictionary:')
print(hurricanes_by_mortality)

# 8 Function that finds the hurricane that caused the greatest damage, and how costly it was:
def return_the_most_damage_hurricane(dict):
    the_most_damage = 0
    the_most_damage_hurricane = ''
    for element in dict:
        if dict[element]['Damage'] != 'Damages not recorded' and dict[element]['Damage'] > the_most_damage:
            the_most_damage_hurricane = element
            the_most_damage = dict[element]['Damage']
    return the_most_damage_hurricane, the_most_damage

the_most_damage_hurricane, the_most_damage = return_the_most_damage_hurricane(hurricanes)
print('\n')
print('The most devastating hurricane is ' + str(the_most_damage_hurricane) + ' with estimated damages of ' + str(the_most_damage) + ' dollars.')

#  Function that rates hurricanes on a damage scale
def return_hurricanes_by_damage(dict):
    hurricanes_by_damage = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for element in dict:
        if dict[element]['Damage'] == 'Damages not recorded':
            pass
        elif dict[element]['Damage'] == 0:
            hurricanes_by_damage[0].append(element)
        elif dict[element]['Damage'] > 0 and dict[element]['Damage'] <= 100000000:
            hurricanes_by_damage[1].append(element)
        elif dict[element]['Damage'] > 100000000 and dict[element]['Damage'] <= 1000000000:
            hurricanes_by_damage[2].append(element)
        elif dict[element]['Damage'] > 1000000000 and dict[element]['Damage'] <= 10000000000:
            hurricanes_by_damage[3].append(element)
        elif dict[element]['Damage'] > 10000000000 and dict[element]['Damage'] <= 50000000000:
            hurricanes_by_damage[4].append(element)
        elif dict[element]['Damage'] > 50000000000:
            hurricanes_by_damage[5].append(element)
    return hurricanes_by_damage

hurricanes_by_damage = return_hurricanes_by_damage(hurricanes)
print('\n')
print('Hurricanes by damage dictionary:')
print(hurricanes_by_damage)
