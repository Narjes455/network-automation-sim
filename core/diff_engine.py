def compare_configs(old, new):
    changes = []

    old_lines = old.splitlines()
    new_lines = new.splitlines()

    for line in new_lines:
        if line not in old_lines:
            changes.append(f"ADDED: {line}")

    for line in old_lines:
        if line not in new_lines:
            changes.append(f"REMOVED: {line}")

    return changes