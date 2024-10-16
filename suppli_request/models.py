from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from supplier.models import TimeStampBase, Supplier

USER = get_user_model()


#TextChoice
class StatusRequestChoice(models.TextChoices):
    STARTED = "ST", _('Iniciado')
    INPROGRESS = "IP", _('Em Andamento')
    CLOSED = "CS", _('Fechado')
    COMPLETED = 'CP', _('Finalizado')
    CANCELLED = 'CC', _('Cancelado')


class UnitItemRequestChoice(models.TextChoices):
    UNIT = "UNI", _('Unidade')
    BOX = "BOX", _('Caixa')
    KILOGRAM = "KG", _('Kilograma')
    BUCKET = "BCK", _("Balde")
    TRAY = "TRY", _('Bandeja')
    BAR = "BAR", _("Barra")
    BLOCK = "BLK", _("Bloco")
    BOBBIN = "BOB", _('Bobina')
    CAPSULE = "CAPS", _('Capsula')
    CARD = "CART", _('Cartela')
    HUNDRED = "HUNDRED", _('Cento')
    OFSET = "SET", _('Conjuento')
    CENTIMETER = "CM", _('Centimetro')
    CENTIMETERSQUARE = "CM2", _('Centrimetro Quadrado')
    DISPLAY = "DISP", _('Display')
    DOZEN = "DOZEN", _('Duzia')
    PACKAGE = "PACKAGE", _('Embalagem')
    BALE = "BALE", _('Fardo')
    SHEET = "SHEET", _('Folha') 
    GALLON = "GALLON", _('Galão')
    BOTTLE = "GF", _('Frasco')
    GRAMS = "GRAMS", _('Gramas')
    GAME = "GAME", _('Jogo')
    KIT = "KIT", _('Kit')
    CAN = "CAN", _('Lata')
    LITER = "LITER", _('Litro')
    METER = "M", _('Metro')
    SQUAREMETER = "M2", ('Metro Quadrado')
    CUBICMETER = "M3", _('Metro Cúbico')
    THOUSAND = "THOUSAND", _('Milheiro')
    MILLILITRE = "ML", _('Mililitro')
    MEGAWATTHOUR = "MWH", _('MegaWhats/Hora')
    PALLET = "PALLET", _('Palete')
    PAIRS = "PAIRS", _('Pares')
    PIECE = "PC", _('Peça')
    PATTER = "POT", ("Pote")
    CARAT = "K", _('Kilate')
    REAM = "REAM", _('Resma')
    ROLL = "ROLL", _('Rolo')
    BAG = "BAG", _("Saco")
    DRUM = "DRUM", _('Tambor')
    TANK = "TANK", _('Tanque')
    TON = "TON", _('Tonelada')
    TUBE = "TUBE", ('Tubo')
    VESSEL = "VESL", ('Vasilhame')
    GLASS = "GLASS", _('Vidro')


# Models
class SupplyResquest(TimeStampBase):
    date_request = models.DateField(_("Data da Requisição"))
    description_request = models.CharField(_("Descrição da Requisição"), max_length=150)
    status = models.CharField(_("Status"), max_length=2, choices=StatusRequestChoice.choices)
    supplier = models.ForeignKey(
        Supplier, 
        verbose_name=_("Fornecedor"), 
        on_delete=models.DO_NOTHING,
        blank=True, null=True
    )
    start_date = models.DateField(_("Inicio do Contrato"), blank=True, null=True)
    delivery_time = models.DateField(_("Prazo de Entrega"), blank=True, null=True)

    class Meta:
        """Meta definition for SuppliResquest."""

        verbose_name = 'Requisição de Fornecimento'
        verbose_name_plural = 'Requisições de Fornecimento'

    @property
    def get_value_total(self):
        itens = ItensSupplyRequest.objects.filter(supply_request=self.id)
        print(itens)
        value_total = 0.00
        for iten in itens:
            print(value_total)
            value_total += iten.value_total_itens_supply_request
        return value_total
    get_value_total.fget.short_description = 'Valor Total da Requisição'
    
    @property
    def get_unit_total(self):
        itens = ItensSupplyRequest.objects.filter(supply_request=self.id)
        unit_total = 0
        for iten in itens:
            unit_total += iten.amount_item
        return unit_total
    get_unit_total.fget.short_description = "Quantidade Total de Itens"
    
    def get_absolute_url(self):
        return reverse("suppli_request-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        """Unicode representation of SuppliResquest."""
        return f'{self.description_request.capitalize()} - {self.status}'


class ItensSupplyRequest(models.Model):
    supply_request = models.ForeignKey(
        SupplyResquest, 
        verbose_name=_("Requisição de Fornecimento"), 
        on_delete=models.CASCADE,
    )
    code_item_request = models.CharField(_("Código do Item Requisitado"), max_length=30)
    description_item = models.CharField(_("Descrição do Item Requisitado"), max_length=200)
    amount_item = models.PositiveIntegerField(_("Quantidade"))
    unit_measurement = models.CharField(_("Unidade"), max_length=8, choices=UnitItemRequestChoice.choices)
    unit_value = models.FloatField(_("Valor Unitãrio"), )

    class Meta:
        """Meta definition for ItensSupplyRequest."""
        verbose_name = 'ItensSupplyRequest'
        verbose_name_plural = 'ItensSupplyRequests'
        
    @property
    def value_total_itens_supply_request(self):
        total = self.amount_item * self.unit_value
        return total
    
    
    def __str__(self):
        """Unicode representation of ItensSupplyRequest."""
        return f'{self.code_item_request} - {self.description_item}'