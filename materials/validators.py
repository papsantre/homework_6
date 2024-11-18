from rest_framework.serializers import ValidationError


class VideoValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        video_link = 'http://youtube.com'
        if value.get('video_link'):
            if video_link not in value.get('video_link'):
                raise ValidationError(f'Разрешена только ссылка на {video_link}')
        return None
