import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, SHOOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOOT_RADIUS)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
   
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt