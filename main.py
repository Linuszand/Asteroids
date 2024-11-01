import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from circleshape import CircleShape
from shot import Shot

def main():
    pygame.init()
    pygame.font.init()
    the_font = pygame.font.SysFont('Comic Sans MS', 30)
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    derp = 0
    time = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    new_triangle = Player(x, y)
    asteroid_field = AsteroidField()
    score = 0
  

    while running:
        text_surf = the_font.render(str(score), False, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(derp)

        for asteroid in asteroids:
            if new_triangle.collision(asteroid):
                print("Game over!")
                running = False
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
                    score += 1
        screen.fill("black")
        screen.blit(text_surf, (0, 0))
        for obj in drawable:
            obj.draw(screen)
        

        pygame.display.flip()

        derp = time.tick(60)/1000
        
if __name__ == "__main__":
    main()
