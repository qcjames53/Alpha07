# Replace all block drops for invalid items
# Run each tick

execute as @e[type=item] store result score @s item_age run data get entity @s Age 1
execute as @e[type=item,scores={item_age=..1},nbt={Item:{id:"minecraft:raw_iron"}}] run data merge entity @s {Item:{id:"minecraft:iron_ore"}}
execute as @e[type=item,scores={item_age=..1},nbt={Item:{id:"minecraft:raw_gold"}}] run data merge entity @s {Item:{id:"minecraft:gold_ore"}}