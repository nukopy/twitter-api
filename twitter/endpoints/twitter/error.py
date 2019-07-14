class TwitterError(Exception):
    """TwitterAPI exception class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = ''

    def __str__(self):
        return self.message


class RateLimitError(TwitterError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
