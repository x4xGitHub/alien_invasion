# Date: 2018/9
# Author: x4x

class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.read_high_score()

        # 游戏刚启动时处于活动状态
        self.game_active = False

        # 游戏刚启动时显示历史最高得分
        self.high_score = self.history_high_score


    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        """初始化历史最高得分"""
        filename = 'high_score.txt'
        with open(filename) as file_object:
            self.history_high_score = file_object.read()
        self.history_high_score = int(self.history_high_score[12:])


            