from api.models import User, Agent, Event, Group
import datetime


def get_active_users() -> User:
    today_less_ten = datetime.date.today() - datetime.timedelta(10)
    return User.objects.filter(last_login__gte=today_less_ten)


def get_amount_users() -> User:
    return User.objects.count()


def get_admin_users() -> User:
    return User.objects.filter(group__name='admin')


def get_all_debug_events() -> Event:
    return Event.objects.filter(level='debug')


def get_all_critical_events_by_user(agent) -> Event:
    return Event.objects.filter(level='critical', agent=agent)


def get_all_agents_by_user(username) -> Agent:
    return Agent.objects.filter(user__name=username)


def get_all_events_by_group() -> Group:
    return Group.objects.filter(user__agent__event__level='information')
