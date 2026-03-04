from datetime import datetime
from task import Task
from repository import TaskRepository

def main() -> None:
    my_task = Task(
        id=1,
        title="Estudar engenharia de software",
        description="Aplicar conceitos de SOLID e Clen Code",
        created_at=datetime.now(),
    )

    lista_de_tarefas = [my_task]

    repo = TaskRepository(file_path="tasks.json")

    print("A guardar tarefas no ficheiro...")
    repo.save_tasks(lista_de_tarefas)
    print("Tarefas guardadas com sucesso!")

    print(f"Tarefa criada: {my_task.title}")
    print(f"Status inicial: {"Completa" if my_task.is_completed else "Pendente"}")

    my_task.mark_complete()

    print(f"Status atual: {"Completa" if my_task.is_completed else "Pendente"}")

if __name__ == "__main__":
    main()