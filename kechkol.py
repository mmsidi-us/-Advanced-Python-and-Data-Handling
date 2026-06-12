class Task:
    """Represents a single task with a title, priority, and completion status."""

    # Class variable — shared across all instances
    VALID_PRIORITIES = ["low", "medium", "high"]

    def __init__(self, title, priority="medium"):
        self.title = title
        self.completed = False           # All tasks start incomplete

        # Validate priority before setting it
        if priority.lower() not in self.VALID_PRIORITIES:
            raise ValueError(f"Priority must be one of {self.VALID_PRIORITIES}")
        self.priority = priority.lower()

    def complete(self):
        """Mark the task as completed."""
        self.completed = True

    def __repr__(self):
        status = "✓" if self.completed else "○"
        return f"[{status}] {self.title} ({self.priority})"

class TaskManager:
    """Manages a collection of tasks."""

    def __init__(self):
        self.tasks = []  # Internal list of Task objects

    def add_task(self, title, priority="medium"):
        """Create and add a new task. Returns the task."""
        task = Task(title, priority)
        self.tasks.append(task)
        return task

    def complete_task(self, title):
        """Mark a task as completed by title. Returns True if found."""
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return True
        return False

    def get_pending(self):
        """Return all incomplete tasks."""
        return [t for t in self.tasks if not t.completed]

    def get_by_priority(self, priority):
        """Return all tasks with the given priority."""
        return [t for t in self.tasks if t.priority == priority]

    def summary(self):
        """Print a summary of all tasks."""
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.completed)
        print(f"\\n Task Summary: {done}/{total} completed")
        for task in self.tasks:
            print(f"  {task}")