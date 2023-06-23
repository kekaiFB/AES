from django.db import models
from smart_selects.db_fields import ChainedForeignKey


#------------------Влкадки---------------------------------------------------------
class Tab(models.Model):  
    title = models.CharField(max_length=150, verbose_name="Название", unique=True)

    class Meta:
        verbose_name = 'Вкладка'
        verbose_name_plural = '1 Вкладки'
        ordering = ['title'] 

    def __str__(self):
        return self.title
    

#------------------Элементы вкладок---------------------------------------------------------
class Element(models.Model):
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE, verbose_name="Вкладка", related_name='elements')
    title = models.CharField(max_length=150, verbose_name="Элемент")
    content = models.TextField(blank=True, verbose_name="Текст", null=True)
    
    class Meta:
        verbose_name = 'Элемент вкладки'
        verbose_name_plural = '2 Элементы вкладок' 
        ordering = ['tab', 'title'] 

    def __str__(self):
        return self.title
    

#------------------Файлы для элемента---------------------------------------------------------
class Files(models.Model):
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE, verbose_name="Вкладка", null=True)
    element = models.ForeignKey(Element, on_delete=models.CASCADE, verbose_name="Элемент", related_name='files',)
    # element = ChainedForeignKey(
    #     Element, 
    #     chained_field="Tab", 
    #     chained_model_field="Tab", 
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True,
    #     verbose_name="Элемент",
    #     related_name='files',
    # )
    files = models.FileField(upload_to="files/%Y/%m/%d/", blank=True, null=True)

    class Meta:
        verbose_name = 'Файлы элемента'
        verbose_name_plural = '2.1 Файлы элементов'
        ordering = ['tab', 'element']  

    def __str__(self):
        return str(self.element)


#------------------Изображения для элемента---------------------------------------------------------
class Images(models.Model):
    tab = models.ForeignKey(Tab, on_delete=models.CASCADE, verbose_name="Вкладка", null=True)
    element = models.ForeignKey(Element, on_delete=models.CASCADE, verbose_name="Элемент", related_name='images',)
    # element = ChainedForeignKey(
    #     Element, 
    #     chained_field="tab", 
    #     chained_model_field="tab", 
    #     show_all=False,
    #     auto_choose=True,
    #     sort=True,
    #     verbose_name="Элемент",
    #     related_name='images',
    # )
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")

    class Meta:
        verbose_name = 'Изображения элемента'
        verbose_name_plural = '2.2 Изображения элементов'
        ordering = ['tab', 'element']  

    def __str__(self):
        return str(self.element)
     
# -------------------------------------------------------------------------------
