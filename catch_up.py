"""
catch_up.py - jump to the end of any checkpoint in one step.

    python catch_up.py 2    your_code/ becomes the finished Checkpoint 2
    python catch_up.py 0    start again from the fresh starter

Your own work is always saved first, in my_attempts/, so nothing you typed is lost.
Your keys (.env) and your notes (notes/) are never touched.
"""

import shutil
import sys
from pathlib import Path

# Every path is worked out from where this file lives, so it works from any folder.
HERE = Path(__file__).resolve().parent
YOUR_CODE = HERE / "your_code"
CHECKPOINTS = HERE / "checkpoints"
MY_ATTEMPTS = HERE / "my_attempts"
STUDENT_FILES = ["prompts.py", "tools.py", "agent.py"]

CHECKPOINT_NAMES = {
    0: "the fresh starter (start again from the beginning)",
    1: "Checkpoint 1: The brain (system prompt and chat history)",
    2: "Checkpoint 2: The hands (web search and the agent loop)",
    3: "Checkpoint 3: The memory (saving and reading notes)",
    4: "Checkpoint 4: Quiz mode (the finished Study Buddy)",
}


def show_options():
    print("Which checkpoint do you want to jump to? Type one of these:\n")
    for number, name in CHECKPOINT_NAMES.items():
        print("    python catch_up.py " + str(number) + "    -> " + name)
    print()


def read_number():
    """The checkpoint number the student typed, or None if it isn't a valid one."""
    if len(sys.argv) != 2:
        return None
    # Accept "2" and also "cp2".
    text = sys.argv[1].strip().lower().removeprefix("cp")
    if text.isdigit() and int(text) in CHECKPOINT_NAMES:
        return int(text)
    return None


def pick_save_folder(number):
    """my_attempts/before_cp2, or before_cp2_2, before_cp2_3... if that one is taken."""
    folder = MY_ATTEMPTS / ("before_cp" + str(number))
    count = 2
    while folder.exists():
        folder = MY_ATTEMPTS / ("before_cp" + str(number) + "_" + str(count))
        count += 1
    return folder


def main():
    number = read_number()
    if number is None:
        show_options()
        return

    source = CHECKPOINTS / ("cp" + str(number))

    # Check the checkpoint files are all there BEFORE changing anything.
    for name in STUDENT_FILES:
        if not (source / name).exists():
            print("Problem: checkpoints/cp" + str(number) + "/" + name + " is missing, so I can't catch you up.")
            print("Fix: download the project again from GitHub, or ask a helper.")
            return

    # Step 1: save the student's own files first.
    save_folder = pick_save_folder(number)
    save_folder.mkdir(parents=True)
    saved = []
    for name in STUDENT_FILES:
        if (YOUR_CODE / name).exists():
            shutil.copyfile(YOUR_CODE / name, save_folder / name)
            saved.append(name)

    # Step 2: copy the checkpoint's files into your_code/.
    YOUR_CODE.mkdir(exist_ok=True)
    for name in STUDENT_FILES:
        shutil.copyfile(source / name, YOUR_CODE / name)

    # Step 3: tell the student what happened.
    where_saved = save_folder.relative_to(HERE).as_posix() + "/"
    print()
    if number == 0:
        print("Done! your_code/ is back to the fresh starter.")
    else:
        print("Done! You're now at the end of " + CHECKPOINT_NAMES[number] + ".")
    if saved:
        print("Your own work is saved in " + where_saved + " so you can compare it later.")
    else:
        print("(There were no files of yours to save.)")
    print()
    print("Next: start Study Buddy again with   python main.py")
    print("(If it's already running, type quit first.)")
    print("If your editor says a file has unsaved changes, close it WITHOUT saving.")
    print()


try:
    main()
except OSError as error:
    print("Problem: couldn't copy the files (" + str(error) + ").")
    print("Fix: close any program using those files, then run the command again.")
