"""
╔══════════════════════════════════════════════════════════╗
║           ⚙️  USER SETTINGS MANAGER  ⚙️                  ║
║         Python Dictionary Practice Project               ║
║         By: MD Shoriful Alam Robin                       ║
╚══════════════════════════════════════════════════════════╝

📚 এই project এ যা শিখবে:
   ✅ Dictionary (dict) কীভাবে কাজ করে
   ✅ Function কীভাবে বানায়
   ✅ if/else condition
   ✅ for loop দিয়ে dict traverse
   ✅ User input নেওয়া
   ✅ String methods (.lower(), .capitalize())
"""

import os
import sys
import json
import time

# ── Windows Unicode Fix ────────────────────
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    os.system('chcp 65001 > nul')

# ══════════════════════════════════════════════
#   🎨 COLOR CODES (Terminal কে সুন্দর করো)
# ══════════════════════════════════════════════

class Colors:
    RESET   = '\033[0m'
    BOLD    = '\033[1m'
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'
    BG_DARK = '\033[40m'

def color(text, clr):
    """Text কে রঙিন করো"""
    return f"{clr}{text}{Colors.RESET}"

def clear_screen():
    """Screen clear করো"""
    os.system('cls' if os.name == 'nt' else 'clear')


# ══════════════════════════════════════════════
#   📦 DEFAULT SETTINGS (শুরুতে যা থাকবে)
# ══════════════════════════════════════════════

test_settings = {
    "theme":         "light",
    "language":      "english",
    "notifications": "enabled",
    "font_size":     "medium",
    "auto_save":     "enabled"
}

# Settings এর valid values
VALID_VALUES = {
    "theme":         ["light", "dark", "system"],
    "language":      ["english", "bangla", "arabic", "french"],
    "notifications": ["enabled", "disabled"],
    "font_size":     ["small", "medium", "large"],
    "auto_save":     ["enabled", "disabled"],
}


# ══════════════════════════════════════════════
#   ⚙️  CORE FUNCTIONS (মূল কাজের functions)
# ══════════════════════════════════════════════

# ── 1. Setting যোগ করো ────────────────────────
def add_setting(settings, kv_pair):
    """
    নতুন setting যোগ করো।
    
    📝 কীভাবে কাজ করে:
    1. key আর value নাও
    2. lowercase করো
    3. key already আছে? → Error দাও
    4. নেই? → যোগ করো
    
    Args:
        settings (dict): সব settings এর dictionary
        kv_pair (tuple): (key, value) এর tuple
    
    Returns:
        str: সফল বা error message
    """
    key, value = kv_pair
    key   = key.lower()    # "Theme" → "theme"
    value = value.lower()  # "DARK"  → "dark"

    # ✋ আগেই আছে?
    if key in settings:
        return color(
            f"⚠️  Setting '{key}' already exists! "
            f"Cannot add a new setting with this name.",
            Colors.YELLOW
        )
    else:
        # ✅ নতুন setting যোগ করো
        settings[key] = value
        return color(
            f"✅ Setting '{key}' added with value '{value}' successfully!",
            Colors.GREEN
        )


# ── 2. Setting update করো ─────────────────────
def update_setting(settings, kv_pair):
    """
    বিদ্যমান setting update করো।
    
    📝 কীভাবে কাজ করে:
    1. key আর value নাও
    2. key আছে? → update করো
    3. নেই? → Error দাও
    
    Args:
        settings (dict): সব settings এর dictionary
        kv_pair (tuple): (key, value) এর tuple
    
    Returns:
        str: সফল বা error message
    """
    key, value = kv_pair
    key   = key.lower()
    value = value.lower()

    # ✅ আছে? তাহলে update করো
    if key in settings:
        old_value = settings[key]   # আগের value রাখো
        settings[key] = value       # নতুন value দাও
        return color(
            f"🔄 Setting '{key}' updated: '{old_value}' → '{value}' successfully!",
            Colors.CYAN
        )
    else:
        # ❌ নেই? Error দাও
        return color(
            f"❌ Setting '{key}' does not exist! "
            f"Cannot update a non-existing setting.",
            Colors.RED
        )


