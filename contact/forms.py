from django import forms
from .models import ContactList, SubscriptionList


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactList
        fields = ["username", "email", "message"]

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "username": "Name or Username",
            "email": "Email Address",
            "message": "Message",
        }

        self.fields["username"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            if field == "message":
                self.fields[field].widget.attrs["class"] = "textarea"
            else:
                self.fields[field].widget.attrs["class"] = "input"
            self.fields[field].label = False


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = SubscriptionList
        fields = ["email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "email": "Email Address",
        }

        for field in self.fields:

            placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "input is-rounded"
            self.fields[field].label = False
