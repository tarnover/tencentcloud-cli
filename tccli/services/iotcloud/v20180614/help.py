# -*- coding: utf-8 -*-
DESC = "iotcloud-2018-06-14"
INFO = {
  "CreateTask": {
    "params": [
      {
        "name": "TaskType",
        "desc": "任务类型，取值为 “UpdateShadow” 或者 “PublishMessage”"
      },
      {
        "name": "ProductId",
        "desc": "执行任务的产品ID"
      },
      {
        "name": "DeviceNameFilter",
        "desc": "执行任务的设备名的正则表达式"
      },
      {
        "name": "ScheduleTimeInSeconds",
        "desc": "任务开始执行的时间。 取值为 Unix 时间戳，单位秒，且需大于等于当前时间时间戳，0为系统当前时间时间戳，即立即执行，最大为当前时间86400秒后，超过则取值为当前时间86400秒后"
      },
      {
        "name": "Tasks",
        "desc": "任务描述细节，描述见下 Task"
      },
      {
        "name": "MaxExecutionTimeInSeconds",
        "desc": "最长执行时间，单位秒，被调度后超过此时间仍未有结果则视为任务失败。取值为0-86400，默认为86400"
      }
    ],
    "desc": "本接口（CreateTask）用于创建一个批量任务。目前此接口可以创建批量更新影子以及批量下发消息的任务"
  },
  "ReplaceTopicRule": {
    "params": [
      {
        "name": "RuleName",
        "desc": "规则名称"
      },
      {
        "name": "TopicRulePayload",
        "desc": "替换的规则包体"
      },
      {
        "name": "ModifyType",
        "desc": "修改类型，0：其他，1：创建行为，2：更新行为，3：删除行为"
      },
      {
        "name": "ActionIndex",
        "desc": "action增删改变更填对应topicRulePayload里面第几个action"
      }
    ],
    "desc": "本接口（ReplaceTopicRule）用于修改替换规则"
  },
  "DescribeDeviceShadow": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品 ID"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}"
      }
    ],
    "desc": "本接口（DescribeDeviceShadow）用于查询虚拟设备信息。"
  },
  "EnableTopicRule": {
    "params": [
      {
        "name": "RuleName",
        "desc": "规则名称"
      }
    ],
    "desc": "本接口（EnableTopicRule）用于启用规则"
  },
  "CreateMultiDevice": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品 ID。创建产品时腾讯云为用户分配全局唯一的 ID"
      },
      {
        "name": "DeviceNames",
        "desc": "批量创建的设备名数组，单次最多创建 100 个设备。命名规则：[a-zA-Z0-9:_-]{1,48}"
      }
    ],
    "desc": "本接口（CreateMultiDevice）用于批量创建物联云设备。"
  },
  "CreateTopicRule": {
    "params": [
      {
        "name": "RuleName",
        "desc": "规则名称"
      },
      {
        "name": "TopicRulePayload",
        "desc": "规则内容"
      }
    ],
    "desc": "本接口（CreateTopicRule）用于创建一个规则"
  },
  "CancelTask": {
    "params": [
      {
        "name": "Id",
        "desc": "任务 ID"
      }
    ],
    "desc": "本接口（CancelTask）用于取消一个未被调度的任务。"
  },
  "DisableTopicRule": {
    "params": [
      {
        "name": "RuleName",
        "desc": "规则名称"
      }
    ],
    "desc": "本接口（DisableTopicRule）用于禁用规则"
  },
  "CreateTopicPolicy": {
    "params": [
      {
        "name": "ProductID",
        "desc": "产品ID"
      },
      {
        "name": "TopicName",
        "desc": "Topic名称"
      },
      {
        "name": "Privilege",
        "desc": "Topic权限，1发布，2订阅，3订阅和发布"
      },
      {
        "name": "BrokerSubscribe",
        "desc": "代理订阅信息"
      }
    ],
    "desc": "本接口（CreateTopicPolicy）用于创建一个Topic"
  },
  "CreateProduct": {
    "params": [
      {
        "name": "ProductName",
        "desc": "产品名称，名称不能和已经存在的产品名称重复。命名规则：[a-zA-Z0-9:_-]{1,32}"
      },
      {
        "name": "ProductProperties",
        "desc": "产品属性"
      },
      {
        "name": "Skey",
        "desc": "创建LoRa产品需要的Skey"
      }
    ],
    "desc": "本接口（CreateProduct）用于创建一个新的物联网通信产品"
  },
  "DescribeProducts": {
    "params": [
      {
        "name": "Offset",
        "desc": "分页偏移，Offset从0开始"
      },
      {
        "name": "Limit",
        "desc": "分页大小，当前页面中显示的最大数量，值范围 10-250。"
      },
      {
        "name": "Filters",
        "desc": "过滤条件"
      }
    ],
    "desc": "本接口（DescribeProducts）用于列出产品列表。"
  },
  "DescribeTask": {
    "params": [
      {
        "name": "Id",
        "desc": "任务ID"
      }
    ],
    "desc": "本接口（DescribeTask）用于查询一个已创建任务的详情，任务保留一个月"
  },
  "DeleteDevice": {
    "params": [
      {
        "name": "ProductId",
        "desc": "设备所属的产品 ID"
      },
      {
        "name": "DeviceName",
        "desc": "需要删除的设备名称"
      },
      {
        "name": "Skey",
        "desc": "删除LoRa设备以及LoRa网关设备需要skey"
      }
    ],
    "desc": "本接口（DeleteDevice）用于删除物联网通信设备。"
  },
  "CreateDevice": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品 ID 。创建产品时腾讯云为用户分配全局唯一的 ID"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称。命名规则：[a-zA-Z0-9:_-]{1,48}。"
      },
      {
        "name": "Attribute",
        "desc": "设备属性"
      },
      {
        "name": "DefinedPsk",
        "desc": "是否使用自定义PSK，默认不使用"
      },
      {
        "name": "Isp",
        "desc": "运营商类型，当产品是NB-IoT产品时，此字段必填。1表示中国电信，2表示中国移动，3表示中国联通"
      },
      {
        "name": "Imei",
        "desc": "IMEI，当产品是NB-IoT产品时，此字段必填"
      },
      {
        "name": "LoraDevEui",
        "desc": "LoRa设备的DevEui，当创建LoRa时，此字段必填"
      },
      {
        "name": "LoraMoteType",
        "desc": "LoRa设备的MoteType"
      },
      {
        "name": "Skey",
        "desc": "创建LoRa设备需要skey"
      }
    ],
    "desc": "本接口（CreateDevice）用于新建一个物联网通信设备。"
  },
  "PublishMessage": {
    "params": [
      {
        "name": "Topic",
        "desc": "消息发往的主题。命名规则：${ProductId}/${DeviceName}/[a-zA-Z0-9:_-]{1,128}"
      },
      {
        "name": "Payload",
        "desc": "消息内容"
      },
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      },
      {
        "name": "Qos",
        "desc": "服务质量等级，取值为0， 1"
      }
    ],
    "desc": "本接口（PublishMessage）用于向某个主题发消息。"
  },
  "DeleteProduct": {
    "params": [
      {
        "name": "ProductId",
        "desc": "需要删除的产品 ID"
      },
      {
        "name": "Skey",
        "desc": "删除LoRa产品需要skey"
      }
    ],
    "desc": "本接口（DeleteProduct）用于删除一个物联网通信产品。"
  },
  "DescribeTasks": {
    "params": [
      {
        "name": "Offset",
        "desc": "分页偏移，从0开始"
      },
      {
        "name": "Limit",
        "desc": "分页的大小，数值范围 1-250"
      }
    ],
    "desc": "本接口（DescribeTasks）用于查询已创建的任务列表，任务保留一个月"
  },
  "DescribeMultiDevices": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品 ID，创建产品时腾讯云为用户分配全局唯一的 ID"
      },
      {
        "name": "TaskId",
        "desc": "任务 ID，由批量创建设备接口返回"
      },
      {
        "name": "Offset",
        "desc": "分页偏移"
      },
      {
        "name": "Limit",
        "desc": "分页大小，每页返回的设备个数"
      }
    ],
    "desc": "本接口（DescribeMultiDevices）用于查询批量创建设备的执行结果。"
  },
  "UpdateTopicPolicy": {
    "params": [
      {
        "name": "ProductID",
        "desc": "产品ID"
      },
      {
        "name": "TopicName",
        "desc": "更新前Topic名"
      },
      {
        "name": "NewTopicName",
        "desc": "更新后Topic名"
      },
      {
        "name": "Privilege",
        "desc": "Topic权限"
      },
      {
        "name": "BrokerSubscribe",
        "desc": "代理订阅信息"
      }
    ],
    "desc": "本接口（UpdateTopicPolicy）用于更新Topic信息"
  },
  "DescribeDevices": {
    "params": [
      {
        "name": "ProductId",
        "desc": "需要查看设备列表的产品 ID"
      },
      {
        "name": "Offset",
        "desc": "分页偏移"
      },
      {
        "name": "Limit",
        "desc": "分页的大小，数值范围 10-100"
      },
      {
        "name": "FirmwareVersion",
        "desc": "设备固件版本号，若不带此参数会返回所有固件版本的设备"
      }
    ],
    "desc": "本接口（DescribeDevices）用于查询物联网通信设备的设备列表。"
  },
  "UpdateDeviceShadow": {
    "params": [
      {
        "name": "ProductId",
        "desc": "产品ID"
      },
      {
        "name": "DeviceName",
        "desc": "设备名称"
      },
      {
        "name": "State",
        "desc": "虚拟设备的状态，JSON字符串格式，由desired结构组成"
      },
      {
        "name": "ShadowVersion",
        "desc": "当前版本号，需要和后台的version保持一致，才能更新成功"
      }
    ],
    "desc": "本接口（UpdateDeviceShadow）用于更新虚拟设备信息。"
  },
  "DescribeMultiDevTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务 ID，由批量创建设备接口返回"
      },
      {
        "name": "ProductId",
        "desc": "产品 ID，创建产品时腾讯云为用户分配全局唯一的 ID"
      }
    ],
    "desc": "本接口（DescribeMultiDevTask）用于查询批量创建设备任务的执行状态。"
  },
  "DescribeDevice": {
    "params": [
      {
        "name": "ProductID",
        "desc": "产品ID"
      },
      {
        "name": "DeviceName",
        "desc": "设备名"
      }
    ],
    "desc": "本接口（DescribeDevice）用于查看设备信息"
  },
  "DeleteTopicRule": {
    "params": [
      {
        "name": "RuleName",
        "desc": "规则名"
      }
    ],
    "desc": "本接口（DeleteTopicRule）用于删除规则"
  }
}