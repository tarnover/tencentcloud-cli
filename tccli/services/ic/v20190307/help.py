# -*- coding: utf-8 -*-
DESC = "ic-2019-03-07"
INFO = {
  "SendSms": {
    "params": [
      {
        "name": "Sdkappid",
        "desc": "应用id"
      },
      {
        "name": "Iccid",
        "desc": "卡片id"
      },
      {
        "name": "Content",
        "desc": "短信内容"
      }
    ],
    "desc": "发送短信息接口"
  },
  "DescribeApp": {
    "params": [
      {
        "name": "Sdkappid",
        "desc": "物联卡应用ID"
      }
    ],
    "desc": "根据应用id查询物联卡应用详情"
  },
  "SendMultiSms": {
    "params": [
      {
        "name": "Sdkappid",
        "desc": "应用id"
      },
      {
        "name": "Iccids",
        "desc": "卡片列表"
      },
      {
        "name": "Content",
        "desc": "短信内容"
      }
    ],
    "desc": "群发短信"
  },
  "DescribeCard": {
    "params": [
      {
        "name": "Sdkappid",
        "desc": "应用id"
      },
      {
        "name": "Iccid",
        "desc": "卡片id"
      }
    ],
    "desc": "查询卡片详细信息"
  },
  "DescribeCards": {
    "params": [
      {
        "name": "Sdkappid",
        "desc": "应用id"
      },
      {
        "name": "Offset",
        "desc": "偏移值"
      },
      {
        "name": "Limit",
        "desc": "列表限制"
      }
    ],
    "desc": "查询卡片列表信息"
  }
}