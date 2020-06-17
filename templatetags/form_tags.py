from django import template

register = template.Library()

# https://ethanshearer.com/view-post/3/070519/sass-with-django-part2-bulma


@register.filter(name="add_class")
def add_class(field, classname):
    existing_classes = field.field.widget.attrs.get("class", None)
    if existing_classes:
        if existing_classes.find(classname) == -1:
            classes = existing_classes + " " + classname
        else:
            classes = existing_classes
    else:
        classes = classname
    return field.as_widget(attrs={"class": classes})
