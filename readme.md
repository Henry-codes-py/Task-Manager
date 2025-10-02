# Task Manager

A simple **command-line Task Manager** written in Python. This project demonstrates file-based user authentication, task management, and basic report generation.

---

## Features

- 🔑 **User Authentication** — Login system using `user.txt`.
- 👥 **User Management** — Register new users (admin only).
- 📝 **Task Management** — Add, view, and complete tasks.
- 📊 **Reports** — Generate `task_overview.txt` and `user_overview.txt` with detailed stats.
- 📈 **Admin Dashboard** — View total users and tasks in the terminal.

---

## Default Admin Credentials

```txt
username: admin
password: password
```

⚠️ Passwords are stored in plain text in `user.txt`. This is for learning/demo purposes only.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/task-manager.git
   cd task-manager
   ```

2. Run the program:
   ```bash
   python task_manager.py
   ```

> Ensure you open the entire folder in VS Code (or run the script from inside the project directory). Otherwise, the program may look for `tasks.txt` and `user.txt` in your root directory.

---

## File Structure

- **`task_manager.py`** — Main program
- **`user.txt`** — Stores credentials (`username;password`)
- **`tasks.txt`** — Stores tasks in the format:
  ```txt
  username;title;description;due_date;assigned_date;Yes/No
  ```
- **`task_overview.txt`** — Auto-generated report on tasks
- **`user_overview.txt`** — Auto-generated per-user report

---

## Menu Options

- `r` — Register a user (admin only)
- `a` — Add a task
- `va` — View all tasks
- `vm` — View my tasks
- `ds` — Display statistics (admin only)
- `gr` — Generate reports
- `e` — Exit program

---

## Example Task Format

```txt
admin;Fix login bug;Ensure login checks password correctly;2025-10-05;2025-09-28;No
```

---

## Known Issues / Future Improvements

- 🚨 Passwords stored in plain text — switch to hashed storage (e.g., bcrypt).
- 🔄 Duplicate functionality in functions vs inline menu code — refactor to avoid redundancy.
- ✏️ Editing/reassigning tasks not yet implemented.
- 🛡️ Add error handling for malformed files.
- ✅ Add unit tests.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repo
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request 🎉

---

## License

This project is released under the [MIT License](LICENSE).

