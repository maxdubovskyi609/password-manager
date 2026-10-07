# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Desktop password manager GUI built with **CustomTkinter** on top of a local **SQLite** database. UI text is in English; code comments and commit messages are in Ukrainian.

## Running

```
pip install customtkinter pillow
python password_manager.py
```

Run from the repository root: image paths (`images/*.png`) and the DB path (`password_manager_db/database.db`) are relative to the current working directory. There is no test suite, linter config, or requirements file.

## Architecture

- `database.py` — opens the SQLite connection and creates the `passwords(id, website, username, password)` table **at import time** (module-level `db`/`cursor` globals). Exposes plain functions: `add_password`, `get_passwords`, `search_password`, `update_password`, `delete_password`, `close_database`. `update_password`/`delete_password` return `cursor.rowcount`, which the UI uses to report "not found". There is no UNIQUE constraint on `(website, username)`, so duplicates are possible.
- `password_manager.py` — procedural script: creates the global `root` `CTk` window, loads icons, defines UI helpers, then one function per feature window (`add_window`, `view_passwords`, `find_window`, `change_window`, `delete_window`), each opening a `CTkToplevel` with a nested callback that calls into `database.py`. Ends with `root.mainloop()`.
  - Shared helpers: `entry()` (input field), `main_button()` (big main-menu button, always parented to global `root`), `second_button()` (action button in a dialog), `create_window()` (Toplevel factory).
  - Style constants (`BTN_COLOR`, `DANGER_COLOR`, `FONT_*`) live at the top of the file.
  - Layout uses `grid` with a single column (`column=0`) everywhere.
- Passwords are stored and displayed in plaintext.

## Current direction

Work happens on the `refactoring` branch. The recent commits extract constants and helper functions step by step; the latest commit ("останні зміни перед OOP") marks the next planned step: refactoring into classes (e.g. a DB class plus `CTk`/`CTkToplevel` subclasses). Keep commits small and incremental in that style.
