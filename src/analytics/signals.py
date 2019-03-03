from django.dispatch import Signal


object_viewed_signal = Signal(providing_args=['instance', 'request'])

search_signals = Signal(providing_args=['instance', 'request'])