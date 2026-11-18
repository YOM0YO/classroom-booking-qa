def can_book(room, start, end, reservations):
    """Check a room request in minutes from midnight for one day."""
    if not 0 <= start < end <= 1440:
        return False
    return all(
        room != used_room or end <= used_start or start >= used_end
        for used_room, used_start, used_end in reservations
    )
