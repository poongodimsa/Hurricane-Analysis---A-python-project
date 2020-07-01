# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville','Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

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
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,
          269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]


#write your update damages function here:

def update_damages():
    
    conversion={"M":1000000,
               "B":1000000000}
    damages_altered=[]
    for i in damages:
        #Keep 'Damages not recorded' as it is
        if i=='Damages not recorded':
            damages_altered.append(i)
        else:
            #apply the conversion for M and B and convert to float
            prefix=i[-1]
            val=float(i[:len(i)-1]) * conversion[prefix]
            damages_altered.append(val)

    return (damages_altered)


# write your construct hurricane dictionary function here:
#construct a dictionary with names as key and details as values
def construct_dictionary():
    #initialize the dictionary
    hurricanes={}
    damages_new=update_damages()
    for i in range(len(names)):
        hurricanes[names[i]]={'Name': names[i], 'Month': months[i], 'Year':years[i], 
                             'Max Sustained Wind': max_sustained_winds[i],
                             'Areas Affected':areas_affected[i],'Damage':damages_new[i],'Deaths':deaths[i]}
    
    return hurricanes

# write your construct hurricane by year dictionary function here:
#Group the dictionary by year with year as key and all the 
def construct_by_year():
    
    hurricanes_year={}
    #get the hurricane dictionary
    hurricanes=construct_dictionary()
   
    #group by year
    for val in hurricanes.values():
        year=val['Year']
        yearly_items=[val]
        if year in hurricanes_year:
            yearly_items.append(hurricanes_year[year]) 
            hurricanes_year[year]=yearly_items
        else:
            hurricanes_year[year]=[val]
   
    return hurricanes_year


# write your count affected areas function here:
from collections import defaultdict
#List the number of times each area is affected
def count_affected_areas():
    count=0
    #using default dictionary which initializes the value to int means zero automatically
    affected_areas_count=defaultdict(int)
    for areas in areas_affected:
        for area in areas:
            affected_areas_count[area] +=1
 
    return affected_areas_count

# write your find most affected area function here:
#find the area which is affected ,axi,um number of times
def find_most_affected_area():
    #get affected areas count dictionary
    area_count_dic=count_affected_areas()
    if not area_count_dic is None:
        most_affected_area=''
        max_count=0
        for area,count in area_count_dic.items():
            if max_count < count:
                most_affected_area=area
                max_count=count
    return most_affected_area,max_count       
        

#print(find_most_affected_area())

# write your greatest number of deaths function here:
#Returns the hurricane details for which maximum death occured
def greatest_death_count():
    hurricanes=construct_dictionary()
    
    max_death_count=0
    hurri_name=''
    for name,data in hurricanes.items():
        if data['Deaths'] > max_death_count:
            max_death_count=data['Deaths']
            hurri_name=name
    return hurri_name,max_death_count

#print(greatest_death_count())

# write your catgeorize by mortality function here:
#categorize the data as per the mortality scale
def catogorize_by_mortality():
        
    mortality_scale = {0: 0,1: 100,2: 500, 3: 1000,  4: 10000}
    hurricanes=construct_dictionary()
    dict_by_mortality={}
    
    #Add keys to the dictionary
    for mort_catogory in mortality_scale.keys():
        dict_by_mortality.update({mort_catogory:[]})
    
    for name,details in hurricanes.items():
        #Iterate mortality scale dictionary
        for mort_catogory,death_count in mortality_scale.items():
            if details['Deaths'] < death_count:
                dict_by_mortality[mort_catogory].append(details)
                break
    return dict_by_mortality


#print(catogorize_by_mortality())


# write your greatest damage function here:
#Returns name of the hurricane that caused maximum damage and the cost
def greatest_damage():
    hurricanes=construct_dictionary()
    most_damagecaused_hurricane=''
    cost=0.0
    for name,details in hurricanes.items():
        if not details['Damage'] == 'Damages not recorded':
            if float(details['Damage']) > cost:
                cost=details['Damage']
                most_damagecaused_hurricane=name
    
    
    return most_damagecaused_hurricane,cost
 
#print(greatest_damage())

# write your catgeorize by damage function here:
#catogorizes hte hurrcane details as per given damage scale 
def categorize_by_damage():
    
    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    
    hurricanes=construct_dictionary()
    dict_by_damage={}
    for damage_catogory in damage_scale.keys():
        dict_by_damage.update({damage_catogory:[]})
    
    for name,details in hurricanes.items():
        if not details['Damage'] == 'Damages not recorded':
            for damage_catogory,damage_count in damage_scale.items():
                if float(details['Damage']) < damage_count:
                    dict_by_damage[damage_catogory].append(details)
                    break
    return dict_by_damage
print(categorize_by_damage())







