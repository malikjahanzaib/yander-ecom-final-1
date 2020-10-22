from django.contrib import admin

from .models import Item,OrderItem,Order, Payment, Coupon,Refund,Address,UserProfile,WishlistItem,Wishlist,Review

def make_refund_accepted(modeladmin,request,queryset):
    queryset.update(refund_requested=False,refund_granted=True)

make_refund_accepted.short_description ='Update orders to refund granted'

def make_review_accepted(modeladmin,request,queryset):
    queryset.update(status=True)

make_review_accepted.short_description = "Update Reviews to be posted(True)"

def make_review_declined(modeladmin,request,queryset):
    queryset.update(status=False)

make_review_declined.short_description = "Update Reviews not to be posted(False)"


def make_received(modeladmin,request,queryset):
    queryset.update(being_delivered=False,received=True)

make_received.short_description ='Update orders to received'

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered','being_delivered','received','refund_requested','refund_granted',
    'billing_address','shipping_address','payment','coupon'
    ]

    list_display_links =['user','billing_address','shipping_address','payment','coupon',]

    list_filter =['user', 'ordered','being_delivered','received','refund_requested','refund_granted',]
    #if only user used then we would be searching a object rather than a field ,hence username added
    search_fields=['user__username','ref_code']
    actions =[make_refund_accepted,make_received]

class AddressAdmin(admin.ModelAdmin):
    list_display=['user','street_address','house_address','country','zip','address_type','default']

    list_filter =['default','address_type','country']

    search_fields =['user','street_address','house_address','zip']

class ReviewAdmin(admin.ModelAdmin):
    list_display=['subject','comment','status','create_at','rate']

    list_filter =['status']

    search_fields=['user__username','status']

    readonly_fields =['subject','comment','ip','user','rate','item']

    actions =[make_review_accepted,make_review_declined]
    
# Register your models here.
#registers our models on the admin pg
admin.site.register(Item)
admin.site.register(OrderItem)
#Now registering this admin class with our associated model i.e Order here
admin.site.register(Order,OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address,AddressAdmin)
admin.site.register(UserProfile)
admin.site.register(WishlistItem)
admin.site.register(Wishlist)
admin.site.register(Review,ReviewAdmin)



