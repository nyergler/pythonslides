from django.conf import settings as django_settings


def settings(request):

    return {
        'GA_ACCT': getattr(
            django_settings, 'GOOGLE_ANALYTICS_ACCT', None,
        ),
    }
