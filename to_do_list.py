print("Welcome Back Boss\nWhat is the task for today?")

task_list = []

while True:
    try:
        choice = int(input(
            "\nEnter your choice here\n1. Add a task\n2. View all tasks\n3. Mark a task as complete\n4. Edit a task\n5. Delete a task\n6. Update task priority\n7. Update a due date\n8. Exit\n"
            "Enter choice: "
        ))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if choice == 1:
        a = {}
        while True:
            try:
                task_id = int(input("Enter the ID of the task: "))

                # Check duplicate ID
                if any(task["id"] == task_id for task in task_list):
                    print("This ID already exists. Please enter a different ID.")
                    continue

                a["id"] = task_id
                break

            except ValueError:
                print("Please enter a valid ID in integer only.")

        # Get title
        while True:
            title = input("Enter the name of the task: ").strip()

            if title:
                a["title"] = title
                break

            print("Task name cannot be empty.")

        # Default status
        a["status"] = False

        # Get due date
        while True:
            due_date = input("Enter the due date of the task: ").strip()

            if due_date:
                a["due_date"] = due_date
                break

            print("Due date cannot be empty.")

        # Get priority
        while True:
            priority = input(
                "Set priority (high/medium/low): "
            ).strip().lower()

            if priority in ["high", "medium", "low"]:
                a["priority"] = priority
                break

            print("Please enter only high, medium, or low.")

        task_list.append(a)

        print("Task added successfully!")

    # 2. View all tasks
    elif choice == 2:
        if len(task_list) == 0:
            print("No task available.")
        else:
            print("\n========== ALL TASKS ==========")

            for task in task_list:
                if task["status"]:
                    status = "Completed"
                else:
                    status = "Pending"

                print(f"\nID: {task['id']}")
                print(f"Title: {task['title']}")
                print(f"Status: {status}")
                print(f"Due Date: {task['due_date']}")
                print(f"Priority: {task['priority']}")

            print("\n===============================")

    # 3. Mark task as complete
    elif choice == 3:
        try:
            task_id = int(input("Enter the task ID here: "))
        except ValueError:
            print("Please enter a valid ID.")
            continue

        found = False

        for task in task_list:
            if task["id"] == task_id:
                task["status"] = True
                found = True
                print("Task marked as completed.")
                break

        if not found:
            print("Task not found.")

    # 4. Edit a task
    elif choice == 4:
        try:
            task_id = int(input("Enter the task ID here: "))
        except ValueError:
            print("Please enter a valid ID...")
            continue

        found = False

        for task in task_list:
            if task["id"] == task_id:
                found = True

                print("\nEnter new details:")

                new_title = input(
                    "Enter the updated name of the task: "
                ).strip()

                if new_title:
                    task["title"] = new_title

                new_due_date = input(
                    "Enter the updated due date: "
                ).strip()

                if new_due_date:
                    task["due_date"] = new_due_date

                while True:
                    new_priority = input(
                        "Enter the priority (high/medium/low): "
                    ).strip().lower()

                    if new_priority in ["high", "medium", "low"]:
                        task["priority"] = new_priority
                        break

                    print("Please enter high, medium, or low.")

                print("Task edited successfully!")
                break

        if not found:
            print("Task not found.")

    # 5. Delete a task
    elif choice == 5:
        try:
            task_id = int(input("Enter the task ID here: "))
        except ValueError:
            print("Please enter a valid ID.")
            continue

        found = False

        for task in task_list:
            if task["id"] == task_id:
                task_list.remove(task)
                found = True
                print("Task removed successfully.")
                break

        if not found:
            print("Task not found.")

    # 6. Update priority
    elif choice == 6:
        try:
            task_id = int(input("Enter the task ID here: "))
        except ValueError:
            print("Please enter a valid ID.")
            continue

        found = False

        for task in task_list:
            if task["id"] == task_id:

                while True:
                    priority = input(
                        "Enter the new priority (high/medium/low): "
                    ).strip().lower()

                    if priority in ["high", "medium", "low"]:
                        task["priority"] = priority
                        found = True
                        print("Priority updated successfully!")
                        break

                    print("Please enter high, medium, or low.")

                break

        if not found:
            print("Task not found.")

    # 7. Update due date
    elif choice == 7:
        try:
            task_id = int(input("Enter the task ID here: "))
        except ValueError:
            print("Please enter a valid ID.")
            continue

        found = False

        for task in task_list:
            if task["id"] == task_id:
                new_date = input(
                    "Enter the updated due date: "
                ).strip()

                if new_date:
                    task["due_date"] = new_date
                    found = True
                    print("Due date updated successfully!")
                else:
                    print("Due date cannot be empty.")

                break

        if not found:
            print("Task not found.")

    # 8. Exit
    elif choice == 8:
        print(
            "\nThank you for visiting us.....\n"
            "If you want something, we are here!"
        )
        break

    # Invalid choice
    else:
        print("Invalid choice. Please enter a number from 1 to 8.")
        continue

    # Ask whether user wants another operation
    cont = input(
        "\nDo you want to perform another operation? (y/n): "
    ).strip().lower()

    if cont == "n":
        print(
            "\nThank you for visiting us.....\n"
            "If you want something, we are here!"
        )
        break