# ── 3. Setting delete করো ─────────────────────
def delete_setting(settings, key):
    """
    একটা setting মুছে ফেলো।
    
    📝 কীভাবে কাজ করে:
    1. key নাও
    2. আছে? → del দিয়ে মুছো
    3. নেই? → Error দাও
    
    Args:
        settings (dict): সব settings এর dictionary
        key (str): মুছতে চাওয়া key
    
    Returns:
        str: সফল বা error message
    """
    key = key.lower()

    if key in settings:
        del settings[key]   # Dictionary থেকে মুছে ফেলো
        return color(
            f"🗑️  Setting '{key}' deleted successfully!",
            Colors.MAGENTA
        )
    else:
        return color(
            f"❌ Setting '{key}' not found! Cannot delete.",
            Colors.RED
        )


# ── 4. সব settings দেখো ───────────────────────
def view_settings(settings):
    """
    সব settings সুন্দরভাবে দেখাও।
    
    📝 কীভাবে কাজ করে:
    1. settings খালি? → message দাও
    2. খালি না? → for loop দিয়ে সব দেখাও
    
    Args:
        settings (dict): সব settings এর dictionary
    
    Returns:
        str: সব settings এর formatted text
    """
    if not settings:
        return color("📭 No settings available.", Colors.YELLOW)

    result = color("\n  ⚙️  Current User Settings:\n", Colors.BOLD)
    result += color("  " + "─" * 35 + "\n", Colors.BLUE)

    for k, v in settings.items():
        # Icon select করো
        icon = get_setting_icon(k)
        # Value color select করো
        v_color = Colors.GREEN if v in ["enabled", "dark"] else Colors.CYAN
        result += f"  {icon} {color(k.capitalize(), Colors.WHITE):<20} "
        result += f"{color(v, v_color)}\n"

    result += color("  " + "─" * 35, Colors.BLUE)
    return result


# ── 5. একটা setting খোঁজো ─────────────────────
def search_setting(settings, key):
    """
    নির্দিষ্ট একটা setting খোঁজো।
    
    Args:
        settings (dict): সব settings এর dictionary
        key (str): খুঁজতে চাওয়া key
    
    Returns:
        str: Setting পাওয়া গেছে বা না
    """
    key = key.lower()
    if key in settings:
        icon = get_setting_icon(key)
        return color(
            f"🔍 Found! {icon} '{key}' = '{settings[key]}'",
            Colors.CYAN
        )
    else:
        return color(
            f"🔍 '{key}' not found in settings.",
            Colors.YELLOW
        )


# ── 6. Settings reset করো ─────────────────────
def reset_settings(settings):
    """
    সব settings default এ ফিরিয়ে দাও।
    
    Args:
        settings (dict): settings dictionary
    """
    default = {
        "theme":         "light",
        "language":      "english",
        "notifications": "enabled",
        "font_size":     "medium",
        "auto_save":     "enabled"
    }
    settings.clear()
    settings.update(default)
    return color("🔄 All settings reset to default!", Colors.GREEN)


# ── 7. Settings export করো ────────────────────
def export_settings(settings, filename="my_settings.json"):
    """
    Settings কে JSON file এ save করো।
    
    Args:
        settings (dict): settings dictionary
        filename (str): file এর নাম
    """
    try:
        with open(filename, 'w') as f:
            json.dump(settings, f, indent=4)
        return color(f"📤 Settings exported to '{filename}' successfully!", Colors.GREEN)
    except Exception as e:
        return color(f"❌ Export failed: {e}", Colors.RED)


# ── 8. Settings import করো ────────────────────
def import_settings(settings, filename="my_settings.json"):
    """
    JSON file থেকে settings load করো।
    
    Args:
        settings (dict): settings dictionary
        filename (str): file এর নাম
    """
    try:
        with open(filename, 'r') as f:
            loaded = json.load(f)
        settings.clear()
        settings.update(loaded)
        return color(f"📥 Settings imported from '{filename}' successfully!", Colors.GREEN)
    except FileNotFoundError:
        return color(f"❌ File '{filename}' not found!", Colors.RED)
    except Exception as e:
        return color(f"❌ Import failed: {e}", Colors.RED)


# ══════════════════════════════════════════════
#   🎨 HELPER FUNCTIONS (সাহায্যকারী functions)
# ══════════════════════════════════════════════

def get_setting_icon(key):
    """Setting এর জন্য icon দাও"""
    icons = {
        "theme":         "🎨",
        "language":      "🌐",
        "notifications": "🔔",
        "font_size":     "🔤",
        "auto_save":     "💾",
    }
    return icons.get(key, "⚙️")


