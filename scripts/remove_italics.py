import os
from pathlib import Path
import re

WIKI_DIR = Path(r"D:\Wiki\wiki\AI_20K_2A202600974")

def remove_italics():
    for file_path in WIKI_DIR.rglob("*.vi.md"):
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        new_lines = []
        for line in lines:
            stripped = line.strip()
            # Remove italics if it starts and ends with a single asterisk (and not double/triple)
            if stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"):
                content = stripped[1:-1]
                leading_ws = line[:len(line) - len(line.lstrip())]
                new_line = leading_ws + content + "\n"
                new_lines.append(new_line)
            else:
                # Some lines might have * just around the text but not the list marker?
                # E.g., `- *Some text*`
                if stripped.startswith("- *") and stripped.endswith("*") and not stripped.startswith("- **"):
                    content = stripped[3:-1]
                    leading_ws = line[:len(line) - len(line.lstrip())]
                    new_line = leading_ws + "- " + content + "\n"
                    new_lines.append(new_line)
                else:
                    new_lines.append(line)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
            
    print("Finished stripping italics from .vi.md files.")

if __name__ == "__main__":
    remove_italics()
