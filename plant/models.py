from django.db import models
from user.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from staff.models import DonationOrg

class Seed(models.Model):
    name = models.CharField('씨앗종류', max_length=10)
    photo = models.ImageField('사진', upload_to='seed/')
    desc = models.TextField('씨앗정보', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "씨앗정보"
        verbose_name = "씨앗"

class State(models.Model):
    state = models.CharField('상태', max_length=10)

    def __str__(self):
        return self.state

    class Meta:
        verbose_name_plural = "작물상태"
        verbose_name = "작물상태"

class Diary(models.Model):
    # STATION_CHOICES = (
    #     ('w', 'water'),
    #     ('s', 'sun'),
    #     ('l', 'love')
    # )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='회원이름')
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE, verbose_name='씨앗종류')
    exp = models.IntegerField('경험치', default=0, validators=[MinValueValidator(0), MaxValueValidator(599)])
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='작물상태')
    # station = models.CharField(max_length=1, choices=(
    #     ("w", "water"),
    #     ("s", "sun"),
    #     ("l", "love")
    # ), default="w")
    weed = models.IntegerField('잡초개수', default=0, validators=[MinValueValidator(0), MaxValueValidator(8)])
    harvest= models.DateField('수확날짜', null=True, blank=True)
    # 기부단체 외래키
    donation = models.ForeignKey(DonationOrg, on_delete=models.CASCADE, verbose_name='작물상태')
    # 외래키의 필드 불러와서 출력
    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = "작물일지"
        verbose_name = "작물"

