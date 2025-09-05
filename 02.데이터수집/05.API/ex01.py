import requests
import os

#REST_API_KEY = '5e301cd31762802933e8ed71eef92344'
def getBooks(url,query,page,size):
    
    try:
        headers = {'Authorization': 'KakaoAK 5e301cd31762802933e8ed71eef92344'}
        url = f'{url}&query={query}&page={page}&size={size}'
        res = requests.request(method= 'get',url=url,headers=headers)
        data = res.json()
        documents = data['documents']
        print(len(documents))
        
        for doc in documents:
            title = doc['title']
            price = doc['sale_price']
            authors = doc['authors']
            publisher = doc['publisher']
            print(title,price,','.join(authors),publisher)
        
        # {'authors': ['한선관', '김태령'], 
        #  'contents': '이 책은 지금까지 경험하지 못한 코딩 교육의 진수를 보여준다. “코딩 교육이 가야 할 방향은 컴퓨팅 사고력을 높이는  것이다.”라고 이 책의 저자들이 말하듯, “디지털 시대에 적합한 창의력과 문제해결력을 기르기 위한 코딩의 기초부터 응용까지 컴퓨터 코드를 작성하는 것은 물론이고, 알고리즘 학습을 통한 컴퓨팅 사고력을 완전 정복한다.', 
        #  'datetime': '2019-02-28T00:00:00.000+09:00', 'isbn': '8970509720 9788970509723', 
        #  'price': 29000, 
        #  'publisher': '생능출판', 
        #  'sale_price': 26100, 
        #  'status': '정상판매', 
        #  'thumbnail': 'https://search1.kakaocdn.net/thumb/R120x174.q85/?fname=http%3A%2F%2Ft1.daumcdn.net%2Flbook%2Fimage%2F4888715%3Ftimestamp%3D20240330130853', 
        #  'title': '파이썬', 
        #  'translators': [], 
        #  'url': 'https://search.daum.net/search?w=bookpage&bookId=4888715&q=%ED%8C%8C%EC%9D%B4%EC%8D%AC'}
         
    except Exception as err:
        print('접속오류:' ,err) 
        
if __name__ == '__main__':
    url ='https://dapi.kakao.com/v3/search/book?target=title'
    page = 1
    size = 10
    
    
    os.system('cls')
    while True:
        query = input('검색도서명> ')
        if query == '': break
        getBooks(url,query,page,size)
    
