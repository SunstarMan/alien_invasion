import sys  # 玩家退出时，我们将使用模块sys来退出游戏
import pygame
from bullet import Bullet


def fire_bullet(ai_settings, screen, ship, bullets):
    """
    如果还没有到达限制，就发射一颗子弹
    :param ai_settings:
    :param screen:
    :param ship:
    :param bullets:
    :return:
    """
    # 创建一颗子弹，并将其加入到编组bullets中(bullets中最多有3颗子弹)
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keydown_event(event, ai_settings, screen, ship, bullets):
    """
    响应按键
    :param event:
    :param ship:
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:  # 玩家摁下空格键，发射子弹
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_event(event, ship):
    """
    响应松开
    :param event:
    :param ship:
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """
    更新屏幕上的图像，并切换到新屏幕
    :param ai_settings:
    :param screen:
    :param ship:
    :return:
    """
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    pygame.display.flip()


def update_bullets(bullets):
    """
    更新子弹的位置，并删除已消失的子弹
    :param bullets:
    :return:
    """
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹:子弹的rect的bottom属性为零，它表明子弹已穿过屏幕顶端
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))  # 若留下这条语句，游戏的速度将大大降低，因为将输出写入到终端而花费的时间比将图形绘制到游戏窗口花费的时间还多
