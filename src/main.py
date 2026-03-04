from datetime import datetime
from task import Task

def main() -> None:
    my_task = Task(
        id=1,
        title="Estudar engenharia de software",
        description="Aplicar conceitos de SOLID e Clen Code",
        created_at=datetime.now(),
    )

    print(f"Tarefa criada: {my_task.title}")
    print(f"Status inicial: {"Completa" if my_task.is_completed else "Pendente"}")

    my_task.mark_as_complete()

    print(f"Status atual: {"Completa" if my_task.is_completed else "Pendente"}")

if __main__ == "__main__":
    main()