import json
import os
import folium

def getAddress():
    with open('data/hollys_location.json', 'r', encoding='utf8') as file:
        data = json.load(file)
        return data
    
def searchAddress(address):
    store_list = getAddress()
    search_list = []

    for store in store_list:
        
        if address in store['address']:
            print(f"{store['name']}, {store['address']}, {store['phone']}")
            search_list.append(store)
    return search_list



def create_map(search_list,address):
    lat = search_list[0]['y']  # 위도
    lng = search_list[0]['x']  # 경도
    location = (lat, lng)
    new_map = folium.Map(location=location, zoom_start=12, width='100%', height='100%')

    for store in search_list:
        text = f"{store['name']}<br>{store['phone']}<br>{store['address']}"
        popup = folium.Popup(text,max_width='200')
        location=(store['y'],store['x'])
        folium.Marker(
            location,
            popup,
            icon=folium.Icon(color='blue', icon='glyphicon-road')
        ).add_to(new_map)
    
    new_map.save(f'data/map/{address}.html')
    return new_map

if __name__ == '__main__':  
    os.system('cls')  
    while True:
        print()
        address = input('매장주소> ')
        if address == '': break
        search_list = searchAddress(address)
        if len(search_list) == 0:
            print('검색한 매장이 없습니다.')
        else:
            sel = input('지도를 출력하실래요(Y)> ')
            if sel == 'Y' or sel == 'y':
                create_map(search_list,address)            


    