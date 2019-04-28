import pygame
import requests
import sys
import os
response = None
pygame.init()
screen = pygame.display.set_mode((1000, 650))
a = 135.626082
b = -26.923984
while True:
    for event in pygame.event.get():
        # при закрытии окна
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                running = False
            if event.key == pygame.K_LEFT:
                a -= 1
            elif event.key == pygame.K_RIGHT:
                a += 1
            elif event.key == pygame.K_UP:
                b += 1
            elif event.key == pygame.K_DOWN:
                b -= 1

    try:
        map_request = "http://static-maps.yandex.ru/1.x/?ll="+str(a)+','+str(b)+"&spn=30.5,23.5&l=map"
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



    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()


    os.remove(map_file)