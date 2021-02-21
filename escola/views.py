from rest_framework    import viewsets
from escola.models     import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo lista de alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo lista de cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """Listando todas as matriculas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
