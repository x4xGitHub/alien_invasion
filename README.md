# Alien Invasion - 外星人入侵
learning project from book "Python Crash Course"  
依据由Eric Matthes老师编写的Python入门书籍《Python编程 从入门到实践》项目部分开发的2D游戏

## 游戏玩法
- 操作  
    按键    | 行为  
    :-----: | :------:  
    p play  | 开始游戏  
    ↑ up    | 玩家向上移动  
    ↓ down  | 玩家向下移动  
    ← right | 玩家向左移动  
    → left  | 玩家向右移动  
    space   | 玩家开火  
    q quit  | 退出游戏  

- 目标  
    合理操作, 挑战关卡, 将每一关的外星人飞船尽可能的消灭, 提升等级(Level, 其实可以说是关卡数), 取得越多的得分(Score)

- 限制/难度  
    玩家飞船数: 3  
    屏幕最大存在子弹数: 3  
    随着Level的提升, 外星人飞船的移动速度会越来越快  
    当外星人飞船触碰到玩家飞船时, 玩家飞船销毁1艘  
    当外星人飞船触碰到界面底部时, 玩家飞船销毁1艘  
    当玩家所有飞船都销毁, 游戏结束

## 开发细节
- Pygame  
    Pygame官方网址: https://www.pygame.org/  
    本项目开发完全基于Pygame模块, 因此在运行代码时必须要先安装并运行Pygame

- alien_invasion.py
    本项目的主文件, 在安装Pygame的基础上, 只需运行该文件  

- 开发环境/工具  
    Windows 10  
    Python 3.6
