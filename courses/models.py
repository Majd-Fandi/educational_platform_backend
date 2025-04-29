from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser

def course_directory_path(instance, filename):
    return f'{instance.title}/{filename}'

def module_directory_path(instance, filename):
    return f'{instance.module.course.title}/module_{instance.module.id}_{instance.module.title}/{filename}'

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    slug = models.SlugField(unique=True, blank=True)
    poster = models.ImageField(upload_to=course_directory_path, null=True, blank=True)
    uploader = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='uploaded_courses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    num_of_lessons = models.PositiveIntegerField(default=0, editable=False)
    size = models.PositiveIntegerField(default=0, editable=False)  # Size in bytes
    course_duration = models.PositiveIntegerField(default=0, editable=False)  # Duration in minutes

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def calculate_size(self):
        total_size = 0
        for module in self.modules.all():
            for video in module.videos.all():
                if video.video_file:
                    total_size += video.video_file.size
            for pdf in module.pdf_files.all():
                if pdf.file:
                    total_size += pdf.file.size
        self.size = total_size

    def calculate_duration(self):
        total_duration = 0
        for module in self.modules.all():
            for video in module.videos.all():
                total_duration += video.duration if video.duration else 0
        self.course_duration = total_duration

    def calculate_num_of_lessons(self):
        self.num_of_lessons = sum(module.videos.count() for module in self.modules.all())

    def update_calculated_fields(self):
        self.calculate_size()
        self.calculate_duration()
        self.calculate_num_of_lessons()
        self.save()

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Video(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to=module_directory_path)
    duration = models.PositiveIntegerField(default=0, help_text="Duration in seconds")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PDFFile(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='pdf_files')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=module_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Rating(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('course', 'user')

    def __str__(self):
        return f"{self.course.title} - {self.user.username} - {self.rating}"

class Download(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='downloads')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    downloaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.title} - {self.user.username}"



# from django.db import models

# class Video(models.Model):
#     title = models.CharField(max_length=255)
#     video_file = models.FileField(upload_to='videos/')  # Videos will be stored in 'media/videos/'
#     uploaded_at = models.DateTimeField(auto_now_add=True)
