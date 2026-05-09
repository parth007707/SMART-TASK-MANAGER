import pandas as pd
import numpy as np

def generate_task_analytics(tasks):

    if len(tasks) == 0:
        return {
            "total_tasks": 0,
            "completed_tasks": 0,
            "pending_tasks": 0,
            "completion_percentage": 0
        }

    task_data = []

    for task in tasks:
        task_data.append({
            "title": task.title,
            "status": task.status
        })

    df = pd.DataFrame(task_data)

    total_tasks = len(df)
    completed_tasks = np.sum(df['status'] == 'Completed')
    pending_tasks = np.sum(df['status'] == 'Pending')

    completion_percentage = (
        completed_tasks / total_tasks
    ) * 100

    return {
        "total_tasks": int(total_tasks),
        "completed_tasks": int(completed_tasks),
        "pending_tasks": int(pending_tasks),
        "completion_percentage": round(
            completion_percentage,
            2
        )
    }
