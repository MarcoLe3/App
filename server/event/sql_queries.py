GET_EVENTS = """
        SELECT id, name, description, location, start_time, end_time, avaliable_tickets
        FROM events
        """