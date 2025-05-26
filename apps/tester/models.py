from django.db import models

class Test(models.Model):
    test_name = models.CharField(max_length=200)
    WorkTime = models.IntegerField(verbose_name='Время выполнения (мин)')
    QuestionsCount = models.IntegerField()
    test_result = models.TextField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.test_name

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    text = models.TextField(max_length=250)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'


class Answer(models.Model):
    QuestionId = models.ForeignKey(Question, on_delete=models.CASCADE)
    Text = models.CharField(max_length=300)
    IsRight = models.BooleanField()

    class Meta:
        verbose_name = 'answer'
        verbose_name_plural = 'answers'

    def __str__(self):
        return self.Text

class UserTest(models.Model):
    ProfileId = models.ForeignKey(Test, on_delete=models.CASCADE)
    UserName = models.CharField(max_length=300, verbose_name="ФИО")
    DateTime = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="Время завершения")
    Rating =models.FloatField(verbose_name="Проценты")

    class Meta:
        verbose_name = 'user_test'
        verbose_name_plural = 'user_tests'

    def __str__(self):
        return self.UserName