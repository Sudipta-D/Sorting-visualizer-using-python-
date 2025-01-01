# Imports
import pygame
import random

# Initialize pygame font
pygame.font.init()

# Set up the display
WIDTH, HEIGHT = 900, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

# Colors and fonts
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 204, 102)
RED = (255, 0, 0)
BLUE = (31, 133, 153)
PURPLE = (157, 102, 255)
COLORS = [GREEN, RED, BLUE, PURPLE]

font_large = pygame.font.SysFont("comicsans", 30)
font_small = pygame.font.SysFont("comicsans", 20)

# Array configuration
NUM_ELEMENTS = 150
array = [0] * (NUM_ELEMENTS + 1)
array_colors = [GREEN] * (NUM_ELEMENTS + 1)

# Generate a new random array
def generate_array():
    for i in range(1, NUM_ELEMENTS + 1):
        array_colors[i] = GREEN
        array[i] = random.randrange(1, 100)

# Initial array generation
generate_array()

# Redraw the screen with updated visuals
def redraw_screen():
    screen.fill(WHITE)
    draw()
    pygame.display.update()
    pygame.time.delay(30)

# Quick Sort Algorithm
def quick_sort(array, left, right):
    if left < right:
        pivot_index = partition(array, left, right)
        quick_sort(array, left, pivot_index - 1)
        redraw_screen()
        for i in range(0, pivot_index + 1):
            array_colors[i] = PURPLE
        quick_sort(array, pivot_index + 1, right)

# Partition function for Quick Sort
def partition(array, low, high):
    pygame.event.pump()
    pivot = array[high]
    array_colors[high] = BLUE
    i = low - 1

    for j in range(low, high):
        array_colors[j] = RED
        redraw_screen()
        array_colors[j] = GREEN

        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    array_colors[high] = GREEN
    return i + 1

# Draw the array and interface text
def draw():
    # Render text
    instructions_sort = font_large.render("SORT: PRESS 'ENTER'", 1, BLACK)
    instructions_new_array = font_large.render("NEW ARRAY: PRESS 'R'", 1, BLACK)
    algorithm_text = font_small.render("ALGORITHM USED: QUICK SORT", 1, BLACK)

    # Display text on the screen
    screen.blit(instructions_sort, (20, 20))
    screen.blit(instructions_new_array, (20, 50))
    screen.blit(algorithm_text, (600, 60))

    # Draw the boundary line
    pygame.draw.line(screen, BLACK, (0, 95), (WIDTH, 95), 6)

    # Calculate element dimensions
    element_width = (WIDTH - 150) // NUM_ELEMENTS
    boundary_spacing = WIDTH / NUM_ELEMENTS
    height_scaling = 550 / 100

    # Draw the array elements as vertical lines
    for i in range(1, NUM_ELEMENTS + 1):
        pygame.draw.line(
            screen,
            array_colors[i],
            (boundary_spacing * i - 3, 100),
            (boundary_spacing * i - 3, array[i] * height_scaling + 100),
            element_width,
        )

# Main loop
run = True
while run:
    # Fill the background
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                generate_array()
            if event.key == pygame.K_RETURN:
                quick_sort(array, 1, len(array) - 1)

    # Update the screen
    draw()
    pygame.display.update()

pygame.quit()
