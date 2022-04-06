import graphene
from graphene import ObjectType
from graphene_django import DjangoObjectType
from authapp.models import User
from projectapp.models import Todo, Project


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff')


class Query(ObjectType):
    todos = graphene.List(TodoType)
    projects = graphene.List(ProjectType)
    users = graphene.List(UserType)

    def resolve_todos(root, info):
        return Todo.objects.filter(is_active=True)

    def resolve_projects(root, info):
        return Project.objects.all()

    def resolve_users(root, info):
        return User.objects.all()

    user_by_name = graphene.Field(UserType, username=graphene.String(required=True))

    def resolve_user_by_name(root, info, username):
        return User.objects.get(username=username)


schema = graphene.Schema(query=Query)

# { todos {
#   id
#   text
#   user {
#     username
#   }
# } }
# { projects {
#   id
#   name
#   users {
#     username
#   }
# } }
# { userByName(username: "kathleennels9") {
#   id
#   firstName
#   lastName
#   email
#   isSuperuser
#   isStaff
# } }
