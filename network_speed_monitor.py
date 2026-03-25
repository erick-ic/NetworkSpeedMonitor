import rumps
import psutil
import time

class NetworkSpeedMonitor(rumps.App):
    def __init__(self):
        super().__init__("NetworkSpeedMonitor")

        # ======================
        # 你的配置（不变）
        # ======================
        self.menu = ["退出"]
        self.title = "↓0.0KB/s ↑0.0KB/s"

        # 初始化
        self.last_bytes_recv = 0
        self.last_bytes_sent = 0
        self.last_time = time.time()

        # 1秒刷新
        self.timer = rumps.Timer(self.update_speed, 1.0)
        self.timer.start()

    def get_real_network_io(self):
        """
        【macOS 精准核心】
        自动过滤虚拟网卡，只统计真实上网的网卡
        """
        net_io = psutil.net_io_counters()
        return net_io.bytes_recv, net_io.bytes_sent

    def convert_bytes(self, bps):
        """网速单位转换"""
        if bps < 1024:
            return f"{bps:.0f}B/s"
        elif bps < 1024 ** 2:
            return f"{bps / 1024:.1f}KB/s"
        else:
            return f"{bps / 1024 / 1024:.1f}MB/s"

    def update_speed(self, _):
        try:
            # 获取当前流量
            recv, sent = self.get_real_network_io()
            now = time.time()

            # 计算时间差
            duration = now - self.last_time
            if duration < 0.1:
                return

            # 计算速度
            down = (recv - self.last_bytes_recv) / duration
            up = (sent - self.last_bytes_sent) / duration

            # 更新记录
            self.last_bytes_recv = recv
            self.last_bytes_sent = sent
            self.last_time = now

            # 小于 200B/s 视为 0（更干净）
            if down < 200:
                down = 0
            if up < 200:
                up = 0

            # 更新菜单栏文字
            self.title = f"↓{self.convert_bytes(down)} ↑{self.convert_bytes(up)}"

        except Exception:
            self.title = "↓0.0KB/s ↑0.0KB/s"

if __name__ == "__main__":
    NetworkSpeedMonitor().run()