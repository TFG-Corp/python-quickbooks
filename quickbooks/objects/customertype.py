from six import python_2_unicode_compatible
from .base import Ref, QuickbooksManagedObject, QuickbooksTransactionEntity


@python_2_unicode_compatible
class CustomerType(QuickbooksManagedObject, QuickbooksTransactionEntity):
    """
    QBO definition: The Vendor represents the seller from whom your company purchases any service or product.
    """

    qbo_object_name = "CustomerType"

    def __init__(self):
        super(CustomerType, self).__init__()
        self.Name = ""
        self.Active = True

    def __str__(self):
        return self.Name

    def to_ref(self):
        ref = Ref()
        ref.name = self.Name
        ref.type = self.qbo_object_name
        ref.value = self.Id

        return ref
