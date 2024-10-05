from django.contrib import admin
from suppli_request import models


# TabularInLine
class ItensSupplyRequestInline(admin.TabularInline):
    '''Tabular Inline View for ItensSuppliyRequest'''

    model = models.ItensSupplyRequest
    min_num = 1
    max_num = 30
    extra = 1


# Admin
@admin.register(models.SupplyResquest)
class SupplyResquestAdmin(admin.ModelAdmin):
    '''Admin View for SupplyResquest'''

    list_display = ('description_request', 'date_request', 'get_unit_total', 'get_value_total', 'status')
    list_filter = ('date_request',)
    inlines = [
        ItensSupplyRequestInline,
    ]

@admin.register(models.Proposal)
class ProposalAdmin(admin.ModelAdmin):
    '''Admin View for models.Proposal'''

    list_display = ('supplier', 'request', 'item_request', 'price_proposal', 'validity')