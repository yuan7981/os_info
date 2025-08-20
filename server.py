import platform
import os
import getpass
from mcp.server.fastmcp import FastMCP
from typing import Dict

mcp = FastMCP("os_info")

@mcp.tool()
async def system_info() -> Dict:
    """
    获取系统基本信息
    """
    try:
        info = {
            "os": platform.system(),
            "os_version": platform.version(),
            "release": platform.release(),
            "architecture": platform.machine(),
            "processor": platform.processor(),
            "cpu_count": os.cpu_count(),
            "user": getpass.getuser()
        }
        return {
            "success": True,
            "message": "获取系统信息成功",
            "info": info
        }
    except Exception as e:
        return {
            "success": False,
            "message": "获取系统信息失败",
            "error": str(e)
        }

if __name__ == "__main__":
    mcp.run(transport="stdio")
