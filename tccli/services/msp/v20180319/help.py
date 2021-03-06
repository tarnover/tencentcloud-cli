# -*- coding: utf-8 -*-
DESC = "msp-2018-03-19"
INFO = {
  "ListMigrationTask": {
    "params": [
      {
        "name": "Offset",
        "desc": "记录起始数，默认值为0"
      },
      {
        "name": "Limit",
        "desc": "记录条数，默认值为10"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID，默认值为空"
      }
    ],
    "desc": "获取迁移任务列表"
  },
  "RegisterMigrationTask": {
    "params": [
      {
        "name": "TaskType",
        "desc": "任务类型，取值database（数据库迁移）、file（文件迁移）、host（主机迁移）"
      },
      {
        "name": "TaskName",
        "desc": "任务名称"
      },
      {
        "name": "ServiceSupplier",
        "desc": "服务提供商名称"
      },
      {
        "name": "SrcInfo",
        "desc": "迁移任务源信息"
      },
      {
        "name": "DstInfo",
        "desc": "迁移任务目的信息"
      },
      {
        "name": "CreateTime",
        "desc": "迁移任务创建时间"
      },
      {
        "name": "UpdateTime",
        "desc": "迁移任务更新时间"
      },
      {
        "name": "MigrateClass",
        "desc": "迁移类别，如数据库迁移中mysql:mysql代表从mysql迁移到mysql，文件迁移中oss:cos代表从阿里云oss迁移到腾讯云cos"
      },
      {
        "name": "SrcAccessType",
        "desc": "源实例接入类型"
      },
      {
        "name": "SrcDatabaseType",
        "desc": "源实例数据库类型"
      },
      {
        "name": "DstAccessType",
        "desc": "目标实例接入类型"
      },
      {
        "name": "DstDatabaseType",
        "desc": "目标实例数据库类型"
      }
    ],
    "desc": "注册迁移任务"
  },
  "ModifyMigrationTaskStatus": {
    "params": [
      {
        "name": "Status",
        "desc": "任务状态"
      },
      {
        "name": "TaskId",
        "desc": "任务ID"
      }
    ],
    "desc": "更新迁移任务状态"
  },
  "DeregisterMigrationTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID"
      }
    ],
    "desc": "取消注册迁移任务"
  },
  "DescribeMigrationTask": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID"
      }
    ],
    "desc": "获取指定迁移任务详情"
  },
  "ModifyMigrationTaskBelongToProject": {
    "params": [
      {
        "name": "TaskId",
        "desc": "任务ID"
      },
      {
        "name": "ProjectId",
        "desc": "项目ID"
      }
    ],
    "desc": "更改迁移任务所属项目"
  },
  "ListMigrationProject": {
    "params": [
      {
        "name": "Offset",
        "desc": "记录起始数，默认值为0"
      },
      {
        "name": "Limit",
        "desc": "返回条数，默认值为500"
      }
    ],
    "desc": "获取迁移项目名称列表"
  }
}