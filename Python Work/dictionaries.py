dict = {
    'species' : 'Panthera',
    'name' : 'Mufasa',
    'color' : 'Yellow'
}

countries = {
    'United Kingdom' : 'London',
    'France' : 'Paris',
    'Germany' : 'Berlin',
    'Spain' : 'Madrid',
    'Italy' : 'Rome'
}

countries['Brazil'] = 'Sao Paulo'
countries['Peru'] = 'Lima'


countries_language = {'United Kingdom' : 'English', 'France' : 'French', 'Germany' : 'German', 'Spain' : 'Spanish', 'Italy' : 'Italian' }
countries.update(countries_language)
print(countries)