def print_header():
    """সুন্দর header দেখাও"""
    clear_screen()
    print(color("\n" + "═" * 55, Colors.BLUE))
    print(color("  ⚙️   USER SETTINGS MANAGER   ⚙️", Colors.BOLD + Colors.CYAN))
    print(color("  Python Dictionary Practice Project", Colors.WHITE))
    print(color("  By: MD Shoriful Alam Robin", Colors.MAGENTA))
    print(color("═" * 55, Colors.BLUE))


def print_menu():
    """Menu দেখাও"""
    print(color("\n  📋 MENU:", Colors.BOLD + Colors.YELLOW))
    print(color("  " + "─" * 35, Colors.BLUE))
    menu_items = [
        ("1", "👁️ ", "View All Settings"),
        ("2", "➕ ", "Add New Setting"),
        ("3", "🔄 ", "Update Setting"),
        ("4", "🗑️ ", "Delete Setting"),
        ("5", "🔍 ", "Search Setting"),
        ("6", "↩️ ", "Reset to Default"),
        ("7", "📤 ", "Export Settings (JSON)"),
        ("8", "📥 ", "Import Settings (JSON)"),
        ("9", "🚪 ", "Exit"),
    ]

    for num, icon, label in menu_items:
        print(f"  {color(f'[{num}]', Colors.CYAN)} {icon}{color(label, Colors.WHITE)}")

    print(color("  " + "─" * 35, Colors.BLUE))


def get_input(prompt):
    """User থেকে input নাও"""
    return input(color(f"\n  {prompt}: ", Colors.YELLOW)).strip()


def print_result(message):
    """Result দেখাও"""
    print(f"\n  {message}")
    input(color("\n  Enter চাপো continue করতে...", Colors.WHITE))


def print_stats(settings):
    """Settings এর statistics দেখাও"""
    total = len(settings)
    print(color(f"\n  📊 Total Settings: {total}", Colors.CYAN))


# ══════════════════════════════════════════════
#   🚀 MAIN PROGRAM (মূল program)
# ══════════════════════════════════════════════

def main():
    """
    মূল program।
    
    📝 এটা কীভাবে কাজ করে:
    1. Header দেখাও
    2. Menu দেখাও
    3. User এর choice নাও
    4. সেই অনুযায়ী function call করো
    5. আবার Menu দেখাও (loop)
    """

    settings = test_settings.copy()  # Original কে safe রাখো

    print_header()
    print(color("\n  👋 Welcome to Settings Manager!", Colors.GREEN))
    print(color("  Python dictionary practice project", Colors.WHITE))
    time.sleep(1.5)

    # ── Main Loop ────────────────────────────
    while True:
        print_header()
        print_stats(settings)
        print_menu()

        choice = get_input("তোমার choice দাও (1-9)")

        # ── View ─────────────────────────────
        if choice == '1':
            print_header()
            print(view_settings(settings))
            input(color("\n  Enter চাপো continue করতে...", Colors.WHITE))

        # ── Add ──────────────────────────────
        elif choice == '2':
            print_header()
            print(color("  ➕ ADD NEW SETTING", Colors.BOLD + Colors.GREEN))
            key   = get_input("Setting এর নাম দাও (key)")
            value = get_input("Setting এর value দাও")

            if key and value:
                result = add_setting(settings, (key, value))
                print_result(result)
            else:
                print_result(color("❌ Key বা value খালি রাখা যাবে না!", Colors.RED))

        # ── Update ───────────────────────────
        elif choice == '3':
            print_header()
            print(color("  🔄 UPDATE SETTING", Colors.BOLD + Colors.CYAN))
            print(view_settings(settings))
            key   = get_input("কোন setting update করবে? (key)")
            value = get_input("নতুন value দাও")

            if key and value:
                result = update_setting(settings, (key, value))
                print_result(result)
            else:
                print_result(color("❌ Key বা value খালি রাখা যাবে না!", Colors.RED))

        # ── Delete ───────────────────────────
        elif choice == '4':
            print_header()
            print(color("  🗑️  DELETE SETTING", Colors.BOLD + Colors.RED))
            print(view_settings(settings))
            key = get_input("কোন setting মুছবে? (key)")

            if key:
                # Confirm করো
                confirm = get_input(f"'{key}' মুছতে চাও? (yes/no)")
                if confirm.lower() in ['yes', 'y', 'হ্যাঁ']:
                    result = delete_setting(settings, key)
                    print_result(result)
                else:
                    print_result(color("❌ Delete বাতিল করা হয়েছে।", Colors.YELLOW))
            else:
                print_result(color("❌ Key খালি রাখা যাবে না!", Colors.RED))

        # ── Search ───────────────────────────
        elif choice == '5':
            print_header()
            print(color("  🔍 SEARCH SETTING", Colors.BOLD + Colors.CYAN))
            key    = get_input("কোন setting খুঁজবে? (key)")
            result = search_setting(settings, key)
            print_result(result)

        # ── Reset ────────────────────────────
        elif choice == '6':
            print_header()
            confirm = get_input("সব settings reset করতে চাও? (yes/no)")
            if confirm.lower() in ['yes', 'y']:
                result = reset_settings(settings)
                print_result(result)
            else:
                print_result(color("↩️  Reset বাতিল করা হয়েছে।", Colors.YELLOW))

        # ── Export ───────────────────────────
        elif choice == '7':
            print_header()
            filename = get_input("File এর নাম দাও (Enter = my_settings.json)")
            if not filename:
                filename = "my_settings.json"
            result = export_settings(settings, filename)
            print_result(result)

        # ── Import ───────────────────────────
        elif choice == '8':
            print_header()
            filename = get_input("কোন file থেকে import করবে? (Enter = my_settings.json)")
            if not filename:
                filename = "my_settings.json"
            result = import_settings(settings, filename)
            print_result(result)

        # ── Exit ─────────────────────────────
        elif choice == '9':
            print_header()
            print(color("\n  👋 ধন্যবাদ! Settings Manager বন্ধ হচ্ছে...", Colors.GREEN))
            print(color("  Made with ❤️  by MD Shoriful Alam Robin\n", Colors.MAGENTA))
            break

        # ── Invalid ──────────────────────────
        else:
            print_result(color("❌ Invalid choice! 1-9 এর মধ্যে দাও।", Colors.RED))


