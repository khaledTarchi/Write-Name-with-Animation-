import pygame
import random

class EnchantedUniverse:
    def __init__(self, width=1100, height=700):
        self.width = width
        self.height = height

        # Initialize pygame and set the window size
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Set the window title
        pygame.display.set_caption("KHALED TR's Enchanted Universe")

        # Load fonts for the text
        self.font_big = pygame.font.Font("beautiful_font.ttf", 180)

        # Create a text surface with the name "KHALED TR"
        self.text_surface = self.font_big.render("KHALED TR", True, (255, 255, 255))  # White color
        self.text_rect = self.text_surface.get_rect(center=(self.width // 2, self.height // 2))

        # Create a clock to control the frame rate
        self.clock = pygame.time.Clock()

        # List to hold particle positions and velocities
        self.particles = []

        # Variable for background color transition
        self.bg_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        self.bg_change_rate = [random.uniform(0.1, 0.5) for _ in range(3)]

    def draw_text(self):
        # Draw the text on the screen with shimmering effect
        color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
        shimmer_text_surface = self.font_big.render("KHALED TR", True, color)
        self.screen.blit(shimmer_text_surface, self.text_rect)

    def handle_particles(self):
        # Add sparkling particles around the text
        for _ in range(3):
            particle = {
                "position": [random.randint(self.text_rect.left - 50, self.text_rect.right + 50),
                             random.randint(self.text_rect.top - 50, self.text_rect.bottom + 50)],
                "velocity": [random.uniform(-1, 1), random.uniform(-1, 1)],
                "color": (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255)),
                "size": random.randint(2, 5)  # Varying particle size
            }
            self.particles.append(particle)

        # Update particle positions and draw them with a trail effect
        for particle in self.particles:
            pygame.draw.circle(self.screen, particle["color"], (int(particle["position"][0]), int(particle["position"][1])),
                               particle["size"])
            particle["position"][0] += particle["velocity"][0]
            particle["position"][1] += particle["velocity"][1]
            particle["velocity"][0] *= 0.99  # Add slight friction
            particle["velocity"][1] *= 0.99
            particle["size"] -= 0.1  # Decrease particle size over time
            if particle["size"] <= 0:
                self.particles.remove(particle)

    def update_background(self):
        # Update background color gradually
        for i in range(3):
            self.bg_color[i] += self.bg_change_rate[i]
            if self.bg_color[i] < 0:
                self.bg_color[i] = 0
                self.bg_change_rate[i] *= -1
            elif self.bg_color[i] > 255:
                self.bg_color[i] = 255
                self.bg_change_rate[i] *= -1

    def run(self):
        # Main game loop
        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # Fill the screen with a dynamic background
            self.screen.fill(self.bg_color)

            # Draw the text with shimmering effect
            self.draw_text()

            # Handle particle effects
            self.handle_particles()

            # Update the background color gradually
            self.update_background()

            # Update the display
            pygame.display.flip()

            # Limit the frame rate
            self.clock.tick(60)

# Create an instance of the EnchantedUniverse class and run the game
if __name__ == "__main__":
    enchanted_universe = EnchantedUniverse()
    enchanted_universe.run()
