from django import forms

class PaymentForm(forms.Form):
    card_name = forms.CharField(max_length=100, label="Kart Üzerindeki İsim")
    card_number = forms.CharField(max_length=16, label="Kart Numarası")
    expiry_month = forms.CharField(max_length=2, label="Son Kullanma Ayı (MM)")
    expiry_year = forms.CharField(max_length=4, label="Son Kullanma Yılı (YYYY)")
    cvv = forms.CharField(max_length=3, label="CVV Kodu")
    installment = forms.ChoiceField(choices=[(str(i), f"{i} Taksit") for i in range(1, 13)], label="Taksit Seçeneği")
