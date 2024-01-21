# Gamerules
gamerule doLimitedCrafting true

# Add scoreboards
scoreboard objectives add item_age dummy

# Grant all recipes
recipe take @a *
execute as @a run function a07:grant_recipes