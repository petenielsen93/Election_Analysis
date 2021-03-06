counties = ["Arapahoe", "Denver", "Jefferson"]
#if "El Paso" in counties:
    #print("El Paso is in the list of counties.")
#else:
    #print("El Paso is not the list of counties.")

#if counties[3] != 'Jefferson':
    #print(counties[2])

#counties.insert(1,"El Paso")
#counties.remove("Arapahoe")
#counties.remove("Denver")
#counties.append("Denver")
#counties.append("Arapahoe")
#print(counties)


#counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}



#for key, value in counties_dict.items():
    #print(f"{key} county has {value:,} registered voters.")

#print(counties_dict["Denver"])

voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#for value in county_dict.values():
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {int((county_dict['registered_voters'])):,} registered voters.")
            

#for county_dict in voting_data:
    #print(county_dict['county'])

#voting_data.insert(2, {"county":"El Paso", "registered_voters": 461149})
#voting_data.remove({"county": "Arapahoe", "registered_voters": 422829})
#voting_data.pop(0)
#voting_data.remove({"county":"Denver", "registered_voters": 463353})
#voting_data.append({"county":"Denver", "registered_voters": 463353})
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#voting_data




