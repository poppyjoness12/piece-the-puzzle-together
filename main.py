def on_a_pressed():
    stone.set_position(20, 20)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def startGame():
    global targetsCompleted, score, timeLimit, stone
    scene.set_background_image(assets.image("""
        cityscape
    """))
    targetsCompleted = 0
    score = 0
    timeLimit = 30
    stone = sprites.create(assets.image("""
        stone
    """), SpriteKind.player)
    controller.move_sprite(stone, 100, 100)
    stone.set_stay_in_screen(True)
    createTargetZones()
    createObstacles()
    
    def on_update_interval():
        global timeLimit
        timeLimit -= 1
        if timeLimit <= 0:
            game.over(False)
    game.on_update_interval(1000, on_update_interval)
    
def createTargetZones():
    global targetZones, targetZone, i
    targetZones = []
    while i <= totalTargets - 1:
        targetZone = sprites.create(assets.image("""
            stone1
        """), SpriteKind.food)
        # Positions each target zone on the screen using calculated coordinates
        targetZone.set_position(80 + i * 40, 60)
        targetZones.append(targetZone)
        i += 1
def createObstacles():
    global obstacle
    if assets.image("""
        obstacle
    """):
        # Create a moving obstacle that stays in the game
        obstacle = sprites.create(assets.image("""
            obstacle
        """), SpriteKind.enemy)
        obstacle.set_position(Math.random_range(30, 130), Math.random_range(30, 110))
        # Give the obstacle some random movement to make it more dynamic
        obstacle.vx = Math.random_range(-50, 50)
        obstacle.vy = Math.random_range(-50, 50)
        # Make sure the obstacle bounces off the screen edges
        obstacle.set_flag(SpriteFlag.BOUNCE_ON_WALL, True)
    else:
        print("Obstacle image not found!")
targetZone: Sprite = None
i = 0
targetZones: List[Sprite] = []
score = 0
targetsCompleted = 0
stone: Sprite = None
obstacle: Sprite = None
timeLimit = 0
totalTargets = 0
level = 1
totalTargets = 3
timeLimit = 30
startGame()
obstacle.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.splash("What are you grateful for?", "")
game.splash("Breathe For 3 Seconds")
game.splash("3")
game.splash("2")
game.splash("1")

def on_on_update():
    global targetsCompleted, score, level
    collectible: Sprite = None
    for targetZone2 in targetZones:
        if stone.overlaps_with(targetZone2):
            targetZone2.set_image(img("""
                . . . . . . . . . . . . . . . . 
                                . . . . . . . . . . . . . . . . 
                                . . . . . . . 2 2 2 2 . . . . . 
                                . . . . . . 2 2 2 2 2 2 . . . . 
                                . . . . . 2 2 2 2 2 2 2 2 . . . 
                                . . . . 2 2 2 2 2 2 2 2 2 2 . . 
                                . . . 2 2 2 2 2 2 2 2 2 2 2 2 . 
                                . . . 2 2 2 2 2 2 2 2 2 2 2 2 . 
                                . . . . 2 2 2 2 2 2 2 2 2 2 . . 
                                . . . . . 2 2 2 2 2 2 2 2 . . . 
                                . . . . . . . 2 2 2 2 . . . . . 
                                . . . . . . . . . . . . . . . .
            """))
            music.ba_ding.play()
            targetsCompleted += 1
            targetZones.remove_element(targetZone2)
            targetZone2.destroy()
            score += 10
            break
    # Check if all targets have been completed
    if targetsCompleted == totalTargets:
        level += 1
        game.show_long_text("Level " + ("" + str(level)) + " completed! Press A to continue.",
            DialogLayout.BOTTOM)
        startGame()
    # Check if the stone overlaps with the collectible
    if collectible and stone.overlaps_with(collectible):
        collectible.destroy()
        score += 5
        music.power_up.play()
    # Check if the stone overlaps with the obstacle
    if obstacle and stone.overlaps_with(obstacle):
        game.over(False)
game.on_update(on_on_update)

def on_update_interval2():
    # Create a new obstacle every 10 seconds
    createObstacles()
game.on_update_interval(5000, on_update_interval2)

# Respawn the obstacle in a new random position every 10 seconds

def on_update_interval3():
    if obstacle:
        obstacle.set_position(Math.random_range(30, 130), Math.random_range(30, 110))
game.on_update_interval(10000, on_update_interval3)
