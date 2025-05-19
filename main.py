import pygame

pygame.init()
pygame.font.init()

score = 0
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
paddle = pygame.Rect(175, 400, 100, 10)
pygame.display.set_caption("Pong")
font = pygame.font.SysFont(None, 50)

bola = {
    "x_pos": 250.0,
    "y_pos": 250.0,
    "x_speed": 3.0,
    "y_speed": 3.0,
}
raio_bola = 10
rodando = True

while rodando:
    clock.tick(60)
    screen.fill((255, 255, 255))
    screen.blit(font.render(f"Pontos: {score}", False, (0, 0, 0)), (175, 0))
    pygame.draw.rect(screen, (0, 255, 0), paddle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # Movimento do paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and paddle.right < 500:
        paddle.x += 7
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= 7

    # Desenha a bola
    bola_rect = pygame.Rect(bola["x_pos"] - raio_bola, bola["y_pos"] - raio_bola, raio_bola * 2, raio_bola * 2)
    pygame.draw.circle(screen, (255, 0, 0), (int(bola["x_pos"]), int(bola["y_pos"])), raio_bola)

    # Colisão com paredes
    if bola["x_pos"] - raio_bola <= 0 or bola["x_pos"] + raio_bola >= 500:
        bola["x_speed"] *= -1
    if bola["y_pos"] - raio_bola <= 0:
        bola["y_speed"] *= -1
    if bola["y_pos"] + raio_bola >= 500:
        rodando = False  # Fim de jogo se a bola passar

    # Colisão com o paddle
    if bola_rect.colliderect(paddle):
        bola["y_speed"] *= -1
        score += 1

    # Atualiza posição da bola
    bola["x_pos"] += bola["x_speed"]
    bola["y_pos"] += bola["y_speed"]

    pygame.display.flip()

pygame.quit()
