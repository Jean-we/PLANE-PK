import pygame as py
from random import randint


py.init()
py.font.init()


# 创建得分情况字体对象
font = py.font.SysFont("击杀敌机", 30)
font_type = py.font.Font(None, 30)

# 初始化得分情况
score = 0
score_text = font.render("fraction: {0}".format(score), False, (255, 255, 255), None)

# 背景板
suface = py.display.set_mode((800,484))

# 标题
py.display.set_caption("飞机大战")
# 游戏背景图片
img_game_background = py.image.load(
    r"/Users/jean/Desktop/python项目实战/自制小程序/飞机大战/素材/images/background.png"
)
# 开始界面图片
Start_the_interface_img = py.image.load(
    r"/Users/jean/Desktop/python项目实战/自制小程序/飞机大战/素材/images/Start_the_interface.png"
)

#窗口矩形位置信息
suface_rect = suface.get_rect()

# FPS
clock = py.time.Clock()


# 精灵类/父类
class Sprite(py.sprite.Sprite):
    def __init__(self):
        # 初始化父类
        super().__init__()


# 英雄飞机类/子类
class Hero_planes:
    def __init__(self, x, y, counter):
        # 时钟
        self.clock = py.time.Clock()
        # 出场动画计数器
        self.counter = counter
        # 英雄飞机图片
        self.old_image = py.image.load(
            r"/Users/jean/Desktop/python项目实战/自制小程序/飞机大战/素材/images/me1.png"
        )
        self.new_image = py.transform.scale(self.old_image, (51, 63))
        # 英雄飞机图片矩形位置
        self.image_rect = self.new_image.get_rect()
        # 出场坐标x/y
        self.location_x = x
        self.location_y = y

    # 飞机出场动画
    def appearance_animation(self):
        suface.blit(self.new_image, (self.location_x, self.location_y))
        if self.location_y == 420:
            suface.blit(self.new_image, (self.location_x, self.location_y))
            self.counter += 1
            return self.counter

        else:
            self.location_y -= 2
            suface.blit(self.new_image, (self.location_x, self.location_y))

    # 操作飞机移动
    def move(self):
        # 更新英雄飞机图片坐标
        self.image_rect.topleft = (self.location_x, self.location_y)
        # 绘制英雄飞机
        suface.blit(self.new_image, (self.location_x, self.location_y))
        # 判断英雄飞机是否在画面内
        if suface.get_rect().contains(self.image_rect):
            # 英雄飞机的移动
            if keys[py.K_w]:
                self.location_y -= 7
                suface.blit(self.new_image, (self.location_x, self.location_y))

            elif keys[py.K_s]:
                self.location_y += 7
                suface.blit(self.new_image, (self.location_x, self.location_y))

            elif keys[py.K_a]:
                self.location_x -= 7
                suface.blit(self.new_image, (self.location_x, self.location_y))

            elif keys[py.K_d]:
                self.location_x += 7
                suface.blit(self.new_image, (self.location_x, self.location_y))

        else:
            # 边界处理
            if self.location_x < 0:
                self.location_x = 0
            elif self.location_x > 730:
                self.location_x = 728
            elif self.location_y < 0:
                self.location_y = 0
            elif self.location_y > 420:
                self.location_y = 418
        py.display.flip()
# 英雄飞机出场计数器
counter = 0
# 英雄飞机初始坐标
a0 = Hero_planes(400, 480, counter=counter)


