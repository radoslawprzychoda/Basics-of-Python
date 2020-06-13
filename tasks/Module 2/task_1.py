from collections import defaultdict

ITEMS_TO_SKIP = ['chewed gum', 'rubbish', 'used tissue']
MAX_INVENTORY_CAP = 80
HEAVY_WEIGHT_THRESHOLD = 70
LIGHT_WEIGHT_THRESHOLD = 60


def display_inventory(inventory):
    '''
    Displays the contents of the inventory
    '''
    print("Inventory:")
    item_total = 0
    for item_name, item_count in inventory.items():
        print(item_count, item_name)
        item_total += item_count
    print(f"Total number of items: {item_total}")
    if item_total >= MAX_INVENTORY_CAP:
        print("CAUTION: You are overloaded, can't move!")
    elif item_total >= HEAVY_WEIGHT_THRESHOLD:
        print("CAUTION: Your equipment is very heavy, you're moving slower than usual!")
    elif item_total >= LIGHT_WEIGHT_THRESHOLD:
        print("CAUTION: Your backpack weighs a lot, your stamina runs out quicker!")


def add_to_inventory(inventory, added_items, items_to_skip):
    '''
    Ads useful items to the inventory and skips not useful.
    Returns a new inventory with added items.
    '''
    skipped = defaultdict(int)
    added_count = 0
    for item_name in added_items:
        if item_name in items_to_skip:
            skipped[item_name] += 1
        else:
            inventory[item_name] += 1
            added_count += 1
    print(f"Added {added_count} items to the inventory")
    # print skipped if any
    if skipped:
        print("Skipped:")
        for skipped_item_name, skipped_item_count in skipped.items():
            print(skipped_item_count, skipped_item_name)
    return inventory


inv = {'gold coin': 42, 'rope': 1}
inv_defdict = defaultdict(int, inv)
dragon_loot = [
    'gold coin', 'chewed gum', 'dagger', 'gold coin', 'gold coin', 'ruby',
    'rubbish', 'chewed gum', 'used tissue', 'rope', 'rope']
inv = add_to_inventory(inv_defdict, dragon_loot, ITEMS_TO_SKIP)
display_inventory(inv)
