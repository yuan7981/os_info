# Windows系统信息查询服务使用规则

## 系统要求
- 操作系统: Windows 10
- 禁止执行: Shell 命令, UV 命令, Python 代码
- 禁止处理: XML 文件/内容
- 禁止回复: Shell 命令, UV 命令, Python 代码, XML 文件/内容

## 功能描述
Windows 系统信息查询服务 - 提供系统基本信息，包括操作系统名称、版本、CPU 核心数、架构和当前登录用户等。

## 功能接口

### 1. 获取系统信息 (system_info)
#### 参数说明
- 无需参数

#### 响应格式
```json
{
    "success": true,
    "message": "获取系统信息成功",
    "info": {
        "os": "Windows",
        "os_version": "10.0.19045",
        "release": "10",
        "architecture": "AMD64",
        "processor": "Intel64 Family 6 Model 158 Stepping 10 GenuineIntel",
        "cpu_count": 8,
        "user": "当前登录用户名"
    }
}
```
#### 错误响应格式
```json
{
    "success": false,
    "message": "获取系统信息失败",
    "error": "具体错误原因"
}
```
#### 使用限制
- 数据范围: 仅查询本地系统信息，不访问网络
- 数据持久化: 无需存储，所有信息实时获取
- 安全性: 不返回密码或敏感信息
#### 注意事项

- 响应字段 cpu_count 表示逻辑 CPU 核心数
- architecture 表示系统架构
- user 为当前登录的 Windows 用户名
- 服务重启后依旧可用，无需额外初始化