# 敌方飞机1/子类
class Enemy_aircraft1(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 飞机对象/suface/老
        self.old_image = py.image.load(
            r"/Users/jean/Desktop/python项目实战/自制小程序/飞机大战/素材/images/enemy1.png"
        )
        # 飞机对象/suface/新
        self.new_image = py.transform.scale(self.old_image, (51, 63))

        # image属性，变量不可变
        self.image = self.new_image
        # 飞机矩形位置
        self.rect = self.new_image.get_rect()
        # 初始值计数器
        self.enumeration = 0

    # 随机位置/速度
    def random(self):
        # 随机位置x/y
        self.rect.x = randint(0, 770)
        self.rect.y = randint(-15, 3)
        # 移动速度
        self.speed = randint(1, 3)

    # 更新
    def update(self):
        if self.enumeration == 0:
            a1.random()
            self.enumeration += 1
        else:
            # 更新操作
            self.rect.y += self.speed
            if self.rect.y > 650:
                # 销毁
                elf_group.remove(self)
                self.enumeration = 0

    # 渲染
    def draw(self):
        self.new_rect = self.image.get_rect()
        suface.blit(self.image, (self.rect.x, self.rect.y))
        py.display.update(self.new_rect)
a1 = Enemy_aircraft1()


# 敌方飞机2/子类
class Enemy_aircraft2(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 飞机对象/suface/老
        self.old_image = py.image.load(
            r"/Users/jean/Desktop/python项目实战/自制小程序/飞机大战/素材/images/enemy2.png"
        )
        # 飞机对象/suface/新
        self.new_image = py.transform.scale(self.old_image, (69, 99))
        # image属性，变量不可变
        self.image = self.new_image
        # 飞机矩形位置
        self.rect = self.new_image.get_rect()
        # 初始值计数器
        self.enumeration = 0

    # 随机位置/速度
    def random(self):
        # 随机位置x/y
        self.rect.x = randint(0, 770)
        self.rect.y = randint(-15, 3)
        # 移动速度
        self.speed = randint(1, 3)

    # 更新
    def update(self):
        if self.enumeration == 0:
            a2.random()
            self.enumeration += 1
        else:
            # 更新操作
            self.rect.y += self.speed
            if self.rect.y > 650:
                # 销毁
                elf_group.remove(self)
                self.enumeration = 0

    # 渲染
    def draw(self):
        self.new_rect = self.image.get_rect()
        suface.blit(self.image, (self.rect.x, self.rect.y))
        py.display.update(self.new_rect)
a2 = Enemy_aircraft2()


# 敌方飞机3/子类
class Enemy_aircraft3(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # 飞机对象/suface/老
        self.old_image = py.image.load(
            r"/Users/jean/Desktop/python项目实战/自制小程序/飞机大战/素材/images/enemy3.png"
        )
        # 飞机对象/suface/新
        self.new_image = py.transform.scale(self.old_image, (84, 149))
        # image属性，变量不可变
        self.image = self.new_image
        # 飞机矩形位置
        self.rect = self.new_image.get_rect()
        # 初始值计数器
        self.enumeration = 0

    # 随机位置/速度
    def random(self):
        # 随机位置x/y
        self.rect.x = randint(0, 770)
        self.rect.y = randint(-15, 3)
        # 移动速度
        self.speed = randint(1, 4)

    # 更新
    def update(self):
        if self.enumeration == 0:
            a3.random()
            self.enumeration += 1
        else:
            # 更新操作
            self.rect.y += self.speed
            if self.rect.y > 650:
                # 销毁
                elf_group.remove(self)
                self.enumeration = 0

    # 渲染
    def draw(self):
        self.new_rect = self.image.get_rect()
        suface.blit(self.image, (self.rect.x, self.rect.y))
        py.display.update(self.new_rect)
a3 = Enemy_aircraft3()


# 子弹类
class Bullent(py.sprite.Sprite):
    def __init__(self):
        # 确保成功调用
        super().__init__()
        # 子弹图片
        self.image = py.image.load(
            r"/Users/jean/Desktop/python项目实战/自制小程序/飞机大战/素材/images/bullet1.png"
        )
        # 初始化子弹矩形位置,也是英雄飞机位置
        self.rect = a0.new_image.get_rect()
        self.rect.x = a0.location_x + a0.new_image.get_width() // 2 - self.rect.width // 2
        self.rect.y = a0.location_y - self.rect.height
        # 子弹速度
        self.speed = 2
    #更新
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

    # 渲染
    def draw(self):
        suface.blit(self.image,(self.rect.x,self.rect.y))






# 子弹精灵组,用于管理子弹发射
bullet_sprites = py.sprite.Group()
# 敌机精灵组，用于统一管理飞机对象
elf_group = py.sprite.Group()


# 渲染变量
a = False
# 游戏主循环
while True:
    if len(list(elf_group)) == 0:
        # 创建事件类型
        SPAWN_ENEMY = py.USEREVENT
        # 创建事件对象
        incident = py.event.Event(SPAWN_ENEMY)
        # 发出事件
        py.event.post(incident)

    # 事件检测
    keys = py.key.get_pressed()

    # 退出事件捕捉
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()

    # 开始界面图片显示
    suface.blit(Start_the_interface_img, (0, 0))
    # 开始游戏区域
    # 开始游戏按钮区域
    region = py.Rect((285,124,580-285,176-124))

    # 获取鼠标位置，返回元祖
    mouse_x, mouse_y = py.mouse.get_pos()
    # 判断鼠标是否在区域内
    if region.collidepoint(mouse_x, mouse_y):
        # 获取鼠标左击事件，返回MOUSEBUTTONDOWN对象
        if event.type == py.MOUSEBUTTONDOWN:
            a = True

    if bool(a) is False:
        # 开始游戏画面
        suface.blit(Start_the_interface_img, (0, 0))

    elif bool(a) is True:
        # 游戏开始画面
        suface.blit(img_game_background, (0, 0))
        # 分数显示
        suface.blit(score_text, (10, 10))
        if a0.counter == 1:
            # 接受事件，并作出操作
            if event.type == SPAWN_ENEMY:
                # 对象添加进精灵组
                elf_group.add(a1)
                elf_group.add(a2)
                elf_group.add(a3)

            # 调用更新
            elf_group.update()
            # 调用渲染
            elf_group.draw(suface)
            # 飞机操作方法
            a0.move()
            # 判断操作
            if keys[py.K_SPACE]:
                # 创建实例对象
                a4 = Bullent()
                # 添加精灵组
                bullet_sprites.add(a4)

            # 渲染子弹
            bullet_sprites.update()
            bullet_sprites.draw(suface)

        else:
            # 飞机出场方法
            a0.appearance_animation()

    # 时钟，控制渲染图片上限
    clock.tick(45)
    py.display.flip()
