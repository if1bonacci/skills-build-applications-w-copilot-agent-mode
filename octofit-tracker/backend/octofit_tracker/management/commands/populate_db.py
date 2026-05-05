from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Create Users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel.name),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc.name),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2024-05-01')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2024-05-02')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2024-05-03')
        Activity.objects.create(user=users[3], type='Yoga', duration=40, date='2024-05-04')

        # Create Workouts
        Workout.objects.create(name='Pushups', description='Do 3 sets of 15 pushups', difficulty='easy')
        Workout.objects.create(name='Squats', description='Do 3 sets of 20 squats', difficulty='medium')
        Workout.objects.create(name='Plank', description='Hold plank for 2 minutes', difficulty='hard')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
