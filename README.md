

# os_info 部署与使用说明

## 一、项目简介
`os_info` 是基于 MCP 协议的 Windows 系统信息查询服务，支持获取本地操作系统、CPU、架构、当前用户等基础信息，适用于自动化运维、系统监控等场景。

## 二、环境要求
- 操作系统：**Windows 10** 及以上
- Python：**3.13 及以上**（建议使用虚拟环境）
- 网络：无需外网，仅本地信息查询

## 三、安装步骤
1. **克隆或下载本项目**
2. **进入 os_info 目录**
3. **安装依赖**
	- 推荐使用 uv：
	  ```powershell
      pip install uv
      uv install .
	  ```

	- 依赖包也可参考 `pyproject.toml` 进行管理。

## 四、启动服务
在 os_info 目录下执行：

```powershell
python server.py
```
或
```powershell
uv run server.py
```

服务默认以 stdio 方式运行，适用于 MCP 框架集成。

## 五、接口说明
### 1. 获取系统信息
- **接口名**：`system_info`
- **请求参数**：无
- **响应示例**：
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
- **错误响应**：
```json
{
	 "success": false,
	 "message": "获取系统信息失败",
	 "error": "具体错误原因"
}
```
- **详细规则**：见 `.clinerules/rules.md`

## 六、常见问题 FAQ
1. **依赖安装失败？**
	- 请确认 Python 版本 >= 3.13，且已激活虚拟环境。
	- 检查 pip/uv 是否可用。
2. **服务无法启动？**
	- 检查端口占用或权限问题。
	- 查看报错信息，确认依赖已全部安装。
3. **接口无响应？**
	- 确认服务已正常运行。
	- 检查调用方式是否符合 MCP 协议。

## 七、注意事项
- 严禁直接执行 Shell、UV 命令及 Python 代码，仅支持接口调用。
- 不处理 XML 文件及内容。
- 不返回任何敏感信息（如密码等）。

## 八、依赖包说明
主要依赖：
- `mcp[cli]>=1.13.0` —— MCP 协议支持
- `schedule>=1.2.2` —— 定时任务支持（如后续扩展）
- `win10toast>=0.9` —— Windows 通知支持

详细依赖请参考 `pyproject.toml`。

## 九、参考与支持
- [MCP 官方文档](https://github.com/modelcontextprotocol)
- 如有问题可提交 issue 或联系维护者。
