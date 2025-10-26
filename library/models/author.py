from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Nombre")
    last_name = models.CharField(max_length=100, verbose_name="Apellido")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Fecha de nacimiento")

    class Meta:
        db_table = "authors"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self) -> str:
        """Get the author fullname."""
        return f"{self.first_name} {self.last_name}"