# ══════════════════════════════════════════════
#   🧪 DEMO MODE (Test করার জন্য)
# ══════════════════════════════════════════════

def run_demo():
    """
    Demo mode — সব functions এক এক করে test করো।
    Manual input ছাড়াই দেখতে পাবে।
    """
    print(color("\n" + "═" * 55, Colors.BLUE))
    print(color("  🧪 DEMO MODE — সব functions test করছি", Colors.BOLD + Colors.CYAN))
    print(color("═" * 55 + "\n", Colors.BLUE))

    settings = {
        "theme": "light",
        "language": "english",
        "notifications": "enabled"
    }

    steps = [
        ("📋 Initial Settings দেখো:", lambda: view_settings(settings)),
        ("➕ 'font_size' add করো:", lambda: add_setting(settings, ("font_size", "large"))),
        ("⚠️  Same key আবার add করো:", lambda: add_setting(settings, ("theme", "dark"))),
        ("🔄 'theme' update করো:", lambda: update_setting(settings, ("theme", "dark"))),
        ("❌ নেই এমন key update করো:", lambda: update_setting(settings, ("volume", "high"))),
        ("🗑️  'language' delete করো:", lambda: delete_setting(settings, "language")),
        ("❌ নেই এমন key delete করো:", lambda: delete_setting(settings, "volume")),
        ("🔍 'theme' search করো:", lambda: search_setting(settings, "theme")),
        ("🔍 নেই এমন key search করো:", lambda: search_setting(settings, "volume")),
        ("📋 Final Settings দেখো:", lambda: view_settings(settings)),
    ]

    for i, (label, func) in enumerate(steps, 1):
        print(color(f"  Step {i}: {label}", Colors.YELLOW))
        result = func()
        print(f"  {result}\n")
        time.sleep(0.5)

    print(color("═" * 55, Colors.BLUE))
    print(color("  ✅ Demo complete!", Colors.GREEN))
    print(color("═" * 55 + "\n", Colors.BLUE))


# ══════════════════════════════════════════════
#   🎬 PROGRAM START
# ══════════════════════════════════════════════

if __name__ == "__main__":
    print(color("\n" + "═" * 55, Colors.BLUE))
    print(color("  ⚙️   USER SETTINGS MANAGER", Colors.BOLD + Colors.CYAN))
    print(color("═" * 55, Colors.BLUE))
    print(color("\n  কোন mode এ চালাবে?", Colors.WHITE))
    print(color("  [1] 🚀 Interactive Mode (নিজে control করবে)", Colors.CYAN))
    print(color("  [2] 🧪 Demo Mode (automatic দেখবে)", Colors.GREEN))
    print(color("  " + "─" * 35, Colors.BLUE))

    mode = input(color("\n  তোমার choice (1 বা 2): ", Colors.YELLOW)).strip()

    if mode == '2':
        run_demo()
    else:
        main()
