import requests
import json

base_url = 'https://swapi.dev/api/films'
response=requests.get(base_url)

complete=response.json()
result=complete['results']
number=int(input('Press 1 to lookup Flim.\nPress 2 to lookup Planets'))
if number == 1:
    a=1
    for i in result:
        title=i['title']
        print('{}.'.format(a)+title)
        a+=1
    film=input(('Enter a film name: '))
    count=complete['count']

    oo=result[0]['title']

    g=0
    while g < count:
        if film == result[g]['title']:
            title=result[g]['title']
            episode_id=result[g]['episode_id']
            director=result[g]['director']
            producer=result[g]['producer']
            release_date=result[g]['release_date']
            print('Title = '+title)
            print('Episode_id = '+str(episode_id))
            print('Director = '+director)
            print('producer = '+producer)
            print('Release_date = '+release_date)
            print('The Characters')
            char_url='https://swapi.dev/api/people/'
            x=0
            for a in result[g]['characters']:
                x+=1
            print(x)
            y=0
            for_char=result[g]['characters']
            while y < x:
                
                chh=for_char[y]
                char_res_url=requests.get(chh)
                char_res=char_res_url.json()
                char_name=char_res['name']
                char_gender=char_res['gender']
                char_height=char_res['height']
                char_skin=char_res['skin_color']
                char_birth=char_res['birth_year']
                print('Name = '+char_name)
                print('Gender = '+char_gender)
                print('Height = '+char_height)
                print('skin = '+char_skin)
                print('Birth = '+char_birth)
                print('\n')

                y+=1

        g=g+1    
elif number ==2:
    planet_url='https://swapi.dev/api/planets/'
    planet_res_url=requests.get(planet_url)
    planet_res=planet_res_url.json()
    planet=planet_res['results']
    h=1
    for b in planet:
        planet_name=b['name']
        planet_rotation=b['rotation_period']
        planet_orbital=b['orbital_period']
        planet_diameter=b['diameter']
        planet_climate=b['climate']
        planet_gravity=b['gravity']
        planet_terrain=b['terrain']
        planet_surface_water=b['surface_water']
        planet_population=b['population']
        print('{}.'.format(h)+'Name = '+planet_name)
        print('  Rotation_period = '+planet_rotation)
        print('  Orbital_period = '+planet_rotation)
        print('  Diameter = '+planet_diameter)
        print('  Climate = '+planet_climate)
        print('  Gravity = '+planet_gravity)
        print('  Terrain = '+planet_terrain)
        print('  Surface_water = '+planet_surface_water)
        print('  Population = '+planet_population)

        h+=1




        #print(planet_name)
else:
    print('Wrong Nubmer')

