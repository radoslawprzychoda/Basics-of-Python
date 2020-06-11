def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for item_name, item_count in inventory.items():
        print(item_count, item_name)
        item_total += item_count
    print("Total number of items: " + str(item_total))
    if item_total >= 80:
        print("CAUTION: You are overloaded, can't move!")
    elif item_total >= 70:
        print("CAUTION: Your equipment is very heavy, you're moving slower than usual!")
    elif item_total >= 60:
        print("CAUTION: Your backpack weighs a lot, your stamina runs out quicker!")


def add_to_inventory(inventory, added_items):
    skipped = {}
    added_count = 0
    for item_name in added_items:
        if item_name in ['chewed gum', 'rubbish', 'used tissue']:
            if item_name in skipped.keys():
                skipped[item_name] += 1
            else:
                skipped[item_name] = 1;
        else:
            if item_name in inventory.keys():
                inventory[item_name] += 1
            else:
                inventory[item_name] = 1
            added_count += 1
    print("Added " + str(added_count) + " items to the inventory")
    # print skipped if any
    if skipped.items():
        print("Skipped:")
        for skipped_item_name, skipped_item_count in skipped.items():
            print(skipped_item_count, skipped_item_name)
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = [
    'gold coin', 'chewed gum', 'dagger', 'gold coin', 'gold coin', 'ruby',
    'rubbish', 'chewed gum', 'used tissue', 'rope', 'rope']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)

