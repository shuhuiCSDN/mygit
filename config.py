config = {
    "config": {
        "logSearchClientType":"3",  # 从tinyLog检索日志时；默认的客户端日志来源 Android 值为 "3"，iOS为 "1" H5为 "7"
        "host_huidu":  "mobile-api2011.elong.com", #   灰度1 : 10.39.34.70 灰度2 : 10.39.34.70:8080 线上: mobile-api2011.elong.com, 新网关 10.172.20.17
        "host_online": "mobile-api2011.elong.com",
        "HeaderReplace": {
            "DeviceId": ["12345678-1234-5678-9012-123456789010"],  # 如果有多个时，随机替换 "12345678-1234-5678-9012-123456789010"
            "Version": "9.65.0", # 微信钱包/H5 对应的 Version值为 "1301001"；对应ClientType为 "7"
            "ClientType":"3"   # Android 值为 "3"，iOS为 "1" H5为 "7"
        },
        "ReplayCount":2000,
        "PageSize" : 200, #一般不用动；从tinyLog每次检索的PageSize大小
        "ReqFilter":"", # E 仅保留E侧请求 T 仅保留T侧请求 为空或者其它值时；保留所有
        "doDiff": False,
        "doFind":False, # 只对回放有效，是否开启结果查找
        "FindParams":{
            "JsonPath": "$..activityName", # bigOperatingTip.id $.cashBackInfo.statusId
            "Method" : "str_contains",  # 目前支持 len_gt len_ge len_lt len_le contains str_contains eq gt ge lt le ne str_eq等对比表达式；与自动化平台保持一致
            "BaseValue":"单"  #  需要进行对比的基准值
        },
        "getPerfReq":True, #生成压测参数化文件的开关；如果为 True ，则只拉取日志，不进行流量回放，只生成压测参数化文件
        "PerfParams":{  #当 getPerfReq 为True时，对压测参数进行的修改和替换
            "version":'9.57.0',  # 生成AES加密参数时，对应的App版本；需要与天锤中压测请求的Header的Version保持一致
            'filterStr':'IsError',  # 从tinylog中对出参作过滤，包含该值的请求才会保存和生成AES字符串，用于过滤无结果请求，防止压测时因参数化数据导致的异常率较高
            'checkInDate':'2020-05-01',
            'checkOutDate':'2020-05-02'
        }
    },
    "name": "hotel",
    "groups": {
        "apis_A":[
            #"/hotel/cities",
            #"/hotel/getHotelTOrder",
            #"/hotel/getRoomNightPromotionInfo",
            #"/hotel/verifyProductBeforeCreateOrder",
            #"/hotel/getHotelInfo",
            #"/hotel/getHotelDetailWithoutProduct",
            #"/hotel/getHotelProductsByRoomType",
            #"/hotel/keyWordsSuggestV5",
            #"/hotel/getHotelDestinationSug",
            "/hotel/hotelListV4",
            #"/hotel/getRoomNightVouchPrepayRuleInfo",
            "/hotel/getHotelDetailWithoutProductV6",
            "/hotel/getHotelProductsByRoomType",
            "/myelong/getHotelOrder",
            "/myelong/getOrderListByType",
        ],
        "apis_B":[
            "/hotel/getFavoriteHotel",
            "/hotel/getHotelRedPacketsInHotelDetail",
            "/hotel/getHotelCommentsV2",
            "/hotel/getCityIdByNameOrLongLng",
            "/hotel/getPriceRangeList",
            "/hotel/getHomepageOrderList",
            "/hotel/getUserComment",
            "/hotel/getCommentRoomTypeByHotelId",
            "/hotel/getEidbyTid",
            "/hotel/getHotCitiesInSearch",
            "/hotel/getRefundOrder",
            "/hotel/getInvoiceDeliveryInfo",
            "/hotel/getMemberTrackListByRouter",
            "/hotel/getHotelImages",
            "/hotel/getSimpleOrderInfo",
            "/hotel/getHotelFilterInfo",
            "/hotel/getHotelOrderStatusByIDs",
            "/hotel/getHotelDetailByRoomGroup",
            "/hotel/getHotelDetailByRoomGroupV2",
            "/hotel/getSearchParametersMapData",
            "/hotel/getFavoriteCity",
            "/hotel/getTCRedPackageInfo",
            "/hotel/getHotelDetailStaticInfo",
            "/hotel/checkUserIsNewForOrderAndBonus",
            "/hotel/resolveLocation",
            "/hotel/getInvoiceDeliveryInfo",
            "/hotel/getMemberTrackListByRouter",
            "/hotel/availableCouponList4Hotel",
            "/hotel/getHotelImagesV2",
            "/hotel/hotelDetailListByIdsV5",
            "/hotel/getFavoritesListByRouter",
            "/hotel/getMemberOrderInfo4Home",
            "/hotel/getAdditionProductStaticInfo",
            "/hotel/getIsElongNewMember",
            "/hotel/getDelieverTypeList",
            "/hotel/hotelListForActivity",
            "/hotel/getMyMemberCards",
            "/hotel/getTCMemberCtripPromotionProperty",
            "/hotel/gethotelorderrefunddetail",
            "/hotel/getResaleOrderList",

        ],
        "apis_C":[
            "/hotel/getLocationTagInfo",
            "/hotel/getMemBrowseHistoryByCityId",
            "/hotel/getContractUrl",
            "/hotel/getHotelHomeOfWhatLiked",
            "/hotel/getLocationList",
            "/hotel/getrecommendinfo",
            "/hotel/getLotteryBonus",
            "/hotel/getSkipGlobalHotelCityList",
            "/hotel/getRecommendHotelList",
            "/hotel/getHomePagePushInfo",
            "/hotel/getWendaList",
            "/hotel/getLocationTypeInfo",
            "/hotel/getTHongbaoPopInfoForFlight",
            "/hotel/getShotelWhiteList",
            "/hotel/getHotelListForFlight",
            "/hotel/getHotelLocationTraffic",
            "/hotel/localityHotelList",
            "/hotel/getHotelKitsInfo",
            "/hotel/getHotelOrderQuestionDetail",
            "/hotel/getRepairInvoiceStatus",
            "/hotel/getLotteryBox",
            "/hotel/getHotelWechat",
            "/hotel/getRealTimeCreditInfo",
            "/hotel/bedTips",
            "/hotel/getGuessRequire",
            "/hotel/hotelThemeList",
            "/hotel/getShareTemplates",
            "/hotel/getResalePageInfo",
            "/hotel/getHotelHomeBottomWendaStyle",
            "/hotel/getLinkers4T",
            "/hotel/getHotelDetailForDP",
            "/hotel/getLotteryRecords",
            "/hotel/hotelPrompt",
            "/hotel/getCheapChannelHotelDetail",
            "/hotel/getHotelLicenseInfo",
            "/hotel/personalProducts",
            "/hotel/getHotelScanHistorys",
            "/hotel/getHotelFavoriteRank",
            "/hotel/getDiscoveryHotelList",
            "/hotel/gethotelListForTCDetail",
            "/hotel/getCanUsePointDeduction",
            "/hotel/getStaticPreferenceInfo",
            "/hotel/gethotelordercancelreasons",
            "/hotel/getHotelFilterInfoPreference",
            "/hotel/getLocationListV2",
            "/hotel/getWendaDetail",
            "/hotel/getStatutoryHoliday",
            "/hotel/hotelDetailNearbyHotelList",
            "/hotel/getHotelHomeBottomWendaDataOfMyHotel",
            "/hotel/getSearchHistory",
            "/hotel/getSellOutRPTime",
            "/hotel/getOrderCancelInvestOption",
            "/hotel/getHotelListForTrain",
            "/hotel/getcouponPopup"
        ],
        "index": [
            "/hotel/hotelListV4",
            "/hotel/getHotelFilterInfo",
            "/hotel/getHotelDestinationSug",
            "/hotel/keyWordsSuggestV5",
            "/hotel/getMemBrowseHistoryByCityId",
            "/hotel/getMemBrowseHistory",
            "/hotel/getFilterItemSearch",
            "/hotel/hotelDetailNearbyHotelList"
        ],
        "index2":[
            "/hotel/getMemberOrderInfo4Home",
            "/hotel/getHotelHomeBottomWendaStyle",
            "/hotel/getMemberTrackListByRouter",
            "/hotel/getFavoritesListByRouter",
            "/hotel/getHotelHomeBottomWendaDataOfMyHotel",
            "/hotel/getHomePageOperatingTip",
            "/hotel/getHotelHomeOfWhatLiked",
            "/hotel/getMyMemberCards",
            "/hotel/getTCMemberCtripPromotionProperty"
        ],
        "detail" : [
            "/hotel/getHotelDetailWithoutProduct",
            "/hotel/getHotelDetailWithoutProductV6",
            "/hotel/getHotelImagesV2",
            "/hotel/getHotelCommentsV2",
            "/hotel/getHotelInfo",
            "/hotel/getCommentRoomTypeByHotelId",
            "/hotel/getRecommendHotelList",
            "/hotel/getHotelProductsByRoomType",
            "/hotel/getUniqueProduct",
            "/hotel/nameDetection"

        ],
        "order" : [
            "/hotel/getHomepageOrderList",
            "/myelong/getHotelOrder",
            "/hotel/getHotelTOrder",
            "/hotel/verifyProductBeforeCreateOrder",
            "/hotel/getRoomNightVouchPrepayRuleInfo",
            "/hotel/getRoomNightPromotionInfo",
            "/hotel/getAdditionProductStaticInfo"
            "/myelong/customerV2/get",
            "/myelong/getOrderListByType",
            "/myelong/getDelieverTypeList",
            "/hotel/gethotelorderrefunddetail",
            "/hotel/getResaleOrderList",


        ],
        "promotion": [
            "/hotel/getcouponPopup",
            "/hotel/getHotelRedPacketsInHotelDetail",
            "/hotel/getHomePagePushInfo",
            "/hotel/getHomePageOperatingTip",
            "/hotel/getIsElongNewMember",
            "/hotel/getTCRedPackageInfo"
        ],
        "market":[
            "/market/isNewUdidList",
            "/market/isNewUdid",
            "/market/settlement",
            # "/market/getActiveChannel",
            # "/market/appActive",
            "/market/adChannelClick",
            "/market/authorizecallback",
            "/market/submitClickInfo",
            "/market/submitClickInfoNormal",
            "/market/updateChannel",
            "/market/isNewUdidList2"
        ],
        "perf_Test":[
            "/hotel/getHotelDetailWithoutProductV6",
            "/myelong/getHotelOrderList",
            "/myelong/getHotelOrder",
            "/hotel/hotelListV4",
            "/hotel/getHotelProductsByRoomType",
            "/hotel/keyWordsSuggestV5",
            "/hotel/getFilterItemSearch",

        ],
        "default": [
            # "/market/getActiveChannel",
            # "/hotel/getHotelProductsByRoomType",
            # "/market/isNewUdidList"
            # "/user/getCardNumbersByMobile",
            # "/myelong/getOrderListByType"
            # "/hotel/getMemberTrackListByRouter",
            # "/hotel/getDelieverTypeList",
            # "/hotel/getHotelOrderQuestionDetail",
            # "/hotel/getHotelOrderStatusByIDs",
            # "/hotel/getCityIdByNameOrLongLng",
            # "/myelong/getHotelOrderList",
            # "/hotel/getRoomNightPromotionInfo",
            # "/hotel/hotelDetailNearbyHotelList",
            # "/hotel/getHomepageOrderList",
            # "/hotel/getHotelDetailByRoomGroupV2",
            # "/myelong/getHotelOrder",
            # "/hotel/getUniqueProduct",
            # "/hotel/getHotelDetailByRoomGroupV2",
            # "/hotel/getHotelDetailWithoutProduct",
            "/hotel/getHotelDetailWithoutProductV6",
            # "/hotel/getWendaDetail",
            # "/hotel/getHotelInfo",
            # "/hotel/getRepairInvoiceStatus"
        ]
    }

}

