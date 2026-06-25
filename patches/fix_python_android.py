#!/usr/bin/env python3
"""
P4A Recipe Hook: Fix Python 3.14 Android compilation error.
Called during python3 prebuild_arch to patch remote_debug source files.
"""
import os, sys

def main(build_dir):
    files_to_fix = [
        os.path.join(build_dir, "Modules", "_remote_debugging_module.c"),
        os.path.join(build_dir, "Python", "remote_debug.h"),
    ]

    fixed = 0
    for filepath in files_to_fix:
        if not os.path.exists(filepath):
            continue

        with open(filepath, "r") as f:
            content = f.read()

        # Fix: #elif defined(__linux__) -> add !defined(__ANDROID__) guard
        # Only where it's followed by search_linux_map_for_section
        old = '#elif defined(__linux__)\n    // On Linux, search'
        new = '#elif defined(__linux__) && !defined(__ANDROID__)\n    // On Linux, search'
        if old in content:
            content = content.replace(old, new)
            with open(filepath, "w") as f:
                f.write(content)
            fixed += 1
            print(f"[FIX] Patched {os.path.basename(filepath)}")

    if fixed == 0:
        print(f"[WARN] No fixes applied to files in {build_dir}")
        return 1
    print(f"[FIX] Successfully patched {fixed} file(s)")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
