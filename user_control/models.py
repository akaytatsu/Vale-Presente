from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

Roles = (("admin", "admin"), ("loja", "loja"))

class CustomUserManager(BaseUserManager):
  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('is_active', True)

    if extra_fields.get("is_staff") is not True:
        raise ValueError("Superuser must have is_staff=True.")

    if extra_fields.get("is_superuser") is not True:
        raise ValueError("Superuser must have is_superuser=True.")

    if not email:
        raise ValueError("Email field is required")

    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save()
    return user


class Store(models.Model):
  name = models.CharField(unique=True, max_length=100)
  address = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['id']
  
  def save(self, *args, **kwargs):
    action = f'Adicionado nova loja: {self.name}'
    if self.pk is not None:
        action = f'Atualizado o nome da loja {self.old_name} para {self.name}'
    super().save(*args, **kwargs)
    #add_user_activity()
  
  def delete(self, *args, **kwargs):
    created_by = self.created_by
    action = f'Deletado a loja: {self.name}'
    super().delete(*args, **kwargs)
    #add_user_activity()

  def __str__(self):
    return self.name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=8, choices=Roles)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True)
    user_store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='users', null=True)

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("created_at", )


class UserActivities(models.Model):
    user = models.ForeignKey(
        CustomUser, related_name="user_activities", null=True, on_delete=models.SET_NULL)
    email = models.EmailField()
    fullname = models.CharField(max_length=255)
    action = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at", )

    def __str__(self):
        return f"{self.fullname} {self.action} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"