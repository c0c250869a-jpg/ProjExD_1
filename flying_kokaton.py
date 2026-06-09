import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)  # 練習8：背景画像の左右反転
    kk_img = pg.image.load("fig/3.png")  # 練習3：こうかとんSurfaceの作成
    kk_img = pg.transform.flip(kk_img, True, False)  # 練習3：こうかとんの左右
    kk_rct = kk_img.get_rect() #練習10
    kk_rct.center = 300, 200#練習10-2:こうかとん
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_lst = pg.key.get_pressed() #練習10-3
        #print(key_let)
        mv_x = -1
        mv_y = 0
        if key_lst[pg.K_UP]:
            mv_y -= 1   #上矢印キーが押されたら # 上に移動
        if key_lst[pg.K_DOWN]:  #下矢印キーが押されたら  
            mv_y += 1#下に移送
        if key_lst[pg.K_LEFT]:
            mv_x -= 1
        if key_lst[pg.K_RIGHT]:
            mv_x += 2
        kk_rct.move_ip(mv_x, mv_y)
        #演習1
        if not key_lst[pg.K_UP] and not key_lst[pg.K_DOWN] and not key_lst[pg.K_LEFT] and not key_lst[pg.K_RIGHT]:
            kk_rct.move_ip(-1,0)

        x = tmr%3200
        screen.blit(bg_img, [-x, 0])  # 練習5：背景画像を右から左へ
        screen.blit(bg_img2, [-x+1600, 0])  # 練習7：2枚目Surface
        screen.blit(bg_img, [-x+3200, 0])  # 練習9：3枚目の背景画像の描画
        screen.blit(kk_img, kk_rct)  # 練習4：こうかとんSurfaceの描画
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()