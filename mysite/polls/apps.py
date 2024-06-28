from django.apps import AppConfig


class PollsConfig(AppConfig):
    name = 'polls'

    def ready(self):
        from polls.models import Vote
        days = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        for day in days:
            if not Vote.objects.filter(day=day).exists():
                Vote.objects.create(day=day)
