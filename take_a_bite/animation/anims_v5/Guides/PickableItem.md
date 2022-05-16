# PickableItem Guide

```py
def setup(self):
	...
	
	self.pickup_object_list = arcade.SpriteList()  
  
	# PickableItem(sprite_path, pos_x, pos_y, sprite_scaling, tag)
	# -> tag | utils.object_tags.py

	# Create pickable items
	self.pickup_object_sprite = PickableItem("assets/food_items/blue_potion.png", randint(0, SCREEN_WIDTH),  
	  randint(0, SCREEN_HEIGHT - 100), sprite_scaling=1.25,  
	  tag=DEFAULT_CONSUMABLE)  
	self.pickup_object_list.append(self.pickup_object_sprite) 
	 
	self.pickup_object_sprite = PickableItem("assets/food_items/pink_potion.png", randint(0, SCREEN_WIDTH),  
	  randint(0, SCREEN_HEIGHT - 100), sprite_scaling=1.25,  
	  tag=PINK_CONSUMABLE)  
	self.pickup_object_list.append(self.pickup_object_sprite)
	
	for pickable_object in self.pickup_object_list:  
	    self.scene.add_sprite('Pick-able object', pickable_object)
	
	...

def on_draw(self):
	...
	
	# Text to let user know the object can be pick
	if self.can_draw_text:  
	    arcade.draw_text('C to pick up', SCREEN_WIDTH - 111, 21,  
		arcade.color.BLUEBERRY,  
		12, bold=True)
		
	...

def on_update(self, delta_time):
	...
	
	power_up_items_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.pickup_object_list)
	
	for power_up_item in power_up_items_hit_list:  
	    self.pickup_object_sprite = power_up_item  
	    if self.player_sprite.picking == PICKING:  
	        power_up_item.remove_from_sprite_lists()  
	        if self.player_sprite.item_picked == DEFAULT_CONSUMABLE:  
	            self.player_sprite.health_points += 1  
  
	if len(power_up_items_hit_list) != 0 and self.player_sprite.power_up == POWERUP_DISABLED:  
	    self.player_sprite.can_pick_up = True  
	    self.can_draw_text = True  
	else:  
	    self.player_sprite.can_pick_up = False  
	    self.can_draw_text = False
	
	...
```
