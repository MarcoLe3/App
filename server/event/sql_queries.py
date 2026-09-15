GET_EVENTS = """
        SELECT id, name, description, location, start_time, end_time, available_tickets
        FROM events
        ORDER BY id
        LIMIT $1 OFFSET $2
        """