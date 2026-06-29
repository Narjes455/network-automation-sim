import difflib


def compare_configs(old_config, new_config):

    old_lines = old_config.splitlines()
    new_lines = new_config.splitlines()

    diff = list(
        difflib.unified_diff(
            old_lines,
            new_lines,
            lineterm=""
        )
    )

    return diff