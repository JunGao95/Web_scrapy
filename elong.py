import requests
from bs4 import BeautifulSoup
Indate = '2019-04-03'
Outdate = '2019-04-04'
url = 'http://hotel.elong.com/ajax/tmapilist/getmergedata'
headers = {'Origin': 'http://hotel.elong.com',
           'Referer': 'http://hotel.elong.com/beijing/',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
           'Accept': 'application/json, text/javascript, */*; q=0.01',
           'Content_type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'X_Requested_With': 'XMLHttpRequest'}
data = {'listRequest.areaID': '',
        'listRequest.bedLargeTypes': '',
        'listRequest.bookingChannel': '1',
        'listRequest.breakfasts': '0',
        'listRequest.cancelFree': 'false',
        'listRequest.cardNo': '192928',
        'listRequest.checkInDate': Indate + ' 00:00:00',
        'listRequest.checkOutDate': Outdate + ' 00:00:00',
        'listRequest.cityID': '0101',
        'listRequest.cityName': '北京市',
        'listRequest.customLevel': '11',
        'listRequest.discountIds': '',
        'listRequest.distance': '20000',
        'listRequest.endLat': '0',
        'listRequest.endLng': '0',
        'listRequest.facilityIds': '',
        'listRequest.highPrice': '0',
        'listRequest.hotelBrandIDs': '',
        'listRequest.isAdvanceSave': 'false',
        'listRequest.isAfterCouponPrice': 'true',
        'listRequest.isCoupon': 'false',
        'listRequest.isDebug': 'false',
        'listRequest.isLimitTime': 'false',
        'listRequest.isLogin': 'false',
        'listRequest.isMobileOnly': 'true',
        'listRequest.isNeed5Discount': 'true',
        'listRequest.isNeedNotContractedHotel': 'false',
        'listRequest.isNeedSimilarPrice': 'false',
        'listRequest.isReturnNoRoomHotel': 'true',
        'listRequest.isStaySave': 'false',
        'listRequest.isTrace': 'false',
        'listRequest.isUnionSite': 'false',
        'listRequest.isnstantConfirm': 'false',
        'listRequest.keywords': '',
        'listRequest.keywordsType': '0',
        'listRequest.language': 'cn',
        'listRequest.lat': '39.74162',
        'listRequest.listType': '0',
        'listRequest.lng': '116.1596',
        'listRequest.lowPrice': '0',
        'listRequest.newVersion': 'false',
        'listRequest.orderFromID': '50793',
        'listRequest.pageIndex': '1',
        'listRequest.pageSize': '20',
        'listRequest.payMethod': '0',
        'listRequest.personOfRoom': '0',
        'listRequest.poiId': '51037780',
        'listRequest.poiName': '良乡',
        'listRequest.promotionChannelCode': '0000',
        'listRequest.promotionSwitch': '-1',
        'listRequest.proxyID': 'ZD',
        'listRequest.rankType': '0',
        'listRequest.returnFilterItem': 'true',
        'listRequest.sectionId': '',
        'listRequest.sellChannel': '1',
        'listRequest.seoHotelStar': '0',
        'listRequest.sortDirection': '1',
        'listRequest.sortMethod': '1',
        'listRequest.standBack': '-1',
        'listRequest.starLevels': '',
        'listRequest.startLat': '0',
        'listRequest.startLng': '0',
        'listRequest.taRecommend': 'false',
        'listRequest.themeIds': '',
        'listRequest.traceId': '887833e4-ddce-4a3f-bbc9-c7ad7ac1d980',
        'listRequest.wordId': '51037780',
        'listRequest.wordType': '5'
}
r = requests.post(url, data, headers=headers)
content = r.json()
soup = BeautifulSoup(r.content, 'html.parser')
text = soup.prettify()
with open('test.txt', 'w', encoding='utf-8') as f:
    f.write(text)



