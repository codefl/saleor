class TrackingStatus:
    PREPARING = "preparing"  # Preparing
    READY = "ready"  # ready for shipping
    IN_TRANSIT = "In transit"  # order is in transit
    IN_DELIVERY = "In delivery"  # order is in delivery
    DELIVERED = "Delivered"  # order delivered

    CHOICES = [
        (PREPARING, "Preparing"),
        (READY, "Ready"),
        (IN_TRANSIT, "In Transit"),
        (IN_DELIVERY, "In Delivery"),
        (DELIVERED, "Delivered"),
    ]
