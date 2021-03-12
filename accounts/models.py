from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField #이미지 킷에서 이미지 처리 필드 임포트
from imagekit.processors import ResizeToFill # 이미지킷에서 리사이즈 기능 임포트


# Create your models here.
def user_path(instance, filename):
    from random import choice
    import string

    arr = [choice(string.ascii_letters) for _ in range(8)]
    pid = ''.join(arr)
    extenstion = filename.split('.')[-1]  
    return 'accounts/{}/{}.{}'.format(instance.user.username, pid, extenstion)

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField('별명', max_length=20, unique=True)
    about = models.CharField(max_length=300, blank=True)
    
    GENDER_C = (
        ('선택암함', '선택안함'),
        ('여성', '여성'),
        ('남성', '남성'),
    )
    gender = models.CharField('성별(선택사항)', max_length=10, choices=GENDER_C, default='N')
    picture = ProcessedImageField(upload_to=user_path, processors=[ResizeToFill(150, 150)],
                                    format='JPEG', options={'quality': 90}, blank=True)

    def __str__(self):
        return self.nickname




