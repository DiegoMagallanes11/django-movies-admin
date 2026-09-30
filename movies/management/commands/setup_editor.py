from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from movies.models import Movie


class Command(BaseCommand):
    help = 'Create the editors group with specific permissions and an editor user'

    def handle(self, *args, **options):
        self.stdout.write('Setting up editors group...')

        group, created = Group.objects.get_or_create(name='editors')
        if created:
            self.stdout.write(self.style.SUCCESS('Group "editors" created'))
        else:
            self.stdout.write('Group "editors" already exists')

        content_type = ContentType.objects.get_for_model(Movie)

        add_permission = Permission.objects.get(
            codename='add_movie',
            content_type=content_type
        )
        change_permission = Permission.objects.get(
            codename='change_movie',
            content_type=content_type
        )

        group.permissions.set([add_permission, change_permission])
        self.stdout.write(self.style.SUCCESS(
            f'Permissions assigned: add_movie, change_movie'
        ))

        editor_user, user_created = User.objects.get_or_create(
            username='editor',
            defaults={'email': 'editor@example.com', 'is_staff': True}
        )
        if user_created:
            editor_user.set_password('editorpass123')
            editor_user.is_staff = True
            editor_user.save()
            self.stdout.write(self.style.SUCCESS('User "editor" created'))
        else:
            self.stdout.write('User "editor" already exists')
            if not editor_user.is_staff:
                editor_user.is_staff = True
                editor_user.save()
                self.stdout.write(self.style.SUCCESS('User "editor" updated with is_staff=True'))

        editor_user.groups.add(group)
        self.stdout.write(self.style.SUCCESS('User "editor" added to group "editors"'))

        self.stdout.write(self.style.SUCCESS('Setup complete!'))
