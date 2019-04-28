import pygame
import requests
import sys
import os

def Load_map(x, y):
    response = None
    b = pygame.Surface((300, 300))
    try:
        map_request = "http://static-maps.yandex.ru/1.x/?ll="+str(x)+","+str(y)+"&z=7&l=sat&size=300,300"
        # map_request = "http://static-maps.yandex.ru/1.x/?&bbox="+str(x)+","+str(y)+"~"+str(x+3)+","+str(y+3)+"&l=sat$size=300,300"
        response = requests.get(map_request)
        if not response:
            print("Ошибка выполнения запроса:")
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)
    except:
        print("Запрос не удалось выполнить. Проверьте наличие сети Интернет.")
        sys.exit(1)

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)

    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    b.blit(pygame.image.load(map_file), (0, 0))
    os.remove(map_file)
    return b


pygame.init()
screen = pygame.display.set_mode((900, 650))
for i in range(4):
    for j in range(4):
        screen.blit(Load_map(121+i*3, -30-j*3), (256*i, 256*j))
#for i in range(650):
    #for j in range(450):
        #r, g, b, a = background.get_at((i, j))
        #if r*2 < b or g*2 < b:
            #pygame.draw.line(background, (0, 0, 0), [i, j], [i, j])
#screen.blit(background, (0, 0))
# pygame.draw.rect(screen, (255, 71, 128), (290, 190, 20, 20), 1)
# background.blit(pix_map[n], (j * 96, i * 96))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()


# os.remove(map_file)