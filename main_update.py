from jira import JIRA

# Configurar credenciales de Jira
jira_url = 'https://carlosprueba.atlassian.net'
jira_user = 'carlosmarsh@hotmail.com'
jira_token = 'ATATT3xFfGF07d8fddMMTUZOnJhzXXLG40txpySkvjsDJaXyI6TmvzqDlOxK8dOQpls_iS9YyFs9oLqQ6D4PRr2oxXkCMpU7Xnbzd1FMUuT3cSQA9jnwjG0v6mG8bJ6soSnwU2PIPn7GD1zdDvDTIlKks79MhIQDrNV-Qtn6FY8wdojpCkba0Wk=ABE9E89C'

# Conectar a Jira
jira = JIRA(jira_url, basic_auth=(jira_user, jira_token))

# ID de la tarea de Jira (por ejemplo, "PDC-63")
issue_id = 'PDC-63'

# Ejecutar la prueba automatizada
def ejecutar_prueba():
    # Lógica de tu prueba aquí
    resultado_prueba = True  # O false dependiendo de la prueba
    return resultado_prueba

resultado = ejecutar_prueba()

# Actualizar la tarea en Jira
if resultado:
    comentario = 'La prueba automatizada se ejecutó exitosamente.'
else:
    comentario = 'La prueba automatizada falló.'

jira.add_comment(issue_id, comentario)
