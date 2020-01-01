import scrapy


class searchTicket(scrapy.Spider):
    name = 'ticket'

    def start_requests(self):
        start_urls = [
            'https://www.singaporeair.com/flightsearch/searchFlight.form', 'https://www.singaporeair.com/flightsearch/calendarSearch.form']
        headers = {
            'user-agent': 'Mozilla/5.0 Chrome/79.0.3945.88 Safari/537.36',
            'referer': 'https://www.singaporeair.com/en_UK/sg/home',
            # 'cookie': 'scs=1; VSSESSION=-EFJKdLNG_CnRtoxwxbZnfSAwEPUB89zluJIQsrb.saa-flsearch-16-pksz6; __gtm_pageLoadTimes={"CIB_ChooseFlight":1577803390877}; saadevice=desktop; AKAMAI_SAA_DEVICE_COOKIE=desktop; AKAMAI_SAA_LOCALE_COOKIE=en_UK; rxVisitor=1577798139235G9VO1LKK82VTL9RDH3O3PQ4OV4OOA2TB; _cls_s=a47fec26-5778-4686-bc4c-8d3c1c42aac6:0; _cls_v=933c8f21-775c-4e99-96bb-b4a9d79a33c5; cookieStateSet=hybridState; D_ZID=A4A62208-D24D-3360-AF57-EEA5EA248FF8; D_ZUID=C9265349-C17B-3C4B-97C3-B94DE98F3300; D_HID=65591421-DA15-33D4-8D42-251A500D782A; D_SID=58.182.165.153:IHZbpJ9ggva4gaTJmAzSTjkOemFWGPLQ1k7Kc9IKZtw; AKAMAI_HOME_PAGE_ACCESSED=true; SQCLOGIN_COOKIE=false; LOGIN_POPUP_COOKIE=false; FARE_DEALS_LISTING_COOKIE=false; RU_LOGIN_COOKIE=false; LOGIN_COOKIE=false; AKAMAI_SAA_COUNTRY_COOKIE=SG; AKAMAI_SAA_AIRPORT_COOKIE=SIN; AKAMAI_SAA_DEVICE_COOKIE=desktop; hybridState=ALLOWED; hvsc=true; _gcl_au=1.1.292738999.1577798155; _gid=GA1.2.1525758066.1577798155; _ga=GA1.2.424978341.1577798155; _fbp=fb.1.1577798155022.628565183; __qca=P0-37419907-1577798155030; e62be4a5a17e1043370f85d6e7b65187=3717a1fc4ec7b3f4d43956ab37b35816; D_IID=AC54162E-AF1B-310C-B892-9D399960146E; D_UID=8FBE6B25-A890-31E6-9B1C-666723B357CD; VSUUID=e43b6838c7efb5ba637dfcd61ecc5e180ec62c42fa3a8fc36a1d0a09a485abfa.saa-flsearch-16-pksz6.1577798177003; 7ed305c744789d6aad2192a9a9b1122d=5ec4446dd6b064a2467ebf86e4f40fc8; insKfStatus=N; insUserLastPointOfSale=SG; insUserLastDestination=CTS; insUserLastOrigin=SIN; ins-product-id=www.singaporeair.com%2Fbooking-sin-to-cts; current-currency=SGD; __sonar=8084773859357184546; insUserIsNew=false; insUserLastSeenAsDay=0; ins-gaSSId=0531de45-50c9-5de1-3e38-82cc6e4e248f_1577801264; AKA_A2=A; HSESSIONID=4OlsEzaUR0EguxH3LA4Skr5Z9cyhWIWhapqTiHHr.saa-home-43-90pzh; JSESSIONID=o-9cZG-nedF7hg8eWvZkt-NK6T18fkA7bf6t9L5GlzOK-dVI_U_h!1498873199; AWSELB=FD3BAB93185BF86B05C7865C4221F0D6A1C31371FEDA873E75E91F6E4B75839E1DD564FEF2B71874226281880AADF4344028D366D2A418A02527E8364F946FE20A5F9226686FA9156AC4198684A93B7C654E5A8E9DDE7483DDEFFF8A8D36724AF9EE683187; __zzat153=MDA0dBA=Fz2+aQ==; gig_bootstrap_3_5pyPNTbHCb_zxq33NNn7feUwRjvj5RHt0XMzDjqdx1UnQzS4Vc7oGvWUgjyDLxsM=sociallogin; cfids153=b29/0SfrUAY6iAX7LarKltWqcwgG3DzNjL/4kz2hgb67Mw1JooNQZ7wHujxt0KAy14DNGWwBLD4s2wplwpmS732FdTVMDsRWVzdmtO8DpWgdckgteigBhDyN8mgEPPFjZPrWeSV5twZYvMBj7rA+krkAoq0cwzXdzcko; AWSALB=6ofsJo1w7SiTyQlMkD2KLd66WnPAI3+OrhfFG21y48T7WuS4aDyr52E8MEv58SEfBrgmOtqTH7juThFq9kFQOl74cCq7uYQE6DZhfWb1UxDVCmmBtiVkBBfyhuGZ; cfids153=3jHyMCf4aIFbyzkhA++nft6eUglqQ700Nfetm56CYMm9fyBP0ckAQcB6gbd8YpWk8McoUHrFrQz3UFlP5YMUZmEaSnaJ4dV0R3sR/iI6pdyv34mi8hW+b6HGweaQd3YAQ1MCNijdb9fqzA6wOJn6TzCB26AJMXG7Hgid; SEARCH_SAA_CIB_COOKIE=SIN|CTS|R|01/01/2020-04/01/2020|economy|1|0|0|31/12/2019 22:42:54|SPK; CIB_SEARCH_HISTORY_1=SIN|CTS|R|01/01/2020-04/01/2020|economy|1|0|0|31/12/2019 10:42:54|CTS; CIB_SEARCH_HISTORY_0=SIN|CTS|R|02/01/2020-04/01/2020|economy|1|0|0|31/12/2019 09:16:19|CTS; dtPC=1$403375343_294h-vSYXKSFDVMXUWOBIXHVAPTWEPSOLYINMC; rxvt=1577805182685|1577801261714; dtLatC=3; insdrSV=8; _gat_UA-17015991-1=1; dtSa=true%7CC%7C-1%7CSee%205-day%20fares%7C-%7C1577803507390%7C403375343_294%7Chttps%3A%2F%2Fwww.singaporeair.com%2Fflightsearch%2FsearchFlight.form%7CSelect%20Flight-Commercial%20Booking%7C1577803382690%7C%2Fbooking; dtCookie=1$QSHEB52QBTKN60EH0E0FSH58J6BSGB42|7bacf3aecd29efdf|1; RT="sl=10&ss=1577798138970&tt=30359&obo=0&bcn=%2F%2F60062f0c.akstat.io%2F&sh=1577803376316%3D10%3A0%3A30359%2C1577803352510%3D9%3A0%3A26075%2C1577803105511%3D8%3A0%3A23020%2C1577803084430%3D7%3A0%3A18587%2C1577801301564%3D6%3A0%3A16394&dm=singaporeair.com&si=70d224fb-f74d-4fe6-8731-e7cd7209f6af&nu=https%3A%2F%2Fwww.singaporeair.com%2Fflightsearch%2FcalendarSearch.form&cl=1577803507389&r=https%3A%2F%2Fwww.singaporeair.com%2Fflightsearch%2FsearchFlight.form&ul=1577803507485"'

        }
        form_data = {
            'origin': 'SIN',
            'destination': 'ZQN',
            'tripType': 'R',
            'departureMonth': '02/01/2020',
            'returnMonth': '04/01/2020',
            'cabinClass': 'Y',
            'numOfAdults': '1'
        }
        cookie = 'scs=1; VSSESSION=-EFJKdLNG_CnRtoxwxbZnfSAwEPUB89zluJIQsrb.saa-flsearch-16-pksz6; __gtm_pageLoadTimes={"CIB_ChooseFlight":1577803390877}; saadevice=desktop; AKAMAI_SAA_DEVICE_COOKIE=desktop; AKAMAI_SAA_LOCALE_COOKIE=en_UK; rxVisitor=1577798139235G9VO1LKK82VTL9RDH3O3PQ4OV4OOA2TB; _cls_s=a47fec26-5778-4686-bc4c-8d3c1c42aac6:0; _cls_v=933c8f21-775c-4e99-96bb-b4a9d79a33c5; cookieStateSet=hybridState; D_ZID=A4A62208-D24D-3360-AF57-EEA5EA248FF8; D_ZUID=C9265349-C17B-3C4B-97C3-B94DE98F3300; D_HID=65591421-DA15-33D4-8D42-251A500D782A; D_SID=58.182.165.153:IHZbpJ9ggva4gaTJmAzSTjkOemFWGPLQ1k7Kc9IKZtw; AKAMAI_HOME_PAGE_ACCESSED=true; SQCLOGIN_COOKIE=false; LOGIN_POPUP_COOKIE=false; FARE_DEALS_LISTING_COOKIE=false; RU_LOGIN_COOKIE=false; LOGIN_COOKIE=false; AKAMAI_SAA_COUNTRY_COOKIE=SG; AKAMAI_SAA_AIRPORT_COOKIE=SIN; AKAMAI_SAA_DEVICE_COOKIE=desktop; hybridState=ALLOWED; hvsc=true; _gcl_au=1.1.292738999.1577798155; _gid=GA1.2.1525758066.1577798155; _ga=GA1.2.424978341.1577798155; _fbp=fb.1.1577798155022.628565183; __qca=P0-37419907-1577798155030; e62be4a5a17e1043370f85d6e7b65187=3717a1fc4ec7b3f4d43956ab37b35816; D_IID=AC54162E-AF1B-310C-B892-9D399960146E; D_UID=8FBE6B25-A890-31E6-9B1C-666723B357CD; VSUUID=e43b6838c7efb5ba637dfcd61ecc5e180ec62c42fa3a8fc36a1d0a09a485abfa.saa-flsearch-16-pksz6.1577798177003; 7ed305c744789d6aad2192a9a9b1122d=5ec4446dd6b064a2467ebf86e4f40fc8; insKfStatus=N; insUserLastPointOfSale=SG; insUserLastDestination=CTS; insUserLastOrigin=SIN; ins-product-id=www.singaporeair.com%2Fbooking-sin-to-cts; current-currency=SGD; __sonar=8084773859357184546; insUserIsNew=false; insUserLastSeenAsDay=0; ins-gaSSId=0531de45-50c9-5de1-3e38-82cc6e4e248f_1577801264; AKA_A2=A; HSESSIONID=4OlsEzaUR0EguxH3LA4Skr5Z9cyhWIWhapqTiHHr.saa-home-43-90pzh; JSESSIONID=o-9cZG-nedF7hg8eWvZkt-NK6T18fkA7bf6t9L5GlzOK-dVI_U_h!1498873199; AWSELB=FD3BAB93185BF86B05C7865C4221F0D6A1C31371FEDA873E75E91F6E4B75839E1DD564FEF2B71874226281880AADF4344028D366D2A418A02527E8364F946FE20A5F9226686FA9156AC4198684A93B7C654E5A8E9DDE7483DDEFFF8A8D36724AF9EE683187; __zzat153=MDA0dBA=Fz2+aQ==; gig_bootstrap_3_5pyPNTbHCb_zxq33NNn7feUwRjvj5RHt0XMzDjqdx1UnQzS4Vc7oGvWUgjyDLxsM=sociallogin; cfids153=b29/0SfrUAY6iAX7LarKltWqcwgG3DzNjL/4kz2hgb67Mw1JooNQZ7wHujxt0KAy14DNGWwBLD4s2wplwpmS732FdTVMDsRWVzdmtO8DpWgdckgteigBhDyN8mgEPPFjZPrWeSV5twZYvMBj7rA+krkAoq0cwzXdzcko; AWSALB=6ofsJo1w7SiTyQlMkD2KLd66WnPAI3+OrhfFG21y48T7WuS4aDyr52E8MEv58SEfBrgmOtqTH7juThFq9kFQOl74cCq7uYQE6DZhfWb1UxDVCmmBtiVkBBfyhuGZ; cfids153=3jHyMCf4aIFbyzkhA++nft6eUglqQ700Nfetm56CYMm9fyBP0ckAQcB6gbd8YpWk8McoUHrFrQz3UFlP5YMUZmEaSnaJ4dV0R3sR/iI6pdyv34mi8hW+b6HGweaQd3YAQ1MCNijdb9fqzA6wOJn6TzCB26AJMXG7Hgid; SEARCH_SAA_CIB_COOKIE=SIN|CTS|R|01/01/2020-04/01/2020|economy|1|0|0|31/12/2019 22:42:54|SPK; CIB_SEARCH_HISTORY_1=SIN|CTS|R|01/01/2020-04/01/2020|economy|1|0|0|31/12/2019 10:42:54|CTS; CIB_SEARCH_HISTORY_0=SIN|CTS|R|02/01/2020-04/01/2020|economy|1|0|0|31/12/2019 09:16:19|CTS; dtPC=1$403375343_294h-vSYXKSFDVMXUWOBIXHVAPTWEPSOLYINMC; rxvt=1577805182685|1577801261714; dtLatC=3; insdrSV=8; _gat_UA-17015991-1=1; dtSa=true%7CC%7C-1%7CSee%205-day%20fares%7C-%7C1577803507390%7C403375343_294%7Chttps%3A%2F%2Fwww.singaporeair.com%2Fflightsearch%2FsearchFlight.form%7CSelect%20Flight-Commercial%20Booking%7C1577803382690%7C%2Fbooking; dtCookie=1$QSHEB52QBTKN60EH0E0FSH58J6BSGB42|7bacf3aecd29efdf|1; RT="sl=10&ss=1577798138970&tt=30359&obo=0&bcn=%2F%2F60062f0c.akstat.io%2F&sh=1577803376316%3D10%3A0%3A30359%2C1577803352510%3D9%3A0%3A26075%2C1577803105511%3D8%3A0%3A23020%2C1577803084430%3D7%3A0%3A18587%2C1577801301564%3D6%3A0%3A16394&dm=singaporeair.com&si=70d224fb-f74d-4fe6-8731-e7cd7209f6af&nu=https%3A%2F%2Fwww.singaporeair.com%2Fflightsearch%2FcalendarSearch.form&cl=1577803507389&r=https%3A%2F%2Fwww.singaporeair.com%2Fflightsearch%2FsearchFlight.form&ul=1577803507485"'
        body = 'origin=SIN&destination=CTS&tripType=R&departureMonth=01%2F01%2F2020&returnMonth=04%2F01%2F2020&cabinClass=Y&numOfAdults=1&numOfChildren=0&numOfInfants=0'
        yield scrapy.FormRequest(url=start_urls[0], callback=self.parse,
                                 method='post',  headers=headers, formdata=form_data)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        textResponse = scrapy.http.TextResponse(body=response.body)
        print(textResponse.xpath("/script"))
        self.log('Saved file %s' % filename)
