def add_setting(add_dict, new_setting_tuple):
    no_key, no_value = new_setting_tuple
    key = no_key.lower()
    value = no_value.lower()
    if key in add_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        add_dict[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(update_dict, update_setting_tuple):
    og_key, og_value = update_setting_tuple
    key = og_key.lower()
    value = og_value.lower()
    if key in update_dict:
        update_dict[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(delete_dict, key):
    deleted_key = key.lower()
    if deleted_key in delete_dict:
        delete_dict.pop(deleted_key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings_dict):
    if settings_dict == {}:
        return "No settings available."

    formatted = [f"{key.capitalize()}: {value}"
    for key, value in settings_dict.items()]

    return "Current User Settings:\n" + "\n".join(formatted) + "\n"

test_settings = {'theme': 'light'}
add_setting({'theme': 'light'}, ('THEME', 'dark'))
add_setting({'theme': 'light'}, ('volume', 'high'))

update_setting({'theme': 'light'}, ('theme', 'dark'))

view_settings({'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'})
