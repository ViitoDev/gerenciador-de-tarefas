from datetime import datetime
from src.task import Task

agora = datetime.now

def test_criar_tarefa_pendente_por_padrao():
    tarefa = Task(
        id=1,
        title="Estudar testes",
        description="Aprendento pytest",
        created_at= agora
    )
    assert tarefa.title == "Estudar testes"
    assert tarefa.is_completed is False

def testar_marcar_tarefa_como_completo():
    tarefa = Task(
        id=2,
        title="Fazer commit",
        description="Subir no github",
        created_at= agora
    )
    tarefa.mark_complete()
    assert tarefa.is_completed == True