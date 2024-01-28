import pygame


def setup():
    global display, blocks, width, height, is_running, button_1, button_3, mouse_x, mouse_y, clock, fps, running_fps, plus, minus, font
    og_height = 600
    width, height = 1300, og_height - 35
    display = pygame.display.set_mode((width, og_height))
    pygame.display.set_caption("Conway's Game Of Life")
    length = 15
    blocks = create_grid(length)
    is_running = False
    mouse_x, mouse_y = 0, 0
    button_1, button_3 = False, False
    clock = pygame.time.Clock()
    fps = 30
    running_fps = 1
    plus, minus = True, True
    font = pygame.font.Font("freesansbold.ttf", 35)


def loop():
    global is_running, button_1, button_3, mouse_x, mouse_y, clock, fps, running_fps, plus, minus
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    button_1 = True
                if event.button == 3:
                    button_3 = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    button_1 = False
                if event.button == 3:
                    button_3 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_SPACE:
                    is_running = not is_running
                if event.key == pygame.K_KP0:
                    running_fps = 1
                if event.key == pygame.K_KP1:
                    running_fps = 30
                if event.key == pygame.K_a:
                    is_running = False
                    for i in blocks:
                        for e in i:
                            e.temp_status = True
                if event.key == pygame.K_d:
                    is_running = False
                    for i in blocks:
                        for e in i:
                            e.temp_status = False
                if event.key == pygame.K_KP_PLUS and plus:
                    running_fps += 1
                    plus = False
                if event.key == pygame.K_KP_MINUS and minus:
                    if running_fps > 1:
                        running_fps -= 1
                    minus = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_KP_PLUS:
                    plus = True
                if event.key == pygame.K_KP_MINUS:
                    minus = True
    if is_running:
        background = (0, 180, 0)
        fps = running_fps
    else:
        background = (255, 90, 0)
        fps = 30
    display.fill(background)
    if is_running:
        for r in range(rows):
            for c in range(columns):
                blocks[r][c].update(blocks)
    for r in range(rows):
        for c in range(columns):
            if not is_running:
                if blocks[r][c].square.collidepoint(mouse_x, mouse_y):
                    if button_1:
                        blocks[r][c].temp_status = True
                    if button_3:
                        blocks[r][c].temp_status = False
            blocks[r][c].draw()
    text = font.render(str(fps), True, (255, 0, 0), background)
    text_sq = text.get_rect()
    text_sq.center = width // 2, 20
    display.blit(text, text_sq)
    pygame.display.update()


class Block:
    DEAD_COLOUR = (180, 180, 180)
    ALIVE_COLOUR = (0, 0, 0)

    def __init__(self, x, y, pos_x, pos_y, w):
        self.x = x
        self.y = y
        self.square = pygame.Rect(pos_x, pos_y, w, w)
        self.status = False
        self.temp_status = False

    def draw(self):
        self.status = self.temp_status
        if self.status:
            self.square = pygame.draw.rect(display, self.ALIVE_COLOUR, self.square)
        else:
            self.square = pygame.draw.rect(display, self.DEAD_COLOUR, self.square)

    def update(self, grid: "list[list[Block]]"):
        # the neighbours wrap around from all sides
        alive_neighbours = 0
        for dx in range(-1, 2):  # -1,0,1
            for dy in range(-1, 2):  # -1,0,1
                if not (
                    (dx == 0) and (dy == 0)
                ):  # if dx and dy both are 0 then the cell is referring to itself
                    neighbour_x = (self.x + dx) % columns
                    neighbour_y = (self.y + dy) % rows
                    neighbour: "Block" = grid[neighbour_y][neighbour_x]
                    if neighbour.status:
                        alive_neighbours += 1
        # if there are two alive neighbours then do nothing
        if alive_neighbours != 2:
            # if there are three alive neighbours then this cell is alive
            if alive_neighbours == 3:
                self.temp_status = True
            # if there are less than two neighbours alive or more than three neighbours alive then this neighbour is dead
            else:
                self.temp_status = False


def create_grid(length) -> "list[list[Block]]":
    global rows, columns
    grid = []
    space = length + length // 5
    columns = width // space
    rows = height // space
    extra_x = (width - columns * space) // 2 + 2
    extra_y = (height - rows * space) // 2 + 2 + 35
    for r in range(rows):
        column = []
        for c in range(columns):
            column.append(Block(c, r, space * c + extra_x, space * r + extra_y, length))
        grid.append(column)
    return grid


if __name__ == "__main__":
    pygame.init()
    setup()
    while True:
        loop()
