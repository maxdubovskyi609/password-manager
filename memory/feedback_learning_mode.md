---
name: feedback-learning-mode
description: Don't write learning-exercise code (like OOP refactors) unprompted — assess understanding first, discuss theory, let the user implement
metadata:
  type: feedback
---

When the user frames a task as something they want to learn (e.g. "хочу освоїти ООП" / converting the project to OOP), do not just write the refactored code yourself, even if they also said they want to move fast. Corrected after I rewrote `database.py` and `password_manager.py` into classes without being asked — user said: assess my current knowledge first, discuss what's unclear theoretically, then let me implement it myself.

**Why:** The user (see [[user_learning_context]], 16yo learning programming) explicitly wants to build real understanding, not just end up with working code they didn't write. "Finish quickly" was about not over-scoping, not about skipping the learning step.

**How to apply:** For learning-flagged tasks: (1) ask questions to gauge what they already know, (2) explain/discuss the parts that are unclear, (3) only then let them write the code, reviewing/giving feedback rather than producing the implementation. Reserve writing code directly for tasks that are about getting something working rather than about learning a concept (e.g. the earlier encryption feature was fine to implement directly since it wasn't framed as a learning exercise).
