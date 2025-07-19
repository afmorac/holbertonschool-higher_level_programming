def generate_invitations(template, attendees):
    import os

    # Verificar tipos de entrada
    if not isinstance(template, str):
        print("Error: template debe ser una cadena de texto.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: attendees debe ser una lista de diccionarios.")
        return

    # Validar si el template está vacío
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Validar si la lista está vacía
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Generar archivos personalizados
    for idx, attendee in enumerate(attendees, start=1):
        # Usar "N/A" si falta algún dato
        name = attendee.get("name", "N/A")
        title = attendee.get("event_title", "N/A")
        date = attendee.get("event_date", "N/A")
        location = attendee.get("event_location", "N/A")

        # Reemplazar los placeholders
        personalized = template.replace("{name}", str(name))
        personalized = personalized.replace("{event_title}", str(title))
        personalized = personalized.replace("{event_date}", str(date))
        personalized = personalized.replace("{event_location}", str(location))

        # Guardar archivo
        filename = f"output_{idx}.txt"
        with open(filename, 'w') as f:
            f.write(personalized)
