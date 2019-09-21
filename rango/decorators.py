from django.core.urlresolvers import reverse
import inspect


def skip_test(self):
    pass


def chapter6(test):
    try:
        reverse('goto')
        print("Chapter 6 - Skipped: " + test.__name__)
        return skip_test
    except:
        return test


def chapter7(test):

    try:
        reverse('login')
        print("Chapter 7 - Skipped: " + test.__name__)
        return skip_test
    except:
        try:
            reverse('auth_login')
            print("Chapter 7 - Skipped: " + test.__name__)
            return skip_test
        except:
            return test


def chapter8(test):
    try:
        reverse('auth_login')
        print("Chapter 8 - Skipped: " + test.__name__)
        return skip_test
    except:
        try:
            from rango.models import User, UserProfile
            return test
        except:
            print("Chapter 8 - Skipped: " + test.__name__)
            return skip_test


def chapter9(test):
    try:
        reverse('auth_login')
        print("Chapter 9 - Skipped: " + test.__name__)
        return skip_test
    except:
        return test
