import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS
)

def main():
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = (
        updateable
    )
    Asteroid.containers = (
        asteroids,
        updateable,
        drawable
    )
    Player.containers = (
        updateable,
        drawable
    )

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        updateable.update(dt)
        for entity in drawable:
            entity.draw(screen)
        pygame.display.flip()
        time_elapsed = clock.tick(60)
        dt = time_elapsed / 1000

if __name__ == "__main__":
    main()
