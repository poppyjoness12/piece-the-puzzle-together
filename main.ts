controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    stone.setPosition(20, 20)
})
function startGame () {
    scene.setBackgroundImage(assets.image`cityscape`)
    targetsCompleted = 0
    score = 0
    timeLimit = 30
    stone = sprites.create(assets.image`stone`, SpriteKind.Player)
    controller.moveSprite(stone, 100, 100)
    stone.setStayInScreen(true)
    createTargetZones()
    createObstacles()
    game.onUpdateInterval(1000, function on_update_interval() {
        
        timeLimit -= 1
        if (timeLimit <= 0) {
            game.over(false)
        }
        
    })
}
function createTargetZones () {
    targetZones = []
    while (i <= totalTargets - 1) {
        targetZone = sprites.create(assets.image`stone1`, SpriteKind.Enemy)
        targetZone.setPosition(80 + i * 40, 60)
        targetZones.push(targetZone)
        i += 1
    }
}
function createObstacles () {
    if (assets.image`
        obstacle
    `) {
        // Create a moving obstacle that stays in the game
        obstacle = sprites.create(assets.image`obstacle`, SpriteKind.Enemy)
        obstacle.setPosition(Math.randomRange(30, 130), Math.randomRange(30, 110))
        // Give the obstacle some random movement to make it more dynamic
        obstacle.vx = Math.randomRange(-50, 50)
        obstacle.vy = Math.randomRange(-50, 50)
        // Make sure the obstacle bounces off the screen edges
        obstacle.setFlag(SpriteFlag.BounceOnWall, true)
    } else {
        console.log("Obstacle image not found!")
    }
}
let targetZone: Sprite = null
let i = 0
let targetZones: Sprite[] = []
let score = 0
let targetsCompleted = 0
let stone: Sprite = null
let obstacle: Sprite = null
let timeLimit = 0
let totalTargets = 0
let level = 1
totalTargets = 3
timeLimit = 30
startGame()
obstacle.setFlag(SpriteFlag.AutoDestroy, true)
game.splash("What are you grateful for?", "")
game.splash("Breathe For 3 Seconds")
game.splash("3")
game.splash("2")
game.splash("1")
game.onUpdate(function () {
    let collectible: Sprite = null
    for (let targetZone2 of targetZones) {
        if (stone.overlapsWith(targetZone2)) {
            targetZone2.setImage(img`
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
                `)
            music.baDing.play()
            targetsCompleted += 1
            targetZones.removeElement(targetZone2)
targetZone2.destroy()
            score += 10
            break;
        }
    }
    // Check if all targets have been completed
    if (targetsCompleted == totalTargets) {
        level += 1
        game.showLongText("Level " + ("" + level) + " completed! Press A to continue.", DialogLayout.Bottom)
        startGame()
    }
    // Check if the stone overlaps with the collectible
    if (collectible && stone.overlapsWith(collectible)) {
        collectible.destroy()
        score += 5
        music.powerUp.play()
    }
    // Check if the stone overlaps with the obstacle
    if (obstacle && stone.overlapsWith(obstacle)) {
        game.over(false)
    }
})
game.onUpdateInterval(5000, function () {
    // Create a new obstacle every 10 seconds
    createObstacles()
})
// Respawn the obstacle in a new random position every 10 seconds
game.onUpdateInterval(10000, function () {
    if (obstacle) {
        obstacle.setPosition(Math.randomRange(30, 130), Math.randomRange(30, 110))
    }
})
